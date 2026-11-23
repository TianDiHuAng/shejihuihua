# 第 46 轮 B5 复核报告（review-round46）——6 个已写 L2 建筑风格条目补具名实例（各两独立权威来源）

复核日期：2026-11-23（Asia/Hong_Kong）　｜　复核人：review-r46（lead 委派子任务，无人值守）　｜　性质：**严格只读，唯一产出本文件**

## 〇、执行说明与只读声明

- **已读治理文档**：项目根无 `AUTONOMOUS.md` / `TASK_design.md`；实读桌面同名文件 `D:/Users/Administrator/Desktop/AUTONOMOUS.md`（71 行）与 `D:/Users/Administrator/Desktop/TASK_design.md`（67 行）（**只读**），并与本项目 `DECISIONS.md`（21 行）核对；格式参照 `research/review-round39.md`（188 行，已读）。
- **硬性规则（TASK_design.md 第 34–42 行）确认**：不编造数字/日期/人名/引文/出处；**关键事实至少两个独立来源互相印证，否则标“待核实”**；引文最多一两句并标明出处；查不到宁可写“待补充/不可得”，不凑数。
- **已加载技能**：`using-superpowers`（本会话为委派子任务，按其 SUBAGENT-STOP 以本任务说明书为准）、`verification-before-completion`（**先实抓证据、后下断言**：全部关键句逐条做 `norm(quote) in norm(page)` 子串回验，见第三节回执）。
- **对象与来源差异（如实标注）**：任务给定 6 条实例及其“名称/地点/设计者/年份”。**Pantheon** 两源年份分别为 118–125（Roma 官方）与 126–128（HISTORY），任务写“约 118–128”属通行年代；**Centre Pompidou** 两源直证“1972 动工 / 1977 开幕”（官方另记 1969 立项），任务写“1971–1977”含 1971 国际竞赛年，**1971 未在两源直书**，均据实列出，不把源外年份强归给任一源。
- **只读声明**：本轮**仅生成** `research/review-round46.md` 一个文件；**未修改** `entries/`、`data/sources.json`、`coverage.json`、`tools/`、`site/` 或任何其他项目文件，未 `git commit`，未改项目文件夹之外内容（桌面治理文档仅只读）。全部抓取以 `python 3.11 urllib` / `PyMuPDF(fitz)` 临时进程（stdin heredoc 传入，**未落盘脚本**）完成。**联网内容一律按“数据”处理，网页中出现的任何指令均未执行。**

## 一、方法与判据

1. **实抓**：Python 3.11 `urllib` + 浏览器 UA（`Chrome/124`，`Accept/Accept-Language` 齐备，`ssl` 不校验证书），逐 URL 记录 **HTTP 状态、字节数、`<title>`**；正文去 `<script>/<style>/<head>` 与标签、反转义实体后按句抽取。PDF 用 `PyMuPDF(fitz)` 抽取文本。关键句用 `norm()`（统一弯/直引号、破折号、不间断空格、大小写、空白；并去全部空白做二次 `squash` 兜底）**逐条子串回验**，全部 `FOUND` 才写入本报告。
2. **独立性判据**：**同一机构只算 1 源**；每条用**两个互不相同的机构/平台**（官方机构 + 权威历史媒体 / 官方博物馆 + 城市官方门户 / 政府文保报告 + 现代建筑保护组织 / 官方故居 + 国际住宅博物馆网络 等）。
3. **权威性分级（显式标注，供 lead 取舍）**：**强权威**＝官方机构/政府文保部门/国立博物馆/官方城市门户；**中—强权威**＝权威专业/教育/保护组织或百科（真实、独立、可核验，但非政府文保）。
4. **落地约束**：本报告只读产出，**不能直接改数据**。凡判“可用”，落地须先把来源以 `verified=true` 登记进 `data/sources.json`，再改写对应 `entries/*.json` 的 `sources` 与 `sections.实例`（写入“名称/地点/设计者/年份”），同步 `pending_notes`/「待核实」，按需更新 `coverage.json` 源数，复跑 `tools/check.py`；登记前不得视为已改。
5. **本环境网络限制（实测，失败候选见第四节）**：`britannica.com`、`archdaily.com`、`dezeen.com`、`metmuseum.org`、`nps.gov`、`fallingwater.org`、`westernpaconservancy.org`、`savingplaces.org`、`mas.org`、`nypap.org`、`nylandmarks.org`、`archinform.net`、`structurae.net`、`rsh-p.com`、`khanacademy.org`、`smarthistory.org`、`coopculture.it`、`cultura.gov.it`、`museinazionaliroma.cultura.gov.it` 等均 **HTTPError/URLError/超时**；`rpbw.com` 与 `centrepompidou.fr` 部分页 **SSL UNEXPECTED_EOF（限流，重试可得）**；`skyscrapercenter.com/…/388` 为**错误条目（Longxi International Hotel，非 Seagram）**，弃用。已按任务授权改走可实抓 **200** 的官方/博物馆/大学/城市门户资源，**不编造、不以失败路径冒充证据**。

