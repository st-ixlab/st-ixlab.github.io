import urllib.request
import re
import os
from pathlib import Path

def extract_album_title(album_id):
    """Extract the actual title from an album page"""
    import html
    import unicodedata
    album_url = f"http://3.34.255.23/activities/?album={album_id}&album_ses=1"
    try:
        with urllib.request.urlopen(album_url, timeout=10) as response:
            html_content = response.read().decode('utf-8', errors='ignore')
        
        # Primary pattern: "Main Album</a> &raquo; [Title]" or "Main Album » [Title]"
        # Handle both HTML entity &raquo; and actual » character
        title_patterns = [
            r'Main Album</a>\s*&raquo;\s*([^<\n]+)',  # Main Album</a> &raquo; Title
            r'Main Album</a>\s*[»›]\s*([^<\n]+)',  # Main Album</a> » Title
            r'Main Album[^<]*[»›]\s*([^<\n]+)',  # Main Album ... » Title
            r'Main Album\s*&raquo;\s*([^<\n]+)',  # Main Album &raquo; Title
            r'Main Album\s*[»›]\s*([^<\n]+)',  # Main Album » Title
        ]
        
        for title_pattern in title_patterns:
            match = re.search(title_pattern, html_content, re.IGNORECASE)
            if match:
                title = match.group(1).strip()
                # Decode HTML entities
                title = html.unescape(title)
                # Clean up the title - remove any trailing HTML tags or entities
                title = re.sub(r'<[^>]+>', '', title)  # Remove any HTML tags
                title = re.sub(r'\s+', ' ', title)  # Normalize whitespace
                title = title.strip()
                if title and len(title) > 1:  # Make sure we got something
                    return title
        
        return None
    except Exception as e:
        print(f"  Error fetching album {album_id}: {e}")
        return None

def create_activity_name_from_title(title):
    """Create a URL-friendly activity name from a title"""
    import unicodedata
    # Normalize Unicode and remove special characters
    activity_name = unicodedata.normalize('NFKD', title).encode('ascii', 'ignore').decode('ascii')
    activity_name = re.sub(r'[^\w\s-]', '', activity_name).strip()
    activity_name = re.sub(r'[-\s]+', '-', activity_name).lower()
    activity_name = activity_name.replace(' ', '-')
    # Remove leading/trailing hyphens
    activity_name = activity_name.strip('-')
    return activity_name

def update_activity_file(filepath, new_title, new_activity_name, old_activity_name):
    """Update the title and activity name in an activity markdown file"""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Update the title in front matter
        title_pattern = r'^title:\s*["\']([^"\']+)["\']'
        new_content = re.sub(title_pattern, f'title: "{new_title}"', content, flags=re.MULTILINE)
        
        # Update description
        desc_pattern = r'^description:\s*["\']([^"\']+)["\']'
        new_desc = f'description: "Photos from {new_title}"'
        new_content = re.sub(desc_pattern, new_desc, new_content, flags=re.MULTILINE)
        
        # Update image paths and gallery ID to use new activity name
        # Update img path
        img_pattern = rf'/assets/img/activities/{re.escape(old_activity_name)}/'
        new_content = re.sub(img_pattern, f'/assets/img/activities/{new_activity_name}/', new_content)
        
        # Update gallery ID
        gallery_id_pattern = rf'id=["\']gallery-{re.escape(old_activity_name)}["\']'
        new_content = re.sub(gallery_id_pattern, f'id="gallery-{new_activity_name}"', new_content)
        
        # Update all image href and src paths
        href_pattern = rf'href=["\']/assets/img/activities/{re.escape(old_activity_name)}/'
        new_content = re.sub(href_pattern, f'href="/assets/img/activities/{new_activity_name}/', new_content)
        
        src_pattern = rf'src=["\']/assets/img/activities/{re.escape(old_activity_name)}/'
        new_content = re.sub(src_pattern, f'src="/assets/img/activities/{new_activity_name}/', new_content)
        
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        
        return True
    except Exception as e:
        print(f"  Error updating {filepath}: {e}")
        return False

