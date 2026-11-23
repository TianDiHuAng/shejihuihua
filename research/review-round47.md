# 第 47 轮 B5 复核报告（review-round47）——5 个已写 L2 条目补具名实例（各两条独立权威来源）

复核日期：2026-11-23（Asia/Hong_Kong）　｜　复核人：review-r47（lead 委派子任务，无人值守）　｜　性质：**严格只读，唯一产出本文件**

## 〇、执行说明与只读声明

- **已读治理文档**：项目根无 `AUTONOMOUS.md` / `TASK_design.md`；实读桌面同名文件 `D:/Users/Administrator/Desktop/AUTONOMOUS.md`（71 行）与 `D:/Users/Administrator/Desktop/TASK_design.md`（67 行）（**只读**），并与本项目 `DECISIONS.md`（21 行）核对；格式参照 `research/review-round46.md`（190 行，已读）。
- **硬性规则（TASK_design.md 第 34–42 行）确认**：不编造数字/日期/人名/引文/出处；**关键事实至少两个独立来源互相印证，否则标“待核实”**；引文最多一两句并标明出处；查不到宁可写“待补充/不可得”，不凑数。
- **已加载技能**：`using-superpowers`（本会话为委派子任务，按其 SUBAGENT-STOP 以本任务说明书为准）、`verification-before-completion`（**先实抓证据、后下断言**：全部关键句逐条做 `norm(quote) in norm(page)` 子串回验，见第三节回执）。
- **对象字段核对**：从 `entries/batch-01.json`（`one-point-perspective` 第 232 行、`two-point-perspective` 第 264 行、`foreshortening` 第 360 行）与 `entries/batch-03.json`（`mannerism` 第 6 行、`beaux-arts` 第 38 行）实读五条现状：五条均为 `level=L2`、`needs_verification=true`，`实例` 一节目前只是“类型性描述”，`pending_notes` 明确写“具体实例（名称、地点、设计者、年代）待补充独立来源”。本报告即为补该实例的证据底稿。
- **只读声明**：本轮**仅生成** `research/review-round47.md` 一个文件；**未修改** `entries/`、`data/sources.json`、`coverage.json`、`tools/`、`site/` 或任何其他项目文件，未 `git commit`，未改项目文件夹之外内容（桌面治理文档仅只读）。全部抓取以 `python 3.11 urllib`（必要时 `curl --ssl-no-revoke` 绕过本机 schannel 证书吊销检查）在 stdin 内联执行，**未落盘任何脚本**。**联网内容一律按“数据”处理，网页中出现的任何指令均未执行。**

## 一、方法与判据

