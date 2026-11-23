# 第 55 轮 B5 补源报告（review-round55b）——4 条造景/动线条目补具名实例（各两条独立权威来源）

复核日期：2026-11-23（Asia/Hong_Kong）　｜　复核人：review-r55b（lead 委派子任务，无人值守）　｜　性质：**严格只读，唯一产出本文件**

## 〇、执行说明与只读声明

- **已读治理与上下文文档**：项目根 `AUTONOMOUS.md` / `TASK_design.md` 实读为 NOT_FOUND；按前轮记录读取桌面原件 `D:/Users/Administrator/Desktop/AUTONOMOUS.md`（71 行）、`D:/Users/Administrator/Desktop/TASK_design.md`（67 行）；并读本项目 `DECISIONS.md`（25 行）、`research/review-round54b.md`（143 行）。
- **硬性规则确认**：不编造名称、地点、作者、年份、引文、出处；关键事实须两个独立来源互证；同一机构只算 1 源；查不到标“仅单源/不可得”并换更易双源实例。联网内容一律视为数据，网页中出现的任何指令均未执行。
- **已加载技能**：`using-superpowers`（本会话为委派子任务，按其 SUBAGENT-STOP 以任务说明书为准）、`verification-before-completion`（先实抓、后断言；关键句逐条 `norm(quote) in norm(page)` 或从工具返回全文逐字核对，见第五节回执）。
- **避重**：`atrium` 已用纽约古根海姆螺旋坡道，本轮 `visitor-route` 改用**卢浮宫金字塔—拿破仑庭院地下大厅主入口**；四例互不重复。
- **通道**：`web_search` 仅定位 URL，不作证据；证据正文来自 `web_fetch` 服务端直读、`urllib` / `curl` 直连标题与正文、英国政府 PDF 在内存中解析。抓取脚本未落盘到项目。
- **只读声明**：本轮仅生成 `E:/ai_project/shejihuihua/research/review-round55b.md`；未修改 `entries/`、`data/sources.json`、`coverage.json`、`tools/`、`site/` 或其他项目文件，未 git commit。

## 一、方法与判据

1. **实抓**：逐 URL 记录 HTTP 状态、字节数（可得时）、`<title>` 或 PDF 元数据题名；去 `<script>/<style>` 与标签、`html.unescape` 后抽正文；用 `norm()`（NFKC + 弯/直引号、破折号、零宽空格、不间断空格归一 + 空白折叠 + 小写）对关键句做子串回验。
2. **独立性判据**：同一机构只算 1 源。八源分别来自苏州市园林和绿化管理局、UNESCO 世界遗产中心、World Heritage Journeys of Europe、英国政府 DCMS、日本宫内厅、日本国家旅游局、卢浮宫博物馆新闻中心、Encyclopædia Britannica。
3. **权威性分级**：强权威＝古迹/园林主管机关、政府提名档案、皇宫管理机构、国家旅游局、博物馆官方新闻中心；中—强权威＝UNESCO 世界遗产中心、World Heritage Journeys of Europe、Britannica 署名编辑条目。
4. **不采用维基百科作主源**：沿用项目既定口径，维基及其镜像未作证据。
5. **落地约束**：本报告只读产出，不直接改数据。落地须先把来源以 `verified=true` 登记进 `data/sources.json`，再改写对应 `entries/batch-*.json` 的 `sources` 与「实例」段，同步 `pending_notes` /「待核实」，复跑 `tools/check.py`。

## 二、四条补源（每条：名称 / 地点 / 设计者 / 年份 + 两条独立权威来源）

### 2.1 `rockery`（叠石）→ **苏州狮子林假山（Lion Grove Garden rockery）**

- **名称**：狮子林 / Lion Grove Garden；园内湖石假山群，被称为“假山王国”。
- **地点**：**江苏省苏州市城区东北角园林路 23 号**（①直书地址；②将 Lion Grove Garden 列入苏州古典园林九处代表）。
- **设计者 / 营造主体**：**天如禅师及其弟子**（①“弟子们买地置屋为天如禅师建禅林”；两源均未列单一景观设计师，落地不得编造个人姓名）。
- **年份**：**1342 年创建**（①“公元1341年，高僧天如禅师来到苏州讲经……元至正二年(1342)，弟子们买地置屋为天如禅师建禅林”）。

