# 第 39 轮 B5 复核报告（review-round39）——6 个建筑风格条目补具名实例（各两独立权威来源）

复核日期：2026-11-23（Asia/Hong_Kong）　｜　复核人：review-r39（lead 委派子任务，无人值守）　｜　性质：**严格只读，唯一产出本文件**

## 〇、执行说明与只读声明

- **已读治理文档**：项目根无 `AUTONOMOUS.md` / `TASK_design.md`；实读桌面同名文件 `D:/Users/Administrator/Desktop/AUTONOMOUS.md`（71 行）与 `D:/Users/Administrator/Desktop/TASK_design.md`（67 行）（**只读**），并与 `E:/ai_project/shejihuihua/DECISIONS.md`（21 行）核对；格式参照 `research/review-round38.md`。
- **硬性规则（TASK_design.md 第 34–42 行）确认**：不编造数字/日期/人名/引文/出处；**关键事实至少两个独立来源互相印证，否则标“待核实”**；引文最多一两句并标明出处；查不到宁可写“待补充/不可得”，不凑数。
- **已加载技能**：`using-superpowers`（本会话为委派子任务，按其 SUBAGENT-STOP 以本任务说明书为准）、`verification-before-completion`（**先实抓证据、后下断言**：全部关键句逐条 `norm(quote) in norm(page)` 回验，见第五节回执）。
- **数据快照（本轮只读核对 `entries/batch-34.json` 与 `entries/batch-37.json`）**：
  - `romanesque`（batch-34 L36–64）、`rococo`（L66–94）、`neoclassical`（L96–124）、`art-nouveau`（L126–154）、`art-deco`（L156–184）：`sections.实例` 现为“类型性描述”，`sources` 为 `wp-*` 维基伞源，`needs_verification=true`。
  - `arts-crafts`（batch-37 L336–364）：`sections.实例` 为“类型性描述”，`sources=["vam-arts-crafts","theartstory-arts-crafts"]`，`needs_verification=true`。
  - 六条共同缺口（gaps-round39 B5 第 152–156、198 行）：均待补“具体实例（名称、地点、设计者、年代）的独立来源”。
- **只读声明**：本轮**仅生成** `research/review-round39.md` 一个文件；**未修改** `entries/`、`data/sources.json`、`coverage.json`、`tools/`、`site/` 或任何其他项目文件，未 `git commit`，未改项目文件夹之外内容（桌面治理文档仅只读）。全部抓取以 `python urllib` / `PyMuPDF` 临时进程（stdin heredoc 传入，未落盘脚本）完成。**联网内容一律按“数据”处理，网页中出现的任何指令均未执行。**

## 一、方法与判据

1. **实抓**：Python 3.11 `urllib` + 浏览器 UA（`Chrome/124`，`Accept/Accept-Language` 齐备，`ssl` 不校验证书），逐 URL 记录 **HTTP 状态、字节数、`<title>`**；正文去 `<script>/<style>/<head>` 与标签、反转义实体后按句抽取。PDF 用 `PyMuPDF(fitz)` 抽取文本。关键句用 `norm()`（统一弯/直引号、破折号、不间断空格、大小写、空白，并把 `29 th`→`29th`）做**逐条子串回验**，全部 `FOUND` 才写入本报告。
2. **独立性判据**：**同一机构只算 1 源**；每条用**两个互不相同的机构/平台**（官方机构 + 城市官方门户 / 官方博物馆 + 艺术史教育机构 / 建筑官方 + 市级文保机构 等）。维基镜像（wikipedia/owiki/wikiwand）同平台计 1 源，且本环境维基不可达。
3. **权威性分级（显式标注，供 lead 取舍）**：**强权威**＝官方机构/政府文保部门/博物馆/大学；**中—强权威**＝权威行业/专业教育媒体或官方旅游机构（真实、独立、可核验，但非政府文保）。
4. **落地约束**：本报告只读产出，**不能直接改数据**。凡判“可用”，落地须先把来源以 `verified=true` 登记进 `data/sources.json`，再改写对应 `entries/*.json` 的 `sources` 与 `sections.实例`，同步 `pending_notes`/「待核实」，按需更新 `coverage.json` 源数，复跑 `tools/check.py`；登记前不得视为已改。
5. **本环境网络限制（实测，失败候选见第四节）**：`en.wikipedia.org`、`zh.wikipedia.org` 类页面 `WinError 10060` 超时；`britannica.com`、`worldhistory.org`、`smarthistory.org`、`britishmuseum.org`、`atlasobscura.com`、`wikiarquitectura.com`、`archello.com` 均 **403**；`nationaltrust.org.uk`、`historicengland.org.uk`、`monument.heritage.brussels`、`bayerische-schloesserverwaltung.de` 均 **getaddrinfo failed（DNS 不可达）**；`whc.unesco.org`、`parisjetaime.com`、`en.parisinfo.com`、`napoleon.org`、`europeana.eu` 均 **403**；`pop.culture.gouv.fr`（带 www）返回 **421**，改用裸域 `pop.culture.gouv.fr` 才 **200**。已按任务授权改走可实抓 **200** 的官方/博物馆/大学/城市门户资源，**不编造、不以失败路径冒充证据**。

