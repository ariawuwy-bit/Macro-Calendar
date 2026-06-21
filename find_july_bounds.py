with open('macro_calendar.html', 'r', encoding='utf-8') as f:
    content = f.read()

# The old July section (from '2026-7': { to the closing }],\n// ===== AUGUST)
old_start = "'2026-7': {"
old_end_marker = "// ===== AUGUST 2026 ====="

start_idx = content.find(old_start)
if start_idx == -1:
    print("ERROR: Could not find 2026-7 section")
    exit(1)

# Find the end - we need to find the matching closing brace
# Strategy: find "// ===== AUGUST" after the start
end_idx = content.find(old_end_marker, start_idx)
if end_idx == -1:
    print("ERROR: Could not find AUGUST marker")
    exit(1)

# Now back up to find the actual closing }],\n before // ===== AUGUST
# The structure is: ... }],\n// ===== AUGUST
# So we need to find the }],\n before end_idx
search_idx = end_idx - 1
while search_idx > start_idx:
    if content[search_idx:search_idx+4] == '  }],\n':
        end_idx = search_idx + 5  # include }],\n
        break
    search_idx -= 1
else:
    print("ERROR: Could not find closing }],")
    exit(1)

print(f"Found July section: {start_idx} to {end_idx}")
print("Current content:")
print(repr(content[start_idx:end_idx]))
