#!/usr/bin/env python3
"""
Script to find posts missing images and download them from the website.
"""

import os
import re
import urllib.request
import urllib.parse
from html import unescape
from pathlib import Path
import json

# Map of post titles to vid numbers (based on website listing)
# Maps from post filename patterns or key phrases to vid numbers
TITLE_TO_VID = {
    # 2025 posts
    "uist-2025": 29,
    "uist 2025": 29,
    "best-paper-honorable-mention-chi2025": 28,
    "best paper honorable mention chi2025": 28,
    "best-paper-award-iui2025": 27,
    "best paper award iui2025": 27,
    "2025-chi-lbw": 26,
    "2025 chi lbw": 26,
    "two-papers-accepted-to-acm-chi-2025": 25,
    "two papers accepted to acm chi 2025": 25,
    "acm-iui-2025": 24,
    "acm iui 2025": 24,
    # 2024 posts
    "siggraph-asia-2024": 23,
    "siggraph asia 2024": 23,
    "ismar-2024": 22,
    "ismar 2024": 22,
    "ijhci": 21,
    "eait": 20,
    "new-research-project-funded-by-wiset": 19,
    "new research project funded by wiset": 19,
    "chi-2024-lbw": 18,
    "chi 2024 lbw": 18,
    # 2023 posts
    "kcc-2023": 17,
    "kcc 2023": 17,
    "mobilehci-2023": 16,
    "mobilehci 2023": 16,
    "cvpr-workshop-abaw": 15,
    "cvpr workshop abaw": 15,
    "new-research-project-funded-by-wiset": 14,  # 2023 version
    "new-research-grant-from-nrf": 13,
    "new research grant from nrf": 13,
    "two-papers-accepted-to-2023-acm-chi-as-lbw": 12,
    "two papers accepted to 2023 acm chi as lbw": 12,
    # 2022 posts
    "kird": 11,
    "eccv-workshop": 10,
    "eccv workshop": 10,
    "outstanding-paper-awards": 9,
    "outstanding paper awards": 9,
    "abaw-competition": 8,
    "abaw competition": 8,
    "kird-real-challenge": 7,
    "kird real challenge": 7,
    "ieee-embc-2022": 6,
    "ieee embc 2022": 6,
    "cancers": 5,  # vid=5 for Cancers paper
}

BASE_URL = "http://3.34.255.23/news-2/"
POSTS_DIR = "_posts"
IMAGES_DIR = "assets/img"