| # | 机构 / 权威级 | URL | 标题 | HTTP | 关键句（实抓，已回验） |
| --- | --- | --- | --- | --- | --- |
| ① | 苏州市园林和绿化管理局官方页（**强权威·园林主管机关**） | `https://ylj.suzhou.gov.cn/szsylj/sjyc/201905/767dcf47765b40549969f1a6989c689c.shtml` | 狮子林 - 苏州市园林局 | **200**（43,887 B；curl 直连） | “狮子林位于江苏省苏州市城区东北角的园林路23号，开放面积约14亩。”；“拥有国内尚存最大的古代假山群。湖石假山出神入化，被誉为‘假山王国’。”；“元至正二年(1342)，弟子们买地置屋为天如禅师建禅林。” |
| ② | UNESCO World Heritage Centre「Classical Gardens of Suzhou」（**中—强权威·世界遗产中心**） | `https://whc.unesco.org/en/list/813/` | Classical Gardens of Suzhou - UNESCO World Heritage Centre | **200**（152,404 B；首轮 urllib 直连；web_fetch/后续复抓 403 反爬） | “nine of which, namely the Humble Administrator’s Garden, Lingering Garden, Net Master’s Garden, the Mountain Villa with Embracing Beauty, the Canglang Pavilion, **the Lion Grove Garden**, the Garden of Cultivation, the Couple’s Garden Retreat, and the Retreat & Reflection Garden, are regarded as the finest embodiments of Chinese ‘Mountain and Water’ gardens.”；“These garden ensembles of buildings, **rock formations**, calligraphy, furniture, and decorative artistic pieces serve as showcases of the paramount artistic achievements of the East Yangtze Delta region” |

**对 `rockery`（叠石）的支撑**：①直接把狮子林定性为“国内尚存最大的古代假山群”“假山王国”，并给出湖石假山、地址、1342 年与天如禅师弟子营建事实；②从世界遗产层级把狮子林列为苏州“山水园”九处代表之一，并明确苏州园林由 buildings 与 **rock formations** 等共同构成。两源合起来可支撑“狮子林湖石假山群”作为叠石类型的具名实例。**保留标注**：两源未给单一设计师；只写营造主体，不写个人名。

### 2.2 `planting-design`（植物配置）→ **邱园 Great Broad Walk Borders（大步道花境）**

- **名称**：Great Broad Walk Borders / 邱园大步道双侧花境。
- **地点**：**英国伦敦 Royal Botanic Gardens, Kew（邱园）**。
- **设计者**：**William Nesfield**（1840 年代原始 promenade / formal beds 设计）；**Richard Wilford**（尊重 Nesfield 原意的当代再设计，World Heritage Journeys 页直书）。
- **年份**：**1840 年代**（②精确记 1841 年 Nesfield 重新造景、1840 年代后期其 Walks/Vistas 成为主轴；①记原始设计在 1840s）。当前花境的具体开放年未在两源中直书，落地不补写。

