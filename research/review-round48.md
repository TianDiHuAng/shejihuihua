# 第 48 轮 B5 复核报告（review-round48）——5 个已写 L2 条目补具名实例（各两条独立权威来源）

复核日期：2026-11-23（Asia/Hong_Kong）　｜　复核人：review-r48（lead 委派子任务，无人值守）　｜　性质：**严格只读，唯一产出本文件**

## 〇、执行说明与只读声明

- **已读治理文档**：项目根无 `AUTONOMOUS.md` / `TASK_design.md`；实读桌面同名文件 `D:/Users/Administrator/Desktop/AUTONOMOUS.md`（71 行）与 `D:/Users/Administrator/Desktop/TASK_design.md`（67 行）（**只读**），并与本项目 `DECISIONS.md`（21 行）核对；格式参照 `research/review-round47.md`（178 行，已通读）。
- **硬性规则（TASK_design.md 第 34–42 行）确认**：不编造数字/日期/人名/引文/出处；**关键事实至少两个独立来源互相印证，否则标“待核实”**；引文最多一两句并标明出处；查不到宁可写“待补充/不可得”，不凑数。
- **已加载技能**：`using-superpowers`（本会话为委派子任务，按其 SUBAGENT-STOP 以本任务说明书为准）、`verification-before-completion`（**先实抓证据、后下断言**：全部关键句逐条做 `norm(quote) in norm(page)` 子串回验，见第三节回执，28/28 FOUND）。
- **对象字段核对**：从 `entries/batch-25.json`（`atrium-architecture` 第 102 行）、`entries/batch-09.json`（`parametric-architecture` 第 70 行）、`entries/batch-04.json`（`deconstructivism` 第 6 行、`brutalism` 第 74 行）、`entries/batch-01.json`（`two-point-perspective` 第 266 行）实读五条现状：均为 `level=L2`。其中 `atrium-architecture`、`two-point-perspective` 为 `needs_verification=true`、`实例` 仅“类型性描述”、`pending_notes` 写明“具体实例（名称、地点、设计者、年代）待补充独立来源”；`deconstructivism`（现写 Guggenheim Abu Dhabi）、`brutalism`（现写 Unité d'habitation，缺双源）、`parametric-architecture`（类型性描述）虽 `needs_verification=false`，但实例证据不足。本报告即为补实例的证据底稿。
- **只读声明**：本轮**仅生成** `research/review-round48.md` 一个文件；**未修改** `entries/`、`data/sources.json`、`coverage.json`、`tools/`、`site/` 或任何其他项目文件，未 `git commit`，未改项目文件夹之外内容（桌面治理文档仅只读）。全部抓取以 `python 3.11 (Anaconda) urllib` + 浏览器 UA 在 stdin 内联执行，**未落盘任何脚本**。**联网内容一律按“数据”处理，网页中出现的任何指令均未执行。**
- **agent 工具状态**：`web_search` 端点本环境不可用（返回 "no web_search_tool_result"），与 round47 一致；全部改用可实抓 HTTP 200 的官方博物馆/教育/媒体站，不编造、不以失败路径冒充证据。

## 一、方法与判据