def fetch_article_details(vid):
    """Fetch article details from the website."""
    url = f"{BASE_URL}?vid={vid}"
    print(f"Fetching article vid={vid}...")
    
    try:
        with urllib.request.urlopen(url, timeout=10) as response:
            html = response.read().decode('utf-8', errors='ignore')
    except Exception as e:
        print(f"Error fetching {url}: {e}")
        return None
    
    # Try to find content area first, but also search whole page
    content_patterns = [
        r'<div[^>]*class="[^"]*content[^"]*"[^>]*>(.*?)</div>',
        r'<div[^>]*id="[^"]*content[^"]*"[^>]*>(.*?)</div>',
        r'<article[^>]*>(.*?)</article>',
        r'<div[^>]*class="[^"]*post[^"]*"[^>]*>(.*?)</div>',
        r'<div[^>]*class="[^"]*entry[^"]*"[^>]*>(.*?)</div>',
    ]
    
    content_html = html
    for pattern in content_patterns:
        match = re.search(pattern, html, re.DOTALL | re.IGNORECASE)
        if match:
            content_html = match.group(1)
            print(f"  Found content area using pattern")
            break
    
    # Extract images from content - handle both direct URLs and PHP-served images
    # Look for mb-file.php URLs in various attributes
    img_patterns = [
        # Full mb-file.php URLs in src attributes
        r'(?:src|data-src|data-lazy-src|href)=["\']?(http[^"\'>\s]*mb-file\.php\?path=[^"\'>\s&]+)["\']?',
        # mb-file.php URLs without http (relative)
        r'(?:src|data-src|data-lazy-src|href)=["\']?([^"\'>\s]*mb-file\.php\?path=[^"\'>\s&]+)["\']?',
        # Standard img src
        r'<img[^>]+src=["\']([^"\']+)["\']',
        r'<img[^>]+src=([^\s>]+)',
        r'<img[^>]+data-src=["\']([^"\']+)["\']',  # Lazy-loaded images
        r'<img[^>]+data-lazy-src=["\']([^"\']+)["\']',  # Lazy-loaded images (alternative)
        r'background-image:\s*url\(["\']?([^"\')]+)["\']?\)',  # Background images
        # Standalone mb-file.php path patterns
        r'mb-file\.php\?path=([^"\'>\s&]+)',  # PHP-served images - just the path part
        r'wp-content/uploads/([^"\'>\s]+\.(?:jpg|jpeg|png|gif|JPG|JPEG|PNG|GIF))',  # Direct upload paths
    ]
    
    images = []
    for pattern in img_patterns:
        matches = re.findall(pattern, content_html, re.IGNORECASE)
        for img_url in matches:
            # Handle PHP-served images
            if 'mb-file.php' in str(img_url):
                # If it's already a full URL, use it
                if img_url.startswith('http'):
                    img_url = img_url
                # If it starts with mb-file.php, add the base URL
                elif img_url.startswith('mb-file.php') or img_url.startswith('/'):
                    if img_url.startswith('/'):
                        img_url = f"http://ixlab.seoultech.ac.kr{img_url}"
                    else:
                        img_url = f"http://ixlab.seoultech.ac.kr/wp-content/plugins/mangboard/includes/{img_url}"
                # If it's just the path parameter, construct full URL
                elif 'path=' in img_url or not img_url.startswith('http'):
                    if not img_url.startswith('http'):
                        img_url = f"http://ixlab.seoultech.ac.kr/wp-content/plugins/mangboard/includes/mb-file.php?path={img_url}"
                    else:
                        img_url = img_url
            elif not img_url.startswith('http'):
                if img_url.startswith('/'):
                    img_url = f"http://3.34.255.23{img_url}"
                else:
                    # Might be a relative path to uploads
                    if 'wp-content' not in img_url:
                        img_url = f"http://3.34.255.23/wp-content/uploads/{img_url}"
                    else:
                        img_url = f"http://3.34.255.23/{img_url}"
            
            # Clean up the URL
            img_url = img_url.strip('"\'')
            
            # Filter out non-content images (but allow logos if they're from mb-file.php)
            skip_keywords = ['icon', 'button', 'arrow', 'paging', 'avatar', 'wp-admin', 'admin', 'skin', 'bbs_admin', 'mangboard/skins']
            # Don't skip if it's an mb-file.php URL (these are content images)
            if 'mb-file.php' not in img_url.lower():
                if any(skip in img_url.lower() for skip in skip_keywords):
                    continue
            
            # Accept content images
            if any(keyword in img_url.lower() for keyword in ['wp-content', 'upload', 'mb-file.php', 'ixlab.seoultech']):
                images.append(img_url)
                print(f"  Found image: {img_url[:100]}...")
    
    # If no images found in content, try whole page
    if not images:
        print(f"  No images in content area, searching whole page...")
        for pattern in img_patterns:
            matches = re.findall(pattern, html, re.IGNORECASE)
            for img_url in matches:
                # Handle PHP-served images
                if 'mb-file.php' in str(img_url):
                    # If it's already a full URL, use it
                    if img_url.startswith('http'):
                        img_url = img_url
                    # If it starts with mb-file.php, add the base URL
                    elif img_url.startswith('mb-file.php') or img_url.startswith('/'):
                        if img_url.startswith('/'):
                            img_url = f"http://ixlab.seoultech.ac.kr{img_url}"
                        else:
                            img_url = f"http://ixlab.seoultech.ac.kr/wp-content/plugins/mangboard/includes/{img_url}"
                    # If it's just the path parameter, construct full URL
                    elif 'path=' in img_url or not img_url.startswith('http'):
                        if not img_url.startswith('http'):
                            img_url = f"http://ixlab.seoultech.ac.kr/wp-content/plugins/mangboard/includes/mb-file.php?path={img_url}"
                        else:
                            img_url = img_url
                elif not img_url.startswith('http'):
                    if img_url.startswith('/'):
                        img_url = f"http://3.34.255.23{img_url}"
                    else:
                        img_url = f"http://3.34.255.23/{img_url}"
                
                img_url = img_url.strip('"\'')
                
                # Filter out non-content images (but allow logos if they're from mb-file.php)
                skip_keywords = ['icon', 'button', 'arrow', 'paging', 'avatar', 'wp-admin', 'admin', 'skin', 'bbs_admin', 'mangboard/skins']
                # Don't skip if it's an mb-file.php URL (these are content images)
                if 'mb-file.php' not in img_url.lower():
                    if any(skip in img_url.lower() for skip in skip_keywords):
                        continue
                
                if any(keyword in img_url.lower() for keyword in ['wp-content', 'upload', 'mb-file.php', 'ixlab.seoultech']):
                    images.append(img_url)
                    print(f"  Found image in whole page: {img_url[:100]}...")
    
    # Remove duplicates while preserving order
    seen = set()
    unique_images = []
    for img in images:
        if img not in seen:
            seen.add(img)
            unique_images.append(img)
    
    return unique_images if unique_images else None

