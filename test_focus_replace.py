import sys
import os

filepath = 'macro_calendar.html'

with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

# The old focus block (as present in the file)
old_focus = """  focus: [
   {bg:'var(--red-bg)',bc:'var(--red)',tc:'var(--red)',title:'FOMC决议',body:'7/28-29 FOMC会议，6月点阵图后首次决议，是否释放9月降息信号是核心关注'},
   {bg:'var(--blue-bg)',bc:'var(--blue)',tc:'var(--blue)',title:'ECB利率',body:'7/23 ECB决议，6月加息后是否连续加息，拉加德新闻发布会措辞是关键'},
   {bg:'var(--purple-bg)',bc:'var(--purple)',tc:'var(--purple)',title:'BOJ政策',body:'7/30日央行决议，6月加息后是否继续加息，日元套利交易平仓风险'},
   {bg:'var(--orange-bg)',bc:'var(--orange)',tc:'var(--orange)',title:'Q2 GDP',body:'中国7/15公布Q2 GDP，市场预期4.8-5.2%，若低于5%将触发降息降准预期'},
   {bg:'rgba(184,148,62,0.06)',bc:'var(--gold)',tc:'var(--gold-dim)',title:'🛢️ 资源国执行',body:'7/1中国《对外投资规定》施行；印尼ESDM 6/18辟谣配额放宽、7/1-31镍矿RKAB修订窗口开启；几内亚铝土矿4/25签署1.5亿吨硬限额、6月起严格执行，6月发运量已主动收缩500万吨；刚果钴/印尼镍/智利锂/澳洲CMPTI 7-8月密集推进；资源民族主义对全球有色金属定价权影响深化'},
   {bg:'var(--lime-bg)',bc:'var(--lime)',tc:'var(--lime)',title:'⚽ 世界杯闭幕',body:'7/19决赛，美加墨世界杯创48队纪录，650万球迷推升CPI分项0.2-0.5个百分点'},
   {bg:'rgba(212,118,10,0.06)',bc:'#d4760a',tc:'#d4760a',title:'🚀 IPO潮+解禁双压',body:'宇树科技7上旬科创板挂牌 + 长鑫存储7-8月科创板 + Anthropic秘密交表后路演预期 + Kraken/Canva Q3上市 + 7/8智谱基石解禁11.6%+7/9 MiniMax解禁63%形成港股AI集中抛压+1500亿港元解禁规模'}
  },"""

print("Old focus found:", old_focus in content)
print("Occurrences:", content.count(old_focus))
