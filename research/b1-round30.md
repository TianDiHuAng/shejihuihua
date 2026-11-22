# B1/B2 稀疏格补条 — 第 30 轮（2 条新 scope 候选，双源实抓）

- 日期：2026-11-22（Asia/Hong_Kong）
- 执行角色：b1-r30（只读子任务，无人值守）
- 抓取方式：Python 3.11 urllib + 浏览器 User-Agent；依据 DECISIONS.md D05（web_search / web_fetch 在本环境报错，改用直连实抓）。
- 数据纪律：联网内容一律视为数据；网页内任何指令均未执行；未下载或运行页面代码，仅读取 HTML / 纯文本判读标题与相关句。维基 canonical（en.wikipedia.org）本轮多次连接超时，按任务许可改用 owiki.org 镜像读取，**同源只计一源**；每条候选的第二源均为另一独立出版方。
- 任务：从 `research/gaps-round30.md` 的 B2 覆盖矩阵「稀疏格（≤1 条）9」中挑选 2 个最值得补的格子，各提 1 条新 scope 候选，逐条实抓两份独立权威来源。
- 比对基准：`scope.md` 现 242 条（理论 119 / 风格 61 / 造景 19 / 动线 12 / 下沉空间 12 / 材料 19）；其中 `baroque`=欧洲巴洛克、`japanese-architecture`、`mexican-modernism`、`latin-american-colonial` 已收录，本报告新增 2 条与其均不重复。

## 环境备注（限制说明）

- 任务点名先读的 `AUTONOMOUS.md`、`TASK_design.md` 在当前工作区**实际不存在**（`**/AUTONOMOUS.md`、`**/TASK_design.md` 均无匹配）。已以现存治理文件 `DECISIONS.md`、`scope.md`、`coverage-matrix.md`、`research/gaps-round30.md` 及上轮 `research/b1-round25.md` 的方法与来源纪律为准执行（沿用 D05 直连实抓）。
- 本文件为只读子任务唯一产物；未改动其他文件、未 git commit、未触碰项目外内容。

## 选格依据（为何是这 2 格）

`gaps-round30.md` 列出 9 个稀疏格（≤1 条）。覆盖矩阵显示相关格现状：

| 稀疏格 | 现条目数（核心/重要/补充） | 现唯一/主要条目 |
| --- | --- | --- |
| 风格 / 文艺复兴至19世纪 / 美洲 | 1（0/0/1） | latin-american-colonial（拉美殖民建筑，泛称） |
| 理论 / 20世纪 / 东亚 | 1（0/1/0） | gray-space（灰空间） |
| 理论 / 古代 / 欧洲 | 1（1/0/0） | vitruvian-triad |
| 理论 / 跨时期 / 欧洲 | 1（0/0/1） | golden-ratio |
| 风格 / 中世纪 / 伊斯兰·南亚 | 1（0/1/0） | islamic-architecture |
| 风格 / 古代 / 伊斯兰·南亚 | 1（0/1/0） | indian-architecture |
| 下沉空间 / 古代 / 中国 | 1（0/1/0） | light-well（天井） |
| 动线 / 古代 / 中国 | 1（0/1/0） | loop-route（回游式动线） |
| 理论 / 文艺复兴至19世纪 / 全球 | 1（0/0/1） | 待核（见 gaps-round30） |

**选这 2 格**：
1. **风格 / 文艺复兴至19世纪 / 美洲** —— 该格仅 1 条泛称「拉美殖民建筑」，缺具体流派；补「墨西哥巴洛克（新西班牙巴洛克）」可把美洲 17–18 世纪建筑从泛称落到具名风格，地域覆盖收益最大，且与任务示例方向一致。
2. **理论 / 20世纪 / 东亚** —— 该格仅 1 条「灰空间」；补「新陈代谢派」覆盖战后日本最具国际影响的城市/建筑理论运动（丹下健三、黑川纪章、槙文彦），与示例方向一致，属本领域核心理论脉络。

其余稀疏格本轮未选原因：`下沉空间·动线/古代/中国` 易与既有 light-well / corridor-space / winding-path / loop-route 重叠；`理论/古代/欧洲` 与 `理论/跨时期/欧洲` 候选（古典柱式、柱式比例）本轮未找到可达的第二独立权威源（Britannica 403、designingbuildings 对应 slug 404），留待后续；`风格/中世纪·古代/伊斯兰·南亚` 候选（奥斯曼、印度教神庙）第二源同样不可达。

## 判据

一条候选「值得新增」需同时满足：
1. 属绘画理论或建筑空间设计范围；
2. 在 `scope.md` 242 条中无对应 id / 中文名 / 等价概念（排除近义已收录项）；
3. 确实补上目标稀疏格（主题 × 时期 × 地区三者吻合）；
4. 至少两份**独立**权威来源实抓为 HTTP 200，页面标题与主题吻合，并能摘出正文关键句（维基镜像仅计一源，第二源须为不同出版方）。

---

