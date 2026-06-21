import re

with open('macro_calendar.html', 'r', encoding='utf-8') as f:
    content = f.read()

# The correct 2026-7 section (with proper syntax)
new_july = """'2026-7': {
  events: {
   1: [{id:'j63',flag:'cn',name:'对外投资新规施行',cls:'pill-cn',stars:'★'}],
   2: [{id:'j01',flag:'us',name:'NFP(6月)',cls:'pill-fed high',stars:'★★★'},{id:'j23',flag:'us',name:'建筑业支出',cls:'pill-data',stars:''}],
   3: [{id:'j02',flag:'us',name:'ISM制造业PMI',cls:'pill-data',stars:'★★'},{id:'j24',flag:'us',name:'ISM非制造业PMI',cls:'pill-data',stars:'★★'}],
   4: [{id:'j03',flag:'us',name:'🇺🇸独立日休市',cls:'pill-event',stars:''},{id:'j25',flag:'un',name:'⚽世界杯1/4决赛',cls:'pill-event',stars:'★★'}],
   5: [],
   6: [],
   7: [{id:'j04',flag:'au',name:'RBA会议',cls:'pill-rba',stars:'★★'},{id:'j26',flag:'un',name:'⚽世界杯半决赛',cls:'pill-event',stars:'★★'},{id:'j66',flag:'hk',name:'智谱基石解禁(11.6%)',cls:'pill-ipo high',stars:'★★★'}],
   8: [{id:'j27',flag:'us',name:'FOMC会议纪要',cls:'pill-fed',stars:'★★'},{id:'j67',flag:'hk',name:'MiniMax解禁(63%)',cls:'pill-ipo high',stars:'★★★'}],
   9: [{id:'j05',flag:'cn',name:'中国CPI/PPI',cls:'pill-cn',stars:'★★'},{id:'j28',flag:'cn',name:'中国进出口',cls:'pill-cn',stars:'★★'}],
  10: [],
  11: [{id:'j29',flag:'us',name:'密歇根初值',cls:'pill-data',stars:''},{id:'j30',flag:'us',name:'Lime IPO',cls:'pill-ipo',stars:'★★'}],
  14: [{id:'j06',flag:'us',name:'CPI(6月)',cls:'pill-fed high',stars:'★★★'}],
  15: [{id:'j07',flag:'us',name:'PPI',cls:'pill-data',stars:'★★'},{id:'j08',flag:'ca',name:'BoC决议',cls:'pill-boc',stars:'★★'},{id:'j09',flag:'cn',name:'Q2 GDP',cls:'pill-cn high',stars:'★★★'}],
  16: [{id:'j31',flag:'us',name:'零售销售',cls:'pill-data',stars:'★★'}],
  17: [{id:'j11',flag:'us',name:'新屋开工',cls:'pill-data',stars:''},{id:'j32',flag:'us',name:'工业生产',cls:'pill-data',stars:''}],
  19: [{id:'j33',flag:'un',name:'⚽世界杯决赛',cls:'pill-event high',stars:'★★★'}],
  20: [{id:'j12',flag:'cn',name:'LPR报价',cls:'pill-cn',stars:'★★'}],
  23: [{id:'j13',flag:'eu',name:'ECB决议',cls:'pill-ecb high',stars:'★★★'},{id:'j14',flag:'us',name:'成屋销售',cls:'pill-data',stars:''}],
  25: [{id:'j34',flag:'us',name:'密歇根终值',cls:'pill-data',stars:''}],
  28: [{id:'j57',flag:'us',name:'FOMC会议(第1日)',cls:'pill-fed high',stars:'★★★'}],
  29: [{id:'j58',flag:'us',name:'FOMC利率决议',cls:'pill-fed high',stars:'★★★'},{id:'j17',flag:'us',name:'消费者信心',cls:'pill-data',stars:''}],
  30: [{id:'j15',flag:'us',name:'GDP速报',cls:'pill-data',stars:'★★'},{id:'j16',flag:'us',name:'PCE',cls:'pill-fed high',stars:'★★★'},{id:'j18',flag:'jp',name:'BOJ决议',cls:'pill-boj high',stars:'★★★'},{id:'j19',flag:'gb',name:'BOE决议',cls:'pill-boe',stars:'★★'}],
  31: [{id:'j20',flag:'us',name:'JOLTS',cls:'pill-data',stars:'★★'},{id:'j35',flag:'cn',name:'中国PMI',cls:'pill-cn high',stars:'★★★'}]
  },
  weekBanners: [
   { beforeDay: 28, cls: 'central-bank-week', icon: '🏦', label: '超级宏观周', detail: '7/28–7/30 · FOMC+BOJ+BOE 三大央行 + GDP速报 + PCE' }
  ],
  midMonth: { title: '📅 7月待定日期事件', pills: [
   {id:'j21',flag:'cn',name:'社融/M2/信贷(中旬)',cls:'pill-cn high',stars:'★★★'},
   {id:'j22',flag:'cn',name:'国民经济数据',cls:'pill-cn',stars:'★★'},
   {id:'j36',flag:'cn',name:'长鑫存储挂牌',cls:'pill-ipo high',stars:'★★★'},
   {id:'j37',flag:'us',name:'Anthropic路演',cls:'pill-ipo',stars:'★★★'},
   {id:'j53',flag:'id',name:'印尼RKAB镍配额修订',cls:'pill-opec high',stars:'★★★'},
   {id:'j54',flag:'id',name:'印尼镍/煤出口关税',cls:'pill-trade high',stars:'★★★'},
   {id:'j55',flag:'cl',name:'智利锂矿国有化推进',cls:'pill-trade high',stars:'★★★'},
   {id:'j56',flag:'cd',name:'刚果钴出口配额执行',cls:'pill-trade high',stars:'★★★'},
   {id:'j59',flag:'cn',name:'中共中央政治局会议(下旬)',cls:'pill-cn high',stars:'★★★'},
   {id:'j60',flag:'pe',name:'秘鲁大选最终结果公布',cls:'pill-opec high',stars:'★★★'},
   {id:'j61',flag:'us',name:'Databricks交表',cls:'pill-ipo high',stars:'★★★'},
   {id:'j62',flag:'us',name:'OpenAI路演',cls:'pill-ipo high',stars:'★★★'},
   {id:'j64',flag:'cn',name:'沐曦股份A+H上市(6/12宣布)',cls:'pill-ipo',stars:'★'},
   {id:'j68',flag:'cn',name:'宇树科技科创板挂牌(7月上旬)',cls:'pill-ipo high',stars:'★★'},
   {id:'j69',flag:'cn',name:'华润新能源深交所挂牌',cls:'pill-ipo high',stars:'★★★'},
   {id:'j70',flag:'cn',name:'中际旭创港股IPO(7月中旬)',cls:'pill-ipo high',stars:'★★★'}
  ]},
  focus: [
   {bg:'var(--red-bg)',bc:'var(--red)',tc:'var(--red)',title:'FOMC决议',body:'7/28-29 FOMC会议，6月点阵图后首次决议，是否释放9月降息信号是核心关注'},
   {bg:'var(--blue-bg)',bc:'var(--blue)',tc:'var(--blue)',title:'ECB利率',body:'7/23 ECB决议，6月加息后是否连续加息，拉加德新闻发布会措辞是关键'},
   {bg:'var(--purple-bg)',bc:'var(--purple)',tc:'var(--purple)',title:'BOJ+BOE',body:'7/30日BOJ与BOE同日决议，BOJ是否继续加息、日元套利交易平仓风险需警惕'},
   {bg:'var(--green-bg)',bc:'var(--green)',tc:'var(--green)',title:'GDP速报+PCE',body:'7/30同日发布Q2 GDP速报+6月PCE，两大核心数据叠加FOMC次日，市场波动极大'},
   {bg:'var(--orange-bg)',bc:'var(--orange)',tc:'var(--orange)',title:'Q2 GDP(中国)',body:'7/15公布Q2 GDP，市场预期4.8-5.2%，若低于5%将触发降息降准预期'},
   {bg:'rgba(184,148,62,0.06)',bc:'var(--gold)',tc:'var(--gold-dim)',title:'🛠️ 资源国执行',body:'7/1中国《对外投资规定》施行；印尼ESDM 6/18辟谣配额放宽、7/1-31镍矿RKAB修订窗口开启；几内亚铝土矿4/25签署1.5亿吨硬限额6月起严格执行；刚果钴/印尼镍/智利锂/澳洲CMPTI 7-8月密集推进；资源民族主义对全球有色金属定价权影响深化'},
   {bg:'var(--lime-bg)',bc:'var(--lime)',tc:'var(--lime)',title:'⚽ 世界杯闭幕',body:'7/19决赛，美加墨世界杯创48队纪录，650万球迷推升CPI分项0.2-0.5个百分点'},
   {bg:'rgba(212,118,10,0.06)',bc:'#d4760a',tc:'#d4760a',title:'🚀 IPO潮+解禁双压',body:'宇树科技7月上旬科创板挂牌+长鑫存储7-8月科创板+华润新能源6/22申购245亿+Anthropic/OpenAI路演预期+7/8智谱基石解禁11.6%+7/9 MiniMax解禁63%形成港股AI集中抛压'}
  ]
},"""

# Find old section
old_start = "'2026-7': {"
old_end = "// ===== AUGUST 2026 ====="

start_idx = content.find(old_start)
if start_idx == -1:
    print("ERROR: start marker not found")
    exit(1)

end_idx = content.find(old_end, start_idx)
if end_idx == -1:
    print("ERROR: end marker not found")
    exit(1)

# Include the // ===== AUGUST line for replacement
end_with_marker = end_idx + len(old_end)

old_section = content[start_idx:end_with_marker]
print(f"Found old section: {len(old_section)} chars")
print("First 100 chars:", repr(old_section[:100]))
print("Last 100 chars:", repr(old_section[-100:]))

# Replace
new_content = content[:start_idx] + new_july + "// ===== AUGUST 2026 =====" + content[end_with_marker:]

with open('macro_calendar.html', 'w', encoding='utf-8') as f:
    f.write(new_content)

print("Done! New file written.")
print(f"Old section length: {len(old_section)}")
print(f"New section length: {len(new_july)}")
