const fs = require('fs');
const content = fs.readFileSync('macro_calendar.html', 'utf8');
const match = content.match(/<script>([\s\S]*?)<\/script>/);
if (!match) { console.log('No script tag found'); process.exit(1); }
const js = match[1];
console.log('JS length:', js.length);

// Check brace/bracket balance, ignoring strings
let b = 0, p = 0, inStr = null, esc = false;
for (let i = 0; i < js.length; i++) {
  const c = js[i];
  if (esc) { esc = false; continue; }
  if (c === '\\') { esc = true; continue; }
  if (inStr) { if (c === inStr) inStr = null; continue; }
  if (c === "'" || c === '"' || c === '`') { inStr = c; continue; }
  if (c === '{') b++;
  if (c === '}') b--;
  if (c === '[') p++;
  if (c === ']') p--;
}
console.log('Final brace balance:', b);
console.log('Final bracket balance:', p);

if (b === 0 && p === 0) {
  console.log('PASS: Braces and brackets are balanced');
} else {
  console.log('FAIL: Imbalance detected');
}
