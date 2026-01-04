
import os
import struct
import re
import glob
from pathlib import Path
import traceback

try:
    from PIL import Image, ExifTags
    HAS_PIL = True
except ImportError:
    HAS_PIL = False

def get_image_dimensions(file_path):
    """Get image dimensions from JPEG or PNG file given a file path"""
    if HAS_PIL:
        try:
            with Image.open(file_path) as img:
                width, height = img.width, img.height
                # Handle EXIF orientation
                try:
                    exif = img._getexif()
                    if exif:
                        for tag, value in exif.items():
                            if tag in ExifTags.TAGS:
                                if ExifTags.TAGS[tag] == 'Orientation':
                                    if value in [5, 6, 7, 8]:
                                        width, height = height, width
                                    break
                except Exception:
                    pass # No EXIF or error reading it
                return width, height
        except Exception as e:
            print(f"PIL Error reading {file_path}: {e}")
            # Fallback will happen below
    
    with open(file_path, 'rb') as f:
        img_data = f.read()
    
    try:
        if img_data[:2] == b'\xff\xd8':
            # JPEG format
            i = 2
            while i < len(img_data) - 9:
                if img_data[i] == 0xFF:
                    marker = img_data[i+1]
                    if marker in [0xC0, 0xC1, 0xC2, 0xC3, 0xC5, 0xC6, 0xC7, 0xC9, 0xCA, 0xCB, 0xCD, 0xCE, 0xCF]:
                        height = struct.unpack('>H', img_data[i+5:i+7])[0]
                        width = struct.unpack('>H', img_data[i+7:i+9])[0]
                        return width, height
                    elif marker == 0xE0 or (marker >= 0xE1 and marker <= 0xEF):
                        segment_length = struct.unpack('>H', img_data[i+2:i+4])[0]
                        i += 2 + segment_length
                        continue
                    elif marker == 0xD8:
                        i += 2
                        continue
                    elif marker == 0xD9:
                        break
                i += 1
        elif img_data[:8] == b'\x89PNG\r\n\x1a\n':
            width = struct.unpack('>I', img_data[16:20])[0]
            height = struct.unpack('>I', img_data[20:24])[0]
            return width, height
    except Exception as e:
        print(f"Error reading dimensions for {file_path}: {e}")
        pass
    return None, None

def process_activity(activity_name, md_file_path):
    print(f"Processing {activity_name}...")
    
    # Paths
    base_dir = Path("d:/lab-web/st-ixlab.github.io")
    img_dir = base_dir / "assets/img/activities" / activity_name
    md_file = base_dir / md_file_path
    
    if not img_dir.exists():
        print(f"Directory not found: {img_dir}")
        return

    # 1. Identify files - Use set for unique files on Windows (case insensitive glob)
    unique_files = set()
    for ext in ['*.jpg', '*.jpeg', '*.png', '*.JPG', '*.JPEG', '*.PNG']:
        for f in img_dir.glob(ext):
            unique_files.add(str(f.resolve()).lower())
            
    files = []
    # Convert back to Path objects
    for f_str in unique_files:
        files.append(Path(f_str))
    
    if not files:
        print(f"No images found in {img_dir}")
        return

    # Sort files
    files.sort(key=lambda x: x.name)
    
    print(f"Found {len(files)} unique images")

    # 2. Generate HTML
    gallery_html = ""
    for file_path in files:
        width, height = get_image_dimensions(file_path)
        filename = file_path.name
        if width and height:
             gallery_html += f"""  <a href="/assets/img/activities/{activity_name}/{filename}"
    target="_blank" data-pswp-width="{width}" data-pswp-height="{height}">
    <img src="/assets/img/activities/{activity_name}/{filename}" alt="" />
  </a>
"""
        else:
             print(f"Could not get dimensions for {filename}")

    # 3. Update Markdown
    if md_file.exists():
        with open(md_file, 'r', encoding='utf-8') as f:
            content = f.read()
            
        gallery_id = f"gallery-{activity_name}"
        pattern = rf'(<div[^>]*id="{gallery_id}"[^>]*>)(.*?)(</div>)'
        
        if re.search(pattern, content, re.DOTALL):
            new_content = re.sub(pattern, rf'\1\n{gallery_html}\3', content, flags=re.DOTALL)
            
            # Update main image (img: ...) to the first image ONLY IF NOT MANUALLY SET
            # But "manually set" is hard to distinguish from "previous first image".
            # Safest is to NOT update 'img:' if it already exists, assuming user might have changed it.
            # But previously the script DID update it.
            # If we want to reflect the FIRST image as thumbnail, we should update it.
            # BUT user manually changed it in KCC / UIST.
            # For KSC, if we add new images, maybe the first one changes?
            # KSC files: album-2025-ksc-1.jpg ...
            # ksc5.jpg triggers alphabetical sort? 'album' comes before 'ksc'.
            # So album-2025-ksc-1.jpg will likely remain first. 
            # So updating it to first image is fine, it will be the same image.
            
            if files:
                 first_image_path = f"/assets/img/activities/{activity_name}/{files[0].name}"
                 # Check if current img is different and effectively "custom"?
                 # Actually, let's just make sure we update it for THIS run on KSC.
                 # For general robustness, we could try to see if 'img:' points to a file that exists.
                 # Let's just update it. The risk is if I run this on UIST/KCC, I overwrite user changes.
                 # Since I am ONLY running on KSC below, it is safe to leave the logic, 
                 # provided I don't call process_activity on UIST/KCC.
                 
                 new_content = re.sub(r'img: .*', f'img: {first_image_path}', new_content)
            
            with open(md_file, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f"Updated {md_file} with {len(files)} images")
        else:
            print(f"Could not find gallery div with id {gallery_id}")

if __name__ == "__main__":
    try:
        if HAS_PIL:
            print("Using PIL for image dimensions.")
        else:
            print("PIL not found, using fallback parser.")

        # ONLY process KSC as requested
        process_activity("2025-ksc", "_activities/2025-ksc.md")
        
    except Exception as e:
        print(f"Fatal error: {e}")
        traceback.print_exc()
