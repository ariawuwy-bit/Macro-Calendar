import re

with open('D:/WorkbuddyStudio/MacroCalendar/macro_calendar.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Find the exact position to insert new event panels
# Insert after e60 panel and before e56 panel
# e60 panel ends with its closing brace, then e56 starts

# Strategy: find the e60 event panel and insert e61/e62 after it
# Also need to add e61d2, e61d3 as extra panels

# First, let's find e60 panel end and e56 panel start
e60_end = content.find("e60:{flag:", 0)
print("e60 starts at:", e60_end)

# Find the closing of e60 (the line ends with '},' after e60 html)
# Let's find "e56:" to know where to insert
e56_pos = content.find("e56:{flag:", e60_end)
print("e56 starts at:", e56_pos)

# Find the CHARACTER position of the end of e60 panel
# The e60 panel is a single-line entry ending with '},'
# Let's find the physical end of the e60 line
e60_line_end = content.find('\n', e60_end)
print("e60 line ends at char:", e60_line_end)
print("Char at e60_line_end:", repr(content[e60_line_end:e60_line_end+5]))

# Now find the ACTUAL end of e60 panel (which may wrap)
# Actually from the Read output, e60 is a single line ending with '},'
# Let's check if there's a comma after e60
e60_actual_end = content.find('},\n', e60_end)
print("e60 panel end (}):", e60_actual_end)
print("After e60 end:", repr(content[e60_actual_end:e60_actual_end+10]))
