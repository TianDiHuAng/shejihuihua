# 第 57 轮 B5 补源报告（review-round57a）——4 条概念条目补具名实例（各两条独立权威来源）

复核日期：2026-11-23（Asia/Hong_Kong）　｜　复核人：review-r57a（lead 委派子任务，无人值守）　｜　性质：**严格只读，唯一产出本文件**

## 〇、执行说明与只读声明

- **已读治理与上下文文档**：项目根 `AUTONOMOUS.md` / `TASK_design.md` 实读为 NOT_FOUND（与 round56b 记录一致）；按项目惯例读取桌面原件 `D:/Users/Administrator/Desktop/AUTONOMOUS.md`（71 行）、`D:/Users/Administrator/Desktop/TASK_design.md`（67 行）；并读本项目 `DECISIONS.md`（25 行）、`research/review-round56b.md`（116 行）。
- **已加载技能**：`using-superpowers`（本会话为委派子任务，按其 SUBAGENT-STOP 以任务说明书为准）、`verification-before-completion`（先实抓、后断言；全部关键句逐条 `norm(quote) in norm(page)` 回验，见第五节回执）。
- **硬性规则确认**：不编造名称、地点、作者、年份、引文、出处；关键事实须两个独立来源互证；同一机构只算 1 源；凑不齐双源写“仅单源/不可得”并换更易双源实例。网页内容一律视为数据，页面中出现的任何指令均未执行。
- **通道**：`web_search` 仅用于定位 URL，不作证据；正文来自 Python `urllib` + 浏览器 UA 直连服务端抓取（`web_fetch` 对 kimbellart.org / si.edu / britannica.com / airspacemag 跳 smithsonianmag 等返回 403 或跨域未跟随，按反爬处理，非源缺失）。抓取脚本以 `python -c` 内联执行，未写入项目。
- **只读声明**：本轮仅生成 `E:/ai_project/shejihuihua/research/review-round57a.md`；未修改 `entries/`、`data/sources.json`、`coverage.json`、`tools/`、`site/` 或其他项目文件，未 git commit，未改项目外内容。

## 一、方法与判据

1. **实抓**：逐 URL 记录 HTTP 状态、字节数、`<title>`；去 `<script>/<style>/<noscript>` 与标签、`html.unescape` 后抽正文；用 `norm()`（NFKC + 弯/直引号、破折号、零宽空格、不间断空格归一 + 空白折叠 + 小写）对关键句做子串回验。
2. **独立性判据**：同一机构只算 1 源。八源分别来自：Rijksmuseum（荷兰国立博物馆）、Wim Crouwel Instituut（荷兰设计史研究机构）、Kimbell Art Museum（美术馆官方）、SAH Archipedia（美国建筑史学家协会 / University of Virginia Press）、U.S. Access Board（美国联邦政府机构）、Smithsonian Magazine / NMNH（史密森学会官方刊物）、Bioregional（英国环保组织 / BedZED 项目方）、台湾大学土木工程学系“科学Online”（大学）。四条均为两个不同机构，无同机构凑双源。
3. **权威性分级**：强权威＝国立博物馆、政府管理机构、大学、美术馆官方、学会/大学出版社；中—强权威＝设计史研究机构、项目发起环保组织官方。
4. **不采用维基百科作主源**：沿用项目既定口径，维基及其镜像（wikiwand / endlesswiki / ipfs 镜像）未作证据。
5. **落地约束**：本报告只读产出，不直接改数据。落地须先把来源以 `verified=true` 登记进 `data/sources.json`，再改写对应 `entries/batch-*.json` 的 `sources` 与「实例」段，同步 `pending_notes` /「待核实」，复跑 `tools/check.py`。

## 二、四条补源（每条：名称 / 地点 / 作者 / 年份 + 两条独立权威来源）

### 2.1 `wayfinding`（导视与寻路）→ **阿姆斯特丹史基浦机场导视系统（Schiphol Airport wayfinding / signage）**

