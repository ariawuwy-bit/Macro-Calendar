import re

with open('macro_calendar.html', 'r', encoding='utf-8') as f:
    content = f.read()

count = 0

# 1. Update e35: pending -> released, add actual data, update date
old_e35 = r"""e35:{flag:'https://flagcdn.com/w40/cn.png',title:'中国5月金融数据（社融/M2/信贷）',date:'6月中旬 待定',html:'<span class="expand-tag pending">待发布</span>三大核心指标：社融、M2、新增人民币贷款。关注社融增速是否回升、居民中长期贷款（≈房贷）是否企稳、M1增速。'}"""

new_e35 = r"""e35:{flag:'https://flagcdn.com/w40/cn.png',title:'中国5月金融数据（社融/M2/信贷）',date:'6月12日 周五',html:'<span class="expand-tag released">已发布</span><strong>📊 实际结果：5月新增社融2.03万亿元，新增人民币贷款5200亿元，M2同比+8.6%，M1同比+5.5%。</strong>央行6月12日发布2026年5月金融统计数据报告。<br><br><strong>关键数据分项：</strong><br>• <strong>货币供应：</strong>M2余额353.67万亿元（同比+8.6%，与上月持平）；M1余额114.89万亿元（同比+5.5%）；M0余额14.69万亿元（同比+11.9%）<br>• <strong>社融：</strong>5月末社融存量458.81万亿元（同比+7.7%）；前5月社融增量17.48万亿元（同比少1.16万亿元，但高于预期的17.15万亿元）<br>• <strong>信贷结构：</strong>前5月人民币贷款增加9.11万亿元——住户贷款减少6314亿元（短期-6942亿，中长期仅+628亿），企事业贷款增加9.63万亿元（中长期+4.99万亿，短期+3.77万亿，票据+6999亿）<br>• <strong>普惠金融：</strong>5月末普惠小微贷款余额37.95万亿元（同比+10.2%）；不含房地产业的服务业中长期贷款余额61.48万亿元（同比+9.6%）<br><br><strong>市场解读：</strong>社融总量超预期（17.48万亿 vs 预期17.15万亿），但结构分化加剧——企业中长期贷款强劲（+4.99万亿）反映制造业和基建支撑，居民端则持续去杠杆（住户贷款净减少6314亿，中长期贷款5个月仅增628亿）。"企业强、居民弱"格局延续，M1增速5.5%处于历史低位，企业活期存款增长乏力暗示投资意愿偏谨慎。社融增速7.7%低于名义GDP增速，金融条件整体偏紧。<br><br><strong>对宏观的影响：</strong><br>• 社融总量超预期→短期稳增长压力缓解，但居民中长期贷款仅增628亿元（5个月累计）显示房地产市场信心仍未恢复<br>• M1增速5.5%处于低位→企业活期存款增长乏力，实体经济活跃度偏弱，与PPI走高形成"价涨量缩"矛盾<br>• 企事业中长期贷款4.99万亿→制造业和基建投资支撑，与半导体/AI产业链资本开支周期形成呼应<br>• 社融增速7.7%低于名义GDP增速→金融条件偏紧，下半年降准降息空间仍存<br><br><strong>对资金的影响：</strong><br>• 居民中长期贷款持续低迷→房地产板块缺乏信贷数据支撑，地产股反弹空间受限<br>• 企业中长期贷款强劲→制造业/基建相关板块（高端制造、新能源基建）获得信贷数据背书<br>• M1-M2剪刀差维持高位（约3.1个百分点）→资金活性不足，A股市场增量资金受限，存量博弈格局延续<br>• 金融数据超预期但结构分化→短期利好有限，市场更关注6/17 FOMC点阵图和6/16国民经济数据'}"""

if old_e35 in content:
    content = content.replace(old_e35, new_e35, 1)
    count += 1
    print("OK: e35 updated")
else:
    print("NOT FOUND: e35")

# 2. Update e26 date from '6月中旬 待定' to '6月12日 周五'
old_e26_date = r"""e26:{flag:'https://flagcdn.com/w40/cn.png',title:'长鑫科技科创板IPO注册生效',date:'6月中旬 待定',html:"""
new_e26_date = r"""e26:{flag:'https://flagcdn.com/w40/cn.png',title:'长鑫科技科创板IPO注册生效',date:'6月12日 周五',html:"""
if old_e26_date in content:
    content = content.replace(old_e26_date, new_e26_date, 1)
    count += 1
    print("OK: e26 date updated")
else:
    print("NOT FOUND: e26 date")

