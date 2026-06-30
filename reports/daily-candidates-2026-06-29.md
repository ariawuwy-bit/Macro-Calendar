# 每日宏观日历候选更新报告

- 运行时间：2026-06-29 08:03:17 CST（北京时间）
- 工作区状态：检查到未跟踪目录 `scripts/`，本次未改动；未执行 `git add`、`commit`、`push`
- 本次操作：仅生成候选报告，未修改 `index.html` / `macro_calendar.html`
- 是否建议同步：建议先人工确认以下“高置信更新/删除”后，再同步到页面与 GitHub

## 新增候选

| 日期（北京时间） | 候选标题 | 类型 | 建议星级 | 置信度 | 是否建议同步 | 说明 |
| --- | --- | --- | --- | --- | --- | --- |
| 7月7日 20:30 | 美国贸易帐 | 经济数据 | ★ | 中 | 可选 | BEA 日程列出 5 月国际贸易数据；对美元、商品与港口链有参考价值，但重要性低于 CPI/PCE/就业。 |
| 7月31日 20:30 | 美国ECI劳工成本 | 经济数据 | ★★ | 高 | 建议 | BLS 日程列出 Q2 Employment Cost Index。ECI 是美联储观察工资通胀的重要指标，当前 7/31 已有中国 PMI、建议同日新增。 |
| 8月4日 22:00 | 美国JOLTS职位空缺 | 经济数据 | ★★ | 高 | 建议 | BLS 日程显示 6 月 JOLTS 在 8/4 发布。当前 7/31 的“美国JOLTS”建议移动到 8/4，而不是重复新增。 |

## 更新候选

| 现有条目 | 当前日期/标题 | 建议更新 | 置信度 | 是否建议同步 | 来源与理由 |
| --- | --- | --- | --- | --- | --- |
| `j18` | 7月30日 BOJ决议 | 移至 7月31日；标题保留“BOJ决议” | 高 | 建议 | BOJ 官方日程显示 7 月会议为 7/30-7/31；利率声明通常在会议最后一日发布。 |
| `j20` | 7月31日 美国JOLTS | 移至 8月4日；标题改为“美国JOLTS职位空缺” | 高 | 建议 | BLS 官方日程显示 6 月 JOLTS 为 8/4 22:00（北京时间）。 |
| `a07` | 8月14日 美国PPI | 移至 8月13日 20:30；标题建议“美国7月PPI” | 高 | 建议 | BLS 官方日程显示 7 月 PPI 为 8/13。 |
| `a12` | 8月27日 美国GDP修正值 | 移至 8月26日 20:30；标题建议“美国Q2 GDP修正值” | 高 | 建议 | BEA 官方日程显示 Q2 GDP 二次估算为 8/26。 |
| `a13` | 8月28日 美国PCE | 移至 8月26日 20:30；标题建议“美国7月PCE” | 高 | 建议 | BEA 官方日程显示 7 月 Personal Income and Outlays 为 8/26。 |
| `j13` | 7月23日 ECB决议 | 保留日期；详情可补充“北京时间 20:15 决议、20:45 新闻发布会” | 高 | 可选 | ECB 官方日程确认 7/23 为货币政策会议。 |
| `j57`/`j58` | 7月28日 FOMC第1日、7月30日 FOMC决议 | 保留；详情说明美东 7/28-7/29，决议北京时间 7/30 02:00 | 高 | 可选 | Fed 官方 FOMC 日程确认 7/28-7/29；当前按北京时间放在 7/30 合理。 |

## 删除/降级建议

| 现有条目 | 建议 | 置信度 | 是否建议同步 | 理由 |
| --- | --- | --- | --- | --- |
| `j03` 7月4日 独立日休市 | 删除或降级为说明，不作为独立交易休市事件 | 高 | 建议 | 2026 年 7/4 为周六，官方交易休市重点应是 7/3 观察假日；当前已有 `j78` 7/3 美股美债休市，7/4 易重复。 |
| `j19` 7月30日 BOE决议 | 删除或移入“待核实” | 中 | 建议人工确认 | 当前 8/6 已有 BOE 决议；英国央行通常不在 7 月另开常规 MPC 决议。建议先删 7/30，保留 8/6。 |
| `a14` 8月29日 美国消费者信心 | 改期待核实或降级 | 中 | 暂不自动同步 | Conference Board 消费者信心通常在月内较早的周二发布，8/29 为周六，当前日期可疑；需进一步用官方发布日程确认。 |

## 排除项

| 项目 | 处理 | 理由 |
| --- | --- | --- |
| 普通中小 IPO / 医疗股 IPO | 排除 | 不符合项目“只收超级 IPO 或显著流动性事件”的口径。 |
| 美国普通周度初请（非节假日前后） | 默认不新增 | 已有 7/2 初请与非农、提前收盘同日，后续周度初请不建议逐周加入，避免噪音。 |
| 普通房价/区域房产数据 | 默认不新增 | 除非与 FOMC 前关键通胀/增长窗口重叠，否则重要性低于 CPI、PCE、就业、GDP。 |
| 未找到官方确认的资源国政策传闻 | 暂不新增 | 印尼、刚果、智利等资源政策若无监管/政府原文或权威媒体新进展，不建议继续堆待定条目。 |

## 来源链接

- Federal Reserve：FOMC 日程（2026 年 7/28-7/29，纪要 8/19）  
  https://www.federalreserve.gov/monetarypolicy/fomccalendars.htm
- BLS：Economic News Release Schedule，2026 年 7 月（非农、CPI、PPI、ECI 等）  
  https://www.bls.gov/schedule/news_release/2026-07_sched.htm
- BLS：Economic News Release Schedule，2026 年 8 月（JOLTS、PPI、CPI、非农等）  
  https://www.bls.gov/schedule/news_release/2026-08_sched.htm
- BEA：News Release Schedule（GDP、Personal Income and Outlays、贸易帐）  
  https://www.bea.gov/news/schedule
- Bank of Japan：Monetary Policy Meetings schedule（7/30-7/31）  
  https://www.boj.or.jp/en/mopo/mpmsche_minu/index.htm
- European Central Bank：Governing Council meeting calendar（7/23 货币政策会议）  
  https://www.ecb.europa.eu/press/calendars/mgcgc/html/index.en.html
- SIFMA：Holiday schedule（美国债市提前收盘/休市参考）  
  https://www.sifma.org/resources/general/holiday-schedule/

## 同步建议

建议同步：上述高置信更新中，优先处理 `j18`、`j20`、`a07`、`a12`、`a13`、`j03`。这些主要是官方日程校正，重复/错误风险较低。

暂缓同步：`j19`、`a14`、资源国政策待定条目，建议用户确认或补充来源后再处理。

提醒：本报告只是候选清单；需要用户确认后，才可以把认可的更新写入 HTML，并由用户决定是否同步到 GitHub。