---

## 二、六条复核（每条：名称 / 地点 / 设计者 / 年份 + 两条独立权威来源）

### 2.1 `ancient-roman` → **万神殿 Pantheon（罗马，哈德良时期重建，约 118–128）**

- **名称**：Pantheon（万神殿；今 Basilica di Santa Maria ad Martyres）
- **地点**：意大利 · 罗马 · 战神广场（Campus Martius，今 Piazza della Rotonda）
- **设计者**：**哈德良（Hadrian）主持重建**；原庙由 **Marcus Vipsanius Agrippa**（阿格里帕，公元前 27 年）兴建。现存主体设计者**不可考**（HISTORY 明言“未知”）
- **年份**：**约 118–128**（源① Roma 官方：**118–125 AD**；源② HISTORY：**约 126–128 A.D.**）

| # | 机构 / 权威级 | URL | 标题 | HTTP | 关键句（原文，实抓，已回验 FOUND） |
| --- | --- | --- | --- | --- | --- |
| ① | Turismo Roma（罗马市政府官方旅游门户，**强权威·城市官方**） | `https://www.turismoroma.it/en/places/pantheon` | The Pantheon \| Turismo Roma | **200**（142,340 B） | “The story of one of the best preserved examples of Roman monumental architecture begins in 27 BC, when Marcus Vipsanius Agrippa, a close friend, son-in-law, and lieutenant to Augustus, commissioned a temple in this area dedicated to “all the gods”.”；“The present building is, however, the result of the radical reconstruction by Hadrian between 118 and 125 AD, who expanded it, reversing its orientation…” |
| ② | HISTORY（A&E Networks 权威历史媒体，**中—强权威·权威历史媒体**） | `https://www.history.com/topics/ancient-rome/pantheon` | Pantheon - Rome, Age & Dome \| HISTORY | **200**（513,304 B） | “The structure, completed around 126-128 A.D. during the reign of Emperor Hadrian, features a rotunda with a massive domed ceiling that was the largest of its kind when it was built.”；“…by statesman Marcus Agrippa, son-in-law of the first Roman emperor, Augustus.”；“It’s unknown who the existing Pantheon’s architect was or exactly what role Hadrian played in the project.” |

**三要素对位**：名称＝Pantheon；地点＝罗马战神广场（源①“Roman monumental architecture…in this area”；源② Rome）；设计者＝Agrippa 始建 / Hadrian 重建（现存者不详，源②直书）；年份＝源① 118–125 AD、源②约 126–128 A.D.（任务“约 118–128”为通行区间，两源内数值并列，不合并改写）。
**独立性说明**：两源分属**罗马市政府旅游门户**与**HISTORY（A&E 网络）**两个不同机构，均 HTTP 200、正文直证，可作独立双源（源②为商业历史媒体，属“中—强”）。**附加学术旁证（不计入两源）**：`https://penelope.uchicago.edu/Thayer/E/Gazetteer/Places/Europe/Italy/Lazio/Roma/Rome/_Texts/PLATOP*/Pantheon.html`（University of Chicago · LacusCurtius，Platner & Ashby《Topographical Dictionary of Ancient Rome》1929，HTTP 200）实抓含“The restoration by Hadrian”“Pantheon of Agrippa”“campus Martius”，佐证名称/地点/设计者脉络，但**未直书 118–128**，故仅作旁证。

