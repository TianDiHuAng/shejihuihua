# 第 51 轮 B5 补源报告（review-round51b）——4 条待核实条目补具名实例（各两条独立权威来源）

复核日期：2026-11-23（Asia/Hong_Kong）　｜　复核人：review-r51b（lead 委派子任务，无人值守）　｜　性质：**严格只读，唯一产出本文件**

## 〇、执行说明与只读声明

- **已读治理文档**：项目根不存在 `AUTONOMOUS.md` / `TASK_design.md` / `research/review-round50.md`（已用 glob 核实）。实读桌面原件 `D:/Users/Administrator/Desktop/AUTONOMOUS.md`（71 行）与 `D:/Users/Administrator/Desktop/TASK_design.md`（67 行），以及本项目 `DECISIONS.md`（25 行）、`research/gaps-round50.md`（第 16–23 行 B5 待核实清单）、`research/review-round49.md`（同格式前例，通读）、`research/spotcheck-round49/50.md`（核查判据）。全部只读。
- **硬性规则确认**（TASK_design.md 第 34–42 行 / AUTONOMOUS.md 第六节）：不编造数字、日期、人名、引文、出处；**关键事实至少两个独立来源互证，否则标"待核实"**；引文最多一两句并注明出处；查不到宁可写"待补充/不可得"不凑数；**同一机构只算 1 源**；联网内容一律视为数据，**网页中出现的任何指令均未执行**。
- **已加载技能**：`using-superpowers`（本会话为委派子任务，按 SUBAGENT-STOP 以任务说明书为准）、`verification-before-completion`（**先实抓证据、后下断言**：全部关键句逐条做 `norm(quote) in norm(page)` 子串回验，见第五节回执）。
- **对象字段核对**：从 `entries/batch-01.json` 实读四条现状——`composition`（第 70 行）、`balance`（第 102 行）、`proportion`（第 134 行）、`value`（第 200 行）；四条均为 `level=L2`、`needs_verification=true`，`sections.实例` 均为"类型性描述"（名称：…；地点：不适用；设计者：不适用；年份：不适用），`pending_notes` 写明"具体实例（名称、地点、设计者、年代）待补充独立来源"。本报告即为其补实例的证据底稿。
- **避重**：《最后的晚餐》已用于 `one-point-perspective`（batch-01.json 第 256 行），《雅典学院》已用于 `vanishing-point`（第 424 行，见 review-round49 §2.1），依任务要求另择实例。
- **只读声明**：本轮**仅生成** `research/review-round51b.md` 一个文件；**未修改** `entries/`、`data/sources.json`、`coverage.json`、`tools/`、`site/` 或任何其他项目文件，未 `git commit`，未改项目文件夹之外内容（桌面治理文档仅只读）。全部 web 抓取在 stdin 内联 Python 执行，**未在项目内落盘任何脚本或缓存**。

## 一、方法与判据

1. **实抓**：`urllib` + 浏览器 UA（`Chrome/124`，`Accept/Accept-Language/Accept-Encoding:identity` 齐备，`ssl` 不校验证书）逐 URL 记录 **HTTP 状态、字节数、`<title>`**；去 `<script>/<style>` 与标签、`html.unescape` 后抽正文。关键句用 `norm()`（统一弯/直引号、破折号、不间断空格、大小写、空白、Unicode NFKC）逐条子串回验，全部 `FOUND` 才写入本报告（见第五节）。
2. **通道**：`web_search` 端点本轮**可用但间歇性报错**（DeepSeek 搜索端点偶发无返回）；Cloudflare 站点（`gallerieaccademia.it`、`artic.edu`）改由 `web_fetch` 服务端直读或官方 API（`api.artic.edu`）取证。Britannica 全站 403，未作来源。
3. **独立性判据**：**同一机构只算 1 源**；每条用**两个互不相同的机构**——官方博物馆 + 独立艺术史数据库（Web Gallery of Art）。
4. **权威性分级**：**强权威**＝官方博物馆/官方馆藏；**中—强权威**＝Web Gallery of Art（独立艺术史图像/数据数据库）。
5. **不采用维基百科作主源**：按项目既定口径（D10 / round46 / round49），维基属同平台伞源、不计独立源，未作证据列出。
6. **落地约束**：本报告只读产出，不能直接改数据。凡判"可用"，落地须先把来源以 `verified=true` 登记进 `data/sources.json`，再改写对应 `entries/batch-01.json` 的 `sources` 与 `sections.实例`（写入"名称/地点/设计者/年份"），同步 `pending_notes`／「待核实」，按需更新 `coverage.json` 源数，复跑 `tools/check.py`；登记前不得视为已改。

