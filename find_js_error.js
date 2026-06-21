const fs = require('fs');
const content = fs.readFileSync('macro_calendar.html', 'utf8');
const match = content.match(/<script>([\s\S]*?)<\/script>/);
if (!match) { console.log('No script tag found'); process.exit(1); }
const js = match[1];

// Try to parse the JS - find exact error location
try {
  new Function(js);
  console.log('JS syntax: OK');
} catch(e) {
  console.log('Syntax error:', e.message);
  // Try to find the line number from error message
  const lineMatch = e.message.match(/(\d+)/);
  if (lineMatch) {
    const lineNum = parseInt(lineMatch[1]);
    const lines = js.split('\n');
    console.log('Context around error:');
    for (let i = Math.max(0, lineNum-3); i < Math.min(lines.length, lineNum+3); i++) {
      console.log(`  Line ${i+1}: ${lines[i]}`);
    }
  }
  // Also try to find problematic object literals by scanning
  console.log('\nScanning for common issues...');
  const lines = js.split('\n');
  for (let i = 0; i < lines.length; i++) {
    const line = lines[i];
    // Check for trailing commas in objects (old IE issue, but not in modern JS)
    // Check for unescaped quotes inside strings
    if (line.includes("'") && line.includes(",")) {
      // skip for now
    }
  }
  // Find lines with standalone } that might be extraneous
  let braceCount = 0;
  for (let i = 0; i < js.length; i++) {
    if (js[i] === '{') braceCount++;
    if (js[i] === '}') braceCount--;
    if (braceCount < 0) {
      // Found extraneous }
      const lineNum = js.substring(0, i).split('\n').length;
      console.log(`Extraneous } near line ${lineNum}: ...${js.substring(Math.max(0,i-30), i+1)}...`);
      break;
    }
  }
  if (braceCount === 0) console.log('Brace count is balanced');
}