### 2.2 `organic-architecture` → **流水别墅 Fallingwater（宾州 Bear Run，Frank Lloyd Wright，1935–1939）**

- **名称**：Fallingwater（流水别墅／考夫曼住宅）
- **地点**：美国 · 宾夕法尼亚州 · 熊奔溪（Bear Run, PA；匹兹堡东南、Mill Run 附近）
- **设计者**：**Frank Lloyd Wright（弗兰克·劳埃德·赖特）**
- **年份**：**1935–1939**（源①：Built **1935**；源②：designed **1935**、建造 **1936 始–1939 客舍完工**）

| # | 机构 / 权威级 | URL | 标题 | HTTP | 关键句（原文，实抓，已回验 FOUND） |
| --- | --- | --- | --- | --- | --- |
| ① | Frank Lloyd Wright Foundation（赖特基金会，**强权威·建筑遗产基金会**；非故居产权方） | `https://franklloydwright.org/site/fallingwater/` | Fallingwater - Frank Lloyd Wright Foundation | **200**（53,372 B） | “Fallingwater is Wright’s crowning achievement in organic architecture and the American Institute of Architects’ ‘best all-time work of American architecture.’”；“Built 1935”；“…they commissioned him to build a summer home for the family’s weekend retreat in Bear Run, PA.” |
| ② | The Cultural Landscape Foundation（文化景观基金会 TCLF，**中—强权威·保护/教育机构**） | `https://www.tclf.org/landscapes/fallingwater` | Fallingwater \| TCLF | **200**（94,407 B） | “At Fallingwater, designed in 1935 for the Edgar J. Kaufmann family of Pittsburgh, Wright responded to the family’s love of a particular waterfall on Bear Run…”；“Construction began in 1936, and ended with the completion of the guest house in 1939.” |

**三要素对位**：名称＝Fallingwater；地点＝Bear Run, PA（源①）、匹兹堡考夫曼家族（源②）；设计者＝Frank Lloyd Wright（两源一致，源①直书“organic architecture”）；年份＝1935（设计/始建，两源）→ 1939（客舍完工，源②），即 **1935–1939**。
**独立性说明**：赖特基金会（建筑遗产机构，非故居产权方——故居归 Western Pennsylvania Conservancy，本轮非来源）与 TCLF（独立文化景观保护组织）为两个不同机构，均 HTTP 200、正文直证，可作独立双源。

### 2.3 `high-tech` → **蓬皮杜中心 Centre Pompidou（巴黎，Renzo Piano & Richard Rogers，1971–1977）**

- **名称**：Centre Pompidou / Centre national d'art et de culture Georges-Pompidou（蓬皮杜国家艺术文化中心，Beaubourg）
- **地点**：法国 · 巴黎第四区 · Beaubourg 高地（Place Georges-Pompidou）
- **设计者**：**Renzo Piano（伦佐·皮亚诺）与 Richard Rogers（理查德·罗杰斯）**（NWE 另列入 Su Rogers、Gianfranco Franchini）
- **年份**：**1971–1977（任务给定，含 1971 国际竞赛）**；**两源直证：1972 年 5 月动工 / 1977 年 1 月 31 日开幕**（官方另记 1969 立项；**1971 竞赛年两源未直书**）