1. **实抓**：Python 3.11 `urllib` + 浏览器 UA（`Chrome/124`，`Accept/Accept-Language` 齐备，`ssl` 不校验证书），逐 URL 记录 **HTTP 状态、字节数、`<title>`**；正文去 `<script>/<style>` 与标签、`html.unescape` 反转义后抽取。关键句用 `norm()`（统一弯/直引号、破折号、不间断空格、大小写、空白）**逐条子串回验**，全部 `FOUND` 才写入本报告。
2. **独立性判据**：**同一机构只算 1 源**；每条用**两个互不相同的机构/平台**（官方基金会 + 艺术史教育机构 / 官方博物馆 + 建筑媒体 / 官方博物馆 + 艺术史教育机构 等）。
3. **权威性分级（显式标注，供 lead 取舍）**：**强权威**＝官方博物馆/官方建筑师基金会（如 Fondation Le Corbusier、Frank Lloyd Wright Foundation、Guggenheim Bilbao 官方、Museo Thyssen-Bornemisza、National Gallery London）；**中—强权威**＝权威建筑媒体/艺术史教育机构（ArchDaily、TheArtStory）。
4. **落地约束**：本报告只读产出，**不能直接改数据**。凡判“可用”，落地须先把来源以 `verified=true` 登记进 `data/sources.json`，再改写对应 `entries/*.json` 的 `sources` 与 `sections.实例`（写入“名称/地点/设计者/年份”），同步 `pending_notes`/「待核实」，按需更新 `coverage.json` 源数，复跑 `tools/check.py`；登记前不得视为已改。
5. **本轮未采用维基百科作主源**：`en.wikipedia.org` 可访问（200），但按项目既定口径（D10 / round46）**维基属同平台伞源、不计独立源**，仅用于快速定位官方 URL 与事实坐标，**不作证据列出**。
6. **JS 单页站问题（本轮实测）**：`guggenheim.org/about-us/history`（200，但正文“doesn't work properly without JavaScript enabled”，无可抽取静态正文）；`guggenheim-bilbao.eus` 官方 Building 页与 Museum 页（200，但 1991/1997 年份由 JS 渲染，静态 HTML 无数字）。故相应年份改由可抽取正文的第二源直证，并在第六节标注口径。

---

## 二、五条复核（每条：名称 / 地点 / 设计者 / 年份 + 两条独立权威来源）

### 2.1 `atrium-architecture` → **纽约所罗门·R·古根海姆美术馆 Solomon R. Guggenheim Museum（纽约，Frank Lloyd Wright，1943 设计委托 / 1959 开馆）**

- **名称**：Solomon R. Guggenheim Museum（所罗门·R·古根海姆美术馆，纽约）
- **地点**：美国 · 纽约市（New York City，曼哈顿上东区）
- **设计者**：**Frank Lloyd Wright（弗兰克·劳埃德·赖特）**
- **年份**：**1943 设计委托 / 1959 开馆**（任务给定；源② 记 “1943-59”；源① 直书 1943 委托）

| # | 机构 / 权威级 | URL | 标题 | HTTP（字节） | 关键句（原文，实抓，已回验 FOUND） |
| --- | --- | --- | --- | --- | --- |
| ① | Frank Lloyd Wright Foundation（赖特官方基金会，**强权威·官方**） | `https://franklloydwright.org/site/solomon-r-guggenheim-museum/` | Solomon R. Guggenheim Museum - Frank Lloyd Wright Foundation | **200**（52,892 B） | “**She wrote Frank Lloyd Wright in 1943**, saying: …”；“Wright’s museum **resembles a white ribbon curled into a cylindrical stack that grows continuously wider as it spirals upwards towards a glass ceiling.**”；“Wright, who had **never received a significant commission in New York**…” |
| ② | TheArtStory（艺术史教育机构，**中—强权威·艺术史教育**） | `https://www.theartstory.org/artist/wright-frank-lloyd/` | Wright Architecture, Bio, Ideas \| TheArtStory | **200**（188,632 B） | 作品条目“**Solomon R. Guggenheim Museum (1943-59)**”；“Its design of a main gallery that consists of **a spiral ramp encircling a skylit atrium** was a radical departure from all previous museums…”；“the Guggenheim Museum building in **New York City**”。 |

**三要素对位**：名称＝Solomon R. Guggenheim Museum（两源一致）；地点＝New York（源① “commission in New York”、源② “New York City”）；设计者＝Frank Lloyd Wright（两源一致）；年份＝**1943 委托（源① 直书）/ 1943–59（源② 直书，含 1959 落成）**，任务“1943 设计/1959 开馆”与源②一致。
**独立性说明**：Frank Lloyd Wright Foundation（赖特官方）与 TheArtStory（独立教育机构）为两个不同机构，均 HTTP 200、正文直证，可作独立双源。
**手法贴合度（诚实标注）**：该馆的核心空间是**绕单一中庭盘旋上升、顶部玻璃天窗采光的连续坡道**（源② 直书“skylit atrium”，源①“spirals upwards towards a glass ceiling”）——属“中庭/采光中庭”的经典原型；但它为单一螺旋坡道环一顶部采光void，与“多层环廊围绕中庭”的形制略有差别，条目 `sections.实例` 宜写明“螺旋坡道环顶部采光中庭”。