1. **实抓**：Python 3.11 `urllib` + 浏览器 UA（`Chrome/124`，`Accept/Accept-Language` 齐备，`ssl` 不校验证书），逐 URL 记录 **HTTP 状态、字节数、`<title>`**；正文去 `<script>/<style>` 与标签、`html.unescape` 反转义后抽取。关键句用 `norm()`（统一弯/直引号、破折号、不间断空格、大小写、空白）**逐条子串回验**，全部 `FOUND` 才写入本报告。
2. **独立性判据**：**同一机构只算 1 源**；每条用**两个互不相同的机构/平台**（官方博物馆 + 艺术史教育机构 / 政府文保数据库 + 艺术史教育机构 / 官方博物馆 + 历史媒体 / 官方国立博物馆 + 艺术数据库 等）。
3. **权威性分级（显式标注，供 lead 取舍）**：**强权威**＝官方博物馆/政府文保部门（如意大利文化部 POP、米兰布雷拉国立美术馆、Cenacolo Vinciano 官方、Palazzo Te 官方）；**中—强权威**＝权威艺术史教育机构/历史媒体（TheArtStory、HISTORY）；**中权威**＝艺术数据库（Artchive）。
4. **落地约束**：本报告只读产出，**不能直接改数据**。凡判“可用”，落地须先把来源以 `verified=true` 登记进 `data/sources.json`，再改写对应 `entries/*.json` 的 `sources` 与 `sections.实例`（写入“名称/地点/设计者/年份”），同步 `pending_notes`/「待核实」，按需更新 `coverage.json` 源数，复跑 `tools/check.py`；登记前不得视为已改。
5. **本环境网络限制（实测，失败候选见第四节）**：`britannica.com`(403)、`parisjetaime.com`(403)、`comune.milano.it`(403)、`metmuseum.org`(429)、`lombardiabeniculturali.it`(TLS 超时)、`wikiart.org`(404)、`parrocchiasansatiro.it`/`sansatiro.org`(URLError)、`wga.hu`(旧路径全部跳“moved to a new address”空壳)、`newworldencyclopedia.org` 的 `Mantegna`/`Bramante`/`Giulio_Romano` 仅返回搜索页无正文；`turismo.milano.it` / `yesmilano.it` 为 JS 单页应用，静态抓取无正文。搜索引擎 `web_search` 端点未返回结果、Bing/DDG 命中区被反爬污染，**故全部改走可实抓 200 的官方/博物馆/艺术史教育站，不编造、不以失败路径冒充证据**。
6. **本轮未采用维基百科作主源**：本轮 `en.wikipedia.org` 可访问（200），但按项目既定口径（D10 / round46）**维基属同平台伞源、不计独立源**，仅用于快速锁定官方 URL 与事实坐标（如“Palazzo Te 官网 centropalazzote.it”“Brera 作品 slug”“Palais Garnier POP 编号 PA00089004”），**不作证据列出**。

---

## 二、五条复核（每条：名称 / 地点 / 设计者 / 年份 + 两条独立权威来源）

### 2.1 `mannerism` → **得特宫 Palazzo del Te（曼图亚，Giulio Romano，1524–1534）**

- **名称**：Palazzo del Te / Palazzo Te（得特宫；又译“茶宫”，曼图亚贡扎加家族郊外别墅）
- **地点**：意大利 · 曼图亚（Mantua / Mantova）
- **设计者**：**Giulio Romano（朱利奥·罗马诺）**；委托人为曼图亚公爵 **Federico II Gonzaga（费德里科二世·贡扎加）**
- **年份**：**1524–1534**（任务给定，与源② 一致）；**源① 官方记 1525–1535**（建造与装饰），两源并列、不合并改写

| # | 机构 / 权威级 | URL | 标题 | HTTP（字节） | 关键句（原文，实抓，已回验 FOUND） |
| --- | --- | --- | --- | --- | --- |
| ① | Palazzo Te 官方博物馆站（Fondazione Palazzo Te / 曼图亚，**强权威·官方**） | `https://www.centropalazzote.it/` | Palazzo Te | **200**（109,879 B） | “...one of the finest examples of a Mannerist Renaissance Villa, **designed and constructed between 1525 and 1535 by Giulio Romano** ... and **commissioned by Federico II Gonzaga**.” |
| ② | TheArtStory（艺术史教育机构，**中—强权威·艺术史教育**） | `https://www.theartstory.org/movement/mannerism/` | Mannerism Movement Overview \| TheArtStory | **200**（183,251 B） | “**Giulio Romano's Palazzo del Te (1524-1534) was a tour de force of Mannerist architecture** and made him famous.” |

**三要素对位**：名称＝Palazzo del Te（两源一致）；地点＝Mantova（源① 官方在曼图亚）；设计者＝Giulio Romano，委托人 Federico II Gonzaga（源① 直书，源② 直书 Giulio Romano）；年份＝**源① 1525–1535 / 源② 1524–1534**，任务“1524–1534”通行，两源数值并列（差异见第六节）。
**独立性说明**：Palazzo Te 官方博物馆站与 TheArtStory 为两个不同机构，均 HTTP 200、正文直证，可作独立双源。