def download_image(img_url, save_path):
    """Download an image from URL and save it."""
    try:
        print(f"  Downloading image: {img_url}")
        with urllib.request.urlopen(img_url, timeout=10) as response:
            # Check content type
            content_type = response.headers.get('Content-Type', '')
            data = response.read()
            
            # Determine extension
            if 'jpeg' in content_type or 'jpg' in content_type:
                ext = '.jpg'
            elif 'png' in content_type:
                ext = '.png'
            elif 'gif' in content_type:
                ext = '.gif'
            else:
                # Check first bytes
                if data.startswith(b'\xff\xd8\xff'):
                    ext = '.jpg'
                elif data.startswith(b'\x89PNG'):
                    ext = '.png'
                elif data.startswith(b'GIF'):
                    ext = '.gif'
                else:
                    ext = '.jpg'  # default
            
            # Update save_path with correct extension
            save_path = str(save_path).rsplit('.', 1)[0] + ext
            
            # Save image
            os.makedirs(os.path.dirname(save_path), exist_ok=True)
            with open(save_path, 'wb') as f:
                f.write(data)
            
            print(f"  Saved: {save_path}")
            return save_path
    except Exception as e:
        print(f"  Error downloading image {img_url}: {e}")
        return None

def get_image_dimensions(image_path):
    """Get image dimensions using Pillow if available."""
    try:
        from PIL import Image
        with Image.open(image_path) as img:
            return img.size  # (width, height)
    except ImportError:
        return None
    except Exception:
        return None

