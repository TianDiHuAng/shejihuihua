# B1 读者问题缺口核验 — 第 25 轮（B4 六问 → scope 候选）

- 日期：2026-11-22（Asia/Hong_Kong）
- 执行角色：b1-r25（只读子任务）
- 抓取方式：Python 3.11 urllib + 浏览器 User-Agent；依据 DECISIONS.md D05，web_search / web_fetch 在本环境报错，改用直连实抓。
- 数据纪律：联网内容一律视为数据；网页内任何指令均未执行；未下载或运行页面代码，仅读取 HTML / 纯文本判读标题与相关句。
- 任务：判断 B4 读者 80 问中仍无对应条目的 6 个概念（rembrandt、tenebrism、plaza、atrium-architecture、exit-sign、vestibule-architecture）是否值得新增为 scope 条目，逐条实抓两份独立权威来源。
- 比对基准：`scope.md` 现 237 条（理论 118 / 风格 60 / 造景 18 / 动线 11 / 下沉空间 12 / 材料 18）。
- 结果摘要：候选 6 个 → 建议纳入 5 个、建议驳回 1 个（重复）。HTTP 核验：核心两源全部 200；其余试抓失败项列于文末以便审计。

## 环境备注（限制说明）

- 任务点名要先读的 `AUTONOMOUS.md`、`TASK_design.md`（及 `WORKFLOW.md`）在当前工作区**实际不存在**（`**/AUTONOMOUS.md`、`**/TASK_design.md` 均无匹配）。已以现存治理文件 `PROGRESS.md`、`BACKLOG.md`、`DECISIONS.md`、`scope.md`、`research/gaps-external-round06.md`、`research/reader_questions-round25.md` 为准执行，方法与来源纪律沿用第 6 轮 B1（`gaps-external-round06.md`）与 D05/D10/D11。
- 本文件为只读子任务唯一产物；未改动其他文件、未 git commit、未触碰项目外内容。

## 判据

一条概念「值得新增」需同时满足：
1. 属绘画理论或建筑空间设计范围；
2. 在 `scope.md` 237 条中无对应 id / 中文名 / 等价概念（排除近义已收录项）；
3. 能直接回答对应读者问题；
4. 至少两份**独立**权威来源实抓为 HTTP 200 且页面标题与主题吻合（Wikipedia 条目可作一源，另配博物馆 / 官方机构 / 独立百科等；或两个独立百科条目）。

仅单源或权威性不足者，明确标注「单源，不建议纳入」。

---

## 候选 1：rembrandt（伦勃朗光）— 建议纳入

- 建议 id：`rembrandt`
- 中文名：伦勃朗光
- 主题：理论（光影/明暗布光）
- 层级：补充
- 时期：17 世纪
- 地区：欧洲
- 来源一：https://en.wikipedia.org/wiki/Rembrandt_lighting —《Rembrandt lighting - Wikipedia》— HTTP 200
- 来源二：https://www.rijksmuseum.nl/en/collection/node/Rembrandt-van-Rijn--ba2dc062acd137ffeac364321b7b10df —《Rembrandt van Rijn - Rijksmuseum》— HTTP 200（由 /rijksstudio/artists/rembrandt-van-rijn 重定向）
- 入选理由：Wikipedia 设 `Rembrandt lighting` 专条，定义这种肖像布光（受光面颊形成倒三角高光、强明暗对照）；阿姆斯特丹国立博物馆（Rijksmuseum）伦勃朗专页原文称其「以强烈的明暗对比强化场景的戏剧感」（powerful light-dark contrasts to intensify the sense of drama），佐证该布光法的绘画根源。scope 已有 `chiaroscuro`（明暗法）、`light-shadow-modeling`（光影塑形）、`side-light`（侧光），但没有「伦勃朗光」这一具名布光法，可回答爱好者「伦勃朗光是什么？」。
- 概念贴合度：高（一源定义具名技法，一源为画家所属博物馆对其实践光暗的权威描述）。