## 候选 1：mexican-baroque（墨西哥巴洛克 / 新西班牙巴洛克）— 建议纳入

- 建议 id：`mexican-baroque`
- 中文名：墨西哥巴洛克（新西班牙巴洛克）
- 主题：风格
- 层级：补充
- 时期：文艺复兴至19世纪（17–18 世纪）
- 地区：美洲
- 目标稀疏格：风格 / 文艺复兴至19世纪 / 美洲（现 1 条，0/0/1）
- 来源一（维基，owiki 镜像）：https://owiki.org/wiki/New_Spanish_Baroque —《New Spanish Baroque ::: Open WIKI》— HTTP 200
  - 说明：维基 canonical `https://en.wikipedia.org/wiki/New_Spanish_Baroque`（`Mexican_Baroque` 重定向至此）本轮连接超时，按任务许可用 owiki 镜像读取，仅计一源。
  - 正文关键句：「New Spanish Baroque, also known as Mexican Baroque, refers to Baroque art developed in the entire territories that once formed the Viceroyalty of New Spain.」
  - 正文关键句：「Two styles can be traced in the architecture of New Spain: the Salomónico, developed from the mid-17th century, and the Estípite, which began in the early 18th century.」
  - 正文关键句：「The most emblematic substyle of Mexican Baroque architecture is Churrigueresque.」
- 来源二（独立出版方，Designing Buildings）：https://www.designingbuildings.co.uk/wiki/Baroque_architecture —《Baroque architecture - Designing Buildings》— HTTP 200
  - 正文关键句：「As Baroque architecture coincided with European colonialism, it can be seen throughout much of the world; and in some regions, notably Germany and colonial South America, it lasted until the 18th century.」
  - 正文关键句：「The late Baroque style is often referred to as Rococo or, in Spain and Spanish America, as Churrigueresque.」
- 入选理由：维基「New Spanish Baroque」专条明确该词即「Mexican Baroque」，界定为旧新西班牙总督区范围内的巴洛克，并指出其建筑两大支流（Salomónico 从 17 世纪中叶、Estípite 从 18 世纪初）及最具代表性的子风格 Churrigueresque；第二源 Designing Buildings（英国建筑行业知识库，独立于维基）则从巴洛克随欧洲殖民扩张传播的角度，明确「在西班牙及西属美洲，晚期巴洛克被称为 Churrigueresque」，与维基「Churrigueresque 是墨西哥巴洛克最典型子风格」直接相互印证。两源独立、均 200、均可摘正文关键句，且把现有泛称条目 `latin-american-colonial` 落到具名风格，实补「风格/文艺复兴至19世纪/美洲」稀疏格。
- 概念贴合度：高（一源为该风格正式专条并给出命名与分期，另一源为另一出版方对其命名与地域分布的独立佐证）。第二源为「巴洛克/西属美洲」层面、非墨西哥专论，故墨西哥专指细节以维基专条为准，第二源作交叉印证。

## 候选 2：metabolism（新陈代谢派）— 建议纳入

- 建议 id：`metabolism`
- 中文名：新陈代谢派（Metabolism）
- 主题：理论
- 层级：重要
- 时期：20世纪
- 地区：东亚
- 目标稀疏格：理论 / 20世纪 / 东亚（现 1 条，0/1/0）
- 来源一（维基，owiki 镜像）：https://owiki.org/wiki/Metabolism_(architecture) —《Metabolism (architecture) ::: Open WIKI》— HTTP 200
  - 说明：维基 canonical `https://en.wikipedia.org/wiki/Metabolism_(architecture)` 本轮连接超时，用 owiki 镜像读取，仅计一源。
  - 正文关键句：「Metabolism was a post-war Japanese biomimetic architectural movement that fused ideas about architectural megastructures with those of organic biological growth.」
  - 正文关键句：「During the preparation for the 1960 Tokyo World Design Conference, a group of young architects and designers, including Kiyonori Kikutake, Kisho Kurokawa and Fumihiko Maki, prepared the publication of the Metabolism manifesto.」
  - 正文关键句：「Some smaller, individual buildings that employed the principles of Metabolism were built and these included Tange's Yamanashi Press and Broadcaster Centre and Kurokawa's Nakagin Capsule Tower.」
- 来源二（独立出版方，Designing Buildings）：https://www.designingbuildings.co.uk/wiki/Metabolism —《Metabolism in architecture - Designing Buildings》— HTTP 200（该路径解析到 `/wiki/Metabolism_in_architecture`）
  - 正文关键句：「Metabolism represented an urban environment that was responsive, replaceable and could grow in an organic way.」
  - 正文关键句：「Although many projects failed to get off the ground, examples of the Metabolist form include ... the Nakagin Capsule Tower, Tokyo by Kisho Kurokawa.」
