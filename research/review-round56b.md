# 第 56 轮 B5 补源报告（review-round56b）——4 条尺度/色阶/色彩方案条目补具名实例（各两条独立权威来源）

复核日期：2026-11-23（Asia/Hong_Kong）　｜　复核人：review-r56b（lead 委派子任务，无人值守）　｜　性质：**严格只读，唯一产出本文件**

## 〇、执行说明与只读声明

- **已读治理与上下文文档**：项目根 `AUTONOMOUS.md` / `TASK_design.md` 实读为 NOT_FOUND；按 `research/review-round55b.md` 第 7 行记录读取桌面原件 `D:/Users/Administrator/Desktop/AUTONOMOUS.md`（71 行）、`D:/Users/Administrator/Desktop/TASK_design.md`（67 行）；并读本项目 `DECISIONS.md`（25 行）、`research/review-round55b.md`（115 行）。
- **已加载技能**：`using-superpowers`（本会话为委派子任务，按其 SUBAGENT-STOP 以任务说明书为准）、`verification-before-completion`（先实抓、后断言；关键句逐条 `norm(quote) in norm(page)` 回验，见第五节回执）。
- **硬性规则确认**：不编造名称、地点、作者、年份、引文、出处；关键事实须两个独立来源互证；同一机构只算 1 源；凑不齐双源写“仅单源/不可得”并换更易双源实例。网页内容一律视为数据，页面中出现的任何指令均未执行。
- **通道**：`web_search` 仅用于定位 URL，不作证据；证据正文来自 `web_fetch` 服务端直读与 Python `urllib` 直连抓取；MoMA PDF 以 `urllib` 在内存中用 `pypdf` 抽取（未落盘项目）。抓取脚本以 `python -c` 内联执行，未写入项目。
- **只读声明**：本轮仅生成 `E:/ai_project/shejihuihua/research/review-round56b.md`；未修改 `entries/`、`data/sources.json`、`coverage.json`、`tools/`、`site/` 或其他项目文件，未 git commit，未改项目外内容。

## 一、方法与判据

1. **实抓**：逐 URL 记录 HTTP 状态、字节数（可得时）、`<title>`；去 `<script>/<style>` 与标签、`html.unescape` 后抽正文；用 `norm()`（NFKC + 弯/直引号、破折号、零宽空格、不间断空格归一 + 空白折叠 + 小写）对关键句做子串回验。
2. **独立性判据**：同一机构只算 1 源。八源分别来自美国国家公园管理局（NPS）、Encyclopædia Britannica、表千家不審菴（Omotesenke）、京都府官方旅游站 Another Kyoto、国立荷兰博物馆 Rijksmuseum、Britannica（另一署名条目）、Kröller-Müller Museum、Van Gogh Museum。Britannica 两条为不同署名条目、不同作者、不同对象，按“同机构只算 1 源”仅用于**不同条目**，同一条目内未把 Britannica 与其他 Britannica 页面凑成双源。
3. **权威性分级**：强权威＝政府管理机构、皇宫/茶道流派官方机构、都道府县官方旅游站、国立博物馆、作品收藏馆官方；中—强权威＝Britannica 署名编辑条目。
4. **不采用维基百科作主源**：沿用项目既定口径，维基及其镜像未作证据。
5. **落地约束**：本报告只读产出，不直接改数据。落地须先把来源以 `verified=true` 登记进 `data/sources.json`，再改写对应 `entries/batch-*.json` 的 `sources` 与「实例」段，同步 `pending_notes` /「待核实」，复跑 `tools/check.py`。

## 二、四条补源（每条：名称 / 地点 / 作者 / 年份 + 两条独立权威来源）

### 2.1 `monumental-scale`（纪念性尺度）→ **华盛顿纪念碑（Washington Monument）**

