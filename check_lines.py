with open('macro_calendar.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

# Print lines 368-377 (1-indexed to 0-indexed: 367-376)
print("Lines 368-376 (0-indexed 367-375):")
for i in range(367, min(376, len(lines))):
    print(f"{i+1}: {lines[i].rstrip()}")
