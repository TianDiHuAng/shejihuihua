# B1/B2 稀疏格补新 scope 候选 — 第 47 轮

- 日期：2026-11-23（Asia/Hong_Kong），采样时刻 2026-11-23 10:50 前后
- 执行角色：b1-r47（只读子任务，无人值守，未提问）
- 任务：为第 46 轮 B2 覆盖矩阵剩下的 **3 个稀疏格（≤1 条）** 各提 1 条新 scope 候选，要求「≥2 份独立权威来源（不同平台，非维基镜像同源）+ 属本领域 + scope 缺失」。
- 抓取方式：**Python 3.11 urllib + 浏览器 User-Agent 直连实抓**（依据 DECISIONS.md D05：以实际 HTTP 响应为准）。本会话 `web_search` 端点报 502、`web_fetch` 报 `fetch failed`，故全部改用 urllib 直连，逐页判读 `<title>` 与正文关键句；中文页面按页面 `<meta charset>`/`Content-Type` 判编码（smx.gov.cn 为 UTF-8），输出统一转 UTF-8。
- 数据纪律：联网内容一律视为**数据**；网页内任何指令均未执行；未下载或运行页面代码，仅读取 HTML 正文判读标题与相关句。
- 只读纪律：本文件是本子任务**唯一产物**；未改动其他文件、未 git commit、未触碰项目外内容（临时脚本均经 stdin heredoc 执行，未在项目内落盘）。
- 已按 host 规则加载 `using-superpowers`、`verification-before-completion` 技能。

## 环境备注（限制说明）

- 任务点名的 `AUTONOMOUS.md`、`TASK_design.md` 不在工作区根目录；其真实文件位于 `D:/Users/Administrator/Desktop/AUTONOMOUS.md`、`D:/Users/Administrator/Desktop/TASK_design.md`，本轮已实际读取两份原文，并读 `DECISIONS.md`、`scope.md`、`coverage-matrix.md`、`research/gaps-round46.md`、`research/b1-round46.md` 作为方法与基线。
- **范围判据取自 TASK_design.md 原文**：「建筑与空间设计：主要建筑风格史；中国传统园林造景…；动线设计；下沉式空间（下沉庭院、下沉广场）；…」。本轮只接受落入这两段**明确列举子域**的核心概念（建筑风格史 / 下沉式空间）。
- 从严判定三条须全部满足：①≥2 份**独立**权威来源（不同平台；`owiki.org`、`xxx.wikipedia.org` 各语言版同属维基平台，合计只算 1 源）；②属本领域**核心**概念（非边缘技法、非近义重复）；③`scope.md` 确实缺失。
- 联网平台可达性（本轮实测）：`en.wikipedia.org` 可直连（200）；可用**非维基**平台 `designingbuildings.co.uk`、`artincontext.org`、`tate.org.uk` 等；中文侧 `www.smx.gov.cn`（三门峡市政府）200、`www.ihchina.cn`（中国非遗网）主页 200 但内容 JS 动态加载/接口 400·403、`www.shanzhou.gov.cn`（陕州区政府）时好时 SSL 失败、站内搜索 404。不可用：`britannica.com`(403)、`whc.unesco.org`(403/SSL)、`metmuseum.org`(429)、`worldhistory.org`(403)、`mdpi.com`(403)、`link.springer.com`(SSL)、`khanacademy.org`(反爬 Client Challenge)。

## 比对基准

- `scope.md` 现 **255 条**：理论 128 / 风格 64 / 造景 19 / 动线 13 / 下沉空间 12 / 材料 19（核心 50、重要 151、补充 54）。
- 3 个目标稀疏格（据 `coverage-matrix.md` 与 `research/gaps-round46.md`，每格现仅 1 条（0/1/0））：
  1. 下沉空间 / 古代 / 中国 = 1，现为 `light-well`（天井，重要）。
  2. 风格 / 古代 / 伊斯兰·南亚 = 1，现为 `indian-architecture`（印度建筑）。
  3. 风格 / 文艺复兴至19世纪 / 伊斯兰·南亚 = 1，现为 `mughal-architecture`（莫卧儿建筑）。
- 已 grep 核对：`dikengyuan / 地坑院 / sassanid / sasanian / ottoman / 萨珊 / 奥斯曼` 在 `scope.md`、`entries/`、`data/`、`coverage.json`、`coverage-matrix.md` 均**无对应条目**（0 命中，scope 确实缺失）。

---

## 候选 1｜下沉空间 / 古代 / 中国