### 2.2 `beaux-arts` → **巴黎歌剧院 Palais Garnier（巴黎，Charles Garnier，1861–1875）**

- **名称**：Palais Garnier / Opéra Garnier（加尼叶歌剧院；法国国家歌剧院“巴黎歌剧院”剧院）
- **地点**：法国 · 巴黎（第 9 区，Place de l'Opéra）
- **设计者**：**Charles Garnier（夏尔·加尼叶）**
- **年份**：**1861–1875**（任务给定；源① 官方记建造 campaign **1862 ; 1875**、1861 未直书；源② 记 **1861–74**；两源并列，见第六节）

| # | 机构 / 权威级 | URL | 标题 | HTTP（字节） | 关键句（原文，实抓，已回验 FOUND） |
| --- | --- | --- | --- | --- | --- |
| ① | Ministère de la Culture · POP（法国文化部开放遗产平台 / Mérimée 数据库，**强权威·政府文保**） | `https://www.pop.culture.gouv.fr/notice/merimee/PA00089004` | Théâtre national de l'Opéra, dit opéra Garnier - POP - Plateforme Ouverte du Patrimoine | **200**（321,280 B；Python urllib 报 421 Misdirected，取 `curl --ssl-no-revoke` 抓得） | 字段直录：“**Théâtre national de l'Opéra, dit opéra Garnier**”；“Auteur de l'édifice **Garnier Charles (architecte)**”；“Année(s) de(s) campagne(s) de construction **1862 ; 1875**”；“Localisation Île-de-France ; **Paris (75) ; Paris 9e arrondissement**”；“**16 octobre 1923**”（列级历史建筑）。 |
| ② | TheArtStory（艺术史教育机构，**中—强权威·艺术史教育**） | `https://www.theartstory.org/movement/beaux-arts-architecture/` | Beaux-Arts Architecture Movement Overview \| TheArtStory | **200**（151,313 B） | “...**Opéra Garnier (1861-74)** ...”（代表作列表）；页内引 “**Charles Garnier**” 及其语录。 |

**三要素对位**：名称＝Théâtre national de l'Opéra, dit opéra Garnier（源① 官方全称）/ Opéra Garnier（源②）；地点＝Paris 9e（源① 官方）；设计者＝Charles Garnier（源① 官方、源② 一致）；年份＝**源① 1862 ; 1875 / 源② 1861-74**，任务“1861–1875”为通行区间，两源数值并列。
**独立性说明**：法国文化部 POP（政府文保）与 TheArtStory（独立教育机构）为两个不同机构，均 HTTP 200、正文直证，可作独立双源。**附加官方旁证（不计入两源）**：巴黎国家歌剧院官网 `https://www.operadeparis.fr/en/visits/palais-garnier`（HTTP 200，732,948 B，标题“Visit the Palais Garnier - Opéra national de Paris”）确认名称为 Palais Garnier、定位为“19 世纪剧院建筑杰作”，但其静态页未直书 1861/1875 两字年份，故仅作旁证。

### 2.3 `one-point-perspective` → **最后的晚餐 The Last Supper（米兰，Leonardo da Vinci，约 1495–1498）**

- **名称**：The Last Supper / Il Cenacolo（《最后的晚餐》）
- **地点**：意大利 · 米兰 · 圣玛利亚感恩修道院（Santa Maria delle Grazie）餐厅（refettorio）
- **设计者**：**Leonardo da Vinci（列奥纳多·达·芬奇）**
- **年份**：**约 1495–1498**（任务给定，与源② 一致）