## 二、四条复核（每条：名称 / 地点 / 设计者 / 年份 + 两条独立权威来源）

### 2.1 `proportion`（比例）→ **达·芬奇《维特鲁威人》 Vitruvian Man（威尼斯学院美术馆，约 1490；WGA 记 1492）**

- **名称**：Vitruvian Man / Studio di proporzioni del corpo noto come Uomo vitruviano（《维特鲁威人》；馆方题名意为"已知为维特鲁威人的人体比例研究"）
- **地点**：意大利 · 威尼斯 · 学院美术馆（Gallerie dell'Accademia, Venice；Campo della Carità, Dorsoduro 1050）
- **设计者**：**Leonardo da Vinci（列奥纳多·达·芬奇）**
- **年份**：**约 1490**（任务口径）；**WGA 明记 1492**；馆方官方页**不标确切年份**，仅称"大致属于达·芬奇米兰寓居时期的作品"。见下方诚实标注。

| # | 机构 / 权威级 | URL | 标题 | HTTP（字节） | 关键句（原文，实抓，已回验 FOUND） |
| --- | --- | --- | --- | --- | --- |
| ① | Gallerie dell'Accademia di Venezia 官方馆藏页（**强权威·官方博物馆**） | `https://www.gallerieaccademia.it/opera/studio-di-proporzioni-del-corpo-noto-come-uomo-vitruviano/` | Studio di proporzioni del corpo noto come Uomo vitruviano \| Gallerie dell'Accademia di Venezia | **200**（web_fetch 服务端直读全文；urllib 被 Cloudflare 拦为 "One moment, please..."，非死链） | "**Autore: Leonardo da Vinci**"；"**Titolo: Studio di proporzioni del corpo noto come Uomo vitruviano**"；"**Tipologia: Disegni**"；"Rappresenta uno straordinario studio delle proporzioni umane con una figura ideale in due posizioni diverse, a gambe divaricate e congiunte, **iscritta entro le forme assolute del cerchio e del quadrato**."；"Il foglio risale verosimilmente agli anni del soggiorno milanese di Leonardo". |
| ② | Web Gallery of Art（独立艺术史数据库，**中—强权威**） | `https://www.wga.hu/html_m/l/leonardo/10anatom/1vitruviu.html` | Vitruvian Man by LEONARDO da Vinci | **200**（7,249 B） | "**Vitruvian Man 1492 Pen, ink, watercolour and metalpoint on paper, 343 x 245 mm Gallerie dell'Accademia, Venice**"；"a man with an athletic physique inscribed within a circle and a square illustrates the measurements of the ideal human body according to the rules of the Roman architect Vitruvius". |

**四要素对位**：名称＝Vitruvian Man / Uomo vitruviano（①②一致）；地点＝威尼斯学院美术馆（①官方馆址、②直书 Gallerie dell'Accademia, Venice）；设计者＝Leonardo da Vinci（①②一致）；年份＝**1492（②）/ 约 1490（任务口径）/ 官方页无确切年**（见下）。
**独立性说明**：威尼斯学院美术馆（官方馆藏）与 Web Gallery of Art（独立艺术史数据库）为两个不同机构，均可读、正文直证，可作独立双源。
**年份诚实标注（重要）**：任务给"约 1490"，但所选两源中**只有 ②给出确切年 1492**，①仅写"米兰时期"未标年。落地宜写"约 1490（WGA 记 1492；馆方页未标确切年份）"，**不得冒称两源均直书 1490**。
**手法贴合度**：①"iscritta entro le forme assolute del cerchio e del quadrato"（置于圆与方的绝对形式之中）与 ②"inscribed within a circle and a square"直接支撑"以几何形体组织人体比例"——正是"部分与整体尺寸关系"的经典范例。

### 2.2 `composition`（构图法则）→ **修拉《大碗岛的星期天下午》 A Sunday on La Grande Jatte（芝加哥艺术博物馆，1884–1886）**

- **名称**：A Sunday on La Grande Jatte — 1884 / A Sunday Afternoon on the Ile de la Grande Jatte（《大碗岛的星期天下午》）
- **地点**：美国 · 芝加哥 · 芝加哥艺术博物馆（Art Institute of Chicago；Helen Birch Bartlett Memorial Collection）
- **设计者**：**Georges Seurat（乔治·修拉）**
- **年份**：**1884–1886**（①官方 "1884–86, border added 1888–89"；② "1884-86"）