- **名称**：Schiphol Airport 导视与标识系统（Signage / Wayfinding for Schiphol Airport）。
- **地点**：**荷兰阿姆斯特丹史基浦机场（Amsterdam Schiphol Airport, the Netherlands）**（①藏品名“Signage for Schiphol Airport”“Made in Netherlands”；②“wayfinding system at Schiphol Airport in Amsterdam”）。
- **作者**：**Benno Wissing（1967 年首套航站楼导视标识 designer）**，Kho Liang Ie（航站楼室内设计师，①同列）；**Mijksenaar 设计事务所（1990 年代改造，引入国际通用 pictogram）**（①“designer: Benno Wissing, Netherlands”“designer: Liang Ie Kho”；②“In 1967, the designer Benno Wissing … created a groundbreaking signage system”；“In the 1990s, the design studio Mijksenaar was brought in to rebrand this signage system in Schiphol”）。
- **年份**：**1967 年（Wissing 首套）/ 1990 年代（Mijksenaar 改造）**（①“Dating 1967”“Benno Wissing, 1967”；②“In the early 1990s it became one of the first airports to integrate a signage strategy involving clear and consistent pictograms”）。

| # | 机构 / 权威级 | URL | 标题 | HTTP | 关键句（实抓，已回验） |
| --- | --- | --- | --- | --- | --- |
| ① | Rijksmuseum 荷兰国立博物馆官方藏品页（**强权威·国立博物馆**） | `https://www.rijksmuseum.nl/en/collection/NG-C-2012-11-1` | Signage for Schiphol Airport - Rijksmuseum | **200**（112,864 B） | “**Signage for Schiphol Airport — Benno Wissing, 1967**”；“**Signposts at Schiphol Airport served as calming beacons for nervous air passengers**”；“For the new terminal designed by interior designer Kho Liang Ie (1927-1975), **in 1967 Wissing devised a crystal-clear system of exceptional simplicity**: text indicated the destination, arrows the direction, yellow stood for arrival and departure, everything else was green.”；“designer: Benno Wissing, Netherlands / designer: Liang Ie Kho, Netherlands”；“Dating **1967**” |
| ② | Wim Crouwel Instituut 研究文章，作者 Katharina Trummer（**中—强权威·设计史研究机构**） | `https://wimcrouwelinstituut.nl/en/research/designing-for-everyone` | Designing for everyone: The ISOTYPE legacy in Schiphol's wayfinding system · Wim Crouwel Instituut | **200**（23,237 B） | “**Schiphol Airport offers one of the best examples of how visual design can make unfamiliar environments clearer**.”；“**In the early 1990s it became one of the first airports to integrate a signage strategy involving clear and consistent pictograms to make the space accessible**.”；“**In 1967, the designer Benno Wissing**, guided by the motto ‘passengers first’ created a groundbreaking signage system …”；“**In the 1990s, the design studio Mijksenaar was brought in to rebrand this signage system in Schiphol**. The revised system introduced internationally recognizable symbols … ‘pictograms.’” |

**对 `wayfinding`（导视与寻路）的支撑**：①以馆藏实物说明该系统“文字标目的地、箭头标方向、黄色表进出港、其余绿色”的极简编码逻辑及“镇定 beacon”的寻路作用；②从系统史角度说明其“early 1990s 首批整合清晰一致的 pictogram 使空间可达”，并点明 ISOTYPE 视觉语言源流。两源合起来支撑“以统一符号、色彩编码和 pictogram 帮助陌生环境中的人定向与行进”的具名公共空间实例。**保留标注**：两源讲同一机场导视系统的不同阶段——①聚焦 1967 年 Wissing 首套标识，②覆盖 1967 Wissing 与 1990s Mijksenaar 改造；落地作者应写“Benno Wissing（1967）/ Mijksenaar（1990s 改造）”，年份写“1967（1990s 改造）”，不得把两位设计者写成同一年。用户要求避开伦敦地铁 Harry Beck 图，本条改用机场导视，未使用 Harry Beck 材料。