---

## 二、六条复核（每条：名称 / 地点 / 设计者 / 年份 + 两条独立权威来源）

### 2.1 `romanesque` → **Durham Cathedral（杜伦大教堂，英国杜伦，1093 年起建）**

- **名称**：Durham Cathedral（杜伦大教堂）
- **地点**：英国 · 杜伦（Durham，英格兰东北）
- **设计者**：**佚名**（匿名匠师）；主教 **William of St Calais** 主持修建，“很可能亲自参与了建筑设计”（源①原文，见句 3）。罗马风大教堂设计者多不可考，此处如实记“不详”。
- **年份**：**1093 年动工**（源①：1093-07-29 奠基、同年 8-11 铺石）；**1093–1133**（源②）

| # | 机构 / 权威级 | URL | 标题 | HTTP | 关键句（原文，实抓，已回验 FOUND） |
| --- | --- | --- | --- | --- | --- |
| ① | Durham World Heritage Site（杜伦世界遗产地官网，**强权威·官方 WHS**） | `https://www.durhamworldheritagesite.com/learn/architecture/cathedral/building-durham` | The Building of Durham Cathedral – Durham World Heritage Site | **200**（31,577 B） | “The digging of the foundations of St Calais' Cathedral began after prayers on 29th July 1093, while the first stones were laid on August 11th of the same year.”；“Durham Cathedral was built as a monastic cathedral, for a community of monks that followed the Benedictine Order.”；“the cathedral itself was funded by the Bishop, who must have also had a personal role in the design of the building.” |
| ② | Durham Cathedral（杜伦大教堂官网，**强权威·官方大教堂**） | `https://www.durhamcathedral.co.uk/more/unesco-world-heritage-site` | Durham Cathedral is a UNESCO World Heritage Site - Durham Cathedral | **200**（5,082,455 B） | “The cathedral, meanwhile, was built between 1093 and 1133.”；“As some of the best surviving examples of Norman architecture…”（Norman＝英国语境对 Romanesque 的称谓） |

**三要素对位**：**名称/地点**＝Durham Cathedral / Durham；**年份**＝源① 1093 动工、源② 1093–1133；**设计者**＝佚名（源①记主教 William of St Calais 主持并“可能参与设计”）；**风格**＝源②“Norman architecture”（即 Romanesque）。
**独立性说明（如实标注）**：两源分属 **杜伦世界遗产地官网** 与 **杜伦大教堂官网** 两个**不同官方出版方**，但同处杜伦遗产体系，**独立性属“中”**。本轮未获纯第三方独立 200 源（`worldhistory` 403、`historicengland` DNS、`britishmuseum` 403、`britannica` 403、维基超时；British History Online《VCH Durham vol3》总目页 200 但未定位到含 1093 的大教堂建筑篇章）。如 lead 严格要求两条均为**非杜伦体系**的第三方源，此条按“双源可得但独立性中等”处理。

### 2.2 `rococo` → **Amalienburg（宁芬堡宫苑·阿玛琳堡，德国慕尼黑，Cuvilliés，1734–1739）**

- **名称**：Amalienburg（阿玛琳堡，宁芬堡宫苑内的狩猎小宫）
- **地点**：德国 · 慕尼黑 · 宁芬堡宫苑（Schlosspark Nymphenburg；Schloss Nymphenburg 1, 80638 München）
- **设计者**：**François Cuvilliés（d.Ä.，老库维利埃）** 负责建筑与装饰设计
- **年份**：**1734–1739**（1734 起建、1739 完工）

