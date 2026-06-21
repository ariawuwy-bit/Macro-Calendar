import re

filepath = 'macro_calendar.html'

with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

# Find 7/28 FOMC meeting in July section
# The July focus block should contain "7/28-29 FOMC"
pattern = r'focus:\s*\[.*?7/28-29 FOMC.*?\}\s*\]'
match = re.search(pattern, content, re.DOTALL)
if match:
    print("Found July focus block!")
    print("Block:")
    print(match.group())
else:
    print("Pattern not found, searching for '7/28-29 FOMC'...")
    idx = content.find('7/28-29 FOMC')
    if idx > 0:
        # Print surrounding context
        start = max(0, idx - 200)
        end = min(len(content), idx + 500)
        print("Context around '7/28-29 FOMC':")
        print(repr(content[start:end]))
    else:
        print("'7/28-29 FOMC' not found at all")
        # Try alternate pattern
        idx2 = content.find('FOMC会议，6月点阵图')
        print("'FOMC会议，6月点阵图' idx:", idx2)
        if idx2 > 0:
            start = max(0, idx2 - 100)
            end = min(len(content), idx2 + 800)
            print(repr(content[start:end]))