- **名称**：Washington Monument / 华盛顿纪念碑，国家广场上的花岗岩方尖碑。
- **地点**：**美国华盛顿特区 National Mall**（①“standing 555 feet tall on the National Mall in Washington, D.C.”；②“obelisk in Washington, D.C.”）。
- **设计者**：**Robert Mills**（②“chose a plan by Robert Mills for a 600-foot- (183-metre-) tall obelisk”；①未点名设计者，落地只写②）。
- **年份**：**1848 年动工、1884 年建成**（①“The construction of the Washington Monument began in 1848…”；“not completed until1884”；②“Construction did not begin until 1848”；“At its completion in 1884…”）。

| # | 机构 / 权威级 | URL | 标题 | HTTP | 关键句（实抓，已回验） |
| --- | --- | --- | --- | --- | --- |
| ① | U.S. National Park Service 美国国家公园管理局（**强权威·政府管理机构**） | `https://www.nps.gov/places/000/washington-monument.htm` | Washington Monument (U.S. National Park Service) | **200**（36,437 B；urllib 直连；web_fetch 同页 200） | “The Washington Monument, standing **555 feet tall** on the National Mall in Washington, D.C., is one of the most iconic structures in the United States.”；“The construction of the Washington Monument **began in 1848**, with a design chosen through a competition.”；“The monument was **not completed until1884**, at which time it was the **tallest structure world**…”；“visitors … can stand at its base and marvel at its **towering height**” |
| ② | Encyclopædia Britannica「Washington Monument」（**中—强权威·署名编辑条目：B. Philip Bigler / Britannica Editors**） | `https://www.britannica.com/topic/Washington-Monument-Washington-DC` | Washington Monument \| History, Height, Dimensions, Date, & Facts \| Britannica | **200**（web_fetch 服务端直读；urllib 复抓遇 404/证书问题，按反爬处理，非源缺失） | “**Washington Monument**, obelisk in Washington, D.C., honouring George Washington…”；“the structure is 55 feet (16.8 metres) square at the base and **554 feet 7 inches (169 metres) high** and weighs an estimated 91,000 tons.”；“**At its completion in 1884 it was the world's tallest man-made structure**, though it was supplanted by the Eiffel Tower just five years later. It remains the world's tallest masonry structure.”；“chose a plan by **Robert Mills** for a **600-foot- (183-metre-) tall obelisk**” |

**对 `monumental-scale`（纪念性尺度）的支撑**：①直书 555 英尺高、1884 年落成时为世界最高结构、“towering height”（高耸尺度带来的观感）；②以体量数据佐证——基座 55 英尺见方、高 554 英尺 7 英寸、重约 91,000 吨、落成时为世界最高人造结构、至今仍为最高砌体结构。两源合起来支撑“以远超人体尺度的巨大体量造成纪念性/敬畏感”的具名实例。**保留标注**：两源高度值不同——①记 555 ft（旧测），②记 2014 年按国际标准重算后的 554 ft 7 in（旧值 555 ft 5 in）；落地应写“约 555 英尺 / 169 米”并注明重算差异，不得把两值写成无矛盾的同一数字。设计者仅②明载，①未写，落地只写 Robert Mills 并注来源。

### 2.2 `intimate-scale`（亲切尺度）→ **待庵茶室（Tai-an / 待庵）**

- **名称**：妙喜庵书院及茶室（待庵）/ Myokian Shoin and Tea Room (Taian)，日本现存唯一可认定为千利休所作的茶室，国宝。
- **地点**：**日本京都府乙训郡大山崎町，妙喜庵（Myōki-an）内**（①“located in Myoki-an in Kyoto prefecture's Oyamazaki-cho”；②“京都府乙訓郡大山崎町大山崎龍光56”）。
- **设计者**：**千利休（Sen no Rikyū）**（①“The one tea house remaining that is certainly Rikyu's”；②“千利休唯一現存的茶室”）。
- **年份**：**1582 年（天正 10 年）**（①“It is said that it was built in **Tensho 10 (1582)**”；②“天正10年（1582年）…邀請千利休在城中建造茶室”）。