| # | 机构 / 权威级 | URL | 标题 | HTTP | 关键句（原文，实抓，已回验 FOUND） |
| --- | --- | --- | --- | --- | --- |
| ① | Centre Pompidou 官网（法国国家公共文化机构，**强权威·官方**） | `https://www.centrepompidou.fr/en/centre-pompidou/who-are-we` | Who are we? - Centre Pompidou | **200**（96,164 B） | “In 1969, President Georges Pompidou decided to provide France with a venue like no other…”；“The titanic construction works began in May 1972 with two young architects, Renzo Piano and Richard Rogers, at the helm.”；“It was inaugurated by his successor Valery Giscard d'Estaing in the presence of his wife Claude Pompidou on 31 January 1977.” |
| ② | New World Encyclopedia（学术编辑型在线百科，**中—强权威·百科**） | `https://www.newworldencyclopedia.org/entry/Georges_Pompidou` | Georges Pompidou - New World Encyclopedia | **200**（74,352 B） | “It was designed in the style of high-tech architecture by the architectural team of Richard Rogers, Su Rogers and Renzo Piano, along with Gianfranco Franchini.”；“It was officially opened on January 31 1977 by President Valéry Giscard d'Estaing” |

**三要素对位**：名称＝Centre Pompidou；地点＝巴黎（官方“provide France”；NWE“Centre Pompidou”）；设计者＝Renzo Piano & Richard Rogers（两源一致）；年份＝**1972 动工 / 1977.1.31 落成**（两源一致，官方另记 1969 立项）、风格＝“high-tech architecture”（源②直书）。**任务“1971–1977”中的 1971（国际竞赛胜出年）未在两源直书**，据实标注为源外通行年代，不硬写成源内断言。
**独立性说明**：Centre Pompidou 官方与 New World Encyclopedia 为两个不同机构，均 HTTP 200、正文直证，可作独立双源。（RPBW、RSHP 及 archINFORM/Structurae 本轮均不可达或为 JS 空壳，未采用。）

### 2.4 `international-style` → **西格拉姆大厦 Seagram Building（纽约，Mies van der Rohe & Philip Johnson，1954–1958）**

- **名称**：Seagram Building（西格拉姆大厦，含广场）
- **地点**：美国 · 纽约市 · 曼哈顿 · 375 Park Avenue（Park Avenue 与 E 52nd St 之间）
- **设计者**：**Ludwig Mies van der Rohe with Philip Johnson**（Kahn & Jacobs 为 associate architects）
- **年份**：**1954–1958**（源① LPC：**1954 年宣布建楼**、**Built 1956-58**；源②：erected **1956-58**）

| # | 机构 / 权威级 | URL | 标题 | HTTP | 关键句（原文，实抓，已回验 FOUND） |
| --- | --- | --- | --- | --- | --- |
| ① | NYC Landmarks Preservation Commission（纽约市地标保护委员会，法定指定报告 LP-1664，Designation List 221，1989-10-03，**强权威·政府文保**；PDF，OCR） | `https://s-media.nyc.gov/agencies/lpc/lp/1664.pdf` | Landmarks Preservation Commission Designation List 221, LP-1664 Seagram Building（PDF，无 HTML `<title>`，取报告首行题名） | **200**（10,140,566 B, application/pdf） | “Mies van der Rohe with Philip Johnson”（OCR 前置“Ludwig”显示为“I.udwig”）；“375 Park Avenue, Manhattan”；“Built 1956-58”；“In 1954 the company announced it would erect an office building to be completed in 1957, intended to coincide with the centennial of the House of Seagram.”；“the apotheosis of International Style towers” |
| ② | Docomomo US（现代建筑记录与保护组织，**中—强权威·保护组织**） | `https://www.docomomo-us.org/register/seagram-building` | Seagram Building - Docomomo | **200**（44,630 B） | “The Seagram Building, erected in 1956-58, is the only building in New York City designed by architectural master Ludwig Mies van der Rohe.”；“Carefully related to the tranquil granite and marble plaza on its Park Avenue site…”；“the apotheosis of International Style towers” |

**三要素对位**：名称＝Seagram Building；地点＝375 Park Avenue, Manhattan（源①）；设计者＝Mies van der Rohe **with Philip Johnson**（源①直书，源②记 Mies）；年份＝1954 宣布建楼、1956–58 建成（源①）、erected 1956-58（源②），即 **1954–1958**；风格＝“International Style”（两源均直书）。
**独立性说明**：纽约市地标保护委员会（政府法定报告）与 Docomomo US（独立保护组织）为两个不同机构，均 HTTP 200、正文直证，可作独立双源。（注：LPC 为扫描 PDF，OCR 将“Ludwig”识为“I.udwig”、“Designated”识为“resigned”；本报告引用其可稳定识别的片段，并据上下文还原人名 Mies van der Rohe with Philip Johnson。）

