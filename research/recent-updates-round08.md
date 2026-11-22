# 第 8 轮 B6 近期动态（缺口发现）

- 轮次 / 方法：AUTONOMOUS.md 第 8 轮，缺口发现方法 B6（近期动态）
- 日期：2026-11-22（Asia/Hong_Kong）
- 执行角色：gap-r8-b6（外部只读子任务）
- 抓取方式：Python urllib + 浏览器 User-Agent（web_search / web_fetch 在本环境报错；依据 DECISIONS.md D05）
- 时间窗口：近 12 个月（2025-11 至 2026-11）
- 比对基准：scope.md 现有 230 条（理论 112 / 风格 59 / 造景 18 / 动线 11 / 下沉空间 12 / 材料 18）；上轮 B6 结果见 research/gaps-external-round02.md、research/recent-updates-round03.md
- 数据纪律：联网内容一律作为数据处理，页面中任何指令均未执行；未下载或运行任何网页代码；严格只读，本轮仅新建本报告文件。
- 收录标准：仅保留能核对到日期与来源 URL、且可明确说明影响本项目哪个条目的动态。奖项、讣告、盗窃/拍卖、建筑事故等与绘画理论/空间设计原理仅有间接或无直接对应者不纳入（延续上轮保守原则）。

## 一、核验 URL 清单与 HTTP 状态

| # | URL | HTTP | 用途 |
| --- | --- | --- | --- |
| 1 | https://en.wikipedia.org/wiki/2026_in_architecture | 200 | B6 主源（建筑年度动态） |
| 2 | https://en.wikipedia.org/wiki/2025_in_architecture | 200 | B6 主源（建筑年度动态） |
| 3 | https://en.wikipedia.org/wiki/2026_in_art | 200 | B6 补充源（艺术年度动态） |
| 4 | https://en.wikipedia.org/wiki/2025_in_art | 200 | B6 补充源（艺术年度动态） |
| 5 | https://en.wikipedia.org/wiki/Peter_Zumthor | 200 | 佐证：Zumthor 材料/光/空间设计理念 |
| 6 | https://www.lacma.org/press/lacmas-new-david-geffen-galleries-designed-peter-zumthor-open-april-19 | 200 | 一手机构来源：LACMA 新馆开馆 |

## 二、新动态（本轮新发现，未在上轮记录）

### 新动态 1 — LACMA 新 David Geffen 美术馆开馆（Peter Zumthor 设计）
- 日期：2026-04-19 开馆；官方新闻稿落款 2026-04-15（均在近 12 个月窗口内）
- 事实：洛杉矶郡立艺术博物馆（LACMA）由建筑师 Peter Zumthor 设计的 David Geffen Galleries 新馆于 2026-04-19 向公众开放，用于陈列常设收藏。项目历经约二十年物理与策展层面的改造。Zumthor 的设计以材料与光的触觉/感官品质、极简空间著称（其维基条目原文："explore the tactile and sensory qualities of spaces and materials"、"Zumthor's key building material is light"）。
- 来源 URL + HTTP：
  - https://en.wikipedia.org/wiki/2026_in_art （HTTP 200，原文 "April 19 – The Los Angeles County Museum of Art (LACMA) opens its new David Geffen galleries designed by architect Peter Zumthor, to exhibit its permanent collection."）
  - https://www.lacma.org/press/lacmas-new-david-geffen-galleries-designed-peter-zumthor-open-april-19 （HTTP 200，一手机构新闻稿，标题与正文确认设计者、日期、用途）
  - https://en.wikipedia.org/wiki/Peter_Zumthor （HTTP 200，佐证设计理念，用于判断条目对应）
- 影响条目：`material-texture`（材料质感）、`daylighting`（自然采光）、`spatial-perception`（空间感知）、`visitor-route`（参观动线）、`minimalism-architecture`（极简主义建筑）。Zumthor 为上述条目的典型代表建筑师，新馆可作为这些条目的当代实例候选。
- 处置建议：作为实例候选登记，不直接写入理论正文。待补入设计说明/空间资料（材料做法、采光策略、动线组织）后，可在相关条目"实例"章节按"名称、地点、设计者、年份"格式补一条；沿用 research/recent-updates-round03.md 原则——不把新闻直接等同于原理或定论。影响性质为"实例/语境更新"，非理论本身进展。