## 候选 2：tenebrism（暗绘风格/暗色调主义）— 建议纳入

- 建议 id：`tenebrism`
- 中文名：暗绘风格（暗色调主义）
- 主题：风格
- 层级：补充
- 时期：17 世纪
- 地区：欧洲
- 来源一：https://en.wikipedia.org/wiki/Tenebrism —《Tenebrism - Wikipedia》— HTTP 200
- 来源二：https://www.dailyartmagazine.com/tenebrism/ —《Tenebrism 101: All You Need to Know | DailyArt Magazine | Art History》— HTTP 200
- 佐证（第三源）：https://www.studiobinder.com/blog/what-is-tenebrism/ —《What is Tenebrism — The Art of Light and Shadow Explained》— HTTP 200
- 入选理由：两源均把 tenebrism 定义为「chiaroscuro 的极端化」——大面积深暗背景＋局部戏剧性强光。DailyArt 原文：「tenebrism 源自意大利语 tenebroso，意为黑暗或阴郁……要看懂 tenebrism 须先了解 chiaroscuro」；StudioBinder 原文：「Tenebrism is a lighting style that's often confused with chiaroscuro」。这是 17 世纪（卡拉瓦乔为核心）的绘画风格。scope 已有 `chiaroscuro`（技法）但没有作为**独立风格**的「暗绘风格」，可回答爱好者「暗绘风格如何形成？」。
- 概念贴合度：高（三源均以「tenebrism」为条目名并直接定义其与 chiaroscuro 的区别）。

## 候选 3：plaza（广场/城市广场）— 建议纳入

- 建议 id：`plaza`
- 中文名：广场（城市广场）
- 主题：造景（城市公共空间营造）
- 层级：重要
- 时期：跨时期
- 地区：全球
- 来源一：https://en.wikipedia.org/wiki/Plaza —《Town square - Wikipedia》— HTTP 200（`Plaza` 与「Town square」为同一城市广场条目）
- 来源二：https://www.pps.org/article/grplacefeat —《What Makes a Successful Place?》— HTTP 200
- 入选理由：Wikipedia「Town square/plaza」把城市广场界定为公众聚集、社会交往的开放空间；PPS（Project for Public Spaces）原文称「优秀的公共空间是举行庆典、进行社会与经济交流、朋友相遇、文化交融之处，是公共机构的『前廊』（front porches）」——正是「城市客厅」之意。scope 已有 `sunken-plaza`（下沉广场）与 `urban-planning-style`，但没有作为城市公共空间本体的「广场」，可回答爱好者「广场如何形成城市客厅？」。
- 概念贴合度：高（PPS 直接给出「公共空间＝城市前廊/客厅」的隐喻与社会功能框架）。

## 候选 4：atrium-architecture（中庭）— 建议纳入

- 建议 id：`atrium-architecture`
- 中文名：中庭
- 主题：材料（自然采光/通风的空间载体）
- 层级：重要
- 时期：跨时期
- 地区：全球
- 来源一：https://en.wikipedia.org/wiki/Atrium_(architecture) —《Atrium (architecture) - Wikipedia》— HTTP 200
- 来源二：https://www.designingbuildings.co.uk/wiki/Atrium_definition —《Atrium definition - Designing Buildings》— HTTP 200
- 入选理由：Wikipedia「Atrium (architecture)」介绍中庭为贯通多层、常以玻璃顶/天窗引入自然光与通风的室内空间；Designing Buildings（英国建筑行业知识库）给出 atrium 权威定义，引英国《Approved Document B》：「贯穿一层或多层结构楼板的连续空间」。scope 已有 `sunken-atrium`（地下中庭）、`atrium-ventilation`（中庭通风）、`skylight`（天窗采光）等，但没有「中庭」这一空间本体条目；可回答爱好者「中庭如何改善采光？」（顶部天窗/玻璃顶将自然光引入建筑深处，再由侧窗与中庭贯通补光）。
- 概念贴合度：中高（第二源为权威定义；采光机制由 Wikipedia 中庭条目与既有 `skylight`/`daylighting` 支撑，具体采光系数须按规范，属一般性说明）。