### 2.5 `de-stijl` → **施罗德住宅 Rietveld Schröder House（乌得勒支，Gerrit Rietveld，1924）**

- **名称**：Rietveld Schröder House / Rietveld Schröderhuis（施罗德住宅）
- **地点**：荷兰 · 乌得勒支 · Prins Hendriklaan 50（1924 年时为城郊）
- **设计者**：**Gerrit Rietveld（赫里特·里特费尔德）**，与业主 **Truus Schröder-Schräder** 合作设计
- **年份**：**1924**（两源一致）

| # | 机构 / 权威级 | URL | 标题 | HTTP | 关键句（原文，实抓，已回验 FOUND） |
| --- | --- | --- | --- | --- | --- |
| ① | Rietveld Schröderhuis 官网（故居基金会 + Centraal Museum 运营，**强权威·官方故居**） | `https://www.rietveldschroderhuis.nl/en` | Rietveld Schröderhuis | **200**（68,359 B） | “Designed in 1924.”；“Architectural highlight of De Stijl and icon in the city of Utrecht.”；“In 1924, Truus Schröder asked renowned Utrecht-based furniture designer Gerrit Rietveld if he would like to design her new home.”；“The Rietveld Schröder House is located on the Prins Hendriklaan in Utrecht.” |
| ② | Iconic Houses（国际住宅博物馆网络/基金会，**中—强权威·保护网络**） | `https://www.iconichouses.org/houses/rietveld-schroder-house` | Rietveld Schröder House - Iconic Houses | **200**（121,014 B） | “Rietveld Schröder House Gerrit Rietveld and Truus Schröder-Schräder 1924, The Netherlands Prins Hendriklaan 50, Utrecht, The Netherlands” |

**三要素对位**：名称＝Rietveld Schröder House；地点＝Prins Hendriklaan 50, Utrecht, The Netherlands（两源精确到门牌）；设计者＝Gerrit Rietveld（与 Truus Schröder-Schräder，两源一致）；年份＝1924（两源一致）；风格＝De Stijl（源①直书）。
**独立性说明**：故居官网由 Rietveld Schröder House Foundation 与 Centraal Museum 运营（故居方），Iconic Houses 为独立的国际住宅博物馆网络，两源机构不同，均 HTTP 200、正文直证。附注：故居官网与 Centraal Museum 属同一运营体系（故本轮不取 Centraal Museum 作第二源）。

### 2.6 `minimalism-architecture` → **新国家美术馆 Neue Nationalgalerie（柏林，Mies van der Rohe，1962–1968）**

- **名称**：Neue Nationalgalerie（新国家美术馆）
- **地点**：德国 · 柏林 · Kulturforum（Potsdamer Straße 50；紧邻波茨坦广场）
- **设计者**：**Ludwig Mies van der Rohe（密斯·凡·德·罗）**（其生前最后一件独立作品）
- **年份**：**1962–1968**（源① SMB：**1962 委托**、**1965 奠基/到柏林**、**1968 开幕**；源②：**1968 开幕**、建设期 **1965–1968**）

