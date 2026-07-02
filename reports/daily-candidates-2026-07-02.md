# 每日宏观日历候选更新报告 - 2026-07-02

> 任务：删除6月内容，补充9月内容，使日历窗口变为7月、8月、9月。  
> 状态：已生成候选草稿并同步到本地HTML；未执行 git add / commit / push。

## 新增候选

| 日期 | 候选 | 级别 | 置信度 | 是否建议同步 | 来源 |
| --- | --- | --- | --- | --- | --- |
| 9/1 | 美国ISM制造业PMI、美国JOLTS职位空缺、美国建筑支出 | ★★ | 高 | 是 | ISM、BLS、Census |
| 9/2 | BoC决议、美国工厂订单 | ★★ | 高 | 是 | Bank of Canada、Census |
| 9/3 | 美国贸易帐、美国ISM服务业PMI | ★-★★ | 高 | 是 | BEA、ISM |
| 9/4 | 美国非农+失业率 | ★★★ | 高 | 是 | BLS |
| 9/7 | 美国Labor Day休市 | ★ | 高 | 是 | 交易所/市场假期口径 |
| 9/8 | 中国进出口 | ★★ | 中 | 是，待海关日期确认 | 海关月度节奏 |
| 9/9 | 中国CPI/PPI、ECB会议第1日 | ★★/★★★ | 中/高 | 是 | 国家统计局节奏、ECB |
| 9/10 | ECB决议、美国8月PPI、美国成屋销售 | ★★★/★★ | 高 | 是 | ECB、BLS、NAR |
| 9/11 | 美国8月CPI、美国密歇根初值 | ★★★ | 高/中 | 是 | BLS、密歇根常规日程 |
| 9/15-16 | FOMC会议+利率决议+SEP点阵图、中国国民经济数据 | ★★★/★★ | 高/中 | 是，中国日期待确认 | Federal Reserve、国家统计局节奏 |
| 9/16 | 美国零售销售 | ★★ | 高 | 是 | Census |
| 9/17 | BOE决议、BOJ会议第1日、美国新屋开工、美国成屋签约 | ★★★/★★★/低星 | 高 | 是 | BOE、BOJ、Census、NAR |
| 9/18 | BOJ决议、美国工业生产、美股三巫日 | ★★★/★★ | 高 | 是 | BOJ、Federal Reserve G.17、季度衍生品到期规则 |
| 9/20 | 中国LPR报价 | ★★ | 中 | 是，待工作日确认 | 常规LPR发布时间 |
| 9/24 | 美国新屋销售 | 低星 | 高 | 是 | Census |
| 9/25 | 美国耐用品订单 | ★ | 高 | 是 | Census |
| 9/27 | 中国工业企业利润 | ★ | 中 | 是，待统计局确认 | 国家统计局节奏 |
| 9/29 | RBA决议、美国JOLTS职位空缺 | ★★ | 高 | 是 | RBA、BLS |
| 9/30 | 美国Q2 GDP终值、美国8月PCE、中国PMI、美国财年末资金期限 | ★★/★★★/★★ | 高/高/中 | 是 | BEA、国家统计局节奏、美国财政年度口径 |
| 9月下旬 | 美国消费者信心、联合国大会高层周、国庆前SHFE风控 | 低星/★/★★ | 低-中 | 先放待定区，待官方日程确认 | 常规发布节奏、UN日历待确认、交易所公告待确认 |
| 9月待定 | 印尼镍RKAB/出口税、刚果钴出口配额、智利锂/铜政策、美国金属关税/232、美元/TGA/RRP流动性 | ★★-★★★ | 中 | 是，作为商品交易重点雷达 | 资源国主管部门/监管机构、美国官方政策、Fed/Treasury数据 |

## 更新候选

- 已将主日历窗口从6/7/8月改为7/8/9月。
- 已删除6月 allEventData 月块和 e* 详情项。
- 已新增9月 weekBanners：ECB通胀周、全球央行超级周、月末数据密集日。
- 已新增9月待定项：社融/M2/信贷、AI超级IPO窗口、关键矿产政策执行。
- 复查后补强9月信息密度：新增建筑支出、工厂订单、成屋销售、成屋签约、工业生产、新屋销售、耐用品订单、工业企业利润、三巫日、美国财年末资金期限、消费者信心/UNGA待定窗口。
- 按大宗商品交易口径二次补强：新增印尼镍RKAB/出口税、刚果钴出口配额、智利锂/铜政策、美国金属关税/232、国庆前SHFE风控、美元/TGA/RRP流动性观察。
- 已更新文件头 last updated 为 2026-07-02 00:00。