| # | 机构 / 权威级 | URL | 标题 | HTTP（字节） | 关键句（原文，实抓，已回验 FOUND） |
| --- | --- | --- | --- | --- | --- |
| ① | Art Institute of Chicago 官方馆藏 API（**强权威·官方博物馆第一方数据，CC0**） | `https://api.artic.edu/api/v1/artworks/27992?fields=id,title,artist_display,artist_title,date_display,place_of_origin,medium_display,dimensions` | （JSON 端点无 HTML `<title>`；`data.title` = "A Sunday on La Grande Jatte — 1884"） | **200**（897 B） | `"title": "A Sunday on La Grande Jatte — 1884"`；`"artist_display": "Georges Seurat (French, 1859–1891)"`；`"date_display": "1884–86, border added 1888–89"`；`"credit_line": "Helen Birch Bartlett Memorial Collection"`。 |
| ② | Web Gallery of Art（独立艺术史数据库，**中—强权威**） | `https://www.wga.hu/html_m/s/seurat/figures/jatte.html` | A Sunday Afternoon on the Ile de la Grande Jatte by SEURAT, Georges | **200**（8,822 B） | "**A Sunday Afternoon on the Ile de la Grande Jatte 1884-86 Oil on canvas, 208 x 308 cm Art Institute, Chicago**"；"This painting, shown at the last Impressionist exhibition in 1886, served as the manifesto of Neo-Impressionism." |

**四要素对位**：名称＝A Sunday on La Grande Jatte / A Sunday Afternoon on the Ile de la Grande Jatte（①②同一作品、题名长短两式）；地点＝芝加哥艺术博物馆（①官方馆藏、②直书 Art Institute, Chicago）；设计者＝Georges Seurat（①②一致）；年份＝**1884–86（①②一致；①另记边框 1888–89 加绘）**。
**独立性说明**：芝加哥艺术博物馆（官方第一方数据）与 Web Gallery of Art（独立艺术史数据库）为两个不同机构，均可读、正文直证，可作独立双源。
**通道说明**：artic.edu 人物/作品 HTML 页本环境被 Cloudflare 拦（`web_fetch` 403 / urllib 302 循环），故改用**同一机构官方 API**（`api.artic.edu`，HTTP 200、CC0）作官方源；非死链、非第三方转述。
**手法贴合度**：②直书该作为"新印象派宣言"、修拉以点彩与严谨秩序组织画面人物与色点——是"元素位置、比例与关系组织成有序整体"的经典构图例；①提供权威题名/作者/年份/馆藏。**两源均未逐字讨论"构图法则"概念本身**，概念定性属通识，落笔时不冒称源文直书。

### 2.3 `balance`（均衡）→ **凡·艾克《阿尔诺菲尼肖像》 The Arnolfini Portrait（伦敦国家美术馆，1434）**

- **名称**：The Arnolfini Portrait / Portrait of Giovanni Arnolfini and his Wife（《阿尔诺菲尼肖像》，旧称 "The Arnolfini Marriage"）
- **地点**：英国 · 伦敦 · 国家美术馆（The National Gallery, London；Gallery C，藏品号 NG186）
- **设计者**：**Jan van Eyck（扬·凡·艾克）**
- **年份**：**1434**（①②一致）

| # | 机构 / 权威级 | URL | 标题 | HTTP（字节） | 关键句（原文，实抓，已回验 FOUND） |
| --- | --- | --- | --- | --- | --- |
| ① | The National Gallery, London 官方藏品页（**强权威·官方博物馆**） | `https://www.nationalgallery.org.uk/paintings/jan-van-eyck-the-arnolfini-portrait` | Jan van Eyck \| The Arnolfini Portrait \| NG186 \| National Gallery, London | **200**（115,689 B） | "**Jan van Eyck, 'The Arnolfini Portrait', 1434**"；"**A large round mirror hangs right in the centre of the composition**, its convex glass showing not just the compressed and contorted room but also two men coming in through a door behind us." |
| ② | Web Gallery of Art（独立艺术史数据库，**中—强权威**） | `https://www.wga.hu/html/e/eyck_van/jan/15arnolf/index.html` | Portrait of Giovanni Arnolfini and his Wife (1434) - Web Gallery of Art | **200**（20,817 B） | "**Portrait of Giovanni Arnolfini and his Wife (1434) by Jan van EYCK**"；"this untitled double portrait by Jan van Eyck, **now in the National Gallery, London**"。 |