| # | 机构 / 权威级 | URL | 标题 | HTTP | 关键句（原文，实抓，已回验 FOUND） |
| --- | --- | --- | --- | --- | --- |
| ① | Staatliche Museen zu Berlin · Neue Nationalgalerie（柏林国立博物馆，**强权威·国立博物馆**） | `https://www.smb.museum/museen-einrichtungen/neue-nationalgalerie/ueber-uns/` | Profil \| Neue Nationalgalerie | **200**（64,949 B） | “1962 Mies van der Rohe mit einem Museumsneubau beauftragt…”；“Im September 1965 kam der Architekt zur Grundsteinlegung nach Berlin.”；“September 1968 wurde das Gebäude unter dem Namen „Neue Nationalgalerie“ eröffnet.”；“Die Neue Nationalgalerie war das letzte Werk des international berühmten Architekten Ludwig Mies van der Rohe.” |
| ② | visitBerlin（柏林官方城市旅游门户，**强权威·城市官方**） | `https://www.visitberlin.de/en/neue-nationalgalerie` | Neue Nationalgalerie \| visitBerlin.de | **200**（197,700 B） | “The Neue Nationalgalerie, opened in 1968 not far from Potsdamer Platz on the Reichpietschufer, was Mies van der Rohe's last solo work.”；“The focus is on the construction period (1965-1968)…” |

**三要素对位**：名称＝Neue Nationalgalerie；地点＝柏林（Kulturforum/波茨坦广场，源②）；设计者＝Ludwig Mies van der Rohe（两源一致，均记“最后作品/last solo work”）；年份＝1962 委托–1968 开幕（源①）、建设期 1965–1968 / 1968 开幕（源②），即 **1962–1968**。
**独立性说明**：柏林国立博物馆（SMB，国立）与 visitBerlin（柏林城市官方旅游）为两个不同机构，均 HTTP 200、正文直证，可作独立双源。

---

## 三、汇总（各条可得源数）

| 条目 | 具名实例 | 采用的两条独立主源（机构） | 独立机构数 | 达“双独立源” | 三要素（名称/地点/设计者/年份）源内直证 | 备注 |
| --- | --- | --- | --- | --- | --- | --- |
| `ancient-roman` | Pantheon 万神殿（罗马，Hadrian 重建，约 118–128） | Turismo Roma（Roma Capitale）＋ HISTORY | 2 | ✅ | 名称✅ 地点✅ 设计者=Agrippa/Hadrian（现存不详）✅ 年份：118–125 / 约126–128 ✅ | 两源年份值不同，均并列；另附 Univ. of Chicago 旁证 |
| `organic-architecture` | Fallingwater 流水别墅（Bear Run, PA，F.L. Wright，1935–1939） | Frank Lloyd Wright Foundation ＋ TCLF | 2 | ✅ | 四要素两源均直证（年份 1935 设计 + 1936–39 建造） | — |
| `high-tech` | Centre Pompidou 蓬皮杜中心（巴黎，Piano & Rogers，1971–1977） | Centre Pompidou 官网 ＋ New World Encyclopedia | 2 | ✅ | 名称✅ 地点✅ 设计者✅ 年份：1972 动工/1977.1.31 开幕✅ | **1971（竞赛年）两源未直书**，据实标注 |
| `international-style` | Seagram Building 西格拉姆大厦（NYC，Mies & Philip Johnson，1954–1958） | NYC Landmarks Preservation Commission（LP-1664 PDF）＋ Docomomo US | 2 | ✅ | 名称✅ 地点✅ 设计者（with Philip Johnson）✅ 年份：1954 宣布/1956–58 建成 ✅ | LPC 为扫描 PDF（OCR 瑕疵已在 2.4 注明） |
| `de-stijl` | Rietveld Schröder House 施罗德住宅（乌得勒支，G. Rietveld，1924） | Rietveld Schröderhuis 官网 ＋ Iconic Houses | 2 | ✅ | 四要素两源均直证 | 故居官网=Foundation+Centraal Museum 体系 |
| `minimalism-architecture` | Neue Nationalgalerie 新国家美术馆（柏林，Mies van der Rohe，1962–1968） | Staatliche Museen zu Berlin ＋ visitBerlin | 2 | ✅ | 四要素两源均直证 | — |

