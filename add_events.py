import re

with open('macro_calendar.html', 'r', encoding='utf-8') as f:
    content = f.read()

count = 0

# ============ 1. Add pills to allEventData (calendar day grids) ============

# e57 G7峰会 -> June 15 (add to existing day 15)
old_d15 = "   15: [{id:'e24',flag:'us',name:'工业生产',cls:'pill-data',stars:''},{id:'e52',flag:'cn',name:'粤芯半导体上会',cls:'pill-ipo',stars:'★★'},{id:'e53',flag:'cn',name:'矿产资源法实施条例',cls:'pill-cn high',stars:'★★★'}],"
new_d15 = "   15: [{id:'e24',flag:'us',name:'工业生产',cls:'pill-data',stars:''},{id:'e52',flag:'cn',name:'粤芯半导体上会',cls:'pill-ipo',stars:'★★'},{id:'e53',flag:'cn',name:'矿产资源法实施条例',cls:'pill-cn high',stars:'★★★'},{id:'e57',flag:'fr',name:'G7峰会(埃维昂)',cls:'pill-event high',stars:'★★★'}],"
if old_d15 in content:
    content = content.replace(old_d15, new_d15, 1)
    count += 1
    print("OK: e57 added to June 15")
else:
    print("NOT FOUND: June 15 pills")

# e58 美伊协议达成 -> June 14 (currently empty)
old_d14 = "   14: [],"
new_d14 = "   14: [{id:'e58',flag:'ir',name:'🕊️美伊停战协议',cls:'pill-trade high',stars:'★★★'}],"
if old_d14 in content:
    content = content.replace(old_d14, new_d14, 1)
    count += 1
    print("OK: e58 added to June 14")
else:
    print("NOT FOUND: June 14 empty")

# e59 美伊签字仪式 -> June 19 (currently has e33 Juneteenth)
old_d19 = "   19: [{id:'e33',flag:'us',name:'Juneteenth休市',cls:'pill-event',stars:''}],"
new_d19 = "   19: [{id:'e33',flag:'us',name:'Juneteenth休市',cls:'pill-event',stars:''},{id:'e59',flag:'ch',name:'美伊正式签字(瑞士)',cls:'pill-trade high',stars:'★★★'}],"
if old_d19 in content:
    content = content.replace(old_d19, new_d19, 1)
    count += 1
    print("OK: e59 added to June 19")
else:
    print("NOT FOUND: June 19 pills")

# ============ 2. Add eventData entries (after e56) ============

old_e56_end = """  // ===== JULY ====="""