### 2.2 `parametric-architecture` → **盖达尔·阿利耶夫中心 Heydar Aliyev Center（巴库，Zaha Hadid Architects，2007–2012）**

- **名称**：Heydar Aliyev Center（盖达尔·阿利耶夫中心；TheArtStory 作 “Heydar Aliyev Cultural Center”）
- **地点**：阿塞拜疆 · 巴库（Baku, Azerbaijan）
- **设计者**：**Zaha Hadid Architects（扎哈·哈迪德事务所，Zaha Hadid）**
- **年份**：**2007–2012**（任务给定，与源② “2007-12” 一致）；**源① ArchDaily 记 completion “Year: 2013”**（与任务差一年，两源并列、见第六节）

| # | 机构 / 权威级 | URL | 标题 | HTTP（字节） | 关键句（原文，实抓，已回验 FOUND） |
| --- | --- | --- | --- | --- | --- |
| ① | ArchDaily（权威建筑媒体，**中—强权威·建筑媒体**） | `https://www.archdaily.com/448774/heydar-aliyev-center-zaha-hadid-architects` | Heydar Aliyev Center / Zaha Hadid Architects \| ArchDaily | **200**（821,837 B） | “Heydar Aliyev Center / **Zaha Hadid Architects**”；“Cultural Center • **Baku, Azerbaijan** Architects: Zaha Hadid Architects”；“Year Completion year of this architecture project **Year: 2013**”（Area 101,801 m²）。 |
| ② | TheArtStory（艺术史教育机构，**中—强权威·艺术史教育**） | `https://www.theartstory.org/artist/hadid-zaha/` | Zaha Hadid Paintings, Bio, Ideas \| TheArtStory | **200**（152,008 B） | 作品条目“**Heydar Aliyev Cultural Center (2007-12)**”；“Her firm would **coin the term Parametricism** to define this signature look and feel.”；“a key part of the regeneration of Baku was moving away from the monumental style of Soviet architecture **towards more flowing forms**”。 |

**三要素对位**：名称＝Heydar Aliyev Center / Cultural Center（两源指同一建筑）；地点＝Baku, Azerbaijan（源① 直书）；设计者＝Zaha Hadid Architects（两源一致）；年份＝**2007–2012（源②）/ completion 2013（源①）**，任务“2007–2012”取源②口径。
**独立性说明**：ArchDaily（建筑媒体）与 TheArtStory（教育机构）为两个不同机构，均 HTTP 200、正文直证，可作独立双源。
**权威级提示（诚实标注）**：**未取得官方一级源**——Zaha Hadid Architects 官网 `zaha-hadid.com`（跳转 `zha.com`）返回 **HTTP 403（Cloudflare “Just a moment...”）**、`heydaraliyevcenter.az` 为 JS 单页（9 KB 无正文）。故本条双源均为“建筑媒体 + 教育机构（中—强）”。另：ArchDaily 静态正文未出现 “parametric/fluid” 字样，参数化定性由源② 的 “Parametricism + flowing forms” 支撑。

### 2.3 `deconstructivism` → **毕尔巴鄂古根海姆美术馆 Guggenheim Museum Bilbao（毕尔巴鄂，Frank Gehry，1991–1997）**

- **名称**：Guggenheim Museum Bilbao（毕尔巴鄂古根海姆美术馆）
- **地点**：西班牙 · 毕尔巴鄂（Bilbao, Spain；Nervión 河畔旧工业区）
- **设计者**：**Frank Gehry（弗兰克·盖里）**
- **年份**：**1991–1997**（任务给定）；**源② 记 “Guggenheim Museum Bilbao (1997)”**（1997 落成/开馆）；**源① 官方 Building 页静态无 1991/1997 数字（年份由 JS 渲染）**