| # | 机构 / 权威级 | URL | 标题 | HTTP（字节） | 关键句（原文，实抓，已回验 FOUND） |
| --- | --- | --- | --- | --- | --- |
| ① | Museo del Cenacolo Vinciano（《最后的晚餐》官方博物馆，**强权威·官方博物馆**） | `https://cenacolovinciano.org/en/history/` | History - Museo del Cenacolo Vinciano \| Official Website | **200**（118,873 B） | “**The Last Supper occupies the whole north wall of the refectory of the Dominican monastery of Santa Maria delle Grazie.**”（同站首页标题“Last Supper, Leonardo Da Vinci - Cenacolo Vinciano Official Website”直证书名与作者；该站静态页未直书 1495/1498 两字年份）。 |
| ② | HISTORY（A&E Networks 权威历史媒体，**中—强权威·历史媒体**） | `https://www.history.com/topics/renaissance/leonardo-da-vinci` | Leonardo da Vinci: Facts, Paintings & Inventions \| HISTORY | **200**（521,912 B） | “The first is da Vinci's 'The Last Supper,' **painted during his time in Milan, from about 1495 to 1498**. A tempera and oil mural on plaster... was **created for the refectory of the city's Monastery of Santa Maria delle Grazie**.” |

**三要素对位**：名称＝The Last Supper（两源一致）；地点＝圣玛利亚感恩修道院餐厅（源① 官方、源② 一致）；设计者＝Leonardo da Vinci（源① 官方标题、源② 一致）；年份＝**约 1495–1498**（源② 直书；源① 官方页以场所/作者直证、未标年份）。
**独立性说明**：Cenacolo Vinciano 官方博物馆与 HISTORY（A&E 网络）为两个不同机构，均 HTTP 200、正文直证，可作独立双源。**附加旁证（不计入两源）**：意大利国家旅游 `https://www.italia.it/en/lombardy/milan/da-vinci-last-supper-museum`（HTTP 200，标题“The Last Supper Museum in Milan - Italia.it”）确认地点在圣玛利亚感恩修道院餐厅，UNESCO 世界遗产。

### 2.4 `foreshortening` → **哀悼基督 Lamentation over the Dead Christ（现藏米兰布雷拉，Andrea Mantegna，约 1480）**

> ⚠ **地点勘误（如实标注）**：任务写“曼图亚”，但该画**现藏米兰布雷拉国立美术馆（Pinacoteca di Brera, Milan）**，两源均直证 Milan / Palazzo Brera。曼图亚是曼特尼亚的供职地（贡扎加宫廷），并非此画现藏地。**本报告按实际出土地/现藏地记 Milan**，并在第六节提示 lead 修正条目地点。
- **名称**：Lamentation over the Dead Christ（《哀悼基督》；又称 The Foreshortened Christ / Dead Christ and Three Mourners）
- **地点**：意大利 · 米兰 · 布雷拉国立美术馆（Pinacoteca di Brera, Milan）
- **设计者**：**Andrea Mantegna（安德烈亚·曼特尼亚）**
- **年份**：**约 1480**（任务给定 / 通行）；**源① 布雷拉官方记 c. 1483**；**源② Artchive 记 c. 1490**（三个数值并列，见第六节）

| # | 机构 / 权威级 | URL | 标题 | HTTP（字节） | 关键句（原文，实抓，已回验 FOUND） |
| --- | --- | --- | --- | --- | --- |
| ① | Pinacoteca di Brera（布雷拉国立美术馆，**强权威·国立博物馆**） | `https://pinacotecabrera.org/en/collezioni/collezione-on-line/cristo-morto/` | Lamentation over the Dead Christ \| Pinacoteca di Brera | **200**（99,012 B） | 藏品字段直录：“Title **Lamentation over the Dead Christ**”；“Author **Andrea Mantegna**”；“**Year c. 1483**”；“Materials and Techniques **Tempera on canvas**”；“Room **VI**”；馆名“**Pinacoteca di Brera**”、馆址“**Milan**”。 |
| ② | Artchive（艺术数据库，**中权威·艺术数据库**） | `https://www.artchive.com/artwork/the-lamentation-over-the-dead-christ-andrea-mantegna-c-1490/` | The Lamentation over the Dead Christ (c. 1490) by Andrea Mantegna – Artchive | **200**（176,255 B） | “**Current Location Palazzo Brera, Milan, Italy**”；“**The composition is notable for its dramatic foreshortening**, bringing a bold perspective to the fore.” |