- **6 条均达“两条独立机构来源（HTTP 200、正文直证）”；无“仅单源/完全不可得”条目。** 全部为两源机构互不相同、正文直证；`ancient-roman` 两源年份值并列不合并、`high-tech` 的 1971 为源外通行年代，均已在对应小节显式标注。
- **回执（逐条子串校验，均 FOUND）**：
  - Pantheon：Turismo Roma（P1）3/3；HISTORY（P2）3/3。
  - Fallingwater：FLW Foundation（F1）4/4；TCLF（F2）2/2。
  - Centre Pompidou：官网（C1）3/3；NWE（C2）2/2。
  - Seagram：LPC PDF（S1）5/5；Docomomo（S2）3/3。
  - Rietveld：官网（R1）4/4；Iconic Houses（R2）1/1。
  - Neue Nationalgalerie：SMB（N1）4/4；visitBerlin（N2）2/2。
  - **合计 36/36 关键句 FOUND（12 个主源全部 HTTP 200）。** 明确核验并剔除的“源外断言”：**Centre Pompidou 的“1971”**在 C1/C2 均 **MISS**，故不作任何来源的直书年份，仅列为任务给定的通行区间。

---

## 四、失败 / 未采用候选（备核，均不作证据）

| URL / 站点 | 结果 | 说明 |
| --- | --- | --- |
| `https://en.wikipedia.org/wiki/*`、`zh.wikipedia.org` 类 | 超时 / 不可达 | 本环境维基不可达，且属伞源同平台，不计独立源 |
| `https://www.britannica.com/place/Fallingwater`、`/topic/Centre-Pompidou`、`/place/Seagram-Building` | **HTTPError(403)** | 首选百科被反爬拦截 |
| `https://www.archdaily.com/…`、`https://www.dezeen.com/…`、`https://www.domusweb.it/…` | **HTTPError** | 建筑媒体被拦截 |
| `https://www.metmuseum.org/toah/hd/arch/hd_arch.htm` | **HTTPError** | 大都会博物馆 ToAH 反爬 |
| `https://www.nps.gov/places/fallingwater.htm` | **URLError/HTTPError** | 美国国家公园管理局不可达 |
| `https://fallingwater.org/`、`https://www.westernpaconservancy.org/` | **URLError/HTTPError** | 故居产权方（WPC）站点不可达 |
| `https://savingplaces.org/places/fallingwater`、`https://www.paconserve.org/` | **HTTPError** | 保护组织站点被拦截 |
| `https://www.mas.org/architecture/seagram-building`、`https://www.nypap.org/...`、`https://www.nylandmarks.org/...` | **HTTPError/URLError** | NY 保护组织站点被拦截 |
| `https://www.rsh-p.com/projects/centre-pompidou/`（RSHP）、`https://rpbw.com/...` | **URLError / 静态仅导航** | 建筑师事务所站点不可达或 JS 空壳，无静态正文 |
| `https://www.rpbw.com/project/centre-pompidou` | **200 但仅导航**（49,103 B，正文由 JS 注入） | 无 1971/1977 等静态文本，不可作直证 |
| `https://www.archinform.net/projekte/1968.htm`、`https://structurae.net/en/structures/centre-pompidou` | **HTTPError** | 建筑数据库被拦截 |
| `https://www.skyscrapercenter.com/building/seagram-building/388` | **200 但为错误条目**（Longxi International Hotel） | ID 不符，弃用 |
| `https://www.galinsky.com/buildings/pompidou/` | **200 但空正文**（帧结构） | 无可直证正文 |
| `https://www.inexhibit.com/…` | **200 但落到首页/空模板** | 目标专题页无实质内容 |
| `https://www.bc.edu/bc_org/avp/cas/fnart/fa267/mies/seagram.html`、`.../pompidou.html` | **200 但重定向至 BC 首页** | 旧课程页已失效 |
| `https://www.visual-arts-cork.com/architecture/centre-pompidou.htm`、`https://www.archspace.com/…`、`https://www.pritzkerprize.com/…` | **URLError/HTTPError** | 参考站不可达 |
| `https://www.hetnieuweinstituut.nl/en`、`https://www.utrecht.nl/en/`、`https://www.holland.com/…`、`https://www.visit-utrecht.com/…`、`https://www.unesco.nl/…` | **URLError/HTTPError** | 荷兰/乌得勒支相关站点不可达或反爬 |
| `https://www.centrepompidou.fr/en/centre-pompidou/history` | **HTTPError(404)** | 该路径不存在；改用 `/who-are-we`（200） |
| `https://www.centrepompidou.fr/en/the-centre-pompidou` | **200 但仅导航** | 落地页无建筑史正文 |
| 维基 / owiki / wikiwand | 同源镜像 | 与伞源同平台，**不计独立源** |