| # | 机构 / 权威级 | URL | 标题 | HTTP（字节） | 关键句（原文，实抓，已回验 FOUND） |
| --- | --- | --- | --- | --- | --- |
| ① | Guggenheim Museum Bilbao 官方（**强权威·官方博物馆**） | `https://www.guggenheim-bilbao.eus/en/the-building` | The Building \| Guggenheim Museum Bilbao | **200**（215,120 B） | “**Designed by Canadian American architect Frank Gehry, the Guggenheim Museum Bilbao building represents a magnificent example of the most groundbreaking 20th-century architecture.**”；“The three levels of the building are **organized around the Atrium** and are connected by means of curved walkways, **titanium and glass** elevators, and staircases.” |
| ② | TheArtStory（艺术史教育机构，**中—强权威·艺术史教育**） | `https://www.theartstory.org/movement/deconstructivism/` | Deconstructivism and Architecture Movement Overview \| TheArtStory | **200**（174,831 B） | 代表作列表“**Guggenheim Museum Bilbao (1997)**”；“The striking curves of the exterior walls, **constructed of titanium, glass, and limestone**, are, according to Gehry, ‘**designed to catch the light**’…” |

**三要素对位**：名称＝Guggenheim Museum Bilbao（两源一致）；地点＝Bilbao（源② “Bilbao's old industrial city center”；源① 为毕尔巴鄂馆官方）；设计者＝Frank Gehry（两源一致）；年份＝**1997（源② 直书）/ 1991–1997（任务）**，源① 官方页静态未标年份（JS），起点 1991 未在所选源直证，见第六节。
**独立性说明**：Guggenheim Bilbao 官方（博物馆）与 TheArtStory（独立教育机构）为两个不同机构，均 HTTP 200、正文直证，可作独立双源。

### 2.4 `brutalism` → **马赛公寓 Unité d'habitation（马赛，Le Corbusier，1947–1952）**

- **名称**：Unité d'habitation（马赛公寓；又称 La Cité radieuse “光辉之城”）
- **地点**：法国 · 马赛（Marseille；南郊、山海之间）
- **设计者**：**Le Corbusier（勒·柯布西耶）**
- **年份**：**1947–1952**（任务给定）；**源① 官方标题记 “1945-1952”、正文“final version … adopted in March 1947”**；源② 记 “Unité d'habitation (1952)”（落成）

| # | 机构 / 权威级 | URL | 标题 | HTTP（字节） | 关键句（原文，实抓，已回验 FOUND） |
| --- | --- | --- | --- | --- | --- |
| ① | Fondation Le Corbusier（勒·柯布西耶官方基金会，**强权威·官方**） | `https://www.fondationlecorbusier.fr/en/work-architecture/achievements-unite-dhabitation-marseille-france-1945-1952/` | Le Corbusier, Unité d’habitation, Marseille, France, 1945-1952 | **200**（96,823 B） | 标题直录“**Le Corbusier, Unité d’habitation, Marseille, France, 1945-1952**”；正文“**the final version of the Marseille Housing Unit was adopted in March 1947**”（选址在“the south of Marseille”）。 |
| ② | TheArtStory（艺术史教育机构，**中—强权威·艺术史教育**） | `https://www.theartstory.org/movement/brutalism/` | Brutalist Architecture Movement Overview \| TheArtStory | **200**（170,612 B） | 代表作“**Unité d’habitation (1952)**”；“Brutalism’s most famous stylistic motif was the use of **raw concrete (French “béton brut”)** for exterior surfaces…；…**to be constructed in war-damaged Marseille, it was the architect’s first public commission**.” |

**三要素对位**：名称＝Unité d'habitation（两源一致）；地点＝Marseille（源① 标题/正文、源② “war-damaged Marseille”）；设计者＝Le Corbusier（源① 标题、源② 语境一致）；年份＝**1945–1952（源① 官方标题，含 1947 定案）/ 1952（源② 落成）**，任务“1947–1952”为建造区间，与“1947 定案、1952 落成”自洽。
**独立性说明**：Fondation Le Corbusier（官方）与 TheArtStory（独立教育机构）为两个不同机构，均 HTTP 200、正文直证，可作独立双源（**本条为四条建筑风格中权威级最高的一条：官方基金会 + 教育机构**）。

