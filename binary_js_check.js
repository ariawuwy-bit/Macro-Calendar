const fs = require('fs');
const content = fs.readFileSync('macro_calendar.html', 'utf8');
const match = content.match(/<script>([\s\S]*?)<\/script>/);
if (!match) { console.log('No script'); process.exit(1); }
const js = match[1];

// Binary search for syntax error
function findError(lines) {
  if (lines.length <= 5) {
    // Try each line
    for (let i = 0; i < lines.length; i++) {
      const test = lines.slice(0, i+1).join('\n');
      try { new Function(test); } catch(e) {
        return { line: i+1, msg: e.message, content: lines[i] };
      }
    }
    return null;
  }
  const mid = Math.floor(lines.length / 2);
  const top = lines.slice(0, mid).join('\n');
  try {
    new Function(top);
    // Top half is OK, error is in bottom half
    return findError(lines.slice(mid));
  } catch(e) {
    // Error is in top half
    return findError(lines.slice(0, mid));
  }
}

const lines = js.split('\n');
console.log('Total JS lines:', lines.length);
const result = findError(lines);
if (result) {
  console.log('\nError found!');
  console.log('Line number (in JS):', result.line);
  console.log('Error message:', result.msg);
  console.log('Line content:', result.content);
  // Show context
  const start = Math.max(0, result.line - 5);
  const end = Math.min(lines.length, result.line + 5);
  console.log('\nContext:');
  for (let i = start; i < end; i++) {
    console.log((i+1) + (i === result.line-1 ? ' >> ' : '    ') + lines[i]);
  }
} else {
  console.log('No single-line error found, might be multi-line issue');
}