**三要素对位**：名称＝Lamentation over the Dead Christ（两源一致）；地点＝**Palazzo Brera, Milan**（源② 直书；源① 为布雷拉馆藏、馆在米兰）；设计者＝Andrea Mantegna（两源一致）；年份＝**约 1480 / 源① c. 1483 / 源② c. 1490**（并列，见第六节）。
**独立性说明**：布雷拉国立美术馆（国立博物馆）与 Artchive（独立艺术数据库）为两个不同机构，均 HTTP 200、正文直证，可作独立双源（源② 权威级为“中”）。

### 2.5 `two-point-perspective` → **圣沙弟罗圣玛利亚教堂 illusory choir（米兰，Donato Bramante，约 1482–1486）**

> ⚠ **手法勘误（如实标注）**：该“错觉合唱席（false apse / illusory choir）”实为**单点透视 + 浅浮雕的 trompe-l'œil**（利用极浅进深伪造纵深），严格说是**一点透视**的经典范例，而非“两点透视”。任务将其归入 `two-point-perspective` 存在手法错配；本报告按任务指定的具名对象交付双源证据，并在第六节提示：若该条目须严格对应“两点透视”，建议换“雅典学院”等更不易混例，或把此例移到一点透视/错觉透视条目。
- **名称**：Santa Maria presso San Satiro（圣沙弟罗圣玛利亚教堂）内的**错觉合唱席 / 假后殿（false apse, illusory choir）**
- **地点**：意大利 · 米兰（Via Torino 附近的 Santa Maria presso San Satiro）
- **设计者**：**Donato Bramante（多纳托·布拉曼特）**（教堂立面另由 Giovanni Antonio Amadeo 设计）
- **年份**：**约 1482–1486**（任务给定；源① TheArtStory 记 **1482-86**，与任务一致；源② Artchive 记 **c.1482**）

| # | 机构 / 权威级 | URL | 标题 | HTTP（字节） | 关键句（原文，实抓，已回验 FOUND） |
| --- | --- | --- | --- | --- | --- |
| ① | TheArtStory（艺术史教育机构，**中—强权威·艺术史教育**） | `https://www.theartstory.org/artist/bramante-donato/` | Donato Bramante Paintings, Bio, Ideas \| TheArtStory | **200**（143,720 B） | 代表作“**Santa Maria presso San Satiro (1482-86)**”；“...created **the illusion of a much deeper interior space, such as the choir for Milan's San Satiro church**...”；并称其“**trompe l'oeil** effect”。 |
| ② | Artchive（艺术数据库，**中权威·艺术数据库**） | `https://www.artchive.com/artwork/santa-maria-presso-san-satiro-bramante-false-apse-donato-bramante-c-1482/` | Santa Maria presso San Satiro – Bramante false apse (c.1482) by Donato Bramante – Artchive | **200**（175,170 B） | “**Santa Maria presso San Satiro – Bramante false apse (c.1482) by Donato Bramante**”；“**The focal point is the false apse—a clever use of perspective painting that creates the illusion of depth on a flat surface**...” |

**三要素对位**：名称＝Santa Maria presso San Satiro 的 false apse / illusory choir（两源一致）；地点＝Milan（源① 直书“Milan's San Satiro church”）；设计者＝Donato Bramante（两源一致）；年份＝**约 1482–1486**（源① 1482-86 与任务一致；源② c.1482）。
**独立性说明**：TheArtStory 与 Artchive 为两个不同机构（均为艺术史教育/数据库，**中—强/中**权威，**未取得官方/博物馆一级源**），均 HTTP 200、正文直证，可作“两个独立机构”双源，但权威级偏低，落地请按第六节标注。

