const fs = require('fs');
const content = fs.readFileSync('macro_calendar.html', 'utf8');
const match = content.match(/<script>([\s\S]*?)<\/script>/);
if (!match) { console.log('No script tag found'); process.exit(1); }
let js = match[1];

// Remove DOM references that would fail in Node
js = js.replace(/document\./g, 'mockDocument.');
js = js.replace(/window\./g, 'mockWindow.');
js = js.replace(/setTimeout\(/g, 'mockSetTimeout(');
js = js.replace(/addEventListener\(/g, 'mockAddEventListener(');

// Mock browser APIs
global.mockDocument = {
  getElementById: () => ({ classList: { add: ()=>{}, remove: ()=>{}, contains: ()=>false }, src: '', style: {}, textContent: '', innerHTML: '', scrollIntoView: ()=>{} }),
  createElement: () => ({ className: '', textContent: '', onclick: null, classList: { add: ()=>{}, remove: ()=>{} } }),
  appendChild: ()=>{}
};
global.mockWindow = {};
global.mockSetTimeout = (fn) => fn();
global.mockAddEventListener = ()=>{};

try {
  eval(js);
  console.log('JS executed without runtime error');
  console.log('visibleMonths:', typeof visibleMonths !== 'undefined' ? visibleMonths.map(m => m.year+'-'+m.month) : 'not defined');
  console.log('allEventData keys:', typeof allEventData !== 'undefined' ? Object.keys(allEventData).length + ' months' : 'not defined');
  console.log('eventData keys:', typeof eventData !== 'undefined' ? Object.keys(eventData).length + ' events' : 'not defined');
} catch(e) {
  console.log('RUNTIME ERROR:', e.message);
  console.log('Stack:', e.stack ? e.stack.split('\n').slice(0,5).join('\n') : 'N/A');
}
