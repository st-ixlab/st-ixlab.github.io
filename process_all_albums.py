import urllib.request
import re
import os
import struct
from pathlib import Path
from urllib.parse import urljoin, urlparse

def get_image_dimensions(img_data):
    """Get image dimensions from JPEG or PNG file data"""
    try:
        if img_data[:2] == b'\xff\xd8':
            # JPEG format - need to find SOF (Start of Frame) marker
            # SOF markers: 0xFFC0-0xFFC3, 0xFFC5-0xFFC7, 0xFFC9-0xFFCB, 0xFFCD-0xFFCF
            i = 2
            while i < len(img_data) - 9:
                if img_data[i] == 0xFF:
                    marker = img_data[i+1]
                    # Check for SOF markers (Start of Frame)
                    if marker in [0xC0, 0xC1, 0xC2, 0xC3, 0xC5, 0xC6, 0xC7, 0xC9, 0xCA, 0xCB, 0xCD, 0xCE, 0xCF]:
                        # Skip length field (2 bytes) and precision (1 byte)
                        # Height is at offset +5, Width is at offset +7
                        height = struct.unpack('>H', img_data[i+5:i+7])[0]
                        width = struct.unpack('>H', img_data[i+7:i+9])[0]
                        return width, height
                    # Skip APP markers and other non-SOF markers
                    elif marker == 0xE0 or (marker >= 0xE1 and marker <= 0xEF):
                        # APP marker - skip the segment
                        segment_length = struct.unpack('>H', img_data[i+2:i+4])[0]
                        i += 2 + segment_length
                        continue
                    elif marker == 0xD8:
                        # Another SOI marker, skip
                        i += 2
                        continue
                    elif marker == 0xD9:
                        # EOI marker, end of image
                        break
                i += 1
        elif img_data[:8] == b'\x89PNG\r\n\x1a\n':
            width = struct.unpack('>I', img_data[16:20])[0]
            height = struct.unpack('>I', img_data[20:24])[0]
            return width, height
    except Exception as e:
        pass
    return None, None