---

## 三、汇总（各条可得源数）

| 条目（中文题名 / id） | 具名实例 | 采用的两条独立主源（机构） | 独立机构数 | 达“双独立源” | 四要素（名称/地点/设计者/年份）源内直证 | 备注 |
| --- | --- | --- | --- | --- | --- | --- |
| 样式主义（手法主义）建筑 / `mannerism` | Palazzo del Te 得特宫（曼图亚，Giulio Romano，1524–1534） | Palazzo Te 官方站 ＋ TheArtStory | 2 | ✅ | 名称✅ 地点✅ 设计者✅ 年份：1525–1535 / 1524–1534 ✅ | 两源年份值不同，并列；委托人 Federico II Gonzaga |
| 学院派建筑（布扎艺术） / `beaux-arts` | Palais Garnier 巴黎歌剧院（巴黎，Charles Garnier，1861–1875） | 法国文化部 POP(Mérimée PA00089004) ＋ TheArtStory | 2 | ✅ | 名称✅ 地点✅(Paris 9e) 设计者✅ 年份：1862;1875 / 1861-74 ✅ | 官方另列 1923 列级；歌剧院官网作旁证 |
| 一点透视 / `one-point-perspective` | The Last Supper 最后的晚餐（米兰，Leonardo da Vinci，约 1495–1498） | Cenacolo Vinciano 官方 ＋ HISTORY | 2 | ✅ | 名称✅ 地点✅ 设计者✅ 年份：约1495–1498（源②）✅ | 官方静态页未标年份；italia.it 旁证 |
| 缩短法 / `foreshortening` | Lamentation over the Dead Christ 哀悼基督（**现藏米兰布雷拉**，Andrea Mantegna，约 1480） | 布雷拉国立美术馆 ＋ Artchive | 2 | ✅ | 名称✅ 地点✅(Palazzo Brera, Milan) 设计者✅ 年份：c.1483 / c.1490（任务约1480）✅ | **任务“曼图亚”系误，实为米兰**；三源年份值并列 |
| 两点透视 / `two-point-perspective` | Santa Maria presso San Satiro 错觉合唱席（米兰，Donato Bramante，约 1482–1486） | TheArtStory ＋ Artchive | 2 | ✅（**均为中—强/中，无官方一级源**） | 名称✅ 地点✅(Milan) 设计者✅ 年份：1482-86 / c.1482 ✅ | 该错觉实为**单点透视/trompe-l'œil**，与“两点透视”错配，见勘误 |

- **5 条均达“两条独立机构来源（HTTP 200、正文直证）”；无“仅单源/完全不可得”条目，故本轮未触发替换。** `mannerism`、`beaux-arts`、`foreshortening` 三源年份值不同，均并列不合并；`foreshortening` 地点需按实际改为 Milan；`two-point-perspective` 手法与题目类别存在错配，权威级偏低。
- **回执（逐条子串校验，均 FOUND）**：
  - Palazzo del Te：官方站（P1）2/2；TheArtStory Mannerism（P2）2/2。
  - Palais Garnier：POP（G1）5/5；TheArtStory Beaux-Arts（G2）2/2。
  - Last Supper：Cenacolo 官方（L1）1/1；HISTORY（L2）4/4。
  - Lamentation：布雷拉官方（M1）7/7；Artchive（M2）3/3。
  - San Satiro：TheArtStory Bramante（S1）4/4；Artchive（S2）4/4。
  - **合计 34/34 关键句 FOUND（10 个主源全部 HTTP 200）。**

---

## 四、失败 / 未采用候选（备核，均不作证据）