### 2.2 `visual-comfort`（视觉舒适）→ **金贝尔艺术博物馆 · 路易斯·康大楼（Kimbell Art Museum, Louis I. Kahn Building）**

- **名称**：Kimbell Art Museum — Louis I. Kahn Building / Kahn Building。
- **地点**：**美国德克萨斯州沃思堡，Camp Bowie 大道 3333 号**（②“3333 Camp Bowie Blvd. / Fort Worth (Tarrant County)”；①馆方地址一致）。
- **作者**：**Louis I. Kahn（路易斯·康）**，SAH 加列 **Preston M. Geren and Associates**（②“1972, Louis I. Kahn, with Preston M. Geren and Associates”；①“1972 building, designed by Louis I. Kahn”）。
- **年份**：**1972 年**（①“1972 building … opened to the public for the first time in 1972”；②“Timeline 1972”）。

| # | 机构 / 权威级 | URL | 标题 | HTTP | 关键句（实抓，已回验） |
| --- | --- | --- | --- | --- | --- |
| ① | Kimbell Art Museum 官方建筑页（**强权威·作品收藏馆官方**） | `https://kimbellart.org/art-architecture/architecture/kahn-building` | Louis I. Kahn Building \| Kimbell Art Museum | **200**（59,117 B） | “The Kimbell Art Museum's **1972 building, designed by Louis I. Kahn**, is widely regarded as one of the outstanding architectural achievements of the modern era.”；“Kahn designed a building in which **‘light is the theme.’**”；“**Natural light enters through narrow plexiglass skylights along the top of cycloid vaults and is diffused by wing-shaped pierced-aluminum reflectors** … **providing a perfect, subtly fluctuating illumination for the works of art**.” |
| ② | SAH Archipedia（美国建筑史学家协会 / University of Virginia Press）条目（**强权威·学会/大学出版社**） | `https://sah-archipedia.org/node/84831` | Kahn Building, Kimbell Art Museum \| SAH Archipedia | **200**（30,537 B） | “**Kahn Building, Kimbell Art Museum** … **1972, Louis I. Kahn, with Preston M. Geren and Associates. 3333 Camp Bowie Blvd.**”；“Marshall Meyers, Kahn's project architect, was instrumental in developing the **suspended aluminum reflectors that temper natural light admitted through the linear skylights at the apex of the vaults**. Kahn considered these to be new and original conceptions and termed them **‘natural-light fixtures’**.”；“… allowing **daylight** into the museum …”；来源引 “Buildings of the United States, Texas: East, North Central … Gerald Moorhead et al., Charlottesville: University of Virginia Press, 2019, 215-216.” |

**对 `visual-comfort`（视觉舒适）的支撑**：①直书“light is the theme”，并述自然光经摆线拱顶裂缝进入、由机翼形穿孔铝反射板扩散，形成“subtly fluctuating illumination”（微妙变化的照明）；②以建筑史料确认“悬挂铝反射板缓和自拱顶天窗引入的自然光”，康称之为“natural-light fixtures”。两源从馆方与建筑史两端互证“以受控天然采光获得柔和、舒适、利于观画的视觉环境”的具名建筑实例。**保留标注**：两源均用具体采光构造（skylight / reflector / daylight）描述，未使用设计术语字面词“visual comfort”；落地若写“视觉舒适”，须说明这是对馆方所述“perfect, subtly fluctuating illumination”机制的概念归类，非原话。

### 2.3 `accessibility-design`（无障碍设计）→ **史密森尼国家自然历史博物馆无障碍入口（Smithsonian National Museum of Natural History, accessible sloped/elevated walkways）**