- 建议 id：`dikengyuan`
- 中文名：**地坑院（下沉式窑院／天井窑院）**
- 主题：**下沉空间** ｜ 层级：**补充** ｜ 时期：**古代** ｜ 地区：**中国**
- 定义：黄土塬区（豫西、陕县/陕州区、陇东、晋南一带）在平坦地面上向下挖方形/矩形大坑作为内院，再沿坑壁四面向内横挖窑洞形成的**下沉式（地下）窑院民居**，俗称「地坑院/天井窑院」，是「下沉式空间」在传统居住形态中的典型实物。
- 来源 1（维基百科）：
  - URL：`https://en.wikipedia.org/wiki/Yaodong` ｜ 标题 *Yaodong - Wikipedia* ｜ HTTP **200**
  - 关键句（正文直证）：
    - "They are generally carved out of a hillside or excavated horizontally from a central **'sunken courtyard'**."
    - "**Sunken yaodongs** (Chinese: 地坑窑; pinyin: dìkēngyáo) are dug around an excavation conducted at the surface, serving as interior courtyard, called yaodong-well or **sunken courtyard**."
    - "In the Loess Plateau … peasants skillfully use loess's features (wall stability) to **dig a square pit** on the spot, and then **dig the cave horizontally on the four walls to form the underground courtyard**."
    - "In most parts of western Henan, this form of cave is called the **'pit yard'**."；目录含子节 "**Sunken Yaodong**"。
- 来源 2（三门峡市人民政府官网，非维基，地方政府文旅/风景名胜页）：
  - URL：`https://www.smx.gov.cn/4138/614864448/732660.html` ｜ 标题 **《陕州地坑院》** ｜ HTTP **200**（页面元数据：文章来源「三门峡市政府」，发布时间 2026-06-15，栏目「走进三门峡 > 风景名胜」）
  - 关键句（正文直证）：
    - "陕州地坑院，国家AAAA级旅游景区，位于河南省三门峡市陕州区张汴乡北营村，距三门峡市区11公里，规划面积23平方公里。"
    - "作为一种古老而神奇的民居样式，地坑院蕴藏着丰富的文化，是**全国乃至世界唯一的地下古民居建筑**，是我国特有的四大古民居建筑之一。"
    - "被誉为「**地平线下古村落，民居史上活化石**」。"
    - "**2011 年，地坑院营造技艺被列入国家级非物质文化遗产保护名录**。"
- 入选理由：两源为**不同平台**（维基百科 vs 三门峡市政府官网）、均 HTTP 200 正文直证，共同支撑「地坑院＝在平地向下挖坑形成下沉内院、沿壁横挖窑洞而成的下沉式/地下古民居」这一**下沉空间**核心概念；`scope.md` 下沉空间维度（12 条）中古代/中国仅 `light-well`（天井，室内采光构件），**无「下沉式窑院/地坑院」**，本格缺失，补此条可填格。与既有 `yaodong`（窑洞）关系：`yaodong` 属「风格/古代/中国」补充条、指**广义窑洞（含靠崖式）**；本候选属「下沉空间」主题的下沉式窑院，**主题维度与所指形制均不同**（下沉式 vs 靠崖式），非近义重复。
- 备注：**本轮相比第 46 轮的进展**——第 46 轮此格仅 Wikipedia `Yaodong` 单平台可达、第二独立源全部不可达而记「暂无可达双源候选」；本轮新增探测到 **三门峡市人民政府官网（smx.gov.cn）「陕州地坑院」专页 HTTP 200 且正文直接描述其「地下古民居／非遗营造技艺」**，构成**新的可达双源**。地坑院营造技艺确为国家级非遗（来源 2 直证）；起源年代学界说法不一，正文只作一般性说明、年份不写死。

---

## 候选 2｜风格 / 古代 / 伊斯兰·南亚

- 建议 id：`sasanian-architecture`
- 中文名：**萨珊建筑（Sasanian architecture，伊万 iwan 起源）**
- 主题：**风格** ｜ 层级：**重要** ｜ 时期：**古代** ｜ 地区：**伊斯兰/南亚**
- 定义：波斯萨珊王朝（224–651 CE）的建筑风格，以**桶形拱顶的伊万（iwan，一侧开敞的拱顶大厅）**、巨大拱券（泰西封 Taq Kasra）、穹顶与火庙为特征；其形制被阿拉伯穆斯林大量继承并融入伊斯兰建筑，是伊斯兰建筑直接前身之一。
- 来源 1（维基百科）：
  - URL：`https://en.wikipedia.org/wiki/Sasanian_architecture` ｜ 标题 *Sasanian architecture - Wikipedia* ｜ HTTP **200**
  - 关键句（正文直证）：
    - "Sasanian architecture refers to the **Persian architectural style** that reached a peak in its development during the **Sasanian era (224–651 CE)**."（配图说明 Taq Kasra，Ctesiphon 萨珊宫殿遗存）
    - "**Much of Sasanian architecture was adopted by Muslims and became part of Islamic architecture.**"
    - "All are characterised by the **barrel-vaulted iwans** introduced in the Parthian era, but now they reached massive proportions, particularly at Ctesiphon."
