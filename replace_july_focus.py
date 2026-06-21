with open('macro_calendar.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

# Line 368-376 (0-indexed: 367-375) contain the July focus block
# We need to replace lines 368-376 (0-indexed: 367-375)
# New focus block lines:
new_focus_lines = [
    "  focus: [\n",
    "   {bg:'var(--red-bg)',bc:'var(--red)',tc:'var(--red)',title:'FOMC决议',body:'7/28-29 FOMC会议，6月点阵图后首次决议，是否释放9月降息信号是核心关注'},\n",
    "   {bg:'var(--blue-bg)',bc:'var(--blue)',tc:'var(--blue)',title:'ECB利率',body:'7/23 ECB决议，6月加息后是否连续加息，拉加德新闻发布会措辞是关键'},\n",
    "   {bg:'var(--purple-bg)',bc:'var(--purple)',tc:'var(--purple)',title:'BOJ+BOE',body:'7/30日BOJ与BOE同日决议，BOJ是否继续加息、日元套利交易平仓风险需警惕'},\n",
    "   {bg:'var(--green-bg)',bc:'var(--green)',tc:'var(--green)',title:'GDP速报+PCE',body:'7/30同日发布Q2 GDP速报+6月PCE，两大核心数据叠加FOMC次日，市场波动极大'},\n",
    "   {bg:'var(--orange-bg)',bc:'var(--orange)',tc:'var(--orange)',title:'Q2 GDP(中国)',body:'7/15公布Q2 GDP，市场预期4.8-5.2%，若低于5%将触发降息降准预期'},\n",
    "   {bg:'rgba(184,148,62,0.06)',bc:'var(--gold)',tc:'var(--gold-dim)',title:'🛢️ 资源国执行',body:'7/1中国《对外投资规定》施行；印尼ESDM 6/18辟谣配额放宽、7/1-31镍矿RKAB修订窗口开启；几内亚铝土矿4/25签署1.5亿吨硬限额6月起严格执行；刚果钴/印尼镍/智利锂/澳洲CMPTI 7-8月密集推进；资源民族主义对全球有色金属定价权影响深化'},\n",
    "   {bg:'var(--lime-bg)',bc:'var(--lime)',tc:'var(--lime)',title:'⚽ 世界杯闭幕',body:'7/19决赛，美加墨世界杯创48队纪录，650万球迷推升CPI分项0.2-0.5个百分点'},\n",
    "   {bg:'rgba(212,118,10,0.06)',bc:'#d4760a',tc:'#d4760a',title:'🚀 IPO潮+解禁双压',body:'宇树科技7月上旬科创板挂牌+长鑫存储7-8月科创板+华润新能源6/22申购245亿+Anthropic/OpenAI路演预期+7/8智谱基石解禁11.6%+7/9 MiniMax解禁63%形成港股AI集中抛压'},\n",
    "  }],\n",
]

# Replace lines 367 to 376 (exclusive of 376 = line 376 is "  },")
# Actually lines 367-375 are the focus block (9 lines)
# Let's check what line 376 is
print("Line 367 (0-idx):", repr(lines[367]))
print("Line 375 (0-idx):", repr(lines[375]))
print("Line 376 (0-idx):", repr(lines[376]) if len(lines) > 376 else "EOF")

# Replace lines 367-375 (9 lines) with new_focus_lines
lines[367:376] = new_focus_lines

with open('macro_calendar.html', 'w', encoding='utf-8') as f:
    f.writelines(lines)

print("Done! Focus block replaced.")