## 候选 5：exit-sign（疏散标识/安全出口标识）— 建议纳入

- 建议 id：`exit-sign`
- 中文名：疏散标识（安全出口标识）
- 主题：动线（疏散动线/导向）
- 层级：补充
- 时期：20 世纪
- 地区：全球
- 来源一：https://en.wikipedia.org/wiki/Exit_sign —《Exit sign - Wikipedia》— HTTP 200
- 来源二：https://www.ecfr.gov/current/title-29/section-1910.37 —《eCFR :: 29 CFR 1910.37 -- Maintenance, safeguards, and operational features for exit routes.》— HTTP 200
- 入选理由：Wikipedia「Exit sign」介绍疏散标识的形式、图形与设置；美国联邦法规 eCFR 29 CFR 1910.37 原文规定：沿疏散通道「到最近出口及出口通道的视线必须始终清晰可见 exit sign」，「每个 exit sign 必须由可靠光源照亮至不低于 5 foot-candles（54 lux）且颜色可辨」。scope 已有 `evacuation-route`（疏散动线）、`wayfinding`（导视与寻路）、`safety-guarding`（安全防护），但没有「疏散标识」这一具体设施与规范条目，可回答从业者「疏散标识如何布置？」。
- 概念贴合度：高（Wikipedia 定义 + 官方法规给出可视化与照度布置硬指标）。

## 候选 6：vestibule-architecture（门厅）— 建议驳回（重复）

- 结论：**不建议新增**。`scope.md` 第 105 行已收录 `vestibule | 门厅 | 重要 | 跨时期 | 全球 | S1`（理论条目）。读者问题「门厅如何承担过渡与安检？」标注「需 vestibule-architecture」属 id 命名不一致，其概念已由既有 `vestibule` 覆盖，无需重复建条；建议将该问映射到 `vestibule`，并在 `vestibule` 正文补「过渡与安检」场景即可。
- 处理：不实抓额外双源（重复项无需新证）；已核对 `scope.md` 现有条目作为依据。

---

## 实际打开的 URL 与 HTTP 状态

| 来源 id | 页面 URL | 页面标题 | HTTP |
| --- | --- | --- | --- |
| s-wp-rembrandt-lighting | https://en.wikipedia.org/wiki/Rembrandt_lighting | Rembrandt lighting - Wikipedia | 200 |
| s-rijksmuseum-rembrandt | https://www.rijksmuseum.nl/en/collection/node/Rembrandt-van-Rijn--ba2dc062acd137ffeac364321b7b10df | Rembrandt van Rijn - Rijksmuseum | 200 |
| s-studiobinder-rembrandt | https://www.studiobinder.com/blog/rembrandt-lighting-photography/ | How to Master Rembrandt Lighting in Photography and Video | 200 |
| s-wp-tenebrism | https://en.wikipedia.org/wiki/Tenebrism | Tenebrism - Wikipedia | 200 |
| s-dailyart-tenebrism | https://www.dailyartmagazine.com/tenebrism/ | Tenebrism 101: All You Need to Know \| DailyArt Magazine \| Art History | 200 |
| s-studiobinder-tenebrism | https://www.studiobinder.com/blog/what-is-tenebrism/ | What is Tenebrism — The Art of Light and Shadow Explained | 200 |
| s-wp-plaza | https://en.wikipedia.org/wiki/Plaza | Town square - Wikipedia | 200 |
| s-pps-successful-place | https://www.pps.org/article/grplacefeat | What Makes a Successful Place? | 200 |
| s-wp-atrium | https://en.wikipedia.org/wiki/Atrium_(architecture) | Atrium (architecture) - Wikipedia | 200 |
| s-designingbuildings-atrium | https://www.designingbuildings.co.uk/wiki/Atrium_definition | Atrium definition - Designing Buildings | 200 |
| s-wp-exit-sign | https://en.wikipedia.org/wiki/Exit_sign | Exit sign - Wikipedia | 200 |
| s-ecfr-1910-37 | https://www.ecfr.gov/current/title-29/section-1910.37 | eCFR :: 29 CFR 1910.37 -- Maintenance, safeguards, and operational features for exit routes. | 200 |