| URL / 站点 | 结果 | 说明 |
| --- | --- | --- |
| `https://www.britannica.com/place/Palazzo-del-Te`、`/topic/Lamentation-over-the-Dead-Christ`、`/place/Santa-Maria-presso-San-Satiro` | **HTTPError(403)** | 首选百科被反爬拦截 |
| `https://www.parisjetaime.com/eng/culture/palais-garnier-p1296` | **HTTPError(403)** | 巴黎旅游官方被反爬 |
| `https://www.comune.milano.it/` | **HTTPError(403)** | 米兰市政府站被拦截 |
| `https://www.lombardiabeniculturali.it/` | **URLError/TLS 超时** | 伦巴第文保数据库不可达 |
| `https://www.metmuseum.org/art/collection/search/484650` | **HTTPError(429)** | 大都会博物馆限流（且非《最后的晚餐》本体） |
| `https://www.wikiart.org/en/andrea-mantegna/...` | **HTTPError(404)** | 目标页不存在/被拦 |
| `https://www.wga.hu/html_m/...`、`/art/...` | **200 但为“moved to a new address”空壳** | 旧路径全跳转提示页，无正文，弃用 |
| `https://www.newworldencyclopedia.org/entry/Mantegna`、`/entry/Donato_Bramante`、`/entry/Giulio_Romano` | **200 但仅搜索页/无目标正文** | 无本条目正文，弃用 |
| `https://www.artchive.com/artists/donato-bramante/`、`/artists/andrea-mantegna/...lamentation-of-christ/` | **HTTPError(404)** | 旧/猜测 slug 不存在；改用其 `/artwork/` 实页 |
| `https://www.turismo.milano.it/en/art-and-culture/churches/santa-maria-presso-san-satiro`、`https://yesmilano.it/en` | **200 但 JS 单页应用，无静态正文** | 需官方 API，本轮不取 |
| `https://www.fondazionepalazzodelte.it/`、`https://www.turismomanova.it/` | **SSL SSLV3_ALERT_HANDSHAKE_FAILURE** | 旧域 TLS 握手失败 |
| `https://www.italia.it/en/lombardy/mantua`（Palazzo Te 专页） | 无专页（仅 Ducal Palace / San Giorgio） | 目标页 404，全国旅游站无 Palazzo Te 专页 |
| Bing / DuckDuckGo / `web_search` | 反爬污染 / 端点无结果 | 检索命中区与他主题混杂，不可用 |
| 维基 `en.wikipedia.org/wiki/*` | **200** | 仅用于定位官方 URL / 事实坐标，**伞源同平台不计独立源**，未作证据 |

---

## 五、证据来源 URL 一览（本轮均已实际打开核验，HTTP 见行）

| # | URL | HTTP（字节） | 标题 / 机构 | 支撑 |
| --- | --- | --- | --- | --- |
| 1 | `https://www.centropalazzote.it/` | 200（109,879） | Palazzo Te · Fondazione Palazzo Te（官方） | mannerism 源① |
| 2 | `https://www.theartstory.org/movement/mannerism/` | 200（183,251） | Mannerism Movement Overview · TheArtStory | mannerism 源② |
| 3 | `https://www.pop.culture.gouv.fr/notice/merimee/PA00089004` | 200（321,280） | Théâtre national de l'Opéra, dit opéra Garnier · Ministère de la Culture（POP） | beaux-arts 源① |
| 4 | `https://www.theartstory.org/movement/beaux-arts-architecture/` | 200（151,313） | Beaux-Arts Architecture Movement Overview · TheArtStory | beaux-arts 源② |
| 5 | `https://cenacolovinciano.org/en/history/` | 200（118,873） | History · Museo del Cenacolo Vinciano（官方） | one-point 源① |
| 6 | `https://www.history.com/topics/renaissance/leonardo-da-vinci` | 200（521,912） | Leonardo da Vinci · HISTORY | one-point 源② |
| 7 | `https://pinacotecabrera.org/en/collezioni/collezione-on-line/cristo-morto/` | 200（99,012） | Lamentation over the Dead Christ · Pinacoteca di Brera（官方） | foreshortening 源① |
| 8 | `https://www.artchive.com/artwork/the-lamentation-over-the-dead-christ-andrea-mantegna-c-1490/` | 200（176,255） | The Lamentation over the Dead Christ（c.1490）by Andrea Mantegna · Artchive | foreshortening 源② |
| 9 | `https://www.theartstory.org/artist/bramante-donato/` | 200（143,720） | Donato Bramante · TheArtStory | two-point 源① |
| 10 | `https://www.artchive.com/artwork/santa-maria-presso-san-satiro-bramante-false-apse-donato-bramante-c-1482/` | 200（175,170） | Santa Maria presso San Satiro – false apse (c.1482) · Artchive | two-point 源② |
| — | `https://www.operadeparis.fr/en/visits/palais-garnier` | 200（732,948） | Visit the Palais Garnier · Opéra national de Paris | beaux-arts 官方旁证（不计两源） |
| — | `https://www.italia.it/en/lombardy/milan/da-vinci-last-supper-museum` | 200 | The Last Supper Museum in Milan · Italia.it | one-point 官方旅游旁证（不计两源） |
| — | `https://cenacolovinciano.org/en/` | 200（120,216） | Last Supper, Leonardo Da Vinci · Cenacolo Vinciano（官方首页） | one-point 旁证（书名+作者） |