### 2.5 `two-point-perspective` → **卡纳莱托《圣马可广场威尼斯景》 The Piazza San Marco in Venice（现藏马德里提森-博内米萨国立博物馆，Canaletto，约 1723–1724）**

> ✅ **本次获得“两点透视”最硬的直接证据**：马德里提森官方藏品页**明确写出该画“He employs two vanishing points located at equal distances from the middle of the work.”**（使用两个位于画面中部等距的灭点）——这正是“两点透视”的定义级描述，远优于 round47 中“单点错觉透视”的错配案例。

- **名称**：The Piazza San Marco in Venice（《圣马可广场威尼斯景》）
- **地点**：画中：意大利 · 威尼斯 · 圣马可广场（Piazza San Marco）；现藏：西班牙 · 马德里 · **Museo Nacional Thyssen-Bornemisza（提森-博内米萨国立博物馆）**，Inv. no. 75（1956.1），Room 17
- **设计者**：**Canaletto（卡纳莱托；Giovanni Antonio Canal，1697–1768）**
- **年份**：**约 1723–1724**（ca. 1723-1724）；布面油画，141.5 × 204.5 cm

| # | 机构 / 权威级 | URL | 标题 | HTTP（字节） | 关键句（原文，实抓，已回验 FOUND） |
| --- | --- | --- | --- | --- | --- |
| ① | Museo Nacional Thyssen-Bornemisza（提森-博内米萨国立博物馆官方藏品页，**强权威·官方博物馆**） | `https://www.museothyssen.org/en/collection/artists/canaletto/piazza-san-marco-venice` | The Piazza San Marco in Venice - Canaletto. Museo Nacional Thyssen-Bornemisza | **200**（138,873 B） | 藏品字段“**Canaletto (Giovanni Antonio Canal) The Piazza San Marco in Venice ca. 1723 - 1724** Oil on canvas. 141.5 x 204.5 cm **Museo Nacional Thyssen-Bornemisza, Madrid**”；“**He employs two vanishing points located at equal distances from the middle of the work.** These points guide the spectator’s gaze into the background…；the **Procuratie lining both sides of the square give depth to the perspective**.” |
| ② | TheArtStory（艺术史教育机构，**中—强权威·艺术史教育**） | `https://www.theartstory.org/artist/canaletto/` | Canaletto Paintings, Bio, Ideas \| TheArtStory | **200**（136,561 B） | “**Canaletto’s superb mastery of perspective**, a technique fostered under the Renaissance tradition of his native Italy…；引文“**the precise perspective ad angolo [angled]**, in keeping with the rules of theatrical scenography […] governs the arrangement of the buildings in the space”。 |

**三要素对位**：名称＝The Piazza San Marco in Venice（源① 直录）；地点＝威尼斯圣马可广场（画中）/ 马德里（现藏，源① 直书）；设计者＝Canaletto（Giovanni Antonio Canal，两源一致）；年份＝**ca. 1723–1724（源① 直录）**。
**独立性说明**：Museo Thyssen-Bornemisza（国立博物馆官方）与 TheArtStory（独立教育机构）为两个不同机构，均 HTTP 200、正文直证——“两点透视”的**核心事实（two vanishing points）由① 官方直证**，② 以“斜角透视 perspective ad angolo / 透视大师”独立佐证该手法归属，可作独立双源。
**附加旁证（第三源，不计入两源）**：National Gallery, London 藏品 `https://www.nationalgallery.org.uk/paintings/canaletto-venice-piazza-san-marco`（HTTP **200**，104,674 B，标题“Canaletto \| Venice: Piazza San Marco \| NG2515”）——另一幅卡纳莱托同题材（about 1758），“**The paving stones and buildings that line the square recede at a sharp angle, which Canaletto exaggerated**, leading our eye deeper into the scene.”，为“圣马可广场类景致的斜角/两点透视”提供同题材的独立博物馆旁证（不同画布，不计主源）。
**诚实标注（严格同画布双源）**：**同一幅画布**（提森这件 ca.1723-24）的“名称/年代/现藏”仅 Thyssen 官方**单一**强源直录；TheArtStory 为独立第二源但佐证的是**作者与“斜角（两点）透视”手法**、并非该件藏品的年代/馆藏。即：**“两点透视手法 + 作者”达双独立源；“该具体画布的四要素”为 Thyssen 单源（此单一强源可信度高，但按项目“关键事实两源”口径仍应标注）**。若 lead 要求“同一画布两条独立来源”，建议将本条 `sections.实例` 表述为“卡纳莱托圣马可广场威尼斯景（两点透视典范）”，并同时列入提森这件（1723-24）与国家美术馆另一件（about 1758）作两馆互证。