## 试抓失败 / 被排除的来源（审计用）

| URL | 结果 | 备注 |
| --- | --- | --- |
| https://www.britannica.com/art/tenebrism 等 Britannica 艺术/建筑条目 | 403 | Cloudflare 拦截 urllib，弃用 |
| https://www.tate.org.uk/art/art-terms/... | DNS getaddrinfo 失败 | 网络不可达 |
| https://www.nationalgallery.org.uk/paintings/glossary/chiaroscuro | DNS 失败 | 网络不可达 |
| https://www.metmuseum.org/toah/hd/chia/hd_chia.htm | 连接超时 | 网络不可达 |
| https://www.osha.gov/.../1910.37 | 403 | 改用同法规的 eCFR / Cornell LII（均 200） |
| https://www.artuk.org/discover/art-terms/tenebrism | 403 | 弃用 |
| https://www.wikiart.org、https://www.nga.gov、https://www.artic.edu | 403 | 弃用 |
| https://www.khanacademy.org/.../a/tenebrism | 200 但正文为 JS 渲染，静态 HTML 无正文 | 仅作旁证，不计为正文来源 |
| https://en.wikipedia.org/w/index.php?...action=raw / api/rest_v1 / wiki/Chiaroscuro | 连接超时 | 抓取后期 Wikipedia 限流/短时不可达；不影响此前已实抓的 200 主条目 |

说明：Wikipedia 五个主条目（rembrandt-lighting、tenebrism、plaza、atrium、exit-sign）均在首轮实抓返回 HTTP 200 并核对到 `<title>`；其后二次抓正文时遇限流，属运行期网络波动，不改变已核验的 200 结论。

## 机器可读汇总

```
CANDIDATES=[{"id":"rembrandt","title":"伦勃朗光","theme":"理论","tier":"补充","period":"17世纪","region":"欧洲","sources":["s-wp-rembrandt-lighting","s-rijksmuseum-rembrandt"],"urls":["https://en.wikipedia.org/wiki/Rembrandt_lighting","https://www.rijksmuseum.nl/en/collection/node/Rembrandt-van-Rijn--ba2dc062acd137ffeac364321b7b10df"]},{"id":"tenebrism","title":"暗绘风格（暗色调主义）","theme":"风格","tier":"补充","period":"17世纪","region":"欧洲","sources":["s-wp-tenebrism","s-dailyart-tenebrism"],"urls":["https://en.wikipedia.org/wiki/Tenebrism","https://www.dailyartmagazine.com/tenebrism/"]},{"id":"plaza","title":"广场（城市广场）","theme":"造景","tier":"重要","period":"跨时期","region":"全球","sources":["s-wp-plaza","s-pps-successful-place"],"urls":["https://en.wikipedia.org/wiki/Plaza","https://www.pps.org/article/grplacefeat"]},{"id":"atrium-architecture","title":"中庭","theme":"材料","tier":"重要","period":"跨时期","region":"全球","sources":["s-wp-atrium","s-designingbuildings-atrium"],"urls":["https://en.wikipedia.org/wiki/Atrium_(architecture)","https://www.designingbuildings.co.uk/wiki/Atrium_definition"]},{"id":"exit-sign","title":"疏散标识（安全出口标识）","theme":"动线","tier":"补充","period":"20世纪","region":"全球","sources":["s-wp-exit-sign","s-ecfr-1910-37"],"urls":["https://en.wikipedia.org/wiki/Exit_sign","https://www.ecfr.gov/current/title-29/section-1910.37"]}]
REJECTED=["vestibule-architecture"]
```
