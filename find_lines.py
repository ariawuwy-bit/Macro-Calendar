import re

fpath = 'D:/WorkbuddyStudio/MacroCalendar/macro_calendar.html'
with open(fpath, 'r', encoding='utf-8') as f:
    lines = f.readlines()

# Print lines around e60 and e56
for i, line in enumerate(lines):
    if 'e60:' in line and 'flag' in line:
        print(f'FOUND e60 at line {i+1}: {line[:80]}')
    if 'e56:' in line and 'flag' in line and 'e60' not in line:
        print(f'FOUND e56 at line {i+1}: {line[:80]}')
