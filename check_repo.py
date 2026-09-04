import os
import re
import yaml
from pathlib import Path

posts_dir = Path("_posts")
assets_dir = Path("assets")

# Find all internal links like [text](/path) or [text](path) or [text](http://ernie55ernie.github.io/path)
link_pattern = re.compile(r'\[.*?\]\((?!http|mailto)(.*?)\)')
site_link_pattern = re.compile(r'\[.*?\]\(https?://ernie55ernie.github.io(.*?)\)')

issues = []

for filepath in posts_dir.glob("*.md"):
    content = filepath.read_text(encoding="utf-8")
    
    # Check front matter
    if content.startswith("---"):
        parts = content.split("---", 2)
        if len(parts) >= 3:
            front_matter = parts[1]
            try:
                yaml.safe_load(front_matter)
            except yaml.YAMLError as e:
                issues.append(f"{filepath}: YAML Error in front matter: {e}")
        else:
            issues.append(f"{filepath}: Malformed front matter boundaries")
    else:
        issues.append(f"{filepath}: Missing front matter")
        
    # Check internal links
    for match in link_pattern.finditer(content):
        link = match.group(1)
        if link.startswith("#"): continue
        link = link.split("#")[0] # remove fragment
        if link == "": continue
        
        # very basic check: if it's an asset, does it exist?
        if link.startswith("/assets/") or link.startswith("assets/"):
            asset_path = link.lstrip("/")
            if not os.path.exists(asset_path):
                issues.append(f"{filepath}: Broken asset link '{link}'")
                
    # Check absolute internal site links
    for match in site_link_pattern.finditer(content):
        link = match.group(1)
        # these are usually routes, harder to verify without building, but let's just log them to see if any stand out
        pass

if not issues:
    print("No immediate YAML or missing asset issues found.")
else:
    for issue in issues:
        print(issue)