def process_album(album_id, album_title):
    """Process a single album - download images and create activity page"""
    print(f"\n{'='*60}")
    print(f"Processing Album {album_id}: {album_title}")
    print(f"{'='*60}")
    
    # Create activity name from title - handle Unicode properly
    import unicodedata
    # Normalize Unicode and remove special characters
    activity_name = unicodedata.normalize('NFKD', album_title).encode('ascii', 'ignore').decode('ascii')
    activity_name = re.sub(r'[^\w\s-]', '', activity_name).strip()
    activity_name = re.sub(r'[-\s]+', '-', activity_name).lower()
    activity_name = activity_name.replace(' ', '-')
    # If empty after processing, use album ID
    if not activity_name:
        activity_name = f"album-{album_id}"
    
    # Fetch the album page
    album_url = f"http://3.34.255.23/activities/?album={album_id}&album_ses=1"
    print(f"Fetching {album_url}...")
    
    try:
        with urllib.request.urlopen(album_url, timeout=10) as response:
            html = response.read().decode('utf-8', errors='ignore')
    except Exception as e:
        print(f"Error fetching album: {e}")
        return False
    
    # Extract all image URLs from the page
    image_patterns = [
        r'src=["\'](http://3\.34\.255\.23/wp-content/uploads/[^"\']+\.(?:jpg|jpeg|png|JPG|JPEG|PNG))["\']',
        r'href=["\'](http://3\.34\.255\.23/wp-content/uploads/[^"\']+\.(?:jpg|jpeg|png|JPG|JPEG|PNG))["\']',
        r'data-src=["\'](http://3\.34\.255\.23/wp-content/uploads/[^"\']+\.(?:jpg|jpeg|png|JPG|JPEG|PNG))["\']',
        r'data-full-url=["\'](http://3\.34\.255\.23/wp-content/uploads/[^"\']+\.(?:jpg|jpeg|png|JPG|JPEG|PNG))["\']',
        r'data-full-image=["\'](http://3\.34\.255\.23/wp-content/uploads/[^"\']+\.(?:jpg|jpeg|png|JPG|JPEG|PNG))["\']',
        r'data-large-file-url=["\'](http://3\.34\.255\.23/wp-content/uploads/[^"\']+\.(?:jpg|jpeg|png|JPG|JPEG|PNG))["\']',
    ]
    
    all_image_urls = []
    for pattern in image_patterns:
        matches = re.findall(pattern, html, re.IGNORECASE)
        all_image_urls.extend(matches)
    
    unique_urls = list(dict.fromkeys(all_image_urls))
    
    if not unique_urls:
        print(f"No images found in album {album_id}")
        return False
    
    print(f"Found {len(unique_urls)} unique image URLs")
    
    # Filter out thumbnails and get full-size URLs
    def get_full_size_url(url):
        """Try to get full-size URL by removing size suffixes"""
        full_url = re.sub(r'-\d+x\d+\.(jpg|jpeg|png)', r'.\1', url, flags=re.IGNORECASE)
        return full_url
    
    potential_urls = []
    for url in unique_urls:
        if not re.search(r'-\d+x\d+\.', url, re.IGNORECASE):
            potential_urls.append(url)
        else:
            full_url = get_full_size_url(url)
            if full_url not in potential_urls:
                potential_urls.append(full_url)
    
    print(f"Testing {len(potential_urls)} potential full-size URLs...")
    
    # Test each URL and get dimensions
    valid_images = []
    for url in potential_urls:
        try:
            print(f"Testing: {url}")
            with urllib.request.urlopen(url, timeout=10) as img_response:
                img_data = img_response.read()
            
            width, height = get_image_dimensions(img_data)
            if width and height:
                print(f"  Dimensions: {width}x{height}")
                # Calculate aspect ratio
                aspect_ratio = width / height if height > 0 else 0
                # Calculate total pixels
                total_pixels = width * height
                
                # Filter criteria:
                # 1. Must be reasonably large (not thumbnails) - at least 1000 pixels in one dimension
                # 2. Must have reasonable aspect ratio (not too square for banners, not too extreme)
                # 3. Must have sufficient total pixels (at least 500,000 pixels)
                # 4. Exclude small square images (like 512x512 banners)
                is_large_enough = width >= 1000 or height >= 1000
                has_good_aspect = 0.3 <= aspect_ratio <= 3.5  # Reasonable aspect ratios
                has_sufficient_pixels = total_pixels >= 500000
                is_not_small_square = not (width == height and width <= 600)  # Exclude small squares like 512x512
                
                if is_large_enough and has_good_aspect and has_sufficient_pixels and is_not_small_square:
                    valid_images.append({
                        'url': url,
                        'width': width,
                        'height': height,
                        'data': img_data
                    })
                    print(f"  [OK] Valid image")
                else:
                    reasons = []
                    if not is_large_enough:
                        reasons.append("too small")
                    if not has_good_aspect:
                        reasons.append(f"bad aspect ratio ({aspect_ratio:.2f})")
                    if not has_sufficient_pixels:
                        reasons.append("insufficient pixels")
                    if not is_not_small_square:
                        reasons.append("small square (likely banner)")
                    print(f"  [SKIP] {'; '.join(reasons)}")
        except Exception as e:
            print(f"  [ERROR] {e}")
    
    if not valid_images:
        print(f"No valid images found for album {album_id}")
        return False
    
    # Sort by size and take top images
    valid_images.sort(key=lambda x: x['width'] * x['height'], reverse=True)
    image_urls = valid_images[:20]  # Limit to top 20 largest images
    
    print(f"\nSelected {len(image_urls)} images:")
    for i, img in enumerate(image_urls, 1):
        print(f"  {i}. {img['width']}x{img['height']}")
    
    # Download the images
    target_dir = Path(f"assets/img/activities/{activity_name}")
    target_dir.mkdir(parents=True, exist_ok=True)
    
    downloaded_files = []
    for i, img_info in enumerate(image_urls, 1):
        try:
            # Determine file extension from URL
            ext = 'jpg'
            if '.png' in img_info['url'].lower():
                ext = 'png'
            elif '.jpeg' in img_info['url'].lower():
                ext = 'jpeg'
            
            filename = f"{activity_name}-{i}.{ext}"
            filepath = target_dir / filename
            
            with open(filepath, 'wb') as f:
                f.write(img_info['data'])
            
            downloaded_files.append({
                'filename': filename,
                'url': img_info['url'],
                'width': img_info['width'],
                'height': img_info['height']
            })
            print(f"Saved {filename} ({img_info['width']}x{img_info['height']})")
        except Exception as e:
            print(f"Error saving {img_info['url']}: {e}")
    
    # Create the markdown file
    if downloaded_files:
        markdown_file = f"_activities/{activity_name}.md"
        
        # Check if file already exists
        if os.path.exists(markdown_file):
            print(f"\n[SKIP] {markdown_file} already exists, skipping...")
            return True
        
        gallery_id = f"gallery-{activity_name}"
        first_image = downloaded_files[0]['filename']
        
        markdown_content = f"""---
layout: post
title: "{album_title}"
description: "Photos from {album_title}"
img: /assets/img/activities/{activity_name}/{first_image}
importance: 2
category: event
images:
  photoswipe: true
---

<div class="pswp-gallery pswp-gallery--single-column" id="{gallery_id}">
"""
        
        for item in downloaded_files:
            filename = item['filename']
            width = item['width']
            height = item['height']
            markdown_content += f"""  <a href="/assets/img/activities/{activity_name}/{filename}"
    target="_blank" data-pswp-width="{width}" data-pswp-height="{height}">
    <img src="/assets/img/activities/{activity_name}/{filename}" alt="" />
  </a>
"""
        
        markdown_content += "</div>\n"
        
        with open(markdown_file, 'w', encoding='utf-8') as f:
            f.write(markdown_content)
        
        print(f"\n[OK] Created {markdown_file} with {len(downloaded_files)} images.")
        return True
    else:
        print(f"\n[ERROR] No images downloaded for album {album_id}")
        return False

