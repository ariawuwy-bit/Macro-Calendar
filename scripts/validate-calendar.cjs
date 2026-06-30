const fs = require('fs');

const files = ['index.html', 'macro_calendar.html'];
const [primary, mirror] = files.map(file => fs.readFileSync(file, 'utf8'));
const failures = [];

if (primary !== mirror) {
  failures.push('index.html and macro_calendar.html are not identical.');
}

const scriptMatch = primary.match(/<script>([\s\S]*)<\/script>/);
if (!scriptMatch) {
  failures.push('No inline script block found.');
} else {
  try {
    new Function(scriptMatch[1]);
  } catch (error) {
    failures.push(`Inline script does not parse: ${error.message}`);
  }

  const script = scriptMatch[1];
  const calendarIds = [];
  const eventPlacements = [];
  const monthBlocks = [...script.matchAll(/'(\d{4})-(\d+)'\s*:\s*\{\s*events:\s*\{([\s\S]*?)\n\s*\},\n\s*weekBanners/g)];
  for (const block of monthBlocks) {
    const year = Number(block[1]);
    const month = Number(block[2]);
    const eventsBody = block[3];
    for (const dayBlock of eventsBody.matchAll(/\n\s*(\d+)\s*:\s*\[([^\]]*)\]/g)) {
      const day = Number(dayBlock[1]);
      for (const idMatch of dayBlock[2].matchAll(/id:'([^']+)'/g)) {
        const id = idMatch[1];
        calendarIds.push(id);
        eventPlacements.push({ id, year, month, day });
      }
    }
  }

  const detailIds = [...script.matchAll(/\n\s*([a-z]\d+)\s*:\s*\{/g)].map(match => match[1]);
  const duplicateCalendarIds = calendarIds.filter((id, idx) => calendarIds.indexOf(id) !== idx);
  const duplicateDetailIds = detailIds.filter((id, idx) => detailIds.indexOf(id) !== idx);
  const detailIdSet = new Set(detailIds);
  const missingDetailIds = [...new Set(calendarIds)].filter(id => !detailIdSet.has(id));

  if (duplicateCalendarIds.length) failures.push(`Duplicate calendar event ids: ${[...new Set(duplicateCalendarIds)].join(', ')}`);
  if (duplicateDetailIds.length) failures.push(`Duplicate detail ids: ${[...new Set(duplicateDetailIds)].join(', ')}`);
  if (missingDetailIds.length) failures.push(`Calendar ids missing detail entries: ${missingDetailIds.join(', ')}`);

  const detailDates = new Map([...script.matchAll(/\n\s*([a-z]\d+)\s*:\s*\{[^\n]*?date:'([^']+)'/g)].map(match => [match[1], match[2]]));
  const weekdays = ['周日', '周一', '周二', '周三', '周四', '周五', '周六'];
  const dateMismatches = [];
  const weekdayMismatches = [];

  for (const placement of eventPlacements) {
    const detailDate = detailDates.get(placement.id) || '';
    const parsed = detailDate.match(/(\d{1,2})月(\d{1,2})日(?:[^周]*(周[一二三四五六日]))?/);
    if (!parsed) continue;

    const detailMonth = Number(parsed[1]);
    const detailDay = Number(parsed[2]);
    const statedWeekday = parsed[3];
    if (detailMonth !== placement.month || detailDay !== placement.day) {
      dateMismatches.push(`${placement.id}: calendar ${placement.month}/${placement.day}, detail ${detailMonth}/${detailDay}`);
    }
    if (statedWeekday) {
      const actualWeekday = weekdays[new Date(Date.UTC(placement.year, detailMonth - 1, detailDay)).getUTCDay()];
      if (actualWeekday !== statedWeekday) {
        weekdayMismatches.push(`${placement.id}: ${detailMonth}/${detailDay} says ${statedWeekday}, actual ${actualWeekday}`);
      }
    }
  }

  if (dateMismatches.length) failures.push(`Date mismatches:\n${dateMismatches.join('\n')}`);
  if (weekdayMismatches.length) failures.push(`Weekday mismatches:\n${weekdayMismatches.join('\n')}`);
}

if (failures.length) {
  console.error(failures.join('\n\n'));
  process.exit(1);
}

console.log('Calendar validation passed.');