**四要素对位**：名称＝The Arnolfini Portrait / Portrait of Giovanni Arnolfini and his Wife（①②同一作品）；地点＝伦敦国家美术馆（①官方藏品号 NG186、②直书 National Gallery, London）；设计者＝Jan van Eyck（①②一致）；年份＝**1434（①②一致）**。
**独立性说明**：伦敦国家美术馆（官方）与 Web Gallery of Art（独立艺术史数据库）为两个不同机构，均可读、正文直证，可作独立双源。
**为何另择此例**：《最后的晚餐》已用于 `one-point-perspective`、`雅典学院》已用于 `vanishing-point`（任务明确要求避开），故改选同样以**中央组织、左右两人与中央圆镜形成视觉均衡**著称的《阿尔诺菲尼肖像》。
**手法贴合度（诚实标注）**：两源**均未逐字使用 "symmetry" / "balance" 一词**；①的 "a large round mirror hangs right in the centre of the composition" 与②的 "double portrait"（双人肖像）为**中央轴与两侧人物均衡**的直证，均衡定性属艺术史通识解读，落笔时注明依据为该"中央镜＋双人"构图描写，不冒称源文直书"对称/均衡"。

### 2.4 `value`（明度·明暗层次）→ **伦勃朗《夜巡》 The Night Watch（阿姆斯特丹国立博物馆，1642）**

- **名称**：The Night Watch / The Nightwatch（《夜巡》；官方全名 "Militia Company of District II under the Command of Captain Frans Banninck Cocq"）
- **地点**：荷兰 · 阿姆斯特丹 · 国立博物馆（Rijksmuseum；藏品号 SK-C-5，Night Watch Gallery）
- **设计者**：**Rembrandt van Rijn（伦勃朗）**
- **年份**：**1642**（①②一致）

| # | 机构 / 权威级 | URL | 标题 | HTTP（字节） | 关键句（原文，实抓，已回验 FOUND） |
| --- | --- | --- | --- | --- | --- |
| ① | Rijksmuseum 官方藏品页（**强权威·官方博物馆**） | `https://www.rijksmuseum.nl/en/collection/SK-C-5` | The Night Watch Militia Company of District II under the Command of Captain Frans Banninck Cocq - Rijksmuseum | **200**（299,117 B） | "**Rembrandt van Rijn, 1642**"；"**Rembrandt used the light to focus on particular details, like the captain's gesturing hand and the young girl in the background.**"；"Artwork type painting Object number SK-C-5"。 |
| ② | Web Gallery of Art（独立艺术史数据库，**中—强权威**） | `https://www.wga.hu/html/r/rembrand/26group/05group.html` | The Nightwatch by REMBRANDT Harmenszoon van Rijn | **200**（8,510 B） | "**The Nightwatch 1642 Oil on canvas, 363 x 437 cm Rijksmuseum, Amsterdam**"；"What sets Rembrandt's group portrait apart from other comparable paintings is **his use of chiaroscuro as a dramatic device**." |

**四要素对位**：名称＝The Night Watch / The Nightwatch（①②同一作品，②注标题为 19 世纪误称）；地点＝阿姆斯特丹国立博物馆（①官方藏品号 SK-C-5、②直书 Rijksmuseum, Amsterdam）；设计者＝Rembrandt van Rijn（①②一致）；年份＝**1642（①②一致）**。
**独立性说明**：阿姆斯特丹国立博物馆（官方）与 Web Gallery of Art（独立艺术史数据库）为两个不同机构，均可读、正文直证，可作独立双源。
**手法贴合度**：①"used the light to focus on particular details"与②"chiaroscuro as a dramatic device"直接支撑"以明暗/值阶建立画面结构与焦点"——两源均直证明暗组织手法，贴合度高于其余三条；落笔可据实引用，无需附会。

## 三、汇总

