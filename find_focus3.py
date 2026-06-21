import re

filepath = 'macro_calendar.html'

with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

# Old focus block pattern (using regex to handle whitespace variations)
# Let's find the July focus block by searching for unique content
pattern = r'focus:\s*\[.*?BOJ政策.*?套利交易平仓风险.*?\}\],'

match = re.search(pattern, content, re.DOTALL)
if match:
    print("Found BOJ policy entry")
    print("Context:", match.group()[:200])
else:
    print("Pattern not found, trying simpler search...")
    # Just find the line with BOJ policy
    lines = content.split('\n')
    for i, line in enumerate(lines):
        if 'BOJ' in line or '套利交易' in line:
            print(f"Line {i}: {line}")
            # Print surrounding lines
            for j in range(max(0,i-5), min(len(lines),i+5)):
                print(f"  {j}: {lines[j]}")
            break