| # | 机构 / 权威级 | URL | 标题 | HTTP | 关键句（实抓，已回验） |
| --- | --- | --- | --- | --- | --- |
| ① | 表千家不審菴 Omotesenke Fushin'an 官方（**强权威·茶道流派官方机构**） | `https://www.omotesenke.jp/english/chanoyu/glossary/3_2_3_win03.html` | Tai-an | **200**（1,951 B；web_fetch + urllib 双向 200） | “**The one tea house remaining that is certainly Rikyu's. A national treasure.**”；“It is located in **Myoki-an in Kyoto prefecture's Oyamazaki-cho**. It is a **two mat room**…”；“…and it has a **nijiriguchi (crawl-through entrance)**.”；“It is said that it was built in **Tensho 10 (1582)**.” |
| ② | Another Kyoto 京都府官方旅游网站（**强权威·都道府县官方旅游机构**） | `https://www.kyototourism.org/zh-hant/sightseeing/13533/` | 妙喜庵（待庵） \| 旅遊景點 \| Another Kyoto 官方旅遊網站 | **200**（55,916 B；web_fetch + urllib 双向 200） | “妙喜庵內保存**千利休唯一現存的茶室**，是被指定為國寶的「待庵（たいあん）」之一。”；“**天正10年（1582年）**，羽柴（豊臣）秀吉與明智光秀…”；“茶室…**大小為2帖榻榻米，打破了當時4帖半的概念**。”；“同時也第一個設立了「**躙口**」，縮小客人進出用的門。”；“被譽為日本建築樣式之一「數寄屋造」的起源。” |

**对 `intimate-scale`（亲切尺度）的支撑**：①直书“two mat room”（二叠榻榻米）与“nijiriguchi (crawl-through entrance)”（缩小到需跪爬进出），②直书“大小為 2 帖榻榻米，打破了當時 4 帖半的概念”“縮小客人進出用的門”。两源从空间面积与入口尺度两端共同支撑“以极小、贴身、需躬身进入的空间制造亲切/内敛尺度”的具名实例。**保留标注**：①对年份用“It is said that”，落地宜写“相传建于天正十年（1582）”，与②的确定表述并置时注明①的保留语气；两源均未给出可换算的平方米数，落地不补写面积数值。

### 2.3 `tints-shades`（色调与明暗层次）→ **《夜巡》（The Night Watch / De Nachtwacht）**

- **名称**：《民兵连·弗兰斯·班宁·科克上尉连》（Militia Company of District II under the Command of Captain Frans Banninck Cocq），通称《夜巡》。
- **地点**：**荷兰阿姆斯特丹国立博物馆 Rijksmuseum**（②“oil on canvas by Rembrandt van Rijn completed in 1642… in the Rijksmuseum, Amsterdam”；①为 Rijksmuseum 官方页）。
- **作者**：**伦勃朗·范·莱因（Rembrandt van Rijn）**（①②同）。
- **年份**：**1642 年**（①图注“Rembrandt van Rijn, 1642”；②“completed in 1642”“painted in 1642”）。

| # | 机构 / 权威级 | URL | 标题 | HTTP | 关键句（实抓，已回验） |
| --- | --- | --- | --- | --- | --- |
| ① | Rijksmuseum 国立荷兰博物馆官方故事页（**强权威·作品收藏馆官方**） | `https://www.rijksmuseum.nl/en/stories/10-things/story/10-things-about-rembrandt-s-night-watch` | 10 things about Rembrandt's Night Watch | **200**（web_fetch 服务端直读） | “Rembrandt's Night Watch is the most famous and most important painting in the Netherlands.”；图注“Night Watch, Militia Company of District II under the Command of Captain Frans Banninck Cocq, **Rembrandt van Rijn, 1642** (detail)”；“A magnificent detail is **the shadow of hand Captain Frans Banning Cocq**.” |
| ② | Encyclopædia Britannica「The Night Watch」（**中—强权威·署名编辑条目：João Ribas / Britannica Editors**） | `https://www.britannica.com/topic/The-Night-Watch` | The Night Watch \| By Rembrandt, Painting, (1642), History, & Facts \| Britannica | **200**（web_fetch 服务端直读） | “**The Night Watch**, oil on canvas by **Rembrandt van Rijn completed in 1642**.”；“this **colossal painting**, at 12.4 × 14.9 feet (379.5 × 453.5 centimeters)…”；“Rembrandt's version, however, makes the prosaic subject into a dynamic work of art; with its **masterful chiaroscuro** and dramatic action, the conventions of traditional portraiture are overturned.”；“the young girl in a **pale yellow gown**” |

