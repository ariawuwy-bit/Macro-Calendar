with open('macro_calendar.html', 'r', encoding='utf-8') as f:
    content = f.read()

idx = content.find('// ===== JULY 2026 =====')
print('JULY idx:', idx)

# Find focus: [ after JULY section
focus_start = content.find('  focus: [', idx)
print('focus_start:', focus_start)

if focus_start > 0:
    # Find the end of this focus block (next ], on its own line with same indent)
    # Look for "  ]," pattern
    focus_end = content.find('\n  ],', focus_start)
    if focus_end == -1:
        # Try alternate pattern
        focus_end = content.find('  },\n', focus_start)
        print('alt focus_end:', focus_end)
    else:
        focus_end = focus_end + 5  # include the ],
    print('focus_end:', focus_end)
    if focus_end > focus_start:
        block = content[focus_start:focus_end]
        print('---FOCUS BLOCK---')
        print(block)
        print('---END---')