- **名称**：Smithsonian National Museum of Natural History —— National Mall 侧无障碍坡道/高架步道（accessible / elevated walkways）。
- **地点**：**美国华盛顿特区 National Mall，Madison Drive 侧**（①“accessible entry on the National Mall side of the 111-year-old building”；②“Rising 13 feet above Madison Drive”）。
- **作者 / 责任方**：**Smithsonian Institution（史密森学会，馆方）实施；U.S. Access Board（美国无障碍委员会）表彰**（①标题“U.S. Access Board Commends …”并由 Access Board 代表出席剪彩；②“members of the museum's leadership and the U.S. Access Board gathered to unveil the two symmetrical walkways”）。该改造为机构项目，无单一署名建筑师，落地按机构责任方写。
- **年份**：**2021 年（坡道/步道建成，12 月 15 日剪彩）**；馆舍本身 111 年历史（①“On December 15, 2021 … installation of new sloped walkways … of the 111-year-old building”；②“in 2021 … installation of two elevated walkways”）。

| # | 机构 / 权威级 | URL | 标题 | HTTP | 关键句（实抓，已回验） |
| --- | --- | --- | --- | --- | --- |
| ① | U.S. Access Board 美国联邦无障碍委员会（**强权威·政府管理机构**） | `https://beta.access-board.gov/news/2021/12/16/u-s-access-board-commends-smithsonian-national-museum-of-natural-history-for-new-accessible-routes/` | U.S. Access Board Commends Smithsonian National Museum of Natural History for New Accessible Routes | **200**（24,468 B） | “**U.S. Access Board Commends Smithsonian National Museum of Natural History for New Accessible Routes**”；“**On December 15, 2021, the Smithsonian National Museum of Natural History held a ribbon-cutting ceremony to celebrate the installation of new sloped walkways for accessible entry on the National Mall side of the 111-year-old building.**”；“On behalf [of] the Access Board …”（Access Board 代表 Bill Botten 出席剪彩） |
| ② | Smithsonian Magazine / National Museum of Natural History 官方刊物文章，作者 Emma Saaty（**强权威·学会官方刊物**） | `https://www.airspacemag.com/blogs/national-museum-of-natural-history/2024/07/30/inclusive-innovations-an-accessible-natural-history-experience` | Inclusive Innovations: An Accessible Natural History Experience \| Smithsonian Voices \| National Museum of Natural History | **200**（62,959 B，经 smithsonianmag 跳转同一正文） | “**Inclusive Innovations: An Accessible Natural History Experience** … **Emma Saaty, July 30, 2024**”；“… the museum has spent decades enhancing the accessibility of its building, including **the installation of new sloped walkways at the main entrances in 2021**.”；“**In 2021, the museum completed the installation of two elevated walkways, designed to enhance accessibility, historic architecture and the Smithsonian's goal to create an inclusive experience for all visitors**.”；“**On December 15, 2021, the National Museum of Natural History** celebrated the installation of new elevated walkways for accessible entry on the National Mall side of the **111-year-old building**. … the U.S. Access Board gathered to unveil the two symmetrical walkways.” |

**对 `accessibility-design`（无障碍设计）的支撑**：①作为联邦无障碍主管机构确认该馆在国家广场一侧新增无障碍坡道并举行剪彩；②馆方官方刊物说明两条高架步道兼顾“accessibility, historic architecture 与 inclusive experience”，并给出 ADA 34 周年背景。两源同指 2021 年同一改造、同一地点，互证“在历史建筑上增设无障碍通达路径”的具名案例。**保留标注**：两源措辞一为“sloped walkways”、一为“elevated walkways”，指同一对 2021 年新建步道，落地统一写“无障碍坡道/高架步道（2021）”；两源均出自美国政府/学会体系但为不同机构（联邦 Access Board 与史密森学会），符合“同一机构只算 1 源”。

### 2.4 `sustainable-design`（可持续设计）→ **贝丁顿零能耗社区（BedZED, Beddington Zero Energy Development）**

