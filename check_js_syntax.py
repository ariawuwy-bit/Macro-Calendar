import re
import sys

with open('macro_calendar.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Extract JS content between <script> tags
script_pattern = re.compile(r'<script[^>]*>(.*?)</script>', re.DOTALL)
matches = script_pattern.findall(content)

all_clean = True
for i, js_content in enumerate(matches):
    # Skip very short scripts (likely CDN links or very short snippets)
    if len(js_content.strip()) < 50:
        continue
    
    # Try to check syntax by looking for common errors
    # Check for mismatched brackets (simple check)
    opens = js_content.count('{')
    closes = js_content.count('}')
    if opens != closes:
        print(f"Script {i}: Mismatch {{}}{opens} vs {closes}}")
        all_clean = False
    
    opens = js_content.count('[')
    closes = js_content.count(']')
    if opens != closes:
        print(f"Script {i}: Mismatch []{opens} vs {closes}]")
        all_clean = False
        
    opens = js_content.count('(')
    closes = js_content.count(')')
    if opens != closes:
        print(f"Script {i}: Mismatch ({opens} vs {closes})")
        all_clean = False

if all_clean:
    print("Basic syntax check passed (bracket matching OK)")
else:
    print("Potential syntax issues found - check bracket matching")
    
# Also check for obvious issues in eventData ids
# Make sure j06, j07, j15, j16, j31 have correct dates
for event_id in ['j06', 'j07', 'j15', 'j16', 'j31']:
    pattern = re.compile(r"'" + event_id + r"':\{.*?date:'[^']*'", re.DOTALL)
    match = pattern.search(content)
    if match:
        # Extract the date
        date_match = re.search(r"date:'([^']*)'", match.group())
        if date_match:
            print(f"{event_id} date: {date_match.group(1)}")
        else:
            print(f"{event_id}: date not found in match")
    else:
        print(f"{event_id}: entry not found")