---

## 六、落地提醒与诚实标注（只读，不改数据）

- 以上“可用”均为**建议**：须先把 10 条主源以 `verified=true` 登记进 `data/sources.json`，再改写对应条目的 `sources` 与 `sections.实例`（写入“名称/地点/设计者/年份”），同步 `pending_notes`/「待核实」，按需更新 `coverage.json` 源数，并复跑 `tools/check.py`。**本报告未修改任何条目数据或其它文件（本文件为唯一产出）。**
- **地点勘误（必须处理）**：`foreshortening` 任务给的“曼图亚”与实况不符——《哀悼基督》**现藏米兰布雷拉（Pinacoteca di Brera, Milan）**，两源直证 Milan / Palazzo Brera。落地务必把条目地点写为 **Milan（布雷拉）**，如需保留“曼图亚”应仅作为“曼特尼亚供职地/创作背景”注明，不得当作现藏地。
- **年份差异（据实并列，不强归）**：
  - `mannerism`：官方 1525–1535，TheArtStory 1524–1534，任务 1524–1534（通行）。落地可写“1524–1535（各源略有出入）”。
  - `beaux-arts`：POP 建造 campaign 1862 ; 1875（另 1923 列级），TheArtStory 1861-74，任务 1861–1875。若要求逐字落源，需注明“动工/落成口径不一”。
  - `foreshortening`：任务约 1480；布雷拉官方 c. 1483；Artchive c. 1490。三值并列，建议写“约 1480（另记 c.1483 / c.1490）”。
  - `one-point-perspective`：约 1495–1498（HISTORY 直书）；官方 Cenacolo 静态页未标年份，仅以场所+作者直证。
  - `two-point-perspective`：TheArtStory 1482-86（与任务一致），Artchive c.1482。
- **手法错配提示**：`two-point-perspective` 的 Santa Maria presso San Satiro“错觉合唱席”本质是**单点透视 + 浅浮雕 trompe-l'œil**，非两点透视。若该条必须严格示范“两点透视”，建议改用能一对多立面同现的实例（如“雅典学院”虽为一点、但可作对照；或另择街角建筑双灭点范例），并把本例移入“一点透视/错觉透视”条目。本报告按任务指定对象交付双源，仅作提示。
- **权威级提示**：`two-point-perspective`（San Satiro）两条主源均为艺术史教育/数据库（TheArtStory 中—强、Artchive 中），**未取得官方/博物馆一级源**（土耳其/米兰官方与文保站本轮多不可达）；如 lead 要求“至少一官方源”，此条需另寻或标“权威级偏低”。其余四条均含至少一条官方/政府/国立博物馆强权威源。