# Main execution
print("Fetching main activities page...")
main_url = "http://3.34.255.23/activities/"
try:
    with urllib.request.urlopen(main_url, timeout=10) as response:
        html = response.read().decode('utf-8', errors='ignore')
except Exception as e:
    print(f"Error fetching main page: {e}")
    exit(1)

# Find all album links - look for patterns like ?album=261 or ?album=269
album_patterns = [
    r'href=["\'][^"\']*\?album=(\d+)[^"\']*["\']',
    r'\?album=(\d+)',
    r'album=(\d+)',
]

all_album_ids = []
for pattern in album_patterns:
    matches = re.findall(pattern, html, re.IGNORECASE)
    all_album_ids.extend(matches)

unique_album_ids = sorted(set(all_album_ids), key=int)
print(f"\nFound {len(unique_album_ids)} unique album IDs: {unique_album_ids}")

# Extract album titles by fetching each album page
album_info = []
print("\nExtracting album titles...")
for album_id in unique_album_ids:
    try:
        album_url = f"http://3.34.255.23/activities/?album={album_id}&album_ses=1"
        with urllib.request.urlopen(album_url, timeout=10) as response:
            album_html = response.read().decode('utf-8', errors='ignore')
        
        # Look for "Main Album »" followed by the title
        title_pattern = r'Main Album\s*[»›]\s*([^<\n]+)'
        title_match = re.search(title_pattern, album_html, re.IGNORECASE)
        if title_match:
            title = title_match.group(1).strip()
            # Clean up title - remove extra whitespace
            title = re.sub(r'\s+', ' ', title)
        else:
            # Fallback: try to find title in h1 or other heading tags
            h1_pattern = r'<h1[^>]*>([^<]+)</h1>'
            h1_match = re.search(h1_pattern, album_html, re.IGNORECASE)
            if h1_match:
                title = h1_match.group(1).strip()
                title = re.sub(r'\s+', ' ', title)
            else:
                # Try to find title in breadcrumb or page title
                breadcrumb_pattern = r'<title>([^<]+)</title>'
                breadcrumb_match = re.search(breadcrumb_pattern, album_html, re.IGNORECASE)
                if breadcrumb_match:
                    title = breadcrumb_match.group(1).strip()
                    # Remove common prefixes
                    title = re.sub(r'^.*?[»›]\s*', '', title, flags=re.IGNORECASE)
                    title = re.sub(r'\s*-\s*.*$', '', title)  # Remove site name suffix
                    title = re.sub(r'\s+', ' ', title).strip()
                else:
                    title = f"Album {album_id}"
        album_info.append((album_id, title))
        print(f"  Album {album_id}: {title}")
    except Exception as e:
        print(f"  Album {album_id}: Error extracting title - {e}")
        album_info.append((album_id, f"Album {album_id}"))

print(f"\nProcessing {len(album_info)} albums...")
print("Note: Existing activity pages will be skipped to avoid overwriting.\n")

successful = 0
failed = 0
skipped = 0

for album_id, album_title in album_info:
    try:
        result = process_album(album_id, album_title)
        if result:
            successful += 1
        else:
            failed += 1
    except Exception as e:
        print(f"Error processing album {album_id}: {e}")
        failed += 1

print(f"\n{'='*60}")
print(f"Summary:")
print(f"  Successful: {successful}")
print(f"  Failed: {failed}")
print(f"  Total: {len(album_info)}")
print(f"{'='*60}")

