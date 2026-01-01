import os
import re

posts_dir = r"d:\lab-web\st-ixlab.github.io\_posts"

# Regex for keywords to highlight (bold)
# Venues and Agencies
venues_agencies = r"(ACM|IEEE|CHI|IUI|CVPR|ECCV|UIST|ISMAR|MobileHCI|CSCW|DIS|IMWUT|ToCHI|TVCG|VR|Siggraph|NeurIPS|ICLR|AAAI|KCC|HCIK|WISET|NRF|IITP|KIRD|ABAW)"
# Action words and Types
actions_types = r"(Accepted|Best Paper|Honorable Mention|Award|Funded|Grant|Project|Outstanding|Technology|Poster|LBW|Full Paper)"

# Compile regex with ignore case for matching, but we want to preserve case in replacement usually,
# or just bold the matched text.
highlight_pattern = re.compile(f"({venues_agencies}|{actions_types})", re.IGNORECASE)

def get_emoji_and_type(text):
    lower_text = text.lower()
    if any(k in lower_text for k in ["award", "won", "place", "received"]):
        return "🏆", "award"
    elif any(k in lower_text for k in ["fund", "grant", "project"]):
        return "💰", "grant"
    elif any(k in lower_text for k in ["paper", "accepted", "poster"]):
        return "📄", "publication"
    return "📢", "news"

def highlight_keywords(text):
    # Function to wrap matched text in ** **
    # We use a lambda to bold exactly what was matched to preserve case
    return highlight_pattern.sub(lambda m: f"**{m.group(1)}**", text)

for filename in os.listdir(posts_dir):
    if not filename.endswith(".md"):
        continue
        
    filepath = os.path.join(posts_dir, filename)
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()
    
    # Extract title
    title_match = re.search(r"^title:\s*(.*)$", content, re.MULTILINE)
    if not title_match:
        print(f"Skipping {filename}: No title found")
        continue

    original_title = title_match.group(1).strip()
    # Remove existing quotes if any
    original_title = original_title.strip('"').strip("'")
    
    # Check if already processed (has emoji)
    if original_title.startswith(("🏆", "💰", "📄", "📢")):
        print(f"Skipping {filename}: Already has emoji")
        continue

    emoji, _ = get_emoji_and_type(original_title + " " + filename)
    
    # Highlight keywords in the title text
    new_title_text = highlight_keywords(original_title)
    
    # Construct new title line
    # Escape double quotes if present in text
    new_title_text_escaped = new_title_text.replace('"', '\\"')
    new_title_line = f'title: "{emoji} {new_title_text_escaped}"'
    
    # Replace in content
    new_content = content.replace(title_match.group(0), new_title_line)
    
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(new_content)
    
    print(f"Updated {filename}:\n  Old: {original_title}\n  New: {emoji} {new_title_text}")
