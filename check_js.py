import re

with open('macro_calendar.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Find all script blocks
scripts = re.findall(r'<script>(.*?)</script>', content, re.DOTALL)
print(f"Found {len(scripts)} script blocks")

for i, s in enumerate(scripts):
    print(f"\n--- Script {i+1}: {len(s)} chars ---")
    opens = s.count('{')
    closes = s.count('}')
    print(f"  Braces: {{ = {opens}, }} = {closes}, mismatch = {opens - closes}")
    ob = s.count('[')
    cb = s.count(']')
    print(f"  Brackets: [ = {ob}, ] = {cb}, mismatch = {ob - cb}")
    if 'allEventData' in s:
        print(f"  -> has allEventData")
    if 'eventData' in s:
        print(f"  -> has eventData")
    # Check for common errors: trailing commas, missing commas
    lines = s.split('\n')
    for j, line in enumerate(lines):
        stripped = line.strip()
        # Check for common issues in JSON-like structures
        if stripped.startswith('//'):
            continue
        if '\\'' in stripped and '\\\\' not in stripped:
            # Possible unescaped quote inside string
            pass
