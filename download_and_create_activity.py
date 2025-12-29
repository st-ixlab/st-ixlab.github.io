import urllib.request
import re
import os
import struct
from pathlib import Path

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

# Configuration
album_url = "http://3.34.255.23/activities/?album=269&album_ses=1"
activity_name = "2017-nvidia-deep-learning-day"
activity_title = "2017 Nvidia Deep Learning Day"
activity_description = "Photos from 2017 Nvidia Deep Learning Day"
target_dir = Path(f"assets/img/activities/{activity_name}")
markdown_file = f"_activities/{activity_name}.md"

print(f"Fetching {album_url}...")
with urllib.request.urlopen(album_url, timeout=10) as response:
    html = response.read().decode('utf-8', errors='ignore')

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

unique_urls = list(dict.fromkeys(all_image_urls))  # Preserve order while removing duplicates

if not unique_urls:
    print("No images found on the page")
    exit(1)

print(f"\nFound {len(unique_urls)} unique image URLs")

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

print(f"\nTesting {len(potential_urls)} potential full-size URLs...")

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

# Sort by size and take top images (or all if less than 20)
valid_images.sort(key=lambda x: x['width'] * x['height'], reverse=True)
image_urls = valid_images[:20]  # Limit to top 20 largest images

print(f"\n\nSelected {len(image_urls)} images:")
for i, img in enumerate(image_urls, 1):
    print(f"  {i}. {img['width']}x{img['height']} - {img['url']}")

# Download the images
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
        
        filename = f"nvidia-dl-day-{i}.{ext}"
        filepath = target_dir / filename
        
        with open(filepath, 'wb') as f:
            f.write(img_info['data'])
        
        downloaded_files.append({
            'filename': filename,
            'url': img_info['url'],
            'width': img_info['width'],
            'height': img_info['height']
        })
        print(f"\nSaved {filename} ({img_info['width']}x{img_info['height']})")
    except Exception as e:
        print(f"Error saving {img_info['url']}: {e}")

# Create the markdown file
if downloaded_files:
    gallery_id = f"gallery-{activity_name}"
    first_image = downloaded_files[0]['filename']
    
    markdown_content = f"""---
layout: post
title: "{activity_title}"
description: "{activity_description}"
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
    print(f"\nDownloaded files with dimensions:")
    for item in downloaded_files:
        print(f"  {item['filename']}: {item['width']}x{item['height']}")
else:
    print(f"\n[ERROR] No images downloaded.")

print("\nAll done!")