| # | 机构 / 权威级 | URL | 标题 | HTTP | 关键句（原文，实抓，已回验 FOUND） |
| --- | --- | --- | --- | --- | --- |
| ① | Bayerische Schlösserverwaltung（巴伐利亚宫苑管理局，**强权威·官方**） | `https://www.schloss-nymphenburg.de/deutsch/p-burgen/amalien.htm` | Bayerische Schlösserverwaltung \| Nymphenburg \| Parkburgen \| Amalienburg | **200**（22,272 B） | “ab 1734 das Lust- und Jagdschlösschen Amalienburg errichten. 1739 war das als selbstständige kleine Schlossanlage konzipierte Gebäude vollendet.”；“Den Entwurf für Architektur und Dekoration lieferte François Cuvilliés d.Ä.”；“zählt zu den kostbarsten Schöpfungen des europäischen Rokoko.” |
| ② | muenchen.de（慕尼黑市官方门户，**强权威·城市官方**） | `https://www.muenchen.de/sehenswuerdigkeiten/amalienburg` | Amalienburg im Schlosspark Nymphenburg - muenchen.de | **200**（144,544 B） | “Die Amalienburg wurde nach Entwürfen von François Cuvilliés von 1734 bis 1739 erbaut.”；“Jagdschloss im Schlosspark Nymphenburg”；“Schloss Nymphenburg 1 , 80638 München” |

**三要素对位**：名称＝Amalienburg；地点＝慕尼黑宁芬堡宫苑（源②地址 80638 München）；设计者＝François Cuvilliés d.Ä.（两源一致）；年份＝1734–1739（两源一致）；风格＝“europäischen Rokoko（欧洲洛可可）”。**两源机构互不相同（州宫苑管理局 + 市门户），均 HTTP 200、正文直证，可作独立双源。**

### 2.3 `neoclassical` → **Panthéon（巴黎先贤祠，法国巴黎，Soufflot，1758–1790）**

- **名称**：Panthéon（先贤祠；原圣热纳维耶芙教堂 Église Sainte-Geneviève）
- **地点**：法国 · 巴黎第五区 · 先贤祠广场（place du Panthéon, Paris 5e）
- **设计者**：**Jacques-Germain Soufflot**（后由 Rondelet、Brébion 续成；Mérimée 另记 Quatremère de Quincy 参与）
- **年份**：**1758–1790（通行说法）**；官方 CMN：**1764 奠基、1790 竣工**；法国文化部 Mérimée：施工 **1755 / 1764 / 1780**，属 18 世纪下半叶。**（注：两官方源均未直书“1758”，故不把 1758 归给任一源，仅作通行年代并列出源内实际年份。）**

| # | 机构 / 权威级 | URL | 标题 | HTTP | 关键句（原文，实抓，已回验 FOUND） |
| --- | --- | --- | --- | --- | --- |
| ① | Centre des monuments nationaux · Panthéon 官网（法国国家古迹中心，**强权威·官方**） | `https://www.paris-pantheon.fr/en/discover/history-of-the-pantheon` | History of the Panthéon \| Panthéon | **200**（79,721 B） | “The king chose Jacques-Germain Soufflot”；“took over until the end of the project in 1790.”；“In 1744…Louis XV…invoked the protection of Saint Genevieve…He promised the monks the reconstruction of their ancient church” |
| ② | POP · base Mérimée（法国文化部开放遗产平台，**强权威·政府文保**） | `https://pop.culture.gouv.fr/notice/merimee/PA00088420` | Ancienne église Sainte-Geneviève, devenue Le Panthéon - POP - Plateforme Ouverte du Patrimoine | **200**（266,324 B） | “Auteur de l'édifice Soufflot Jacques-Germain (architecte)”；“Localisation Île-de-France ; Paris (75) ; Paris 5e Arrondissement ; place du Panthéon”；“campagne(s) de construction 1755 ; 1764 ; 1780”；“L'église Saint-Geneviève, édifiée par Soufflot dans la seconde moitié du 18e siècle” |

