import os
import re

posts_dir = r"d:\lab-web\st-ixlab.github.io\_posts"
categories_map = {
    "publication": ["accepted", "paper"],
    "award": ["award", "won", "place", "received"],
    "grant": ["fund", "grant", "project"]
}

def get_category(filename):
    lower_name = filename.lower()
    for cat, keywords in categories_map.items():
        if any(k in lower_name for k in keywords):
            return cat
    return "news"

for filename in os.listdir(posts_dir):
    if not filename.endswith(".md"):
        continue
        
    filepath = os.path.join(posts_dir, filename)
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()
        
    category = get_category(filename)
    
    # Regex to replace 'categories: news' or similar
    # Assumes 'categories: ...' exists.
    new_content = re.sub(r"^categories:.*$", f"categories: {category}", content, flags=re.MULTILINE)
    
    if new_content != content:
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(new_content)
        print(f"Updated {filename} to category: {category}")
    else:
        print(f"Skipped {filename} (no change or pattern not found)")