---

## 三、汇总（各条可得源数）

| 条目（中文题名 / id） | 具名实例（名称、地点、设计者、年份） | 采用的两条独立主源（机构） | 独立机构数 | 达“双独立源” | 四要素源内直证（名称/地点/设计者/年份） | 权威级 / 备注 |
| --- | --- | --- | --- | --- | --- | --- |
| 中庭 / `atrium-architecture` | 纽约古根海姆美术馆（纽约，Frank Lloyd Wright，1943 设计/1959 开馆） | Frank Lloyd Wright Foundation ＋ TheArtStory | 2 | ✅ | 名称✅ 地点✅(New York) 设计者✅ 年份：1943 / 1943-59 ✅ | 强（官方基金会＋教育）；空间为“螺旋坡道环顶部采光中庭” |
| 参数化建筑 / `parametric-architecture` | 盖达尔·阿利耶夫中心（巴库，Zaha Hadid Architects，2007–2012） | ArchDaily ＋ TheArtStory | 2 | ✅ | 名称✅ 地点✅(Baku) 设计者✅ 年份：2007-12 / completion 2013 ✅ | 中—强（建筑媒体＋教育）；**无官方一级源**（ZHA 站 403、官方站 JS） |
| 解构主义 / `deconstructivism` | 毕尔巴鄂古根海姆美术馆（毕尔巴鄂，Frank Gehry，1991–1997） | Guggenheim Bilbao 官方 ＋ TheArtStory | 2 | ✅ | 名称✅ 地点✅(Bilbao) 设计者✅ 年份：1997（官方静态缺数字）✅ | 强（官方博物馆＋教育）；1991 起点未直证 |
| 粗野主义 / `brutalism` | 马赛公寓 Unité d'habitation（马赛，Le Corbusier，1947–1952） | Fondation Le Corbusier 官方 ＋ TheArtStory | 2 | ✅ | 名称✅ 地点✅(Marseille) 设计者✅ 年份：1945-1952 / 1952 ✅ | **最强**（官方基金会＋教育） |
| 两点透视 / `two-point-perspective` | 提森《圣马可广场威尼斯景》（马德里，Canaletto，约1723–1724） | Museo Thyssen-Bornemisza 官方 ＋ TheArtStory | 2 | ✅（手法/作者双源；**同画布四要素以 Thyssen 单强源**） | 名称✅ 地点✅(画中威尼斯/现藏马德里) 设计者✅ 年份✅(ca.1723-24，源① 直录) | **两点透视有官方定义级直证**（two vanishing points）；同画布第二独立源未得，另 NGL 同题材旁证 |

- **5 条均达“两条独立机构来源（HTTP 200、正文直证、28/28 关键句 FOUND）”；无“完全不可得”条目，故本轮未触发整体替换。** 例外与提示：`parametric-architecture` 无官方一级源（中—强权威）；`two-point-perspective` 的“两点透视”核心事实有官方定义级直证，但“同一画布”四要素仅 Thyssen 单强源（另 TheArtStory 佐证手法、NGL 同题材旁证）。
- **回执（逐条子串校验，均 FOUND；详见 §五 抓取清单）**：
  - 古根海姆（纽约）：FLW 基金会（G1）3/3；TheArtStory Wright（G2）3/3。
  - 阿利耶夫中心：ArchDaily（H1）3/3；TheArtStory Zaha（H2）3/3。
  - 毕尔巴鄂：Guggenheim Bilbao 官方（B1）2/2；TheArtStory 解构（B2）3/3。
  - 马赛公寓：Fondation Le Corbusier（M1）2/2；TheArtStory 粗野（M2）3/3。
  - 两点透视：Thyssen（T1）3/3；TheArtStory Canaletto（T2）2/2；NGL 旁证（N1）1/1。
  - **合计 28/28 关键句 FOUND（11 个 URL 全部 HTTP 200）。**