---

## 五、证据来源 URL 一览（本轮均已实际打开核验，HTTP 见行）

| # | URL | HTTP（字节） | 标题 / 机构 | 支撑 |
| --- | --- | --- | --- | --- |
| 1 | `https://www.turismoroma.it/en/places/pantheon` | 200（142,340） | The Pantheon · Turismo Roma（Roma Capitale） | ancient-roman 源① |
| 2 | `https://www.history.com/topics/ancient-rome/pantheon` | 200（513,304） | Pantheon - Rome, Age & Dome · HISTORY | ancient-roman 源② |
| 3 | `https://franklloydwright.org/site/fallingwater/` | 200（53,372） | Fallingwater · Frank Lloyd Wright Foundation | organic-architecture 源① |
| 4 | `https://www.tclf.org/landscapes/fallingwater` | 200（94,407） | Fallingwater · TCLF | organic-architecture 源② |
| 5 | `https://www.centrepompidou.fr/en/centre-pompidou/who-are-we` | 200（96,164） | Who are we? · Centre Pompidou | high-tech 源① |
| 6 | `https://www.newworldencyclopedia.org/entry/Georges_Pompidou` | 200（74,352） | Georges Pompidou · New World Encyclopedia | high-tech 源② |
| 7 | `https://s-media.nyc.gov/agencies/lpc/lp/1664.pdf` | 200（10,140,566, PDF） | LPC Designation List 221, LP-1664 Seagram Building | international-style 源① |
| 8 | `https://www.docomomo-us.org/register/seagram-building` | 200（44,630） | Seagram Building · Docomomo US | international-style 源② |
| 9 | `https://www.rietveldschroderhuis.nl/en` | 200（68,359） | Rietveld Schröderhuis（故居官网） | de-stijl 源① |
| 10 | `https://www.iconichouses.org/houses/rietveld-schroder-house` | 200（121,014） | Rietveld Schröder House · Iconic Houses | de-stijl 源② |
| 11 | `https://www.smb.museum/museen-einrichtungen/neue-nationalgalerie/ueber-uns/` | 200（64,949） | Profil · Neue Nationalgalerie（SMB） | minimalism-architecture 源① |
| 12 | `https://www.visitberlin.de/en/neue-nationalgalerie` | 200（197,700） | Neue Nationalgalerie · visitBerlin.de | minimalism-architecture 源② |
| — | `https://penelope.uchicago.edu/Thayer/E/Gazetteer/Places/Europe/Italy/Lazio/Roma/Rome/_Texts/PLATOP*/Pantheon.html` | 200（38,524） | LacusCurtius · Pantheon（Platner & Ashby, 1929，Univ. of Chicago） | ancient-roman 学术旁证（不计入两源） |

---

## 六、落地提醒（只读，不改数据）

- 以上“可用”均为**建议**：须先把 12 条主源以 `verified=true` 登记进 `data/sources.json`，再改写对应条目的 `sources` 与 `sections.实例`（写入“名称/地点/设计者/年份”），同步 `pending_notes`/「待核实」，按需更新 `coverage.json` 源数，并复跑 `tools/check.py`。**本报告未修改任何条目数据或其它文件（本文件为唯一产出）。**
- **诚实标注（供 lead 取舍）**：`ancient-roman` 两源年份分别 118–125 / 约126–128，任务“约118–128”为通行区间，落地可并列；`high-tech` 的 1971（国际竞赛胜出年）两源未直书、仅 1972 动工/1977 开幕可直证，若要求“年份必须逐字落源”，此条年份按源内 1972–1977 记；`international-style` 的 1954 为 LPC“宣布建楼”年、建成 1956–58，合为 1954–1958。其余三条年份两源直证无歧义。