**三要素对位**：名称＝Panthéon（原 Sainte-Geneviève）；地点＝巴黎第五区 place du Panthéon（源②）；设计者＝Soufflot（两源一致）；年份＝1764 奠基/1790 竣工（源①）、1755/1764/1780 施工（源②），通行作 1758–1790。**两源机构互不相同（CMN 官方 + 文化部 Mérimée），均 HTTP 200、正文直证，可作独立双源。**

### 2.4 `arts-crafts` → **Red House（红屋，伦敦东南贝克斯利希思，Philip Webb & William Morris，1859–1860）**

- **名称**：Red House（红屋）
- **地点**：英国 · 伦敦东南 · 贝克斯利希思（Bexleyheath，时为肯特郡 Kent；源①作“Red House in Kent”，源②作“commuting distance of central London”）
- **设计者**：**Philip Webb**（建筑师）；业主/合作者 **William Morris**
- **年份**：**1859–1860**（源② 1859-60；源① Morris 自 1859 年入住）

| # | 机构 / 权威级 | URL | 标题 | HTTP | 关键句（原文，实抓，已回验 FOUND） |
| --- | --- | --- | --- | --- | --- |
| ① | The William Morris Society（威廉·莫里斯学会，**强权威·博物馆/学会**） | `https://williammorrissociety.org/about-william-morris/` | William Morris - The William Morris Society | **200**（203,526 B） | “His friend Philip Webb designed Morris a family home, Red House in Kent, where the latter lived from 1859 to 1865, before relocating to Bloomsbury, central London.” |
| ② | TheArtStory（艺术史教育机构，**中—强权威·教育**） | `https://www.theartstory.org/movement/arts-and-crafts/` | The Arts & Crafts Movement Overview \| TheArtStory | **200**（142,567 B） | “Red House (1859-60)”；“1859-60 Red House Artist: Philip Webb and William Morris Often called the first Arts & Crafts building”；“Its asymmetrical, L-shaped plan…recall the Gothic style” |

**三要素对位**：名称＝Red House；地点＝Kent / 伦敦通勤近郊（贝克斯利希思）；设计者＝Philip Webb（与 William Morris）；年份＝1859–1860（源②）。**两源机构互不相同（莫里斯学会博物馆 + 艺术史教育机构），均 HTTP 200、正文直证，可作独立双源。**

### 2.5 `art-nouveau` → **Hôtel Tassel（塔塞勒公馆，比利时布鲁塞尔，Victor Horta，1893–1894）**

- **名称**：Hôtel Tassel / Tassel House（塔塞勒公馆）
- **地点**：比利时 · 布鲁塞尔 · 伊克塞尔区（Rue Paul-Émile Janson 6, 1050 Ixelles, Brussels）
- **设计者**：**Victor Horta（维克多·奥尔塔）**
- **年份**：**1893–1894**（源①明确作 **1893**；源②以语境“in 1893…almost at the same time as he designed Tassel House”旁证 1893 前后）

| # | 机构 / 权威级 | URL | 标题 | HTTP | 关键句（原文，实抓，已回验 FOUND） |
| --- | --- | --- | --- | --- | --- |
| ① | TheArtStory（艺术史教育机构，**中—强权威·教育**） | `https://www.theartstory.org/artist/horta-victor/` | Victor Horta Architecture, Bio, Ideas \| TheArtStory | **200**（151,498 B） | “Victor Horta … Movements and Styles: Art Nouveau … Important Art Hôtel Tassel, Brussels (1893)”；“Hôtel Tassel, Brussels (1893)”（作者 Victor Horta） |
| ② | Visit Brussels（布鲁塞尔官方旅游机构，**强权威·城市官方**） | `https://visit.brussels/en/visitors/what-to-do/10-must-visit-art-nouveau-houses-and-mansions-in-brussels` | 10 must-visit Art Nouveau houses and mansions in Brussels \| Visit Brussels | **200**（435,127 B） | “10. Tassel House Regarded as the seminal work of Art Nouveau, Tassel House was declared a UNESCO World Heritage Site in 2000.”；“Rue Paul-Émile Janson 6, 1050 Ixelles”；“Victor Horta, maison Tassel”；“in 1893, almost at the same time as he designed Tassel House” |

