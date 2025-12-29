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

# Fetch the page
album_url = "http://3.34.255.23/activities/?album=261&album_ses=1"
print(f"Fetching {album_url}...")
with urllib.request.urlopen(album_url, timeout=10) as response:
    html = response.read().decode('utf-8', errors='ignore')

# Find the div with id="aigpl-gallery-2"
gallery_match = re.search(r'<div[^>]*id=["\']aigpl-gallery-2["\'][^>]*>(.*?)</div>', html, re.DOTALL | re.IGNORECASE)
if not gallery_match:
    print("Could not find div with id='aigpl-gallery-2'")
    # Try alternative pattern
    gallery_match = re.search(r'id=["\']aigpl-gallery-2["\']', html, re.IGNORECASE)
    if gallery_match:
        # Get content after the id attribute
        start_pos = gallery_match.end()
        # Find the closing div tag
        div_content = html[start_pos:]
        # Look for images in this section
        print("Found aigpl-gallery-2, searching for images...")
    else:
        print("Could not find aigpl-gallery-2 at all")
        exit(1)
else:
    div_content = gallery_match.group(1)
    print(f"Found div with id='aigpl-gallery-2', content length: {len(div_content)}")

# Extract all image URLs from the gallery div
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
    matches = re.findall(pattern, div_content if 'div_content' in locals() else html, re.IGNORECASE)
    all_image_urls.extend(matches)

unique_urls = list(set(all_image_urls))
print(f"\nFound {len(unique_urls)} unique image URLs in gallery:")

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
        print(f"\nTesting: {url}")
        with urllib.request.urlopen(url, timeout=10) as img_response:
            img_data = img_response.read()
        
        width, height = get_image_dimensions(img_data)
        if width and height:
            print(f"  Dimensions: {width}x{height}")
            if width >= 5000 or height >= 2000:
                valid_images.append({
                    'url': url,
                    'width': width,
                    'height': height,
                    'data': img_data
                })
                print(f"  [OK] Valid large image")
            else:
                print(f"  [SKIP] Too small")
    except Exception as e:
        print(f"  [ERROR] {e}")

# Sort by size and take top 5
valid_images.sort(key=lambda x: x['width'] * x['height'], reverse=True)
image_urls = valid_images[:5]

print(f"\n\nSelected {len(image_urls)} large images:")
for i, img in enumerate(image_urls, 1):
    print(f"  {i}. {img['width']}x{img['height']} - {img['url']}")

# Download the images
target_dir = Path("assets/img/activities/2016-winter-conference")
target_dir.mkdir(parents=True, exist_ok=True)

downloaded_files = []
for i, img_info in enumerate(image_urls, 1):
    try:
        filename = f"winter-conf-{i}.jpg"
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

# Update the markdown file
markdown_file = "_activities/2016-winter-conference.md"
if os.path.exists(markdown_file) and downloaded_files:
    with open(markdown_file, 'r', encoding='utf-8') as f:
        md_content = f.read()
    
    # Find and replace each image entry with correct dimensions
    for i, item in enumerate(downloaded_files, 1):
        filename = item['filename']
        width = item['width']
        height = item['height']
        local_path = f"/assets/img/activities/2016-winter-conference/{filename}"
        
        def replace_dims(match, w=width, h=height):
            return f'{match.group(1)}{w}{match.group(2)}{h}{match.group(3)}'
        
        pattern = rf'(<a href="{re.escape(local_path)}"\s+data-pswp-width=")\d+("\s+data-pswp-height=")\d+(")'
        md_content = re.sub(pattern, replace_dims, md_content)
    
    with open(markdown_file, 'w', encoding='utf-8') as f:
        f.write(md_content)
    print(f"\n[OK] Updated {markdown_file} with correct image dimensions.")
else:
    print(f"\n[ERROR] Markdown file {markdown_file} not found or no images downloaded.")

print("\nDownloaded files with dimensions:")
for item in downloaded_files:
    print(f"  {item['filename']}: {item['width']}x{item['height']}")