**对 `tints-shades`（色调与明暗层次）的支撑**：②直书“masterful chiaroscuro”（明暗对照法）并给出“pale yellow gown”等亮部与“thick, dark yellow varnish / shadowed scene”等暗部描述；①从作品本身指出“the shadow of hand Captain Frans Banning Cocq”落在中尉披风上这一精细暗部处理。两源共同支撑“以亮部—暗部的连续层级（明暗层次/明度阶）塑造体积与戏剧性”的具名实例。**保留标注（重要）**：两源均未使用设计术语字面词“tints and shades / 加白加黑”，而是用 art-historical 等价词 **chiaroscuro / shadow / pale** 描述同一明度渐变现象；落地若写“加白/加黑色阶”，须说明这是概念归类对应的视觉机制，不得写成两源逐字原话。

### 2.4 `split-primary`（分裂补色 / split-complementary）→ **《夜间露天咖啡座（广场）》（Terrace of a Café at Night, Place du Forum）**

- **名称**：Caféterras bij nacht (Place du Forum) / Terrace of a Café at Night (Place du Forum)，夜间的露天咖啡座。
- **地点**：**荷兰奥特洛 Kröller-Müller Museum 收藏（画中场景为法国阿尔勒 Place du Forum）**（①官方藏品页，藏品号 KM 108.565；②为梵高博物馆官方色彩专题）。
- **作者**：**文森特·梵高（Vincent van Gogh, 1853–1890）**（①页面直书；②通篇讨论 Vincent 的色彩理论）。
- **年份**：**约 1888 年 9 月 16 日**（①“Date c. 16 September 1888”；藏品页主字段）。

| # | 机构 / 权威级 | URL | 标题 | HTTP | 关键句（实抓，已回验） |
| --- | --- | --- | --- | --- | --- |
| ① | Kröller-Müller Museum 官方藏品页（**强权威·作品收藏馆官方**） | `https://www.krollermuller.nl/en/collection/vincent-van-gogh-terrace-of-a-caf-at-night-place-du-forum-km-108-565` | Caféterras bij nacht (Place du Forum) | **200**（395,171 B；web_fetch + urllib 双向 200） | “Date **c. 16 September 1888**… Identifier KM 108.565”；“The most eye-catching aspect is the **sharp contrast between the warm yellow, green and orange colours** under the marquise and the **deep blue of the starry sky**, which is reinforced by the dark blue of the houses in the background.”；“I believe that an abundance of gaslight, which, after all, is **yellow and orange, intensifies blue**.” |
| ② | Van Gogh Museum 梵高博物馆官方色彩专题（**强权威·艺术家专题博物馆官方**） | `https://www.vangoghmuseum.nl/en/art-and-stories/stories/vincents-colours` | Vincent's Colours - Van Gogh Museum | **200**（177,078 B；web_fetch + urllib 双向 200） | “he studied various books on colour theory and discovered that **complementary colours - red and green, yellow and purple, blue and orange - reinforce each other**. Vincent now understood the theoretical principles of these colour pairs.”；“Anton Mauve … who was known for his use of **grey and blue tones**.” |