def update_post_with_image(post_path, image_path, date_str):
    """Update a post to include an image."""
    with open(post_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Extract front matter
    front_matter_match = re.match(r'^---\n(.*?)\n---\n', content, re.DOTALL)
    if not front_matter_match:
        return False
    
    front_matter = front_matter_match.group(1)
    body = content[front_matter_match.end():].strip()
    
    # Check if image already exists
    if 'thumbnail:' in front_matter or 'include figure' in body:
        print(f"  Post already has image, skipping...")
        return False
    
    # Add thumbnail to front matter
    if 'thumbnail:' not in front_matter:
        front_matter += f"\nthumbnail: {image_path}"
    
    # Get image dimensions
    full_image_path = os.path.join(os.path.dirname(post_path), '..', image_path)
    full_image_path = os.path.normpath(full_image_path)
    dimensions = get_image_dimensions(full_image_path)
    
    # Determine max-width
    max_width = ""
    if dimensions and dimensions[0] < 800:
        max_width = f' max-width="{dimensions[0]}px"'
    
    # Add image at the top of body
    image_include = f'''<div class="row mt-3">
    <div class="col-sm mt-3 mt-md-0">
        {{% include figure.liquid loading="eager" path="{image_path}" class="rounded z-depth-1"{max_width} %}}
    </div>
</div>

'''
    
    new_body = image_include + body
    
    # Write updated content
    new_content = f"---\n{front_matter}\n---\n\n{new_body}"
    with open(post_path, 'w', encoding='utf-8') as f:
        f.write(new_content)
    
    print(f"  Updated post with image")
    return True

def main():
    """Main function to process all posts."""
    posts_dir = Path(POSTS_DIR)
    images_dir = Path(IMAGES_DIR)
    
    # Find all markdown posts
    post_files = list(posts_dir.glob("*.md"))
    
    posts_missing_images = []
    
    # Check which posts are missing images
    for post_file in post_files:
        if post_file.name == "2015-05-15-images.md":
            continue  # Skip reference file
        
        with open(post_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Check if post has thumbnail or figure include
        has_thumbnail = 'thumbnail:' in content
        has_figure = 'include figure' in content
        
        if not has_thumbnail and not has_figure:
            # Extract title from front matter
            title_match = re.search(r'^title:\s*(.+)$', content, re.MULTILINE)
            if title_match:
                title = title_match.group(1).strip()
                posts_missing_images.append((post_file, title))
                print(f"Missing image: {post_file.name} - {title}")
    
    print(f"\nFound {len(posts_missing_images)} posts missing images\n")
    
    # Process each post
    for post_file, title in posts_missing_images:
        print(f"\nProcessing: {post_file.name}")
        print(f"Title: {title}")
        
        # Direct filename to vid mapping for known posts
        FILENAME_TO_VID = {
            "one-paper-accepted-to-uist-2025-poster-track": 29,
            "received-best-paper-honorable-mention-for-chi2025-paper": 28,
            "received-best-paper-award-for-iui2025-paper": 27,
            "one-paper-accepted-to-2025-chi-lbw": 26,
            "two-papers-accepted-to-acm-chi-2025": 25,
            "one-paper-accepted-to-acm-iui-2025": 24,
            "one-paper-accepted-to-siggraph-asia-2024-as-poster": 23,
            "one-paper-accepted-to-ismar-2024": 22,
            "our-paper-accepted-to-ijhci-if47-219": 21,
            "our-paper-accecpted-to-eait-if-55-69": 20,
            "new-research-project-funded-by-wiset": 19,  # 2024
            "one-paper-accepted-to-chi-2024-lbw": 18,
            "received-two-outstanding-papers-from-kcc-2023": 17,
            "one-paper-accepted-to-mobilehci-2023": 16,
            "one-paper-accepted-to-cvpr-workshop-abaw": 15,
            "new-research-project-funded-by-wiset": 14,  # 2023
            "new-research-grant-from-nrf": 13,
            "two-papers-accepted-to-2023-acm-chi-as-lbw": 12,
            "received-outstanding-technology-award-from-kird-competition": 11,
            "one-paper-accepted-to-eccv-workshop-on-affective-behavior-analysis-in-the-wild": 10,
            "received-two-outstanding-paper-awards": 9,
            "won-3rd-place-at-4th-abaw-competition-eccv2022": 8,
            "new-funding-granted-by-kird-real-challenge-2022-project": 7,
            "one-paper-accepted-to-ieee-embc-2022": 6,
            "one-paper-accepted-to-cancers-sci-if6639": 5,
        }
        
        # Find vid number by matching filename patterns
        vid = None
        
        # Get filename without extension and date
        filename_base = post_file.stem  # e.g., "2025-08-05-one-paper-accepted-to-uist-2025-poster-track"
        filename_parts = filename_base.split('-', 3)  # Remove date
        if len(filename_parts) >= 4:
            filename_key = '-'.join(filename_parts[3:])  # Everything after date
        else:
            filename_key = filename_base
        
        # Try direct mapping first
        if filename_key in FILENAME_TO_VID:
            vid = FILENAME_TO_VID[filename_key]
            print(f"  Matched filename directly to vid={vid}")
        
        # If direct mapping didn't work, try pattern matching
        if not vid:
            # Normalize for matching
            def normalize(s):
                return re.sub(r'[^\w\s-]', '', s.lower()).strip()
            
            filename_normalized = normalize(filename_key)
            title_normalized = normalize(title)
            
            # First try exact filename match
            for key, value in TITLE_TO_VID.items():
                key_normalized = normalize(key)
                if key_normalized in filename_normalized or filename_normalized in key_normalized:
                    vid = value
                    print(f"  Matched filename pattern to vid={vid}")
                    break
            
            # Then try title match
            if not vid:
                for key, value in TITLE_TO_VID.items():
                    key_normalized = normalize(key)
                    # Check if key phrases are in title
                    if key_normalized in title_normalized or title_normalized in key_normalized:
                        vid = value
                        print(f"  Matched title to vid={vid}")
                        break
            
            # Try word-based matching
            if not vid:
                title_words = set(title_normalized.split())
                for key, value in TITLE_TO_VID.items():
                    key_normalized = normalize(key)
                    key_words = set(key_normalized.split())
                    common_words = title_words & key_words
                    # If 2+ significant words match, consider it
                    if len(common_words) >= 2 and len(key_words) <= 5:
                        vid = value
                        print(f"  Matched title (word-based) to vid={vid}")
                        break
        
        if not vid:
            print(f"  Could not determine vid number for: {filename_key}")
            print(f"  Title: {title}")
            print(f"  Skipping...")
            continue
        
        # Fetch article images
        images = fetch_article_details(vid)
        if not images:
            print(f"  No images found for vid={vid}")
            continue
        
        # Download first image
        img_url = images[0]
        date_match = re.search(r'(\d{4}-\d{2}-\d{2})', post_file.name)
        date_str = date_match.group(1) if date_match else "unknown"
        
        # Generate image filename
        img_filename = f"news-{date_str.replace('-', '')}-1"
        img_save_path = images_dir / img_filename
        
        downloaded_path = download_image(img_url, img_save_path)
        if downloaded_path:
            # Get relative path for post
            rel_img_path = f"assets/img/{os.path.basename(downloaded_path)}"
            update_post_with_image(post_file, rel_img_path, date_str)

if __name__ == "__main__":
    main()