new_events = """
 e57:{flag:'https://flagcdn.com/w40/fr.png',title:'G7峰会（埃维昂）',date:'6月15-17日',html:'<span class="expand-tag released">已开幕</span><strong>📊 第52届G7峰会于6月15日在法国埃维昂莱班开幕。</strong>法国担任轮值主席国，6/15-17为期三天。<br><br><strong>核心议题：</strong><br>• <strong>中东局势与美伊协议</strong>：6/14美伊停战协议达成、霍尔木兹海峡开放——这是G7开幕前最重磅的地缘变化，将主导峰会讨论<br>• <strong>AI治理与出口管制</strong>：法国力推AI全球治理框架，与美国在技术封锁范围上存在分歧<br>• <strong>贸易战与关税协调</strong>：美欧关税分歧持续，特朗普232关税与欧盟反制措施是焦点<br>• <strong>乌克兰援助</strong>：G7内部对援助规模和方式存在分歧<br>• <strong>全球债务与发展融资</strong>：法国突破G7封闭传统，邀请中东国家、新兴经济体及国际金融机构参会<br><br><strong>特别看点：</strong><br>• 法国顶着美日反对，将G7办成"扩大版世界大会"——特邀中国等多方出席，罕见突破G7封闭排他传统<br>• 特朗普14日刚过完80岁生日，15日即赴会——美伊协议后的首次G7，特朗普可能以"和平缔造者"姿态主导议程<br>• 联合公报能否就贸易和中东达成一致是最大悬念——去年加拿大峰会上特朗普提前离场，公报都没发<br><br><strong>对宏观的影响：</strong><br>• 若G7就贸易关税达成协调框架→全球贸易战风险降温，制造业PMI预期上修，利好出口导向型经济体<br>• 若G7就AI出口管制达成更严标准→中国AI产业链（芯片、设备）面临进一步限制，国产替代逻辑强化<br>• 美伊协议已在G7开幕前达成→中东地缘风险溢价大幅消退，能源价格下行压力加大，全球通胀预期下修<br>• 若联合公报提及对华政策调整→人民币汇率和A股外资流向将直接受影响<br><br><strong>对资金的影响：</strong><br>• G7贸易关税协调若取得进展→全球风险偏好回升，资金从避险资产（黄金、美债）流向风险资产（新兴市场、成长股）<br>• AI出口管制加严→A股AI概念股短期承压，但国产替代概念（寒武纪、海光信息）反而受益<br>• 中东风险消退→原油空头逻辑强化，能源股承压；黄金避险需求边际下降<br>• 联合公报若提及中国→人民币汇率波动加大，北向资金流向受影响'},
 e58:{flag:'https://flagcdn.com/w40/ir.png',title:'美伊停战协议达成 + 霍尔木兹海峡开放',date:'6月14日 周六',html:'<span class="expand-tag released">已生效</span><strong>📊 6月14日美东时间下午，特朗普宣布美伊协议"已完成"，正式批准霍尔木兹海峡"免费开放"，下令立即解除美国海军海上封锁。</strong>伊朗最高国家安全委员会15日凌晨确认伊美停战谅解备忘录达成。巴基斯坦总理夏巴兹15日确认美伊已达成和平协议。<br><br><strong>14项条款核心内容：</strong><br>• <strong>所有战线即刻永久停火</strong>，含黎巴嫩战线<br>• <strong>霍尔木兹海峡重新开放，无通行费</strong><br>• <strong>60天内谈判伊朗浓缩铀问题</strong><br>• 美国逐步解除对伊朗制裁及海上封锁<br>• 伊朗承诺"无限期不获取或研发核武器"<br>• 如有违规，将通过调解协调机制处理<br>• 正式签字仪式定于6月19日在瑞士举行<br><br><strong>对宏观的影响：</strong><br>• 霍尔木兹海峡是全球约20%石油运输的咽喉通道——重新开放意味着<strong>中东能源风险溢价大幅消退</strong>，布伦特原油价格中枢预计下移$8-15/桶<br>• 5月PPI能源分项环比+10.7%（汽油+23.4%）的主因——霍尔木兹封锁——正在逆转，<strong>6月PPI能源分项将大幅回落</strong>，传导至7-8月CPI能源分项下行<br>• 伊朗石油可自由出口→全球原油供给边际增加约1.5-2百万桶/日，供需格局从偏紧转向宽松<br>• 中东地缘风险系统性下修→全球通胀预期下修，美联储9月降息概率回升<br>• 60天浓缩铀谈判是后续核心风险——若谈判破裂，停火可能瓦解<br><br><strong>对资金的影响：</strong><br>• <strong>原油：</strong>霍尔木兹开放+伊朗石油回归→布伦特原油空头逻辑确立，$65-70/桶可能成为新中枢（此前$75-85）<br>• <strong>黄金：</strong>地缘风险溢价消退→避险需求下降，黄金承压；但若60天核谈破裂则迅速反弹<br>• <strong>铜铝等工业金属：</strong>霍尔木兹开放降低运输保险费→中东-亚洲航线运费回落，LME铝价承压；但中国铝土矿进口（几内亚航线不经霍尔木兹）影响有限<br>• <strong>LNG/天然气：</strong>卡塔尔LNG出口恢复正常→亚洲LNG现货价格下行，利好日韩印等进口国<br>• <strong>能源股：</strong>ExxonMobil、雪佛龙、中海油短线承压；但伊朗产量回归需要6-12个月爬坡，短期供给冲击有限<br>• <strong>航空/航运：</strong>霍尔木兹通行费取消+保险费回落→中远海控、马士基等航运股成本改善；航空股燃油成本下行<br>• <strong>美联储降息预期：</strong>通胀下行预期升温→9月降息概率从此前约35%回升至50%+→美债收益率下行，成长股估值修复'},
 e59:{flag:'https://flagcdn.com/w40/ch.png',title:'美伊正式签字仪式（瑞士）',date:'6月19日 周四',html:'<span class="expand-tag pending">待举办</span><strong>美伊停战谅解备忘录正式签字仪式。</strong>6月14日双方确认协议文本后，正式签字仪式定于6月19日在瑞士举行。<br><br><strong>核心看点：</strong><br>• 签字仪式由巴基斯坦斡旋主持，瑞士提供中立场地<br>• 14项条款正式签署后具有国际法约束力<br>• 60天浓缩铀谈判的启动时间和框架可能同步公布<br>• 签字后伊朗石油出口的回归时间表将明确<br><br><strong>对宏观的影响：</strong><br>• 正式签字将6/14的口头确认转化为法律效力→中东和平前景进一步确认，能源市场风险溢价持续消退<br>• 60天核谈启动→若市场预期谈判顺利→伊朗石油全面回归预期升温，油价进一步承压<br>• 若签字仪式出现意外（如伊朗代表临时提出新条件）→市场将剧烈波动，油价反弹$3-5/桶<br><br><strong>对资金的影响：</strong><br>• 签字顺利→原油继续承压，黄金避险需求进一步下降<br>• 签字意外→油价反弹+黄金上涨+美债收益率下行的避险组合<br>• 60天核谈框架若包含"分阶段解除制裁"→伊朗石油回归时间线更明确，中期原油供给预期上修'},

  // ===== JULY ====="""