---

## 四、失败 / 未采用候选（备核，均不作证据）

| URL / 站点 | 结果 | 说明 |
| --- | --- | --- |
| `https://www.zaha-hadid.com/architecture/heydar-aliyev-centre/`（→ `https://www.zha.com/...`） | **HTTP 403（Cloudflare “Just a moment...”）** | 扎哈事务所官网被反爬拦截，故参数化条无官方一级源 |
| `https://www.heydaraliyevcenter.az/` | **200 但仅 9 KB，标题阿塞拜疆语，JS 单页无正文** | 官方站无可抽取静态文本，弃用 |
| `https://www.guggenheim.org/about-us/history` | **200 但 “doesn't work properly without JavaScript enabled”** | 官方历史页为 JS 单页，无静态正文，不能作关键句来源（仅作 URL 线索） |
| `https://www.guggenheim-bilbao.eus/en/the-building`、`/en/the-museum` 的 1991/1997 数字 | **200，但静态 HTML 无 “1991/1997/opened” 字样（JS 渲染）** | 官方页仅用于 Gehry/titanium/atrium；年份改由 TheArtStory 直证 |
| `https://www.nga.gov/collection/artist-info.1109.html`、`https://www.nga.gov/artworks/...` | **HTTP 403** | 华盛顿国家美术馆被反爬 |
| `https://www.royalcollection.org.uk/collection/400532/...` | **HTTP 403** | 英国皇家收藏被拦 |
| `https://www.artnet.com/artists/canaletto/`、`https://www.barnebys.com/artist/canaletto` | **HTTP 403** | 拍卖/艺术市场数据库被拦，未能给提森画布找第二源 |
| `https://collectionapi.metmuseum.org/public/collection/v1/search?...` | **HTTP 410 Gone** | Met 旧检索 API 下线（大都会直接 429/403） |
| `https://www.nationalgalleries.org/`、`https://www.museodelprado.es/en` | **HTTP 403** | 苏格兰国立美术馆、普拉多被拦 |
| `https://www.frick.org/` | **HTTP 418** | 弗里克收藏异常拦截 |
| `https://smarthistory.org/...`、`https://www.britannica.com/...`（round47 记录） | **HTTP 403** | 艺术史教育/百科首选被反爬 |
| `https://en.wikipedia.org/wiki/...` | **200** | 仅用于定位官方 URL/事实坐标，**伞源同平台不计独立源**，未作证据 |

---

## 五、证据来源 URL 一览（本轮均已实际打开核验，HTTP 见行）