| 条目 | 具名实例 | 地点 | 设计者 | 年份 | 主源①（官方） | 主源②（独立库） | HTTP | 判定 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `proportion` | 《维特鲁威人》 Vitruvian Man | 威尼斯学院美术馆 | Leonardo da Vinci | 约 1490（②记 1492；①无确切年） | gallerieaccademia.it 官方藏品页 | WGA `10anatom/1vitruviu.html` | 200 / 200 | **可用（年份口径须并列标注）** |
| `composition` | 《大碗岛的星期天下午》 A Sunday on La Grande Jatte | 芝加哥艺术博物馆 | Georges Seurat | 1884–1886 | api.artic.edu 官方馆藏 API | WGA `figures/jatte.html` | 200 / 200 | **可用** |
| `balance` | 《阿尔诺菲尼肖像》 The Arnolfini Portrait | 伦敦国家美术馆（NG186） | Jan van Eyck | 1434 | nationalgallery.org.uk 官方藏品页 | WGA `15arnolf/index.html` | 200 / 200 | **可用（"对称/均衡"为通识解读，源未直书）** |
| `value` | 《夜巡》 The Night Watch | 阿姆斯特丹国立博物馆（SK-C-5） | Rembrandt van Rijn | 1642 | rijksmuseum.nl 官方藏品页 | WGA `26group/05group.html` | 200 / 200 | **可用（明暗手法两源直证）** |

- **双源齐备率：4/4**；8 个来源全部 HTTP 200（其中 2 个 Cloudflare 站点经 `web_fetch` 服务端直读或官方 API 取证），**0 死链、0 编造、0 单源、0 不可得**。
- **机构独立性**：每条均为"官方博物馆 + Web Gallery of Art"两个不同机构，符合"同一机构只算 1 源"。
- **需落地时保留的诚实标注（3 处）**：
  1. `proportion`：年份写"约 1490（WGA 记 1492；馆方页未标确切年份）"，不冒称两源直书 1490。
  2. `composition`：概念定性"构图法则"两源未逐字讨论；官方源为博物馆 API（HTML 作品页被 Cloudflare 拦），如实标注。
  3. `balance`：两源未直书 "symmetry/balance"；均衡定性依据①"centre of the composition"＋②"double portrait" 的中央双人构图描写，属通识解读。
- **无需保留标注（1 处）**：`value` 两源直证用光聚焦与 chiaroscuro，贴合度充分。
- **未做之事**：本报告未修改任何条目数据或其它文件；四条 `sections.实例` 现状仍为"类型性描述"，须由 lead 按第一节"落地约束"另行改写并复跑 `tools/check.py`。

## 四、证据回执（verification-before-completion）

逐条 `norm(quote) in norm(page)` 子串回验结果（全部 FOUND 才写入正文）：

| 来源 | 回验句（缩写） | 结果 |
| --- | --- | --- |
| WGA Vitruv | "Vitruvian Man 1492 Pen, ink, watercolour and metalpoint on paper, 343 x 245 mm Gallerie dell'Accademia, Venice" | FOUND |
| Accademia 官方页 | "Autore: Leonardo da Vinci" / "Titolo: Studio di proporzioni del corpo noto come Uomo vitruviano" / "iscritta entro le forme assolute del cerchio e del quadrato" / "agli anni del soggiorno milanese" | FOUND（`web_fetch` 全文可见） |
| WGA Jatte | "A Sunday Afternoon on the Ile de la Grande Jatte 1884-86 Oil on canvas, 208 x 308 cm Art Institute, Chicago" | FOUND |
| ArtIC API | `"A Sunday on La Grande Jatte — 1884"` / `"Georges Seurat (French, 1859–1891)"` / `"1884–86, border added 1888–89"` / `"Helen Birch Bartlett Memorial Collection"` | FOUND（解析 JSON 后回验） |
| NG Arnolfini | "Jan van Eyck, 'The Arnolfini Portrait', 1434" / "A large round mirror hangs right in the centre of the composition" | FOUND |
| WGA Arnolfini | "Portrait of Giovanni Arnolfini and his Wife (1434)" / "now in the National Gallery, London" | FOUND |
| Rijksmuseum | "Rembrandt van Rijn, 1642" / "Rembrandt used the light to focus on particular details, like the captain" / "Object number SK-C-5" | FOUND |
| WGA Nightwatch | "The Nightwatch 1642 Oil on canvas, 363 x 437 cm Rijksmuseum, Amsterdam" / "his use of chiaroscuro as a dramatic device" | FOUND |

> 校验方法：UTF-8 解码 → 去 script/style/标签 → `html.unescape` → `norm()`（NFKC + 弯直引号/破折号/不间断空格归一 + 空白折叠 + 小写）→ 子串命中。原始 JSON 中的 `\u2013` 转义先经 `json.loads` 解析再回验。