def rename_files_and_directories(old_activity_name, new_activity_name):
    """Rename markdown file and image directory"""
    activities_dir = Path("_activities")
    img_dir = Path("assets/img/activities")
    
    old_md_file = activities_dir / f"{old_activity_name}.md"
    new_md_file = activities_dir / f"{new_activity_name}.md"
    
    old_img_dir = img_dir / old_activity_name
    new_img_dir = img_dir / new_activity_name
    
    renamed = []
    
    # Rename markdown file
    if old_md_file.exists():
        if new_md_file.exists() and new_md_file != old_md_file:
            print(f"  Warning: Target markdown file {new_md_file.name} already exists, skipping rename")
        else:
            try:
                old_md_file.rename(new_md_file)
                renamed.append(('md_file', str(old_md_file), str(new_md_file)))
                print(f"  Renamed: {old_md_file.name} -> {new_md_file.name}")
            except Exception as e:
                print(f"  Error renaming markdown file: {e}")
                return None, renamed
    else:
        print(f"  Warning: Markdown file {old_md_file} does not exist")
    
    # Rename image directory
    if old_img_dir.exists():
        if new_img_dir.exists() and new_img_dir != old_img_dir:
            print(f"  Warning: Target image directory {new_img_dir.name} already exists, skipping rename")
        else:
            try:
                old_img_dir.rename(new_img_dir)
                renamed.append(('img_dir', str(old_img_dir), str(new_img_dir)))
                print(f"  Renamed: {old_img_dir.name}/ -> {new_img_dir.name}/")
            except Exception as e:
                print(f"  Error renaming image directory: {e}")
                return None, renamed
    else:
        print(f"  Warning: Image directory {old_img_dir} does not exist")
    
    return new_md_file if old_md_file.exists() else old_md_file, renamed

# Main execution
activities_dir = Path("_activities")
album_files = list(activities_dir.glob("album-*.md"))

print(f"Found {len(album_files)} album activity files to update\n")

updated = 0
failed = 0
skipped = 0

for filepath in sorted(album_files):
    # Extract album ID from filename
    match = re.search(r'album-(\d+)\.md', filepath.name)
    if not match:
        print(f"[SKIP] {filepath.name} - couldn't extract album ID")
        skipped += 1
        continue
    
    album_id = match.group(1)
    print(f"Processing album {album_id}...")
    
    # Extract the actual title
    title = extract_album_title(album_id)
    
    if title:
        print(f"  Found title: {title}")
        # Create activity name from title
        new_activity_name = create_activity_name_from_title(title)
        # If activity name is empty or too short, use album ID as fallback
        if not new_activity_name or len(new_activity_name) < 3:
            new_activity_name = f"album-{album_id}"
            print(f"  Warning: Generated activity name is too short, using fallback: {new_activity_name}")
        else:
            print(f"  Generated activity name: {new_activity_name}")
        
        old_activity_name = filepath.stem  # e.g., "album-1523"
        
        # Skip if already renamed
        if old_activity_name == new_activity_name:
            print(f"  [SKIP] Already using correct name: {old_activity_name}")
            skipped += 1
            continue
        
        # First rename files and directories
        new_filepath, renamed_items = rename_files_and_directories(old_activity_name, new_activity_name)
        
        if new_filepath is None:
            print(f"  [ERROR] Failed to rename files/directories")
            failed += 1
            continue
        
        # Update the content of the (possibly renamed) file
        if update_activity_file(new_filepath, title, new_activity_name, old_activity_name):
            print(f"  [OK] Updated and renamed {old_activity_name} -> {new_activity_name}")
            updated += 1
        else:
            print(f"  [ERROR] Failed to update {new_filepath.name}")
            failed += 1
    else:
        print(f"  [SKIP] Could not extract title for album {album_id}")
        skipped += 1

print(f"\n{'='*60}")
print(f"Summary:")
print(f"  Updated: {updated}")
print(f"  Failed: {failed}")
print(f"  Skipped: {skipped}")
print(f"  Total: {len(album_files)}")
print(f"{'='*60}")