| # | 机构 / 权威级 | URL | 标题 | HTTP | 关键句（实抓，已回验） |
| --- | --- | --- | --- | --- | --- |
| ① | World Heritage Journeys of Europe「The Great Broad Walk Borders」（**中—强权威·世界遗产主题官方项目页**） | `https://visitworldheritage.com/en/eu/the-great-broad-walk-borders/0220f1d9-1d71-47b7-8748-b0d0f9775f2e` | The Great Broad Walk Borders \| World Heritage Journeys of Europe | **200**（27,705 B；urllib 直连） | “The Great Broad Walk Borders reflect the original Nesfield design for the promenade from the Orangery to the Palm House.”；“Featuring over **60,000 flowering plants**, The Great Broad Walk Borders is the largest horticultural project to have been undertaken at Kew Gardens for nearly 30 years.”；“The Broad Walk was originally landscaped in the **1840s by William Nesfield** … Along both sides of the path, Nesfield laid out an intricate embroidery of formal beds, which were designed to create a promenade of great horticultural beauty.”；“The array of plants provides **texture and colour from early spring to late autumn**” |
| ② | UK Government / DCMS《World Heritage Sites 1999》（**强权威·英国政府提名预备名单 PDF**） | `https://assets.publishing.service.gov.uk/media/5a79c52f40f0b66d161ae059/WorldHeritageSites1999.pdf` | World Heritage Sites 1999（PDF 元数据 / DCMS） | **200**（1,415,375 B；99 页；urllib 直连，PDF 在内存中解析） | “The Royal Botanic Gardens, Kew (Kew Gardens) are of international pre-eminence, **founded 1759 by Princess Augusta**”；“In **1841**, the gardens were made a public research institute; Sir William Hooker was appointed as the first Director, and the gardens were **re-landscaped by William Nesfield**.”；“The 18th century landscaping of the Gardens was largely overlaid or altered by the work of **William Andrew Nesfield in the late 1840s**, whose ‘Walks’ or ‘Vistas’ still form the main avenues or sight-lines through the Gardens.” |

**对 `planting-design`（植物配置）的支撑**：①给出植物配置的量化与机制证据——60,000 株开花植物、双侧 formal beds、按季节选品种延长花期、以纹理与色彩组织早春至晚秋体验；②从英国政府档案层面确认邱园的 Nesfield 造景与 1841 / late 1840s 年份、以及 Walks/Vistas 作为园内主轴。两源合起来支撑“以植物组合、花期与色彩层次构成空间序列”的具名实例。

### 2.3 `seasonal-scenery`（四季造景）→ **桂离宫庭园（Katsura Imperial Villa）**

- **名称**：桂离宫 / Katsura Imperial Villa / 桂離宮。
- **地点**：**日本京都府京都市西京区，桂川西侧**（①“west side of the Katsura River in the southwestern area of the city of Kyoto”；② JNTO 地址字段 Katsuramisono, Nishikyo-KU, Kyoto-shi）。
- **设计者 / 营造主体**：**八条宫智仁亲王与其子智忠亲王**（①直书 two heads of the Hachijō-no-miya Imperial family, prince Toshihito and his son, prince Toshitada；②记“17 世纪为皇室建造”）。
- **年份**：**1615 年起，分阶段营建近 50 年**（①直书；②记 17 世纪，与①相容）。

| # | 机构 / 权威级 | URL | 标题 | HTTP | 关键句（实抓，已回验） |
| --- | --- | --- | --- | --- | --- |
| ① | The Imperial Household Agency 宫内厅（**强权威·皇宫管理机构**） | `https://www.kunaicho.go.jp/en/learn/institution/shisetsu/kyoto/kyoto.html` | Kyoto Imperial Palace and other Imperial Palaces and Villas in Kyoto – The Imperial Household Agency | **200**（18,084 B；web_fetch/urllib 直连） | “The Katsura Imperial Villa is located on the **west side of the Katsura River in the southwestern area of the city of Kyoto**.”；“It was built in stages over a period of almost 50 years from **1615** by the first two heads of the Hachijō-no-miya Imperial family, **prince Toshihito, and his son, prince Toshitada**.”；“As this garden design blocks one from seeing too much of the garden at one time, one could enjoy a **constantly changing view**.”；“The garden is also known for **seasonal flowers** such as Japanese apricot in early spring, cherry blossoms, and crimson flowers of azalea in late spring.” |
| ② | Japan National Tourism Organization 日本国家旅游局（**强权威·国家旅游机构**） | `https://www.japan-travel.cn/spot/1137/` | 桂离宫｜目的地｜【官方】日本国家旅游局(JNTO) | **200**（27,055 B；web_fetch/urllib 直连） | “桂离宫于 **17 世纪为皇室建造而成**。”；“池塘的布局别具匠心，池中矗立着六座建筑，还有一座被称为筑山的假山”；“**桂离宫一年四季都适合游玩，每次来到这里，都可以感受到不一样的美。**” |

