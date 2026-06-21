const fs = require('fs');
const content = fs.readFileSync('macro_calendar.html', 'utf8');

// Find 2026-7 section
const startMarker = "'2026-7': {";
const startIndex = content.indexOf(startMarker);
if (startIndex === -1) { console.log('NOT FOUND'); process.exit(1); }

// Find matching closing brace
let braceCount = 1;
let pos = startIndex + startMarker.length - 1; // points to opening {
const chars = [];
while (braceCount > 0 && pos < content.length - 1) {
  pos++;
  const c = content[pos];
  if (c === '{') braceCount++;
  if (c === '}') braceCount--;
  chars.push(c);
}
// Now chars has everything including the closing }
const section = startMarker + chars.join('');
console.log('Section length:', section.length);
console.log('---');
console.log(section);
console.log('---');
// Check: does it end with /n?
// Write to file for inspection
fs.writeFileSync('july_section_dump.txt', section);
console.log('Dumped to july_section_dump.txt');
