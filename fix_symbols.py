import re
import sys

def fix_file(filepath):
    with open(filepath, 'r') as f:
        content = f.read()

    def clean_text(m):
        text = m.group(1)
        url = m.group(2)
        
        # Remove unwanted symbols from the text part
        # User specified: [, ], |, etc. We'll also remove \ and *
        for sym in ['[', ']', '|', '\\', '*', '~', '<', '>', '{', '}']:
            text = text.replace(sym, '')
        
        # Also let's ensure no [ ] | in the URL just in case
        for sym in ['[', ']', '|']:
            url = url.replace(sym, '')
            
        return f"[{text}]({url})"
        
    # We will match any markdown link [text](url)
    # Be careful not to match things across multiple lines incorrectly
    new_content = re.sub(r'\[([^\]]+)\]\((https?://[^)]+)\)', clean_text, content)
    
    with open(filepath, 'w') as f:
        f.write(new_content)

for filepath in [
    '/Users/ernie.chang/Documents/ernie/ernie55ernie.github.io/_posts/2026-08-12-fed.md',
    '/Users/ernie.chang/Documents/ernie/ernie55ernie.github.io/_posts/2026-08-13-rag.md',
    '/Users/ernie.chang/Documents/ernie/ernie55ernie.github.io/_posts/2026-08-15-cpi.md'
]:
    fix_file(filepath)
    print(f"Cleaned symbols in {filepath}")
