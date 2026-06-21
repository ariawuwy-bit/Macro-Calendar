const fs = require('fs');
const c = fs.readFileSync('macro_calendar.html', 'utf8');

// Find position of '2026-7' section
const idx = c.indexOf("'2026-7'");
console.log("'2026-7' starts at char:", idx);

// Find 'focus: [' after this point
const focusIdx = c.indexOf('focus: [', idx);
console.log("focus: [ starts at char:", focusIdx);

// Show ~800 chars from focusIdx
console.log('\n=== Context around focus: [ ===');
console.log(c.substring(focusIdx, focusIdx + 800));
console.log('===\n');

// Also find the closing '}]' after focus
const closeIdx = c.indexOf('  }],', idx);
console.log("First '  }],' after 2026-7 starts at char:", closeIdx);
console.log('Context:');
console.log(c.substring(closeIdx - 20, closeIdx + 30));
