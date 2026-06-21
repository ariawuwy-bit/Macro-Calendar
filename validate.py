import re
import sys

with open('macro_calendar.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Basic bracket matching check on entire file
# (simple check - not perfect but catches obvious errors)
opens = content.count('{')
closes = content.count('}')
print("Overall {{ }} count: {0} open, {1} close".format(opens, closes))

opens = content.count('[')
closes = content.count(']')
print("Overall [ ] count: {0} open, {1} close".format(opens, closes))

opens = content.count('(')
closes = content.count(')')
print("Overall ( ) count: {0} open, {1} close".format(opens, closes))

# Check specific eventData entries for correct dates
print("\n=== Checking eventData date fields ===")

# Check j06 - should be 7/14
idx = content.find("j06:{")
if idx > 0:
    end = content.find('}', idx)
    chunk = content[idx:end+1]
    if '7月14日' in chunk:
        print("j06 date: OK (7/14)")
    else:
        print("j06 date: PROBLEM - " + chunk[:100])
else:
    print("j06 not found")

# Check j07 - should be 7/15
idx = content.find("j07:{")
if idx > 0:
    end = content.find('}', idx)
    chunk = content[idx:end+1]
    if '7月15日' in chunk:
        print("j07 date: OK (7/15)")
    else:
        print("j07 date: PROBLEM - " + chunk[:100])
else:
    print("j07 not found")

# Check j15 - should be 7/30
idx = content.find("j15:{")
if idx > 0:
    end = content.find('}', idx)
    chunk = content[idx:end+1]
    if '7月30日' in chunk:
        print("j15 date: OK (7/30)")
    else:
        print("j15 date: PROBLEM - " + chunk[:100])
else:
    print("j15 not found")

# Check j16 - should be 7/30
idx = content.find("j16:{")
if idx > 0:
    end = content.find('}', idx)
    chunk = content[idx:end+1]
    if '7月30日' in chunk:
        print("j16 date: OK (7/30)")
    else:
        print("j16 date: PROBLEM - " + chunk[:100])
else:
    print("j16 not found")

# Check j31 - should be 7/16
idx = content.find("j31:{")
if idx > 0:
    end = content.find('}', idx)
    chunk = content[idx:end+1]
    if '7月16日' in chunk:
        print("j31 date: OK (7/16)")
    else:
        print("j31 date: PROBLEM - " + chunk[:100])
else:
    print("j31 not found")

# Check j70 exists
idx = content.find("j70:{")
if idx > 0:
    print("j70 (InnoLight IPO): OK - found")
    end = content.find('}', idx)
    chunk = content[idx:end+1]
    if '中际旭创' in chunk or 'InnoLight' in chunk:
        print("  Title: OK")
    else:
        print("  Title: missing - " + chunk[:100])
else:
    print("j70 (InnoLight IPO): NOT FOUND")

# Check July allEventData has j06 on day 14, j07 on day 15, j31 on day 16, j15/j16 on day 30
print("\n=== Checking allEventData July dates ===")

july_start = content.find("// ===== JULY 2026 =====")
july_end = content.find("// ===== AUGUST 2026 =====")
if july_start > 0 and july_end > 0:
    july_block = content[july_start:july_end]
    
    # Check j06 on day 14
    day14_line = [l for l in july_block.split('\n') if "'14':" in l or ' 14: [' in l]
    if day14_line:
        if 'j06' in day14_line[0]:
            print("j06 in allEventData: OK (on day 14)")
        else:
            print("j06 in allEventData: PROBLEM - not on day 14")
            print("  Line: " + day14_line[0].strip())
    else:
        print("Day 14 not found in allEventData")
    
    # Check j07 on day 15
    day15_line = [l for l in july_block.split('\n') if "'15':" in l or ' 15: [' in l]
    if day15_line:
        if 'j07' in day15_line[0]:
            print("j07 in allEventData: OK (on day 15)")
        else:
            print("j07 in allEventData: PROBLEM - not on day 15")
            print("  Line: " + day15_line[0].strip())
    else:
        print("Day 15 not found in allEventData")
    
    # Check j31 on day 16
    day16_line = [l for l in july_block.split('\n') if "'16':" in l or ' 16: [' in l]
    if day16_line:
        if 'j31' in day16_line[0]:
            print("j31 in allEventData: OK (on day 16)")
        else:
            print("j31 in allEventData: PROBLEM - not on day 16")
            print("  Line: " + day16_line[0].strip())
    else:
        print("Day 16 not found in allEventData")
    
    # Check j15 and j16 on day 30
    day30_line = [l for l in july_block.split('\n') if "'30':" in l or ' 30: [' in l]
    if day30_line:
        line = day30_line[0]
        if 'j15' in line and 'j16' in line:
            print("j15+j16 in allEventData: OK (both on day 30)")
        else:
            print("j15/j16 in allEventData: PROBLEM")
            print("  Line: " + line.strip())
    else:
        print("Day 30 not found in allEventData")
else:
    print("Could not find July block")