| # | URL | HTTP（字节） | 标题 / 机构 | 支撑 |
| --- | --- | --- | --- | --- |
| 1 | `https://franklloydwright.org/site/solomon-r-guggenheim-museum/` | 200（52,892） | Solomon R. Guggenheim Museum · Frank Lloyd Wright Foundation（官方） | atrium 源① |
| 2 | `https://www.theartstory.org/artist/wright-frank-lloyd/` | 200（188,632） | Wright Architecture · TheArtStory | atrium 源② |
| 3 | `https://www.archdaily.com/448774/heydar-aliyev-center-zaha-hadid-architects` | 200（821,837） | Heydar Aliyev Center / Zaha Hadid Architects · ArchDaily | parametric 源① |
| 4 | `https://www.theartstory.org/artist/hadid-zaha/` | 200（152,008） | Zaha Hadid · TheArtStory | parametric 源② |
| 5 | `https://www.guggenheim-bilbao.eus/en/the-building` | 200（215,120） | The Building · Guggenheim Museum Bilbao（官方） | deconstructivism 源① |
| 6 | `https://www.theartstory.org/movement/deconstructivism/` | 200（174,831） | Deconstructivism Movement Overview · TheArtStory | deconstructivism 源② |
| 7 | `https://www.fondationlecorbusier.fr/en/work-architecture/achievements-unite-dhabitation-marseille-france-1945-1952/` | 200（96,823） | Le Corbusier, Unité d’habitation, Marseille, France, 1945-1952 · Fondation Le Corbusier（官方） | brutalism 源① |
| 8 | `https://www.theartstory.org/movement/brutalism/` | 200（170,612） | Brutalist Architecture Movement Overview · TheArtStory | brutalism 源② |
| 9 | `https://www.museothyssen.org/en/collection/artists/canaletto/piazza-san-marco-venice` | 200（138,873） | The Piazza San Marco in Venice · Museo Nacional Thyssen-Bornemisza（官方） | two-point 源① |
| 10 | `https://www.theartstory.org/artist/canaletto/` | 200（136,561） | Canaletto · TheArtStory | two-point 源② |
| — | `https://www.nationalgallery.org.uk/paintings/canaletto-venice-piazza-san-marco` | 200（104,674） | Canaletto \| Venice: Piazza San Marco \| NG2515 · National Gallery, London | two-point 同题材旁证（不计两源） |

---

## 六、落地提醒与诚实标注（只读，不改数据）

- 以上“可用”均为**建议**：须先把 10 条主源以 `verified=true` 登记进 `data/sources.json`，再改写对应条目的 `sources` 与 `sections.实例`（写入“名称/地点/设计者/年份”），同步 `pending_notes`/「待核实」，按需更新 `coverage.json` 源数，并复跑 `tools/check.py`。**本报告未修改任何条目数据或其它文件（本文件为唯一产出）。**
- **年份口径差异（据实并列，不强归）**：
  - `atrium-architecture`：源① 记 1943 委托（未含 1959），源② 记 “1943-59”；任务“1943 设计/1959 开馆”取源②。落地可写“1943 设计委托、1959 开馆（1943–59）”。
  - `parametric-architecture`：任务/源② 2007–2012；源① ArchDaily 记 completion **2013**。落地可注“2007 设计、2012–2013 落成，各源略有出入”。
  - `deconstructivism`：任务 1991–1997；源② 记 1997（落成）；源① 官方静态无年份。落地可写“1991–1997（1997 落成）”，并知 1991 起点未在所引源直证。
  - `brutalism`：任务 1947–1952；源① 官方标题“1945-1952”（1947 定案、1952 落成）；源② “1952”。落地可写“1947–1952（项目 1945、1947 定案、1952 落成）”。
- **权威级提示**：`parametric-architecture` 的 ArchDaily＋TheArtStory 均为“中—强”，**无官方/博物馆一级源**（ZHA 官网 Cloudflare 403、官方站 JS）；如 lead 要求“至少一官方源”，此条需另寻或标“权威级偏低”。其余四条均含至少一条官方/基金会/国立博物馆强权威源。
- **两点透视的严格性**：`two-point-perspective` 的**“two vanishing points”由提森官方直接给出**，是真正“两点透视”的定义级证据（优于 round47 的“单点错觉透视”错配）；但**“同一画布四要素”仅 Thyssen 单强源**，TheArtStory 佐证的是作者与“斜角透视”手法。建议 `sections.实例` 采用“卡纳莱托圣马可广场威尼斯景（两点透视典范；提森本 1723-24 / 国家美术馆另本 about 1758）”，并在 `sources` 同时登记 Thyssen、TheArtStory，必要时附 NGL 作旁证。
- **名词一致性**：`deconstructivism` 现 `sections.实例` 写的是“Guggenheim Abu Dhabi（在建）”；本轮提供“毕尔巴鄂古根海姆（1991–1997，已建成典范）”作为更稳妥的已落成实例，建议替换或并列（阿布扎比仍在建，作实例证据力较弱）。
