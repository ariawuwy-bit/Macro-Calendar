fpath = 'D:/WorkbuddyStudio/MacroCalendar/macro_calendar.html'
with open(fpath, 'r', encoding='utf-8') as f:
    lines = f.readlines()

# Line numbers are 0-indexed, so line 494 = index 493, line 495 = index 494
# Insert after e60 (index 493)
insert_idx = 494  # after line 494 (0-indexed: 493), so insert at position 494

new_panels = [
    '\n',
    ' e61:{flag:\'https://flagcdn.com/w40/cn.png\',title:\'2026夏季达沃斯论坛\',date:\'6月23-25日（大连）\',html:\'<span class="expand-tag pending">待举办</span><strong>世界经济论坛第十七届新领军者年会（夏季达沃斯），6月23-25日在大连举行。</strong>主题"规模化创新"，来自90+国家和地区的1,700余名代表出席。<br><br><strong>核心议题：</strong><br>• 规模化创新：前沿技术从实验推向大规模应用<br>• 全球增长引擎：亚洲作为全球增长核心引擎的角色<br>• 新一轮工业化：AI驱动的产业变革与供应链重构<br>• 地缘经济碎片化：贸易壁垒、关税与产业链安全<br>• 能源转型：绿色技术规模化与关键矿产供应链<br>• 中国政策信号：国家领导人可能发表开幕致辞释放经济政策信号<br><br><strong>对宏观的影响：</strong><br>• 达沃斯论坛是观察中国政策信号的重要窗口，开幕式致辞可能涉及稳增长、扩内需、科技自立等方向<br>• 关键矿产供应链议题与日历中资源国管制（几内亚、印尼、智利等）直接相关，论坛期间可能有矿产合作倡议<br>• AI"规模化创新"主题与陆家嘴论坛科创板AI扩围形成政策共振<br>• 地缘经济碎片化议题将涉及232关税、供应链去风险等中美经贸热点<br><br><strong>对资金的影响：</strong><br>• 若开幕式释放稳增长信号→A股周期/消费板块短线催化<br>• 关键矿产合作倡议→锂、钴、稀土等相关资源股可能受消息驱动<br>• AI规模化创新→大模型、算力、机器人产业链关注度提升<br>• 关注大连本地股（冰山冷热、大连重工等）的地缘主题机会\'},\n',
    ' e61d2:{flag:\'https://flagcdn.com/w40/cn.png\',title:\'夏季达沃斯论坛(第2日)\',date:\'6月24日\',html:\'<span class="expand-tag pending">进行中</span>夏季达沃斯论坛第二日，聚焦AI规模化应用与能源转型分论坛。\'},\n',
    ' e61d3:{flag:\'https://flagcdn.com/w40/cn.png\',title:\'夏季达沃斯论坛(闭幕)\',date:\'6月25日\',html:\'<span class="expand-tag pending">闭幕日</span>夏季达沃斯论坛闭幕日，发布《2026年十大新兴技术》报告。\'},\n',
    ' e62:{flag:\'https://flagcdn.com/w40/eu.png\',title:\'S&P Global PMI初值（欧元区+美国）\',date:\'6月23日 21:45/22:45\',html:\'<span class="expand-tag pending">待发布</span><strong>6月PMI初值：欧元区21:45发布，美国22:45（北京时间）发布。</strong><br><br><strong>背景：</strong><br>• 5月欧元区制造业PMI 49.5（收缩），服务业PMI 53.2（扩张）<br>• 5月美国ISM制造业PMI 54.0%（四年新高），S&P Global制造业PMI 52.0%<br>• 6月PMI初值是FOMC鹰派决议后首个重要经济数据，直接影响市场对"经济强+政策鹰"叙事的定价<br><br><strong>关注点：</strong><br>• 欧元区PMI若重回50以上→欧元走强，欧央行7/23加息预期升温<br>• 美国PMI若维持54+高位→确认经济韧性，"更高更久"利率叙事强化<br>• 若PMI意外走弱→市场可能重新定价降息预期，美债收益率下行<br><br><strong>对宏观的影响：</strong><br>• 美国PMI强劲→消费韧性和制造业复苏确认，美联储年内降息窗口进一步收窄<br>• 欧元区PMI若回升→欧盟经济衰退担忧缓解，欧央行政策路径更可预测<br>• PMI价格分项值得关注：若投入/产出价格分项跳升→通胀压力从能源向制造业传导<br><br><strong>对资金的影响：</strong><br>• 美国PMI超预期→美元走强，黄金承压，美债收益率上行<br>• 欧元区PMI超预期→欧元走强，欧股上涨<br>• PMI价格分项跳升→通胀保值债券（TIPS）需求上升，大宗商品获得支撑\'},\n',
]

# Insert the new panels
for i, panel in enumerate(new_panels):
    lines.insert(insert_idx + i, panel)

with open(fpath, 'w', encoding='utf-8') as f:
    f.writelines(lines)

print(f'Inserted {len(new_panels)} lines after line 494')
print('Done!')
