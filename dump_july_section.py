import re

with open('macro_calendar.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Find the 2026-7 section - locate "2026-7': {"
marker = "'2026-7': {"
idx = content.find(marker)
if idx == -1:
    print("ERROR: could not find 2026-7 section")
    exit(1)

# Find the end of this section (next "'2026-" or "// =====")
# We need to find matching brace
start_brace = idx + len(marker) - 1  # Point to the opening {
brace_count = 1
pos = start_brace + 1
while brace_count > 0 and pos < len(content):
    if content[pos] == '{':
        brace_count += 1
    elif content[pos] == '}':
        brace_count -= 1
    pos += 1

section_end = pos
print(f"Found 2026-7 section: chars {idx} to {section_end}")
print(f"Section length: {section_end - idx}")
print()
print("=== Current 2026-7 section ===")
print(content[idx:section_end])
print("=== End ===")