# 3. Add e47 to June 10 calendar day (after e16 line)
old_june10 = r"""   10: [{id:'e14',flag:'cn',name:'中国CPI/PPI',cls:'pill-cn',stars:'★★'},{id:'e15',flag:'us',name:'美国CPI',cls:'pill-fed high',stars:'★★★'},{id:'e16',flag:'ca',name:'加央行决议',cls:'pill-boc',stars:'★★'}],"""
new_june10 = r"""   10: [{id:'e14',flag:'cn',name:'中国CPI/PPI',cls:'pill-cn',stars:'★★'},{id:'e15',flag:'us',name:'美国CPI',cls:'pill-fed high',stars:'★★★'},{id:'e16',flag:'ca',name:'加央行决议',cls:'pill-boc',stars:'★★'},{id:'e47',flag:'zw',name:'津巴布韦锂矿配额',cls:'pill-trade high',stars:'★★★'}],"""
if old_june10 in content:
    content = content.replace(old_june10, new_june10, 1)
    count += 1
    print("OK: e47 added to June 10")
else:
    print("NOT FOUND: June 10 pills")

# 4. Add e26 and e35 to June 12 calendar day (after e51)
old_june12 = r"""   12: [{id:'e21',flag:'us',name:'SpaceX挂牌SPCX',cls:'pill-ipo high',stars:'★★★'},{id:'e22',flag:'us',name:'密歇根初值',cls:'pill-data',stars:''},{id:'e23',flag:'cn',name:'华为HDC',cls:'pill-event high',stars:'★★★'},{id:'e51',flag:'cn',name:'惠科股份申购',cls:'pill-ipo',stars:'★★'}],"""
new_june12 = r"""   12: [{id:'e21',flag:'us',name:'SpaceX挂牌SPCX',cls:'pill-ipo high',stars:'★★★'},{id:'e22',flag:'us',name:'密歇根初值',cls:'pill-data',stars:''},{id:'e23',flag:'cn',name:'华为HDC',cls:'pill-event high',stars:'★★★'},{id:'e51',flag:'cn',name:'惠科股份申购',cls:'pill-ipo',stars:'★★'},{id:'e26',flag:'cn',name:'长鑫科技注册生效',cls:'pill-ipo high',stars:'★★★'},{id:'e35',flag:'cn',name:'社融/M2/信贷',cls:'pill-cn',stars:''}],"""
if old_june12 in content:
    content = content.replace(old_june12, new_june12, 1)
    count += 1
    print("OK: e26+e35 added to June 12")
else:
    print("NOT FOUND: June 12 pills")

# 5. Replace midMonth for June - keep only e27 and e46
old_midmonth = r"""  midMonth: { title: '📅 6月待定日期事件', pills: [
   {id:'e26',flag:'cn',name:'长鑫科技注册生效(6/12)',cls:'pill-ipo high',stars:'★★★'},
   {id:'e27',flag:'cn',name:'长江存储IPO申请(预期)',cls:'pill-ipo',stars:'★★'},
   {id:'e35',flag:'cn',name:'社融/M2/信贷(中旬)',cls:'pill-cn',stars:''},
   {id:'e46',flag:'gn',name:'几内亚铝土矿出口管制(待出台)',cls:'pill-trade high',stars:'★★★'},
   {id:'e47',flag:'zw',name:'津巴布韦锂矿出口配额(已执行)',cls:'pill-trade high',stars:'★★★'},
   {id:'e54',flag:'cn',name:'宇树科技科创板过会(6/1)',cls:'pill-ipo high',stars:'★★★'}
  ]},"""

new_midmonth = r"""  midMonth: { title: '📅 6月待定日期事件', pills: [
   {id:'e27',flag:'cn',name:'长江存储IPO申请(预期)',cls:'pill-ipo',stars:'★★'},
   {id:'e46',flag:'gn',name:'几内亚铝土矿出口管制(待出台)',cls:'pill-trade high',stars:'★★★'}
  ]},"""

if old_midmonth in content:
    content = content.replace(old_midmonth, new_midmonth, 1)
    count += 1
    print("OK: midMonth refactored")
else:
    # Try alternate format
    idx = content.find("6月待定日期事件")
    if idx >= 0:
        print(f"midMonth found at {idx}, but exact string not matched")
        print(repr(content[idx:idx+300]))
    else:
        print("NOT FOUND: midMonth section")

# 6. Update last updated timestamp
old_ts = r"""<!-- last updated: 2026-06-14 18:45 -->"""
new_ts = r"""<!-- last updated: 2026-06-15 03:12 -->"""
if old_ts in content:
    content = content.replace(old_ts, new_ts, 1)
    count += 1
    print("OK: timestamp updated")
else:
    print("NOT FOUND: timestamp")

with open('macro_calendar.html', 'w', encoding='utf-8') as f:
    f.write(content)

print(f"\nTotal changes: {count}")
