import sys
with open('macro_calendar.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Find JULY 2026 section
idx = content.find('// ===== JULY 2026 =====')
print('JULY idx:', idx)

if idx > 0:
    # Find focus: [ in JULY section
    focus_start = content.find('  focus: [', idx)
    print('focus_start:', focus_start)
    
    if focus_start > 0:
        # Find end: next '  },' (end of month object) or '  focus: [' in next section
        # The focus block ends with '  },' (closing the month object)
        # Actually it ends with '  ],' then newline then '// ====='
        rest = content[focus_start:]
        end_marker = rest.find('\n  },')
        if end_marker == -1:
            end_marker = rest.find('\n  // =====')
        print('end_marker relative:', end_marker)
        if end_marker > 0:
            block = rest[:end_marker]
            print('---FOCUS BLOCK---')
            print(block)
            print('---END---')
        else:
            print('Could not find end of focus block')
    else:
        print('focus not found after JULY')
else:
    print('JULY section not found')
