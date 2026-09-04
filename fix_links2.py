import re
import sys

def fix_file(filepath):
    with open(filepath, 'r') as f:
        content = f.read()
    
    # 1. Fix the escaped brackets I added in rag.md: \[ and \]
    content = content.replace('\\[', '(').replace('\\]', ')')
    
    # 2. Fix | in link texts in cpi.md and others.
    def replace_pipe(m):
        text = m.group(1).replace('|', '-')
        url = m.group(2)
        return f"[{text}]({url})"
        
    content = re.sub(r'\[([^\]]+)\]\((https?://[^)]+)\)', replace_pipe, content)
    
    # 3. Check for any remaining literal '[' or ']' inside the text part of a link
    content = content.replace('[[', '[(').replace(']]', ')]')
    
    with open(filepath, 'w') as f:
        f.write(content)

for filepath in [
    '/Users/ernie.chang/Documents/ernie/ernie55ernie.github.io/_posts/2026-08-12-fed.md',
    '/Users/ernie.chang/Documents/ernie/ernie55ernie.github.io/_posts/2026-08-13-rag.md',
    '/Users/ernie.chang/Documents/ernie/ernie55ernie.github.io/_posts/2026-08-15-cpi.md'
]:
    fix_file(filepath)
    print(f"Fixed {filepath}")
