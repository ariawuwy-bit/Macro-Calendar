with open('macro_calendar.html', 'r', encoding='utf-8') as f:
    content = f.read()

# The j70 entry to insert after j69
j70_entry = """j70:{flag:'https://flagcdn.com/w40/cn.png',title:'中际旭创港股IPO',date:'7月中旬 待定',html:'<span class="expand-tag pending">待上市</span><strong>★★★ 港股2026年最大IPO。</strong>中际旭创（InnoLight，300308.SZ）计划7月中旬登陆港交所，代码待定。拟募资<strong>546亿港元（约70亿美元）</strong>，为2026年港股市场规模最大的IPO项目。<br><br><strong>关键信息：</strong><br>• A股代码300308.SZ，为全球光模块龙头，AI数据中心核心供应商<br>• 2025年营收超400亿元，净利润超80亿元，盈利能力强劲<br>• 港股二次上市（A+H），募资用于海外产能扩张+下一代1.6T/3.2T光模块研发<br>• 联席保荐人：高盛、摩根士丹利、中金公司<br>• 预计7月中旬正式挂牌，具体日期待港交所聆讯结果<br><br><strong>对宏观的影响：</strong><br>• 中际旭创港股上市是"AI基础设施资本化"浪潮的关键里程碑，光模块赛道获全球资本认可<br>• A+H双平台打通→中国AI产业链核心环节获得国际定价权，对美股NVDA供应链叙事形成部分对冲<br>• 546亿港元募资为港股2026年最大IPO→对港股流动性形成阶段性压力，但被动资金（恒科指数纳入）将形成对冲<br><br><strong>对资金的影响：</strong><br>• 申购冻结资金约<strong>1,500-2,500亿港元</strong>，对港股短期流动性有压制<br>• 挂牌后快速纳入恒生科技指数→触发约<strong>20-30亿美元</strong>被动资金强制买入<br>• A股中际旭创（300308.SZ）面临"H股上市→A股稀缺性下降→估值承压"逻辑，但港股定价可能反过来锚定A股估值上限<br>• AI光模块产业链（源杰科技、光库科技、博创科技）获情绪联动催化<br>• 与长鑫科技（295亿A股）、宇树科技（42亿A股）形成"硬科技IPO三剑客"→6-8月全球IPO吸金规模超2,000亿元'},
"""

# Find j69 entry end (the closing } of j69)
# Insert after j69's complete entry
j69_end = content.find('  },', content.find("j69:{flag")) + 4  # Find first "})," after j69 start

print("j69 found at:", content.find("j69:{flag"))
print("First '  },' after j69 at:", j69_end)

# Actually, let's find the exact end of j69 by searching for the pattern more precisely
j69_start = content.find("j69:{flag")
if j69_start == -1:
    print("j69 not found!")
else:
    # Find the end of j69 entry - it ends with "},\n" (comma after closing brace)
    # Look for "},\n" after j69_start, but not inside the html string
    # Simpler: find the next "j" entry after j69 (j56 or jNN)
    # Actually after j69 comes j56 (Congo cobalt)
    j56_start = content.find("j56:{flag", j69_start)
    print("j56 starts at:", j56_start)
    if j56_start > j69_start:
        # The text between j69_start and j56_start is j69 + whitespace
        j69_full = content[j69_start:j56_start]
        print("j69 entry length:", len(j69_full))
        print("j69 entry ends with:", repr(j69_full[-100:]))
        
        # Now insert j70 between j69 and j56
        new_content = content[:j56_start] + j70_entry + "\n" + content[j56_start:]
        
        with open('macro_calendar.html', 'w', encoding='utf-8') as f:
            f.write(new_content)
        print("j70 inserted after j69!")
    else:
        print("j56 not found after j69")