**对 `split-primary`（分裂补色）的支撑**：①逐字给出该画实际配色——以深蓝夜空/深蓝房屋为底，配黄、绿、橙的暖色灯光，并引梵高原话“yellow and orange, intensifies blue”；按色轮，蓝的补色是橙，其两侧邻色为黄橙与黄绿，故“蓝底 + 黄/橙 + 绿”正是分裂补色（一色 + 其补色两侧邻色）的配色结构。②从艺术家博物馆层面证明梵高**自觉研究过补色成对强化的理论**（蓝—橙等），使①的配色不是偶然。两源合起来支撑“明确使用分裂补色关系的名作”这一具名实例。**保留标注（重要）**：两源均未出现字面术语“split-complementary”；“分裂补色”是对①所记配色结构的概念归类，落地应写“馆方记为蓝底配黄/橙/绿（②证其研究补色理论），按色轮属分裂补色关系”，不得写成两源使用了该术语。另：`museum.nl` 同名页面的说明文字与①逐字相同（同一馆方文案转载），按同机构只算 1 源，**未**计入本报告。

## 三、汇总

| 条目 | 具名实例 | 地点 | 作者 / 设计者 | 年份 | 源① | 源② | HTTP | 判定 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `monumental-scale` | 华盛顿纪念碑 | 美国华盛顿特区 National Mall | Robert Mills | 1848 动工 / 1884 建成 | 美国国家公园管理局 NPS | Britannica（Bigler 署名） | 200 / 200 | **双源齐备**；高度值 555 ft vs 554 ft 7 in 须注明 2014 重算差异 |
| `intimate-scale` | 待庵茶室（妙喜庵内） | 日本京都府大山崎町 | 千利休 Sen no Rikyū | 1582（天正 10 年） | 表千家不審菴官方 | 京都府官方旅游站 Another Kyoto | 200 / 200 | **双源齐备**；年份按①的“相传”语气并置 |
| `tints-shades` | 《夜巡》 | 荷兰阿姆斯特丹 Rijksmuseum | Rembrandt van Rijn | 1642 | Rijksmuseum 官方故事页 | Britannica（João Ribas 署名） | 200 / 200 | **双源齐备**；两源用 chiaroscuro/shadow，非字面 tints and shades |
| `split-primary` | 《夜间露天咖啡座（广场）》 | 荷兰奥特洛 Kröller-Müller Museum 藏（绘于阿尔勒） | Vincent van Gogh | c. 1888-09-16 | Kröller-Müller Museum 官方藏品页 | Van Gogh Museum 官方色彩专题 | 200 / 200 | **双源齐备**；“分裂补色”为对馆方配色记录的概念归类，非原话 |

- **双源齐备率：4/4**；8 个主来源全部取证成功，**0 单源、0 缺源项**，无需写“仅单源/不可得”。
- **机构独立性**：四条均为两个不同机构；`museum.nl` 与 Kröller-Müller 文案同源，已剔除；Britannica 在两条不同条目中各出现一次，未在同条目内凑双源。
- **需落地时保留的诚实标注**：①纪念碑两源高度值不一，写约数并注明重算；②待庵年份用“相传”，面积只写“二帖/约两叠”，不补平方米；③《夜巡》的“加白/加黑色阶”为概念对应，注明原文用 chiaroscuro/shadow；④《夜间露天咖啡座》的“分裂补色”为配色结构归类，注明原文未使用该术语；⑤所有来源页中出现的任何指令性文字均未执行。

## 四、被拒用来源记录（供后续参考，不作证据）