- 来源 2（Art in Context，艺术史教育与研究平台，非维基）：
  - URL：`https://artincontext.org/persian-art/` ｜ 标题 *Persian Art - A History of Ancient Persian Paintings and Iranian Art* ｜ HTTP **200**
  - 关键句（正文直证）：
    - "**Sasanian architecture developed monumental domed chambers, barrel vaults, iwans, palaces, and fire temples.**"
    - "Parthian builders also used **barrel-vaulted halls and the iwan**, a vaulted space open on one side."
- 入选理由：两源为**不同平台**（维基百科 vs 艺术史平台 Art in Context）、均 HTTP 200 正文直证，把「萨珊建筑」明确认定为一种**波斯建筑风格**并给出伊万（iwan）/桶形拱顶/穹顶等特征，且指出其被伊斯兰建筑继承；`scope.md` 风格维度（64 条）中无 `sasanian/persian` 具名风格，伊斯兰·南亚·古代格仅 `indian-architecture` 1 条泛条，补此条可填格且补上「伊万 iwan 起源」这一对伊斯兰建筑极关键的风格源头，与既有《伊斯兰建筑》伞条形成「波斯源头 vs 泛伊斯兰」区分，非近义重复。与任务建议方向「Sassanid/Persian 建筑（伊万 iwan 起源）」一致。
- 备注：**地区/时期粗分说明**——萨珊波斯（224–651 CE）为**前伊斯兰**时期，但本项目地区仅设「伊斯兰/南亚」粗粒度桶（无「西亚/波斯」独立桶），且萨珊为伊斯兰建筑 iwan 形制的直接源头，故归入「伊斯兰/南亚」桶、时期归「古代」（含古典时代晚期至中世纪早期，属本项目粗分口径，与 `indian-architecture` 归古代一致）；入库时建议对 `region`/`period` 标注意见并核对期限口径。

---

## 候选 3｜风格 / 文艺复兴至19世纪 / 伊斯兰·南亚

- 建议 id：`ottoman-architecture`
- 中文名：**奥斯曼建筑（Ottoman architecture）**
- 主题：**风格** ｜ 层级：**重要** ｜ 时期：**文艺复兴至19世纪** ｜ 地区：**伊斯兰/南亚**
- 定义：奥斯曼帝国（安纳托利亚/巴尔干/伊斯坦布尔为中心）的建筑风格，以**集中式大穹顶＋半穹顶**覆盖的中心平面清真寺为标志（受圣索菲亚大教堂影响），古典期（16–17 世纪）由建筑师**米马尔·希南（Mimar Sinan）**确立，代表如苏莱曼尼耶清真寺（1550–1557）。
- 来源 1（维基百科）：
  - URL：`https://en.wikipedia.org/wiki/Ottoman_architecture` ｜ 标题 *Ottoman architecture - Wikipedia* ｜ HTTP **200**
  - 关键句（正文直证）：
    - "Early Ottoman architecture experimented with multiple building types over the course of the 14th to 15th centuries, progressively evolving into the **classical Ottoman style of the 16th and 17th centuries**."
    - "This style integrated the Ottoman tradition with influences from the **Hagia Sophia**, resulting in monumental mosque buildings focused around a **high central dome with a varying number of semi-domes**."
    - 目录含 "**Classical period (16th to 17th centuries)**"、"**The era of Sinan**"、"Dome design"。
- 来源 2（Art in Context，艺术史教育与研究平台，非维基）：
  - URL：`https://artincontext.org/islamic-architecture/` ｜ 标题 *Islamic Architecture - Building Styles Across the Muslim World* ｜ HTTP **200**
  - 关键句（正文直证）：
    - "**Ottoman architecture produced a special style of monumental, representational structure** based on the model of pre-existing Byzantine domes: broad central domes with enormous diameters were placed on top of a center-plan building."
    - "**Mimar Sinan, an Ottoman architect**, built some of the most ornate domed structures."
    - "**Suleymaniye Mosque (Istanbul, Turkey) – 1558 Architect Mimar Sinan**…"