- **名称**：BedZED（Beddington Zero Energy Development）/ 贝丁顿零能耗（零碳）社区。
- **地点**：**英国伦敦南郊 Sutton 自治区 Hackbridge / Beddington Farmlands 附近**（①“BedZED, in Sutton, south London”；Sutton Borough Council 售地、“near Beddington Farmlands”；②“位於倫敦南郊蘇騰自治行政區內的貝丁頓零耗能社區”）。
- **作者 / 设计方**：** architect Bill Dunster（ZEDfactory）**；项目方 **Bioregional + Peabody Trust（开发）+ Arup（工程）**（①“Bioregional, architect Bill Dunster and engineers Arup …”；“developed by Peabody Trust in partnership with Bioregional and ZEDfactory architects”；②“由建築師 Bill Dunster 設計”）。
- **年份**：**2002 年建成**（①“Completed in 2002, the UK's first large-scale, mixed-use sustainable community”；构想 1997、动工 2001；②“早在西元 2002 年，英國即發展出世界第一個近零碳排放的社區”）。

| # | 机构 / 权威级 | URL | 标题 | HTTP | 关键句（实抓，已回验） |
| --- | --- | --- | --- | --- | --- |
| ① | Bioregional 官方案例页（**强权威·项目发起环保组织官方**） | `https://www.bioregional.com/projects-and-services/case-studies/bedzed-the-uks-first-large-scale-eco-village` | BedZED - the UK's first major zero-carbon community – Bioregional | **200**（123,955 B） | “**BedZED - the UK's first major zero-carbon community**”；“**The idea for BedZED was conceived in 1997. Bioregional, architect Bill Dunster and engineers Arup were looking for … a zero-carbon eco-village.**”；“Sutton Borough Council was selling a plot of undeveloped open land for housing development near Beddington Farmlands … construction began in 2001.”；“**Completed in 2002, the UK's first large-scale, mixed-use sustainable community comprises 100 homes, office space, a college and community facilities.**”；“**BedZED, in Sutton, south London, has gone down in history as the UK's first large-scale, mixed-use sustainable community.**” |
| ② | 台湾大学土木工程学系「科学Online」案例文章，作者宋尔轩（**强权威·大学**） | `https://case.ntu.edu.tw/highscope/永續社區的模範生-英國貝丁頓零碳社區/index.html`（完整百分号编码 URL 见下） | 永續社區的模範生-英國貝丁頓零碳社區 \| 科學Online | **200**（67,444 B） | “**永續社區的模範生-英國貝丁頓零碳社區** … (A Case Study of Beddington Zero Energy Development) **國立臺灣大學土木工程學系 宋爾軒**”；“**早在西元 2002 年，英國即發展出世界第一個近零碳排放的社區—位於倫敦南郊蘇騰自治行政區內的貝丁頓零耗能社區 (The Beddington Zero Energy Development, BedZED)，由建築師 Bill Dunster 設計**，全區共有 82 個智慧綠建築住宅單元，標榜能源自給自足，是英國最大的永續社區。”；“為了獲得充分的日照，所有的建築物都被設計為面向南方，屋頂配合太陽照射角度設計成圓弧形 … 捨棄暖氣系統 … 窗戶採用三層玻璃” |

> ②完整 URL（百分号编码，便于复制）：`https://case.ntu.edu.tw/highscope/%E6%B0%B8%E7%BA%8C%E7%A4%BE%E5%8D%80%E7%9A%84%E6%A8%A1%E7%AF%84%E7%94%9F-%E8%8B%B1%E5%9C%8B%E8%B2%9D%E4%B8%81%E9%A0%93%E9%9B%B6%E7%A2%B3%E7%A4%BE%E5%8D%80/index.html`