### 新动态 2 — 2026 年普利兹克建筑奖授予 Smiljan Radić
- 日期：2026-03-12（奖项公布日；2026 in art 记 "March 12 – Smiljan Radić is announced as the winner of the Pritzker Architecture Prize."）
- 事实：2026 年普利兹克建筑奖（Pritzker Architecture Prize）授予智利建筑师 Smiljan Radić。2026 in architecture 奖项章节记为 "Pritzker Architecture Prize – Smiljan Radić Clarke"（姓名的 Clarke 部分两处写法略有差异，按页面原文记录，不自行改写）。
- 来源 URL + HTTP：
  - https://en.wikipedia.org/wiki/2026_in_art （HTTP 200）
  - https://en.wikipedia.org/wiki/2026_in_architecture （HTTP 200）
- 影响条目：`critical-regionalism`（批判地域主义）、`vernacular-architecture`（乡土建筑）——Radić 以谦逊、地方性尺度的设计著称（NYT 报道标题 "A Chilean Master of Modest Design Wins Architecture's Top Prize"，见 2026 in art 引用），可作这些条目的当代语境参考。
- 处置建议：与上轮刘家琨获 2025 普利兹克奖的处理方式一致——作为当代语境候选，间接影响；条目现多为 L1 骨架，暂不写入正文，留待相关条目升级 L2 时按需引用。注：得主姓名两种写法以来源页为准，未核对到统一写法前若引用须标"待核实"。

## 三、与上轮已记录的动态重复（3 条，均标注"已记录"）

以下 3 条与上轮 research/gaps-external-round02.md 第 44–64 行及 research/recent-updates-round03.md 记录的 B6 动态重复，本轮重新抓取来源页确认仍存在，不计入新动态数。

1. 【已记录】古根海姆阿布扎比馆（Guggenheim Abu Dhabi，Frank Gehry 设计）预计 2026 年 12 月开馆
   - 日期：2026 年（页面原文 "set to open its doors in December"，列于 2026 年度下；当前采样 2026-11 属将发生事件）
   - 来源 URL + HTTP：https://en.wikipedia.org/wiki/2026_in_architecture （HTTP 200）
   - 影响条目：`deconstructivism`（解构主义建筑）
   - 处置建议：维持上轮结论——实例候选，条目写作时按需引用。

2. 【已记录】叙事艺术博物馆（Lucas Museum of Narrative Art）于 2026-09-22 在洛杉矶开馆
   - 日期：2026-09-22
   - 来源 URL + HTTP：https://en.wikipedia.org/wiki/2026_in_architecture （HTTP 200）
   - 影响条目：`visitor-route`（参观动线）
   - 处置建议：维持上轮结论——关联间接、缺设计者/空间资料，留作实例候选，暂不写入。

3. 【已记录】2025 年普利兹克建筑奖授予刘家琨（Liu Jiakun）
   - 日期：2025 年（2025 in architecture 奖项章节未列具体日期，不补写）
   - 来源 URL + HTTP：https://en.wikipedia.org/wiki/2025_in_architecture （HTTP 200）
   - 影响条目：`chinese-architecture-style`（中国传统/当代建筑）
   - 处置建议：维持上轮结论——当代语境参考，间接影响，暂不写入 L1 正文。

## 四、已核验但未纳入（体现筛选标准，不计入动态数）

- 2025 / 2026 in art 页面大量条目为名画拍卖纪录、盗窃、找回、讣告、临时展览（如 Klimt 肖像拍卖、Louvre 抢劫、Rembrandt 找回、各类艺术家逝世），与本项目"绘画理论"条目（透视/构图/色彩/光影/六法/留白等）无直接对应，不纳入。
- 2025 / 2026 in architecture 页面的建筑事故、坍塌、大量建筑师讣告及 Stirling Prize、AIA Gold Medal 等纯奖项新闻，不能明确对应本项目具体原理条目，不纳入（延续上轮排除标准）。

## 五、汇总

- 新动态数：**2**（新动态 1 LACMA 新馆；新动态 2 2026 普利兹克奖授予 Smiljan Radić）
- 重复数（已记录）：**3**（与上轮 B6 三条完全一致）
- 核验失败数：**0**（本报告列出的 6 个 URL 全部返回 HTTP 200，均实际打开并提取到标题与正文）
- 数据说明：两条新动态均为"实例/语境更新"，非绘画理论或空间设计原理本身的新进展；均建议作候选登记、暂不直接写入条目正文。