- 入选理由：两源为**不同平台**（维基百科 vs 艺术史平台 Art in Context）、均 HTTP 200 正文直证，把「奥斯曼建筑」明确认定为一种建筑风格并给出「集中大穹顶＋半穹顶、中心平面、希南古典期」等特征；`scope.md` 风格维度中无 `ottoman` 具名风格，伊斯兰·南亚·文艺复兴至19世纪格仅 `mughal-architecture` 1 条，补此条可填格。与既有 `islamic-architecture`（中世纪泛条）、`mughal-architecture`（南亚莫卧儿）形成「奥斯曼（西亚/安纳托利亚）vs 莫卧儿（南亚）」区分，非近义重复。与任务建议方向「奥斯曼建筑（Ottoman architecture）」一致。
- 备注：奥斯曼建筑跨越 14–20 世纪，本条按目标格时期「文艺复兴至19世纪」，聚焦其**古典期 16–17 世纪**（与本项目粗分口径相符）；地区归「伊斯兰/南亚」桶（奥斯曼属伊斯兰文明圈；地区桶无独立「西亚」项）。

---

## 双源可达性明细（本轮实测 HTTP）

### 入选双源（均 HTTP 200，不同平台，正文关键句已逐条核对）
| 格 | 来源 A（平台） | HTTP | 来源 B（平台，非维基） | HTTP |
| --- | --- | --- | --- | --- |
| 下沉空间/古代/中国 | `https://en.wikipedia.org/wiki/Yaodong`（Wikipedia） | 200 | `https://www.smx.gov.cn/4138/614864448/732660.html`（三门峡市人民政府官网） | 200 |
| 风格/古代/伊斯兰·南亚 | `https://en.wikipedia.org/wiki/Sasanian_architecture`（Wikipedia） | 200 | `https://artincontext.org/persian-art/`（Art in Context） | 200 |
| 风格/文艺复兴至19世纪/伊斯兰·南亚 | `https://en.wikipedia.org/wiki/Ottoman_architecture`（Wikipedia） | 200 | `https://artincontext.org/islamic-architecture/`（Art in Context） | 200 |

### 备选方向（同为≥2 独立权威源、不同平台、均 200，供 lead 择优/替换）
| 格 | 备选 id/名 | 来源 A | HTTP | 来源 B（非维基） | HTTP |
| --- | --- | --- | --- | --- | --- |
| 风格/古代/伊斯兰·南亚 | `indian-rock-cut-architecture` 印度岩凿建筑（佛教石窟：阿旃陀/埃洛拉） | `https://en.wikipedia.org/wiki/Indian_rock-cut_architecture`（Wikipedia；另 `Ajanta_Caves`/`Ellora_Caves` 亦 200） | 200 | `https://artincontext.org/ajanta-caves/`（Art in Context） | 200 |
| 风格/文艺复兴至19世纪/伊斯兰·南亚 | `safavid-architecture` 萨法维建筑（伊斯法罕） | `https://en.wikipedia.org/wiki/Naqsh-e_Jahan_Square`（Wikipedia；`Safavid_architecture` 重定向至 `Safavid_Iran` 200） | 200 | `https://artincontext.org/persian-art/`（Art in Context；"Safavid Isfahan joined mosques, palace, bazaar, and public square…"） | 200 |

### 第二源不可达记录（下沉空间/古代/中国 之排除项；本轮 smx.gov.cn 成功，其余为负向排除）
| 尝试 URL | 结果 |
| --- | --- |
| `britannica.com/technology/yaodong` | 403 |
| `designingbuildings.co.uk/wiki/{Cave_dwelling, Earth_sheltered_construction, Underground_building, Sunken_courtyard, Yaodong, Cave}` | 404（均无专页） |
| `artincontext.org/{cave-dwelling, underground-architecture, earth-sheltered, cave-dwellings}` | 404 |
| `www.ihchina.cn/project.html?tid=8`（传统技艺名录，地坑院营造技艺所在类） | 200 但正文 **JS 动态加载**，静态页无条目文本；`http://` 版 400/403 抖动 |
| `www.shanzhou.gov.cn`（陕州区政府）站内搜索 | 404／SSL handshake 失败 |
| `travelchinaguide.com/cityguides/henan/sanmenxia/` | 200 但正文未提及「地坑院/坑院」 |
| `metmuseum.org`(429)、`khanacademy.org`(反爬)、`worldhistory.org`(403)、`whc.unesco.org`(403) | 不可用 |