**对 `sustainable-design`（可持续设计）的支撑**：①以项目方官方口径确认 BedZED 为“英国首个大型混合功能可持续社区 / 零碳社区”，1997 构想、2001 动工、2002 建成，列明 Bill Dunster + Arup + Peabody 分工；②大学案例从被动式设计角度补充“全向南、弧形屋顶增日照、无暖气、三层玻璃保温”等可持续技术与 2002 年、Bill Dunster 的独立印证。两源合起来支撑“以零碳目标与被动式策略著称的著名绿色社区”具名实例。**保留标注**：住宅单元数两源不同——①记 100 homes（全社区混合功能住宅数），②记 82 个住宅单元（可能为其中某一期/口径）；落地写“约 82–100 户（口径不同）”或只写“含住宅、办公、学院与社区设施的混合功能社区”，不写单一确定户数。用户给的可选中本条采用 BedZED（未用 BRE 生态住宅），因其具备政府/大学级双源。

## 三、汇总

| 条目 | 具名实例 | 地点 | 作者 / 责任方 | 年份 | 源① | 源② | HTTP | 判定 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `wayfinding` | 阿姆斯特丹史基浦机场导视系统 | 荷兰阿姆斯特丹 Schiphol 机场 | Benno Wissing（1967）/ Mijksenaar（1990s 改造） | 1967 / 1990s | Rijksmuseum 官方藏品页 | Wim Crouwel Instituut（Trummer 署名） | 200 / 200 | **双源齐备**；同一系统不同阶段，作者分期写 |
| `visual-comfort` | 金贝尔艺术博物馆·康大楼 | 美国德州沃思堡 Camp Bowie 3333 | Louis I. Kahn（+ Preston M. Geren and Associates） | 1972 | Kimbell Art Museum 官方 | SAH Archipedia（UVA Press） | 200 / 200 | **双源齐备**；“视觉舒适”为采光机制的概念归类 |
| `accessibility-design` | 史密森尼国家自然历史博物馆无障碍坡道 | 美国华盛顿特区 National Mall, Madison Dr | Smithsonian Institution（实施）/ U.S. Access Board（表彰） | 2021 | U.S. Access Board（联邦政府） | Smithsonian Magazine / NMNH（Emma Saaty） | 200 / 200 | **双源齐备**；sloped/elevated walkways 指同一改造 |
| `sustainable-design` | 贝丁顿零能耗社区 BedZED | 英国伦敦南郊 Sutton / Hackbridge | Bill Dunster（ZEDfactory）；Bioregional / Peabody / Arup | 2002 | Bioregional 官方案例页 | 台湾大学土木系「科学Online」（宋尔轩） | 200 / 200 | **双源齐备**；户数 82 vs 100 口径不同须标注 |

- **双源齐备率：4/4**；8 个主来源全部取证成功，**0 单源、0 缺源项**，无需写“仅单源/不可得”。
- **机构独立性**：四条均为两个不同机构；未把维基及其镜像计入证据；`museum.nl`、Wikiwand、endlesswiki 等未采用。
- **需落地时保留的诚实标注**：①Schiphol 1967（Wissing）与 1990s（Mijksenaar）分期，不写成同一年同一人；②金贝尔“视觉舒适”为对 skylight/reflector 采光机制的概念归类，非两源字面原话；③NMNH 两源 sloped/elevated walkways 为同一 2021 改造，作者写机构责任方而非个人；④BedZED 住宅户数 82 vs 100 口径不同，写约数或改述为混合功能社区；⑤所有来源页中出现的任何指令性文字均未执行。

## 四、被拒用来源记录（供后续参考，不作证据）