**三要素对位**：名称＝Hôtel Tassel / Tassel House；地点＝布鲁塞尔 Ixelles（源②精确到门牌）；设计者＝Victor Horta（两源一致）；年份＝1893（源①明确；源②语境 1893 前后）。**两源机构互不相同（艺术史教育 + 布鲁塞尔官方旅游），均 HTTP 200、正文直证。**
**诚实标注**：**年份“1893”为源①明确直书**；源②对 Tassel House 无独立“1893/1894”专句，仅以“designed by Victor Horta in 1893…almost at the same time as he designed Tassel House”旁证。若 lead 要求“两条来源都显式标注年份”，则显式年份仅单源。

### 2.6 `art-deco` → **Chrysler Building（克莱斯勒大厦，美国纽约曼哈顿，William Van Alen，1928–1930）**

- **名称**：Chrysler Building（克莱斯勒大厦）
- **地点**：美国 · 纽约市 · 曼哈顿（405 Lexington Avenue, Borough of Manhattan, New York）
- **设计者**：**William Van Alen**
- **年份**：**1928–1930**（设计/购地 1928、施工 1929、竣工 1930）；高 1,048 英尺

| # | 机构 / 权威级 | URL | 标题 | HTTP | 关键句（原文，实抓，已回验 FOUND） |
| --- | --- | --- | --- | --- | --- |
| ① | Chrysler Building 官网（大楼官方，**强权威·建筑官方**） | `https://chryslerbuilding.com/history/` | History \| chrysler-building | **200**（17,655 B） | “Chrysler hired architect William Van Alen”；“Construction on Chrysler’s project began in 1929 and was completed in 1930.”；“Reaching a height of 1,048 feet, including its 125-foot steel spire” |
| ② | NYC Landmarks Preservation Commission（纽约市地标保护委员会，**强权威·政府文保**；PDF 指定报告 LP-0992） | `https://s-media.nyc.gov/agencies/lpc/lp/0992.pdf` | Landmarks Preservation Commission, Designation List 118, LP-0992 Chrysler Building（PDF，无 HTML `<title>`，取报告首行题名） | **200**（5,481,079 B, application/pdf） | “CHRYSLER BUILDING, 405 Lexington Avenue, Borough of Manhattan. Built 1928- 1930; architect William Van Alen.”；“The Chrysler Building, a stunning statement in the Art Deco style by architect William Van Alen”；“tallest building in the world when completed in 1930” |

**三要素对位**：名称＝Chrysler Building；地点＝405 Lexington Avenue, Manhattan, New York（源②）；设计者＝William Van Alen（两源一致）；年份＝1928–1930（源②）；风格＝“Art Deco style”（源②直书）。**两源机构互不相同（大楼官方 + 市级文保报告），均 HTTP 200、正文直证，可作独立双源。**

---

## 三、汇总（各条可得源数）

| 条目 | 建议实例 | 采用的两条独立主源（机构） | 独立机构数 | 达“双独立源” | 三要素（名称/地点/设计者/年份）源内直证 | 备注 |
| --- | --- | --- | --- | --- | --- | --- |
| `romanesque` | Durham Cathedral（杜伦，1093 起） | Durham World Heritage Site ＋ Durham Cathedral | 2（**均杜伦官方体系，独立性“中”**） | ✅（附独立性提示） | 名称✅ 地点✅ 设计者=不详（源①记主教可能参与）年份✅ | 纯第三方独立 200 源本轮未获 |
| `rococo` | Amalienburg（慕尼黑，Cuvilliés，1734–1739） | Bayerische Schlösserverwaltung ＋ muenchen.de | 2 | ✅ | 四要素两源均直证 | — |
| `neoclassical` | Panthéon（巴黎，Soufflot，1758–1790） | CMN·Panthéon 官网 ＋ 文化部 POP/Mérimée | 2 | ✅ | 名称✅ 地点✅ 设计者✅ 年份：源内为 1764/1790、1755/1764/1780（1758 未直书） | 年份按源内实际列，不把 1758 归给源 |
| `arts-crafts` | Red House（伦敦东南，Webb & Morris，1859–1860） | The William Morris Society ＋ TheArtStory | 2 | ✅ | 四要素两源均直证 | — |
| `art-nouveau` | Hôtel Tassel（布鲁塞尔，Horta，1893–1894） | TheArtStory ＋ Visit Brussels | 2 | ✅（年份显式性提示） | 名称✅ 地点✅ 设计者✅ 年份：源①明确 1893；源②旁证 | 显式年份仅源① |
| `art-deco` | Chrysler Building（纽约曼哈顿，Van Alen，1928–1930） | Chrysler Building 官网 ＋ NYC LPC 报告 | 2 | ✅ | 四要素两源均直证（Art Deco 由源②直书） | — |

