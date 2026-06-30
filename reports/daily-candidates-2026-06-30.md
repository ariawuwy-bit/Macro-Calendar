# 每日宏观日历候选更新报告

- 运行时间：2026-06-30 15:11:39 CST（北京时间）
- 工作区状态：检查到 `index.html`、`macro_calendar.html` 已有未提交改动；`reports/`、`scripts/` 为未跟踪目录
- 本次操作：仅生成本候选报告，未修改 `index.html` / `macro_calendar.html`
- 是否建议同步：建议人工确认后同步；本次最高优先级是修正 BOE 日期

## 新增候选

| 日期（北京时间） | 候选标题 | 类型 | 建议星级 | 置信度 | 是否建议同步 | 说明 |
| --- | --- | --- | --- | --- | --- | --- |
| 7月30日 19:00 | BOE决议 | 央行会议 | ★★★ | 高 | 建议 | 英国央行官网当前显示 Bank Rate 下一次决议日期为 2026年7月30日。当前 HTML 已无 7/30 BOE 条目，应恢复为高优先级央行事件。 |
| 7月7日 20:30 | 美国贸易帐 | 经济数据 | ★ | 中 | 可选 | BEA 官方日程列出 2026年5月美国国际贸易数据于美东 7/7 08:30 发布。对美元、商品链、港口链有参考价值，但重要性低于 CPI/PCE/就业。昨日候选仍未体现在当前 HTML。 |

## 更新候选

| 现有条目 | 当前状态 | 建议更新 | 置信度 | 是否建议同步 | 来源与理由 |
| --- | --- | --- | --- | --- | --- |
| `a03` | 8月6日 BOE决议 | 删除或移至 7月30日；若采用移动，标题保留“BOE决议”，详情改为英国央行 7/30 决议 | 高 | 建议 | BOE 官网确认下一次 Bank Rate 决议为 7/30；当前 8/6 日期与官方口径不符。 |
| `j13` | 7月23日 ECB决议 | 保留日期；详情可补充“7/22-7/23 会议，7/23 会后发布会” | 高 | 可选 | ECB 官方会议日程显示 7/23 为货币政策会议 Day 2 并有 press conference。 |
| `j18` | 7月31日 BOJ决议 | 当前已体现在 HTML，保持 | 高 | 已体现在工作区 | BOJ 官方日程为 7/30-7/31，7/31 发布 Outlook Report。 |
| `j20` | 8月4日 美国JOLTS职位空缺 | 当前已体现在 HTML，保持 | 高 | 已体现在工作区 | BLS 8月日程列出 8/4 美东 10:00 发布 6月 JOLTS。 |
| `a07` | 8月13日 美国7月PPI | 当前已体现在 HTML，保持 | 高 | 已体现在工作区 | BLS 8月日程列出 8/13 美东 08:30 发布 7月 PPI。 |
| `a12` | 8月26日 美国Q2 GDP修正值 | 当前已体现在 HTML，保持 | 高 | 已体现在工作区 | BEA 日程列出 8/26 美东 08:30 发布 Q2 GDP Second Estimate。 |
| `a13` | 8月26日 美国7月PCE | 当前已体现在 HTML，保持 | 高 | 已体现在工作区 | BEA 日程列出 8/26 美东 08:30 发布 7月 Personal Income and Outlays。 |
| `j57`/`j58` | 7月28日 FOMC第1日、7月30日 FOMC决议 | 保留；详情说明美东 7/28-7/29，决议北京时间 7/30 02:00 | 高 | 可选 | Fed 官方 FOMC 日程确认 7/28-7/29。 |

## 删除/降级建议

| 现有条目 | 建议 | 置信度 | 是否建议同步 | 理由 |
| --- | --- | --- | --- | --- |
| `a03` 8月6日 BOE决议 | 删除或移动到 7月30日 | 高 | 建议 | 与 BOE 官网“Next due: 30 July 2026”不一致；若恢复 7/30 BOE，应避免 8/6 重复/错误。 |
| `j03` 7月4日 独立日休市 | 保持删除/不恢复 | 高 | 已体现在工作区 | 2026年7月4日为周六，BLS 7月日程显示 7/3 为 Independence Day holiday；当前已有 7/3 美股美债休市，7/4 不宜重复。 |
| `a14` 8月下旬 美国消费者信心 | 保持待核实，不放具体 8/29 | 中 | 已体现在工作区 | 8/29 为周六，当前 HTML 已改为“8月下旬 待定”，比固定日期更稳妥。 |
| 普通/中型 IPO（如 Oura、Consensys 等） | 降级或不展示在主日历 | 中 | 建议人工复核 | 与项目口径相比，除 OpenAI、Databricks、Canva、Kraken 等可能有显著流动性影响者，普通 IPO 不应挤占宏观日历。 |

## 排除项

| 项目 | 处理 | 理由 |
| --- | --- | --- |
| 普通中小 IPO / 医疗股 IPO | 排除 | 不符合“只收超级 IPO 或显著流动性事件”的口径。 |
| 美国普通周度初请（非节假日前后） | 默认不新增 | 容易变成周度噪音；当前 7/2 初请因非农和提前收盘同日可保留。 |
| BLS 地区就业、房价、低权重住房数据 | 默认不新增 | 重要性低于 CPI、PPI、PCE、就业、GDP、ECI。 |
| BEA 7/21 直接投资、7/10 服务贸易扩展明细 | 排除 | 对宏观交易窗口影响有限，不符合主日历优先级。 |
| 未有官方确认的新资源国政策传闻 | 暂不新增 | 等政府/监管原文或权威财经媒体确认后再收。 |

## 来源链接

- Federal Reserve：FOMC 2026 年会议日程（7/28-7/29）  
  https://www.federalreserve.gov/monetarypolicy/fomccalendars.htm
- BLS：Schedule of Selected Releases for July 2026（就业、CPI、PPI、ECI 等）  
  https://www.bls.gov/schedule/2026/07_sched.htm
- BLS：Schedule of Selected Releases for August 2026（JOLTS、非农、CPI、PPI 等）  
  https://www.bls.gov/schedule/2026/08_sched.htm
- BEA：Release Schedule（贸易帐、GDP、Personal Income and Outlays）  
  https://www.bea.gov/news/schedule
- Bank of Japan：Monetary Policy Meetings 2026（7/30-7/31）  
  https://www.boj.or.jp/en/mopo/mpmsche_minu/index.htm
- European Central Bank：Governing Council meeting calendar（7/22-7/23）  
  https://www.ecb.europa.eu/press/calendars/mgcgc/html/index.en.html
- Bank of England：Interest rates and Bank Rate（Next due: 30 July 2026）  
  https://www.bankofengland.co.uk/monetary-policy/the-interest-rate-bank-rate

## 同步建议

建议同步：

1. 恢复/新增 `7月30日 BOE决议`，星级 ★★★，央行高优先级。
2. 删除或移动当前 `a03 8月6日 BOE决议`，避免错误日期。
3. 可选新增 `7月7日 美国贸易帐`，星级 ★，若希望保持主日历精简可不加。

暂缓同步：

1. 普通 IPO 与中型 IPO 是否降级，需要结合用户偏好的“流动性影响”阈值人工确认。
2. 资源国政策待定项建议继续等待官方或权威媒体新进展。

提醒：本报告只是候选清单；需要用户确认后，才可以把认可的更新写入 HTML，并由用户决定是否同步到 GitHub。