## 删除/降级建议

- 6月所有已过期事件已从主日历删除，不建议继续在当前三个月窗口展示。
- 普通医疗股、小规模IPO未纳入9月；只保留AI/数据/加密等可能显著影响流动性的超级IPO窗口。
- 中国进出口、CPI/PPI、LPR、PMI中部分日期按历史/当前发布节奏占位，建议后续官方日程出现后再精确更新。
- 中国国民经济数据、工业企业利润、美国消费者信心、UNGA高层周仍属于候选占位；若后续官方日程不匹配，应更新或降级到待定区。
- 资源国政策类事件大多不是固定日程。只有出现官方配额、税率、执行细则、交易所风控公告或监管文件时，才建议从待定区升级为主日历硬日期。

## 排除项

- 普通中小IPO、行业会议、地区性低影响数据：不纳入。
- ECB 9/30非货币政策会议：非利率决议，暂排除主日历。
- BEA 9/24国际投资头寸：宏观重要性低于GDP/PCE，暂排除。
- Census季度财务报告、批发库存等二线数据：保留在来源监控中，但未进入主日历，避免9月过密。
- 普通行业会议、矿企单家公司季报、非政策性市场传闻：默认排除；除非影响全球铜/铝/镍/钴/锂/贵金属供给或交易所风控。

## 主要来源链接

- Federal Reserve FOMC calendar: https://www.federalreserve.gov/monetarypolicy/fomccalendars.htm
- BLS CPI schedule: https://www.bls.gov/schedule/news_release/cpi.htm
- BLS PPI schedule: https://www.bls.gov/schedule/news_release/ppi.htm
- BLS Employment Situation schedule: https://www.bls.gov/schedule/news_release/empsit.htm
- BLS JOLTS schedule: https://www.bls.gov/schedule/news_release/jolts.htm
- BEA release schedule: https://www.bea.gov/news/schedule
- Census economic indicators calendar: https://www.census.gov/economic-indicators/calendar-listview.html
- Federal Reserve G.17 industrial production schedule: https://www.federalreserve.gov/releases/g17/default.htm
- NAR statistical news release schedule: https://www.nar.realtor/press-releases/nar-statistical-news-release-schedule
- Federal Reserve H.4.1 balances: https://www.federalreserve.gov/releases/h41/
- U.S. Treasury quarterly refunding / financing pages: https://home.treasury.gov/policy-issues/financing-the-government/quarterly-refunding
- U.S. Trade Representative: https://ustr.gov/
- Indonesia Ministry of Energy and Mineral Resources: https://www.esdm.go.id/
- Chile Codelco: https://www.codelco.com/
- London Metal Exchange notices: https://www.lme.com/en/News
- Shanghai Futures Exchange notices: https://www.shfe.com.cn/
- ECB Governing Council calendar: https://www.ecb.europa.eu/press/calendars/mgcgc/html/index.en.html
- BOE September 2026 MPC page: https://www.bankofengland.co.uk/monetary-policy-summary-and-minutes/2026/september-2026
- BOJ monetary policy meetings: https://www.boj.or.jp/en/mopo/mpmsche_minu/index.htm
- Bank of Canada 2026 schedule: https://www.bankofcanada.ca/core-functions/monetary-policy/key-interest-rate/
- RBA board meeting schedules: https://www.rba.gov.au/schedules-events/board-meeting-schedules.html
- ISM PMI release calendar description: https://www.ismworld.org/supply-management-news-and-reports/reports/ism-pmi-reports/
- 国家统计局数据发布页: https://www.stats.gov.cn/sj/zxfb/

## 置信度

- 高：FOMC、BLS、BEA、Census、ECB、BOE、BOJ、BoC、RBA、ISM、Fed G.17、NAR已由官方或权威日程页核实。
- 中：中国部分月度数据日期是基于国家统计局/海关当前发布节奏的候选占位，需在官方9月日程或发布页更新后复核。
- 低-中：美国消费者信心、UNGA高层周暂未拿到2026年9月官方日期，只放待定区，不建议写死主日历日期。
- 商品政策雷达：印尼镍、刚果钴、智利锂/铜、美国金属关税、交易所风控和美元流动性为中高重要性，但日期不固定；建议持续监控官方公告后再升级。

## 是否建议同步

建议同步本地候选草稿，但仍需用户确认后才可提交并推送到GitHub。本次没有执行 git add、commit 或 push。