content = content.replace(old_e56_end, new_events, 1)
count += 1
print("OK: e57/e58/e59 eventData added")

# ============ 3. Update weekBanners for央行超级周 ============

old_banner = "{ beforeDay: 15, cls: 'central-bank-week', icon: '🏦', label: '央行超级周', detail: '6/15–6/21 · BOJ+FOMC+BOE三大央行+陆家嘴论坛' }"
new_banner = "{ beforeDay: 15, cls: 'central-bank-week', icon: '🏦', label: '央行超级周+地缘剧变', detail: '6/15–6/21 · G7峰会+美伊协议+BOJ+FOMC+BOE+陆家嘴论坛' }"
if old_banner in content:
    content = content.replace(old_banner, new_banner, 1)
    count += 1
    print("OK: weekBanner updated")
else:
    print("NOT FOUND: weekBanner")

# ============ 4. Add focus items ============

old_focus = """  focus: ["""
new_focus_items = """  focus: [
   {bg:'rgba(46,109,164,0.06)',bc:'#2e6da4',tc:'#2e6da4',title:'🕊️ 美伊停战',body:'6/14美伊协议达成！霍尔木兹海峡开放，伊朗石油可自由出口，布伦特原油中枢下移$8-15。6/19瑞士正式签字。60天浓缩铀谈判是后续核心风险'},
   {bg:'var(--blue-bg)',bc:'var(--blue)',tc:'var(--blue)',title:'🇫🇷 G7埃维昂',body:'6/15-17法国G7峰会，法国邀请新兴经济体参会，AI治理/贸易关税/中东/乌克兰四大议题。特朗普以"和平缔造者"姿态出席'},'"""

# Replace the first focus: [ with our new items prepended
content = content.replace("  focus: [\n   {bg:", "  focus: [\n   {bg:'rgba(46,109,164,0.06)',bc:'#2e6da4',tc:'#2e6da4',title:'🕊️ 美伊停战',body:'6/14美伊协议达成！霍尔木兹海峡开放，伊朗石油可自由出口，布伦特原油中枢下移$8-15。6/19瑞士正式签字。60天浓缩铀谈判是后续核心风险'},\n   {bg:'var(--blue-bg)',bc:'var(--blue)',tc:'var(--blue)',title:'🇫🇷 G7埃维昂',body:'6/15-17法国G7峰会，法国邀请新兴经济体参会，AI治理/贸易关税/中东/乌克兰四大议题'},\n   {bg:", 1)
count += 1
print("OK: focus items added")

# ============ 5. Update timestamp ============

content = content.replace("<!-- last updated: 2026-06-15 03:05 -->", "<!-- last updated: 2026-06-15 13:58 -->", 1)
count += 1
print("OK: timestamp updated")

with open('macro_calendar.html', 'w', encoding='utf-8') as f:
    f.write(content)

print(f"\nTotal changes: {count}")