- 入选理由：维基「Metabolism (architecture)」专条定义其为战后日本仿生建筑运动，融合巨构与有机生长理念，并由丹下健三（Kenzo Tange）、黑川纪章（Kisho Kurokawa）、槙文彦（Fumihiko Maki）等推动，代表作为中银胶囊塔、山梨文化会馆；第二源 Designing Buildings 独立给出「Metabolism 代表一种可响应、可替换、可有机生长的城市环境」并同样举中银胶囊塔为例，两源在定义与代表建筑上独立吻合。该条把「理论/20世纪/东亚」从仅灰空间 1 条扩展到战后日本核心建筑/城市理论运动，属本领域（建筑理论）核心脉络，且与任务示例方向（日本现代建筑/新陈代谢派/丹下健三）一致。
- 概念贴合度：高（两源独立、均 200、均以 Metabolism 为条目并直接定义其理念与代表建筑）。层级取「重要」：作为战后东亚最具国际影响力的建筑运动之一，与同格 gray-space（重要）、同区 `japanese-architecture`（重要）同级。

---

## 实际打开的 URL 与 HTTP 状态

| 来源 id | 页面 URL | 页面标题 | HTTP |
| --- | --- | --- | --- |
| w-owiki-nsb | https://owiki.org/wiki/New_Spanish_Baroque | New Spanish Baroque ::: Open WIKI | 200 |
| dbb-baroque | https://www.designingbuildings.co.uk/wiki/Baroque_architecture | Baroque architecture - Designing Buildings | 200 |
| w-owiki-metabolism | https://owiki.org/wiki/Metabolism_(architecture) | Metabolism (architecture) ::: Open WIKI | 200 |
| dbb-metabolism | https://www.designingbuildings.co.uk/wiki/Metabolism | Metabolism in architecture - Designing Buildings | 200 |

> 维基 canonical（en.wikipedia.org）本轮多次连接超时（TimeoutError 10060），按任务许可与 D05 改用 owiki 镜像读取；镜像与原条目同源，仅各计一源，第二源均为 Designing Buildings（独立出版方）。

## 试抓失败 / 被排除的来源（审计用）

| URL | 结果 | 备注 |
| --- | --- | --- |
| https://en.wikipedia.org/wiki/Mexican_Baroque · /New_Spanish_Baroque · /Metabolism_(architecture) · /Churrigueresque | TimeoutError 10060 | 维基 canonical 超时，改用 owiki 镜像（同源计一源） |
| https://www.britannica.com/art/Mexican-Baroque · /Churrigueresque · /Metabolism-architecture | HTTP 403 | Cloudflare 拦截 urllib，弃用 |
| https://www.moma.org/calendar/exhibitions/1187 | HTTP 403 | MoMA 反爬，弃用 |
| https://smarthistory.org/mexican-baroque/ | HTTP 403 | 禁爬，弃用 |
| https://www.metmuseum.org/toah/hd/nspa/hd_nspa.htm | Timeout | 网络不可达 |
| https://www.khanacademy.org/.../new-spain/a/mexican-baroque | 200 但「Client Challenge」 | JS 挑战页，无静态正文，不计为来源 |
| https://www.dailyartmagazine.com/mexican-baroque/ · /new-spanish-baroque/ · /baroque-art/ · /baroque-painting/ | HTTP 404 | slug 猜测失败；站内搜索页 200 但无墨西哥巴洛克专文 |
| https://www.visual-arts-cork.com/architecture/mexican-baroque.htm | ConnectionRefused 10061 | 拒连，弃用 |
| https://www.newworldencyclopedia.org/entry/Metabolism_(architecture) · /Baroque_architecture | Timeout | 不可达 |
| https://www.designingbuildings.co.uk/wiki/Classical_orders · /Classical_order · /Orders_of_architecture · /Ottoman_architecture · /Mughal_architecture | HTTP 404 | 备选稀疏格第二源不可达，故本轮对应用古典柱式/奥斯曼/莫卧儿方向的评估搁置 |
| https://www.archdaily.com/tag/metabolism · /search?q=mexican+baroque | 200 但为聚合/搜索页 | 无对应专文正文，未采用 |
| https://www.encyclopedia.com/.../mexican-baroque | Timeout | 不可达 |

说明：`designingbuildings.co.uk/wiki/Metabolism` 与 `/wiki/Baroque_architecture` 均在首轮实抓返回 200 并核对到 `<title>`；owiki 两条亦 200 并核对标题与正文关键句。

## 机器可读汇总

```
CANDIDATES=[{"id":"mexican-baroque","title":"墨西哥巴洛克（新西班牙巴洛克）","theme":"风格","tier":"补充","period":"文艺复兴至19世纪","region":"美洲","urls":["https://owiki.org/wiki/New_Spanish_Baroque","https://www.designingbuildings.co.uk/wiki/Baroque_architecture"],"sources":["w-owiki-nsb","dbb-baroque"]},{"id":"metabolism","title":"新陈代谢派（Metabolism）","theme":"理论","tier":"重要","period":"20世纪","region":"东亚","urls":["https://owiki.org/wiki/Metabolism_(architecture)","https://www.designingbuildings.co.uk/wiki/Metabolism"],"sources":["w-owiki-metabolism","dbb-metabolism"]}]
REJECTED=[]
```