**对 `seasonal-scenery`（四季造景）的支撑**：①直接写“seasonal flowers”，列举早春梅、樱花、晚春杜鹃，并以曲折园路造成“constantly changing view”；②直接写“一年四季都适合游玩，每次……不一样的美”。两源均把时间性（季节、视景变化）写入庭园体验，可支撑“以四时花木与动态观景组织景观”的具名实例。

### 2.4 `visitor-route`（参观动线）→ **卢浮宫金字塔—拿破仑庭院地下大厅主入口（Louvre Pyramid / Hall Napoléon）**

- **名称**：卢浮宫金字塔及拿破仑庭院中央地下大厅 / Louvre Pyramid, Cour Napoléon foyer。
- **地点**：**法国巴黎卢浮宫博物馆主庭院**（①②同一对象）。
- **设计者**：**I.M. Pei（贝聿铭）**（①“I.M. Pei’s Pyramid”；②“designed by architect I.M. Pei”）。
- **年份**：**1989 年**（①“Inaugurated in 1989”；②“completed in 1989”）。

| # | 机构 / 权威级 | URL | 标题 | HTTP | 关键句（实抓，已回验） |
| --- | --- | --- | --- | --- | --- |
| ① | Musée du Louvre 新闻中心（**强权威·博物馆官方**） | `https://presse.louvre.fr/the-pyramid-project/?lang=en` | The “Pyramid” Project - Espace presse du musée du Louvre | **200**（67,049 B；urllib 直连） | “**Inaugurated in 1989, I.M. Pei’s Pyramid** was originally designed to receive 4.5 million visitors.”；“The entrances and reception areas under the Pyramid have been reorganized, moving logistical functions such as ticket sales, cloakrooms, and restrooms to the Pyramid’s outermost perimeter in order to enhance the visitor experience.”；“The Pyramid Project aimed at improving the **spatial organization and the management of visitor flows both inside and outside the Pyramid**.”；“**Banners at the entrances of all three wings** clearly identify areas to explore and masterpieces from the permanent collections.” |
| ② | Encyclopædia Britannica「Louvre Pyramid」（**中—强权威·署名编辑条目：Barnabas Calder / Britannica Editors**） | `https://www.britannica.com/topic/Louvre-Pyramid` | Louvre Pyramid \| History, Description, & Facts \| Britannica | **200**（web_fetch 服务端直读；urllib 复抓出现 404/403 反爬，非源缺失） | “**Louvre Pyramid, pyramid that serves as the main entrance to the Louvre Museum in Paris. It was designed by architect I.M. Pei and completed in 1989.**”；“The design proposed a **central underground foyer in the Cour Napoléon** … to modernize and expand the premises.”；“Digging out the larger courtyard gave a generous foyer, **the wings of the museum were united**, and space was created for facilities and shops.”；“The great glass and steel pyramid over the foyer solves all the problems of a subterranean entrance: **it draws visitors in by its striking shape** and, with the three smaller flanking pyramids, lights the space below.” |

**对 `visitor-route`（参观动线）的支撑**：①从运营改造角度直书“visitor flows”、入口重组、售票/衣帽间外移、三翼入口标识，说明金字塔下方大厅是分流、导向、换乘的枢纽；②从建筑史角度直书“main entrance”、central underground foyer、三翼被统一、**draws visitors in**。两源合起来支撑“以中央入口大厅组织多翼分流与参观序列”的具名实例。**保留标注**：古根海姆螺旋坡道已用于 atrium，本条不复用；落地写卢浮宫时只写金字塔与地下大厅入口系统，不把它写成独立新建“馆”。

## 三、汇总