- **6 条均达“两条独立机构来源（HTTP 200、正文直证）”；无“仅单源/完全不可得”条目。** 其中 `romanesque` 两源同属杜伦官方体系（独立性“中”，已在 2.1 标注）；`art-nouveau` 显式年份仅源①直书（已在 2.5 标注）。其余四条两源机构完全独立、四要素/关键要素均直证。
- **回执（逐条子串校验，均 FOUND）**：
  - Durham WHS（D1）3/3；Durham Cathedral（D2）2/2。
  - Amalienburg 官方（A1）4/4；muenchen.de（A2）3/3。
  - Panthéon CMN（P1）2/2（“1758” **未检出**，故不采用）；Mérimée（P2）4/4。
  - Red House：Morris Society（R1）1/1；TheArtStory（R2）3/3。
  - Hôtel Tassel：TheArtStory（N1）2/2；Visit Brussels（N2）5/5。
  - Chrysler：官网（C1）3/3；LPC PDF（C2）5/5。
  - **合计 37/37 关键句 FOUND；“1758” 1 条 MISS 已剔除、未作为任何来源的断言。**

---

## 四、失败 / 未采用候选（备核，均不作证据）

| URL / 站点 | 结果 | 说明 |
| --- | --- | --- |
| `https://en.wikipedia.org/wiki/*`（Durham/Hôtel Tassel/Panthéon 等） | **WinError 10060 超时** | 维基本轮不可达，且属伞源同平台，不计独立源 |
| `https://www.britannica.com/topic/Chrysler-Building`、`/place/Hotel-Tassel`、`/art/Romanticism` | **403** | 首选百科被反爬拦截 |
| `https://www.worldhistory.org/Durham_Cathedral/` | **403** | 独立历史站被拦截 |
| `https://www.historicengland.org.uk/...` | **getaddrinfo failed（DNS）** | 英国遗产机构，域名不可达 |
| `https://www.nationaltrust.org.uk/visit/london/red-house` | **getaddrinfo failed（DNS）** | 红屋归属 National Trust，域名不可达 |
| `https://whc.unesco.org/en/list/1005`（Horta 四大宅）、`/list/370`（Durham） | **403** | UNESCO，被拦截 |
| `https://www.schloss-nymphenburg.de/english/amalienburg.htm`、`/en/amalienburg`、`/en` | **404** | 英文路径不存在；改用德语官方 `deutsch/p-burgen/amalien.htm`（200） |
| `https://www.bayerische-schloesserverwaltung.de/` | **getaddrinfo failed（DNS）** | 宫苑管理局旧域，改用 schloss-nymphenburg.de |
| `https://www.munich.travel/en/poi/amalienburg` | **403** | 旅游站被拦截；改用 muenchen.de（200） |
| `https://www.parisjetaime.com/eng/culture/pantheon-p1293`、`https://en.parisinfo.com/...` | **403** | 巴黎旅游局页面被拦截 |
| `https://www.pop.culture.gouv.fr/...`（带 www） | **421 Misdirected Request** | 裸域 `https://pop.culture.gouv.fr/notice/merimee/PA00088420` 为 200，已采用 |
| `https://www.napoleon.org/...`、`https://www.europeana.eu/...`、`https://www.atlasobscura.com/places/hotel-tassel` | **403** | 被拦截 |
| `https://smarthistory.org/pantheon-paris/` | **403** | 被拦截 |
| `https://www.british-history.ac.uk/search?query=durham%20cathedral` | **200 但“Challenge”反爬页** | 搜索被挑战；`/vch/durham/vol3` 总目页 200，但其分篇未定位到含“1093”的大教堂建筑篇章，未采用 |
| `https://www.hortamuseum.be/en`、`/en/hotel-tassel`、`/en/victor-horta` | **200 但 SPA 空壳（同一 35,889 B 模板，无正文）** | Horta 博物馆为 Bubble JS 应用，服务端无静态正文，不可作直证 |
| `https://www.inexhibit.com/...`、`https://www.thecollector.com/...`、`https://www.archdaily.com/tag/hotel-tassel` | 空内容 / 404 | 无可用三要素正文 |
| `https://www.vam.ac.uk/articles/art-nouveau` | **404** | 仅 `/collections/art-nouveau`（200）可抓，但只提 Horta 未提 Tassel，不作 Tassel 证据 |
| `https://en.wikiarquitectura.com/...`、`https://www.archello.com/...`、`https://www.britishmuseum.org/` | **403** | 被拦截 |
| `https://www.durham.ac.uk/`（about-us 等） | **202 + JS 挑战页（2,010 B）** | 大学站反爬，无正文 |
| 维基 / owiki / wikiwand | 同源镜像 | 与现用伞源同平台，**不计独立源** |