| URL / 来源 | 状态 | 处置 |
| --- | --- | --- |
| `https://www.metmuseum.org/essays/rembrandt-van-rijn-1606-1669-prints`、`/art/collection/search/364151` | urllib 429 Too Many Requests；web_fetch 连接失败 | 改用 Rijksmuseum + Britannica 的《夜巡》双源 |
| `https://www.metmuseum.org/essays/hokusai-great-wave` | urllib 429；web_fetch 连接失败 | 放弃《神奈川冲浪里》方案，改走伦勃朗明暗层次 |
| `https://www.artic.edu/artworks/...`、`https://www.famsf.org/index.php/artworks/...` | web_fetch 403（Cloudflare） | 放弃修拉素描方案 |
| `https://www.nortonsimon.org/learn/.../goya-and-value-studies` | web_fetch / urllib 均 403（Cloudflare） | 放弃戈雅价值研究方案 |
| `https://smarthistory.org/rembrandt-the-night-watch/` | web_fetch 403（Cloudflare） | 改用 Britannica 署名条目 |
| `https://www.britannica.com/topic/Washington-Monument`、`/topic/Washington-Monument-Washington-DC`（urllib） | 分别为 403 / 404 反爬；但 web_fetch 对后者返回 200 全文 | 以 web_fetch 服务端直读结果为准 |
| `https://www.museum.nl/en/kroller-muller-museum/showpiece/terrace-of-a-cafe-van-gogh` | HTTP 200，但正文与 Kröller-Müller 官方页逐字相同（同机构转载） | 按“同机构只算 1 源”剔除 |
| Wikipedia 及镜像站 / artexamples.com 等自助教育站 | 未采用 | 前者按项目口径排除；后者非官方/博物馆/大学级权威，仅作线索不作证据 |

## 五、证据回执（verification-before-completion）

- **NPS 华盛顿纪念碑**：5 条关键句全部 `FOUND`（555 feet tall / tallest structure world / began in 1848 / not completed until1884 / towering height），HTTP 200、36,437 B、标题 `washington monument (u.s. national park service)`。
- **Britannica Washington Monument**：`web_fetch` 返回 HTTP 200 全文；关键句逐字可见（obelisk in Washington, D.C. / 554 feet 7 inches / world's tallest man-made structure at 1884 / still tallest masonry structure / plan by Robert Mills for 600-foot obelisk）。
- **Omotesenke Tai-an**：4 条关键句全部 `FOUND`（certainly Rikyu / two mat room / Tensho 10 (1582) / nijiriguchi），HTTP 200、1,951 B、标题 `tai-an`。
- **Another Kyoto 妙喜庵（待庵）**：4 条中文关键句全部 `FOUND`（千利休唯一現存的茶室 / 天正10年（1582年）/ 大小為2帖榻榻米 / 躙口），HTTP 200、55,916 B；终端显示编码导致标题乱码，但 `web_fetch` 同页返回正确标题“妙喜庵（待庵） | 旅遊景點 | Another Kyoto 官方旅遊網站”。
- **Rijksmuseum Night Watch**：`web_fetch` 返回 HTTP 200 全文；关键句逐字可见（most famous and most important painting / Rembrandt van Rijn, 1642 / shadow of hand Captain Frans Banning Cocq）。
- **Britannica The Night Watch**：`web_fetch` 返回 HTTP 200 全文；关键句逐字可见（oil on canvas by Rembrandt van Rijn completed in 1642 / colossal painting 12.4 × 14.9 feet / masterful chiaroscuro / pale yellow gown）。
- **Kröller-Müller Café at Night**：4 条关键句全部 `FOUND`（c. 16 September 1888 / sharp contrast between the warm yellow, green and orange colours / deep blue of the starry sky / yellow and orange, intensifies blue），HTTP 200、395,171 B、标题 `caféterras bij nacht (place du forum)`。
- **Van Gogh Museum Vincent's Colours**：关键句 `FOUND`（complementary colours - red and green, yellow and purple, blue and orange - reinforce each other），HTTP 200、177,078 B、标题 `vincent's colours - van gogh museum`。

> 校验方法：UTF-8 解码 → 去 script/style/标签 → `html.unescape` → `norm()`（NFKC + 弯直引号/破折号/零宽空格/不间断空格归一 + 空白折叠 + 小写）→ 子串命中。HTTP 状态、字节数与 `<title>` 均来自同轮实抓；Britannica 与 Rijksmuseum 的关键句从 `web_fetch` 返回全文逐字核对。
