fpath = 'D:/WorkbuddyStudio/MacroCalendar/macro_calendar.html'
with open(fpath, 'r', encoding='utf-8') as f:
    content = f.read()

# Fix weekBanners order: should be beforeDay:8, beforeDay:15, beforeDay:22
old_banners = """  weekBanners: [
   { beforeDay: 8, cls: 'tech-week', icon: '🧪', label: '科技超级周', detail: '6/8–6/14 · WWDC+HDC+智谱入恒科+SpaceX+OpenAI递表' },
   { beforeDay: 22, cls: 'central-bank-week', icon: '🏦', label: '地缘超级周', detail: '6/22–6/28 · 美伊谈判+霍尔木兹再封锁+夏季达沃斯+PMI初值+PCE' },
   { beforeDay: 15, cls: 'central-bank-week', icon: '🏦', label: '央行超级周+地缘剧变', detail: '6/15–6/21 · G7峰会+美伊协议+BOJ+FOMC+BOE+陆家嘴论坛' }
  ],"""

new_banners = """  weekBanners: [
   { beforeDay: 8, cls: 'tech-week', icon: '🧪', label: '科技超级周', detail: '6/8–6/14 · WWDC+HDC+智谱入恒科+SpaceX+OpenAI递表' },
   { beforeDay: 15, cls: 'central-bank-week', icon: '🏦', label: '央行超级周+地缘剧变', detail: '6/15–6/21 · G7峰会+美伊协议+BOJ+FOMC+BOE+陆家嘴论坛' },
   { beforeDay: 22, cls: 'central-bank-week', icon: '🏦', label: '地缘超级周', detail: '6/22–6/28 · 美伊谈判+霍尔木兹再封锁+夏季达沃斯+PMI初值+PCE' }
  ],"""

if old_banners in content:
    content = content.replace(old_banners, new_banners, 1)
    with open(fpath, 'w', encoding='utf-8') as f:
        f.write(content)
    print("Fixed weekBanners order!")
else:
    print("ERROR: old_banners not found")
    # Debug
    idx = content.find('weekBanners')
    if idx >= 0:
        print("Found weekBanners at:", idx)
        print(repr(content[idx:idx+400]))