### 打开 URL 计数（本轮）
- 实际发起 HTTP 请求 **约 45+ 次**（含失败重试、同页取多段）；去重后 **约 40 个不同 URL**；其中 **HTTP 200 约 20 个**，其余为 403/404/429/421/SSL/超时/反爬（主要用于第二源排除与备选探测）。
- 入选 3 格的 6 份来源**全部 HTTP 200**、标题与正文关键句均逐条核对（见上「入选双源」表）；备选 2 组的 URL 亦验证 200。

---

## 机器可读汇总

```
ROUND=47
SCOPE_TOTAL=255   # 理论128/风格64/造景19/动线13/下沉12/材料19
TARGET_CELLS=["下沉空间/古代/中国","风格/古代/伊斯兰/南亚","风格/文艺复兴至19世纪/伊斯兰/南亚"]
DOUBLE_SOURCE_CANDIDATES=3
CELL_NO_DOUBLE_SOURCE=[]   # 3 格本轮均取得可达双源

CANDIDATES=[
 {"id":"dikengyuan","title":"地坑院（下沉式窑院／天井窑院）","theme":"下沉空间","tier":"补充","period":"古代","region":"中国","sources":["wp-yaodong","smx-shanzhou-dikengyuan"],"urls":["https://en.wikipedia.org/wiki/Yaodong","https://www.smx.gov.cn/4138/614864448/732660.html"]},
 {"id":"sasanian-architecture","title":"萨珊建筑（Sasanian architecture，伊万 iwan 起源）","theme":"风格","tier":"重要","period":"古代","region":"伊斯兰/南亚","sources":["wp-sasanian-architecture","artincontext-persian-art"],"urls":["https://en.wikipedia.org/wiki/Sasanian_architecture","https://artincontext.org/persian-art/"]},
 {"id":"ottoman-architecture","title":"奥斯曼建筑（Ottoman architecture）","theme":"风格","tier":"重要","period":"文艺复兴至19世纪","region":"伊斯兰/南亚","sources":["wp-ottoman-architecture","artincontext-islamic-architecture"],"urls":["https://en.wikipedia.org/wiki/Ottoman_architecture","https://artincontext.org/islamic-architecture/"]}
]

ALTERNATES=[
 {"cell":"风格/古代/伊斯兰/南亚","id":"indian-rock-cut-architecture","title":"印度岩凿建筑（佛教石窟：阿旃陀/埃洛拉）","theme":"风格","tier":"重要","period":"古代","region":"伊斯兰/南亚","sources":["wp-indian-rock-cut-architecture","artincontext-ajanta-caves"],"urls":["https://en.wikipedia.org/wiki/Indian_rock-cut_architecture","https://artincontext.org/ajanta-caves/"]},
 {"cell":"风格/文艺复兴至19世纪/伊斯兰/南亚","id":"safavid-architecture","title":"萨法维建筑（Safavid architecture，伊斯法罕）","theme":"风格","tier":"重要","period":"文艺复兴至19世纪","region":"伊斯兰/南亚","sources":["wp-naqsh-e-jahan-square","artincontext-persian-art"],"urls":["https://en.wikipedia.org/wiki/Naqsh-e_Jahan_Square","https://artincontext.org/persian-art/"]}
]

SECOND_SOURCE_FAILED_CELL1=["britannica 403","designingbuildings 6 slugs 404","artincontext 4 slugs 404","ihchina JS-rendered/400-403","shanzhou.gov.cn search 404/SSL","travelchinaguide 未含地坑院","met 429/khanacademy 反爬/worldhistory 403/unesco 403"]

NOTE_REGION_PERIOD={
 "dikengyuan":"下沉空间主题补充条；与风格条 yaodong（广义窑洞）主题维度/形制不同，非重复。起源年代不写死。",
 "sasanian-architecture":"前伊斯兰波斯，归伊斯兰/南亚粗分桶（伊万 iwan 起源、伊斯兰建筑前身）；period 古代为粗分口径，入库核对",
 "ottoman-architecture":"跨越14-20世纪；按目标格聚焦古典期16-17世纪；归伊斯兰/南亚粗分桶"
}
```

是否发现新缺口：**是**——3 个稀疏格（下沉空间/古代/中国、风格/古代/伊斯兰·南亚、风格/文艺复兴至19世纪/伊斯兰·南亚）本轮**均给出「≥2 独立权威来源 + 不同平台 + 属本领域 + scope 缺失」的新 scope 候选**；其中「下沉空间/古代/中国」相比第 46 轮新增可达第二源（三门峡市人民政府官网「陕州地坑院」专页），由「暂无可达双源」转为**可双源**。另额外给出 2 条已验证的备选方向（印度岩凿建筑、萨法维建筑）供择优。