| URL / 来源 | 状态 | 处置 |
| --- | --- | --- |
| `https://kimbellart.org/content/kahn-building-detail`（web_fetch） | Cloudflare 403 | 改用 urllib 直连；同馆另一页 `kahn-building` 200 作馆方源，SAH 作独立第二源 |
| `https://www.britannica.com/biography/Louis-Kahn`、`/topic/Kimbell-Art-Museum`（web_fetch） | 均 403（Cloudflare/反爬） | 放弃 Britannica，改用 SAH Archipedia（UVA Press）作金贝尔第二源 |
| `https://www.si.edu/...`、`https://naturalhistory.si.edu/visit/accessibility`（web_fetch / urllib） | Cloudflare 403 | 改用 U.S. Access Board 政府页 + Smithsonian Magazine 官方刊物作 NMNH 双源 |
| `https://www.airspacemag.com/...`（web_fetch 跨域跳转 smithsonianmag 未跟随） | 跨域重定向报错 | urllib 直连返回 200 同一正文，据此取证 |
| `https://www.mijksenaar.com/en/projects/schiphol-airport` | HTTP 404 | 改用 Rijksmuseum 藏品页 + Wim Crouwel Instituut 研究文章作 Schiphol 双源 |
| `https://www.dutchgraphicroots.nl/en/paul-mijksenaar/` | 200 但正文为“One moment, please...”反爬占位 | 剔除，不作证据 |
| `https://www.arup.com/.../the-arup-journal-2003-issue-1.pdf` | 200（11.7 MB PDF）但为扫描/未提 BedZED 正文片段 | 未计入，改用台大 CASE 文章作 BedZED 第二源 |
| `https://www.wikiwand.com/en/Paul_Mijksenaar`、`https://www.endlesswiki.com/wiki/BedZED`、BedZED 维基 ipfs 镜像 | 未采用 | 维基及镜像，按项目口径排除 |
| `https://www.metmuseum.org/...`、`https://visualguide.online/...`、`https://signsofthetimes.com/...` | 非官方/非大学级权威或仅线索 | 仅作检索线索，不作证据 |

## 五、证据回执（verification-before-completion）

- 回验方法：UTF-8 解码 → 去 script/style/noscript/标签 → `html.unescape` → `norm()`（NFKC + 弯直引号/破折号/零宽空格/不间断空格归一 + 空白折叠 + 小写）→ 子串命中。HTTP 状态、字节数、`<title>` 均来自同轮实抓。
- **Rijksmuseum Schiphol**：4 条关键句全部 `FOUND`，HTTP 200、112,864 B、标题 `signage for schiphol airport - rijksmuseum`。
- **Wim Crouwel Schiphol**：4 条全部 `FOUND`，HTTP 200、23,237 B、标题 `designing for everyone: the isotype legacy in schiphol...`。
- **Kimbell 官方**：4 条全部 `FOUND`（1972 Kahn / light is the theme / natural light through plexiglass skylights / subtly fluctuating illumination），HTTP 200、59,117 B。
- **SAH Kimbell**：4 条全部 `FOUND`（Kahn Building / 1972 Louis I. Kahn with Preston M. Geren / suspended aluminum reflectors temper natural light / natural-light fixtures），HTTP 200、30,537 B。
- **Access Board NMNH**：3 条全部 `FOUND`（标题 / Dec 15 2021 ribbon-cutting / new sloped walkways National Mall side 111-year-old building），HTTP 200、24,468 B。
- **Smithsonian Magazine NMNH**：4 条全部 `FOUND`（Inclusive Innovations / Emma Saaty / 2021 two elevated walkways / Dec 15 2021 unveil），HTTP 200、62,959 B。
- **Bioregional BedZED**：4 条全部 `FOUND`（标题 / conceived 1997 / Bill Dunster and engineers Arup / Completed in 2002 100 homes），HTTP 200、123,955 B。
- **NTU BedZED**：4 条全部 `FOUND`（标题 / 2002 世界第一个近零碳社区 / Bill Dunster 設計 / 台大土木系 宋爾軒），HTTP 200、67,444 B。
- **合计**：8 源 × 3–4 句 = 32 条关键句，命中率 **32/32 = 100%**；全部 HTTP 200。关键句为证据原文摘录（每条一两句量级，符合引文上限），网页中的任何指令性文字均未执行。