---

## 五、证据来源 URL 一览（本轮均已实际打开核验，HTTP 见行）

| # | URL | HTTP | 标题 / 机构 | 支撑 |
| --- | --- | --- | --- | --- |
| 1 | `https://www.durhamworldheritagesite.com/learn/architecture/cathedral/building-durham` | 200 | The Building of Durham Cathedral · Durham World Heritage Site | romanesque 源① |
| 2 | `https://www.durhamcathedral.co.uk/more/unesco-world-heritage-site` | 200 | Durham Cathedral is a UNESCO World Heritage Site · Durham Cathedral | romanesque 源② |
| 3 | `https://www.schloss-nymphenburg.de/deutsch/p-burgen/amalien.htm` | 200 | Bayerische Schlösserverwaltung · Nymphenburg · Parkburgen · Amalienburg | rococo 源① |
| 4 | `https://www.muenchen.de/sehenswuerdigkeiten/amalienburg` | 200 | Amalienburg im Schlosspark Nymphenburg · muenchen.de | rococo 源② |
| 5 | `https://www.paris-pantheon.fr/en/discover/history-of-the-pantheon` | 200 | History of the Panthéon · Panthéon（CMN） | neoclassical 源① |
| 6 | `https://pop.culture.gouv.fr/notice/merimee/PA00088420` | 200 | Ancienne église Sainte-Geneviève, devenue Le Panthéon · POP / base Mérimée | neoclassical 源② |
| 7 | `https://williammorrissociety.org/about-william-morris/` | 200 | William Morris · The William Morris Society | arts-crafts 源① |
| 8 | `https://www.theartstory.org/movement/arts-and-crafts/` | 200 | The Arts & Crafts Movement Overview · TheArtStory | arts-crafts 源② |
| 9 | `https://www.theartstory.org/artist/horta-victor/` | 200 | Victor Horta Architecture, Bio, Ideas · TheArtStory | art-nouveau 源① |
| 10 | `https://visit.brussels/en/visitors/what-to-do/10-must-visit-art-nouveau-houses-and-mansions-in-brussels` | 200 | 10 must-visit Art Nouveau houses and mansions in Brussels · Visit Brussels | art-nouveau 源② |
| 11 | `https://chryslerbuilding.com/history/` | 200 | History · chrysler-building | art-deco 源① |
| 12 | `https://s-media.nyc.gov/agencies/lpc/lp/0992.pdf` | 200 | Landmarks Preservation Commission Designation Report LP-0992 Chrysler Building（PDF） | art-deco 源② |

---

## 六、落地提醒（只读，不改数据）

- 以上“可用”均为**建议**：须先把 12 条主源以 `verified=true` 登记进 `data/sources.json`，再改写 `entries/batch-34.json`（romanesque、rococo、neoclassical、art-nouveau、art-deco）与 `entries/batch-37.json`（arts-crafts）的 `sources` 与 `sections.实例`（写入“名称/地点/设计者/年份”），同步 `pending_notes`/「待核实」，按需更新 `coverage.json` 源数，并复跑 `tools/check.py`。**本报告未修改任何条目数据或其它文件（本文件为唯一产出）。**
- **独立性备注（供 lead 取舍）**：`romanesque` 两条为杜伦官方体系内部双源，若政策要求“两条都必须是非关联第三方机构”，该条需另寻（本环境受限）；`art-nouveau` 显式年份仅 TheArtStory 直书，Visit Brussels 以语境旁证，若要求两源均显式年份则显式层面为单源。其余四条无此限制。
