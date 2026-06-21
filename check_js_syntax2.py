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
        print("Script " + str(i) + ": Mismatch {{}}{opens} vs {closes}").format(opens=opens, closes=closes))
        all_clean = False
    
    opens = js_content.count('[')
    closes = js_content.count(']')
    if opens != closes:
        print("Script " + str(i) + ": Mismatch [{opens}] vs [{closes}]").format(opens=opens, closes=closes))
        all_clean = False
        
    opens = js_content.count('(')
    closes = js_content.count(')')
    if opens != closes:
        print("Script " + str(i) + ": Mismatch ({opens}) vs ({closes})").format(opens=opens, closes=closes))
        all_clean = False

if all_clean:
    print("Basic syntax check passed (bracket matching OK)")
else:
    print("Potential syntax issues found - check bracket matching")
    
# Also check for obvious issues in eventData ids
# Make sure j06, j07, j15, j16, j31 have correct dates
for event_id in ['j06', 'j07', 'j15', 'j16', 'j31']:
    pattern = re.compile(r'"' + event_id + r'"\s*:\s*\{[^}]*?date\s*:\s*\'[^\']*\'', re.DOTALL)
    match = pattern.search(content)
    if match:
        # Extract the date
        date_match = re.search(r"date\s*:\s*'([^']*)'", match.group())
        if date_match:
            print(event_id + " date: " + date_match.group(1))
        else:
            print(event_id + ": date not found in match")
    else:
        print(event_id + ": entry not found")

# Check allEventData JULY entries for j06, j07, j15, j16, j31
print("\nChecking allEventData for JULY dates...")
july_events_start = content.find("// ===== JULY 2026 =====")
july_events_end = content.find("// ===== AUGUST 2026 =====")
if july_events_start > 0 and july_events_end > 0:
    july_content = content[july_events_start:july_events_end]
    
    # Check j06 is on day 14
    j06_pos = july_content.find("'j06'")
    if j06_pos > 0:
        # Find the line with j06
        line_start = july_content.rfind('\n', 0, j06_pos) + 1
        line_end = july_content.find('\n', j06_pos)
        if line_end > line_start:
            line = july_content[line_start:line_end]
            print("j06 line: " + line.strip())
    
    # Check j07 is on day 15
    j07_pos = july_content.find("'j07'")
    if j07_pos > 0:
        line_start = july_content.rfind('\n', 0, j07_pos) + 1
        line_end = july_content.find('\n', j07_pos)
        if line_end > line_start:
            line = july_content[line_start:line_end]
            print("j07 line: " + line.strip())

    # Check j15 is on day 30
    j15_pos = july_content.find("'j15'")
    if j15_pos > 0:
        line_start = july_content.rfind('\n', 0, j15_pos) + 1
        line_end = july_content.find('\n', j15_pos)
        if line_end > line_start:
            line = july_content[line_start:line_end]
            print("j15 line: " + line.strip())

    # Check j16 is on day 30
    j16_pos = july_content.find("'j16'")
    if j16_pos > 0:
        line_start = july_content.rfind('\n', 0, j16_pos) + 1
        line_end = july_content.find('\n', j16_pos)
        if line_end > line_start:
            line = july_content[line_start:line_end]
            print("j16 line: " + line.strip())

    # Check j31 is on day 16
    j31_pos = july_content.find("'j31'")
    if j31_pos > 0:
        line_start = july_content.rfind('\n', 0, j31_pos) + 1
        line_end = july_content.find('\n', j31_pos)
        if line_end > line_start:
            line = july_content[line_start:line_end]
            print("j31 line: " + line.strip())