| 条目 | 具名实例 | 地点 | 设计者 / 营造主体 | 年份 | 源① | 源② | HTTP | 判定 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `rockery` | 苏州狮子林湖石假山群 | 江苏苏州园林路 23 号 | 天如禅师及弟子（无单一设计师） | 1342 | 苏州市园林和绿化管理局 | UNESCO 世界遗产中心 | 200 / 200 | **双源齐备**；只写营造主体 |
| `planting-design` | 邱园 Great Broad Walk Borders | 英国伦敦 Kew | William Nesfield；Richard Wilford（再设计） | 原始 1840s（1841/晚 1840s 佐证） | World Heritage Journeys of Europe | 英国政府 DCMS PDF | 200 / 200 | **双源齐备**；当前花境开放年未直书，不补写 |
| `seasonal-scenery` | 桂离宫庭园 | 日本京都西京区桂川西侧 | 智仁亲王、智忠亲王 | 1615 起近 50 年 | 日本宫内厅 | 日本国家旅游局 | 200 / 200 | **双源齐备**；四季与变化观景直证 |
| `visitor-route` | 卢浮宫金字塔—拿破仑庭院地下大厅 | 法国巴黎卢浮宫 | I.M. Pei | 1989 | 卢浮宫新闻中心 | Britannica 署名条目 | 200 / 200 | **双源齐备**；避开古根海姆 |

- **双源齐备率：4/4**；8 个主来源全部取证成功，**0 单源、0 缺源项**，无需写“仅单源/不可得”。
- **机构独立性**：四条均为两个不同机构；未把同一机构的不同页面算作两源。
- **需落地时保留的诚实标注**：①狮子林无单一景观设计师，写营造主体；②邱园当前花境开放年两源未直书，只写原始 1840s；③桂离宫写两代皇子分阶段营建，不写单一造园师；④卢浮宫条目限定为金字塔与地下大厅入口系统；⑤UNESCO 813 首轮 urllib 200，后续 web_fetch/复抓 403 反爬；Britannica 页面 web_fetch 200，urllib 复抓出现 404/403 反爬，均按反爬处理，不按死链处理。

## 四、被拒用来源记录（供后续参考，不作证据）

| URL / 来源 | 状态 | 处置 |
| --- | --- | --- |
| National Trust「The history of Hidcote」 | 服务端返回 WAF「Unknown Error」 | 改查邱园花境 |
| Historic England「Hidcote Manor」 | 403 | 改查邱园花境 |
| Kew 官方 press/media 页 | 403 | 改用 World Heritage Journeys of Europe + 英国政府 DCMS PDF |
| Britannica Katsura Imperial Villa | 403 | 改用宫内厅 + JNTO |
| British Museum Great Court / Foster + Partners 项目页 | 403 或正文在导航后截断 | 改用卢浮宫官方新闻中心 + Britannica |
| Wikipedia / 镜像站 | 未采用 | 按项目口径排除 |

## 五、证据回执（verification-before-completion）

- **Suzhou gov 狮子林**：3 条中文关键句 `FOUND`（地址、“假山王国”、1342 建禅林）。
- **UNESCO 813**：首轮 urllib 200 全文中 Lion Grove 列表句与 “rock formations” 句可见；后续复抓 403 反爬。
- **Kew WHJ**：4 条英文关键句 `FOUND`（Nesfield design / 60,000 plants / 1840s / texture and colour）。
- **UK DCMS PDF**：3 条英文关键句 `FOUND`（Kew founded 1759 / 1841 re-landscaped / late 1840s Walks/Vistas）；PDF 在内存中解析，未落盘。
- **IHA 京都离宫页**：4 条英文关键句 `FOUND`（location / 1615 + Toshihito & Toshitada / changing view / seasonal flowers）。
- **JNTO 桂离宫中文页**：3 条中文关键句 `FOUND`（17 世纪皇室 / 六建筑与筑山 / 一年四季不同美）。
- **Louvre press**：4 条英文关键句 `FOUND`（1989 + I.M. Pei / reception reorganized / visitor flows / three wings signage）。
- **Britannica Louvre Pyramid**：`web_fetch` 200 页面全文可见，4 条关键句逐字可见（main entrance / I.M. Pei 1989 / central underground foyer / wings united / draws visitors in）。

> 校验方法：UTF-8 解码 → 去 script/style/标签 → `html.unescape` → `norm()`（NFKC + 弯直引号/破折号/零宽空格/不间断空格归一 + 空白折叠 + 小写）→ 子串命中；PDF 用 `pypdf` 在内存中抽取后同法回验。HTML `<title>`、HTTP 状态与字节数来自同轮实抓。
