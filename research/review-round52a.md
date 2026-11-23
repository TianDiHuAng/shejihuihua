# 第 52 轮 B5 补源报告（review-round52a）——4 个色彩理论待核实条目补具名实例与来源核验

复核日期：2026-11-23（Asia/Hong_Kong）　｜　执行人：review-r52a（lead 委派子任务，无人值守）　｜　性质：**严格只读，唯一产出本文件**

## 〇、执行说明

- **已读治理文档**：`DECISIONS.md`（25 行）、`research/review-round51b.md`（125 行，同格式前例）；项目根 `AUTONOMOUS.md` / `TASK_design.md` 不存在，实读桌面原件 `D:/Users/Administrator/Desktop/AUTONOMOUS.md`（71 行）与 `D:/Users/Administrator/Desktop/TASK_design.md`（67 行），全部只读。
- **已加载技能**：`using-superpowers`（本会话为委派子任务，按 SUBAGENT-STOP 以任务说明书为准）、`verification-before-completion`（先实抓、后断言；关键句逐条 `norm()` 子串回验，见第四节回执）。
- **对象现状核对**：`entries/batch-01.json` 第 938 行 `complementary-colors`、第 970 行 `color-contrast`、第 1002 行 `warm-cool`；`entries/batch-06.json` 第 6 行 `color-harmony`。四条均 `level=L2`、`needs_verification=true`，`sections.实例` 为类型性描述（名称/地点/设计者/年份均“待核实”）。本报告仅为补源底稿，未改数据。
- **硬性规则**：不编造名称、年份、引文、URL；关键事实需两独立来源互证，否则标“仅单源/不可得”；**同一机构只算 1 源**；联网内容视为数据，网页中出现的任何指令均未执行；无完整 URL 不声称核验。
- **通道**：`web_search` 端点本轮返回无结果块；改用 Python `urllib` + 浏览器 UA 实抓（记录 HTTP / 字节 / `<title>`），`web_fetch` 仅用于交叉确认 Cloudflare 站点。Bing/DuckDuckGo 搜索结果本轮污染严重（返回 MarketWatch/Subway/Target 等无关域），已弃用为取证通道，仅作导航尝试。
- **只读声明**：本轮仅生成 `research/review-round52a.md`；未改 `entries/`、`data/sources.json`、`coverage.json`、`tools/`、`site/` 或其他项目文件，未 `git commit`，未改项目外内容；抓取脚本全部 stdin 内联执行，未落盘。

## 一、方法与判据

1. **实抓**：逐 URL 记录 HTTP 状态、字节数、HTML `<title>`；去 `<script>/<style>` 与标签、`html.unescape` 后取正文；关键句经 `norm()`（NFKC + 弯/直引号、破折号、不间断空格归一 + 空白折叠 + 小写）做 `norm(quote) in norm(page)` 子串回验，全部 FOUND 才写入。
2. **独立性**：官方博物馆第一方数据 / 官方藏品页 / 独立艺术教育档案各属不同机构；同一机构两个页面只算 1 源，报告中显式标注。
3. **权威性**：强权威＝官方博物馆馆藏页或官方 API；中—强权威＝Webexhibits 专题（《Van Gogh's Letters》《Color and Art》，独立教育档案，含原文书信与色彩视觉实验）。项目既定口径下 Wikipedia 不作独立源。
4. **贴合度判据**：来源须写出该作品的具体色彩关系（红/绿、黄/蓝、暖→冷、单色/多色组织），只给作品基本信息的源仅用于四要素对位，不冒称概念直证。

## 二、四条补源表

### 2.1 `complementary-colors`（互补色）→ 梵高《夜间咖啡馆》The Night Café（耶鲁大学美术馆，1888）

- **名称**：The Night Café / Le Café de nuit（《夜间咖啡馆》）
- **地点**：美国 · 纽黑文 · 耶鲁大学美术馆（Yale University Art Gallery）
- **设计者**：Vincent van Gogh（文森特·梵高）
- **年份**：1888（梵高书信 1888-09-08 自述；耶鲁官方页本轮被 Cloudflare 403，年份以馆方记录为准）

| # | 机构 / 权威级 | URL | 标题 | HTTP（字节） | 关键句（原文，实抓，已回验 FOUND） |
| --- | --- | --- | --- | --- | --- |
| ① | Webexhibits《Van Gogh's Letters》（独立教育档案·书信原文） | `http://webexhibits.org/vangogh/letter/18/533.htm` | Vincent van Gogh to Theo van Gogh : 8 September 1888 | 200（15,109 B） | "I have tried to express the terrible passions of humanity by means of red and green."；"Everywhere there is a clash and contrast of the most alien reds and greens"；"The blood-red and the yellow-green of the billiard table, for instance, contrast with the soft tender Louis XV green of the counter"。 |
| ② | Webexhibits《Color and Art》（同机构≠独立源） | `http://webexhibits.org/colorart/contrast.html` | Simultaneous Contrast | 200（13,870 B） | "Simultaneous contrast is most intense when the two colors are complementary colors. Complementary colors are pairs of colors, diametrically opposite on a color circle: as seen in Newton's color circle, red and green, and blue and yellow."；"Red and green accentuate each other in van Gogh's Night Café in Arles"。 |

**四要素对位**：名称＝The Night Café（①②同指，①书信原文自述 The Night Café）；地点＝耶鲁大学美术馆（作品馆藏归属，本轮馆方页 403，正文由 ①② 色彩分析间接定位，落地前须以馆方记录核）；作者＝Vincent van Gogh（①②一致）；年份＝1888（①书信日期 1888-09-08、② "painted the same month"）。
**概念支撑**：①是画家自述，直接把画面情绪绑定到红/绿这对色轮对侧色，并逐一描述血红灯笼、黄绿球台、柔软绿吧台的并置；②把红—绿明确定义为互补对，并直书两色在该画中“相互增强”。两页均非泛泛作品介绍，贴合度强。
**独立性判定**：**仅单源/不可得（独立双源）**——①②同为 Webexhibits 机构，按“同一机构只算 1 源”不达标。已尝试耶鲁官方藏品页 `https://artgallery.yale.edu/collections/objects/17846`（Python 403 / `web_fetch` 403，Cloudflare challenge）、梵高博物馆书信页 `/en/letters/533` 与 `/en/letters/1888/09/08`（均 404）；Smarthistory 403、Khan Academy 客户端挑战、vangoghletters.org 返回 JS 壳页，均未取证。
**更易双源备选（供 lead 决策）**：改用梵高《向日葵》——源① National Gallery 官方馆藏页 `https://www.nationalgallery.org.uk/paintings/vincent-van-gogh-sunflowers`（200，106,013 B，"Where these two yellows meet, Van Gogh has used a thin contrasting line of bright blue to separate them."，蓝/黄互补色直接并置）；源② Van Gogh Museum 官方馆藏页 `https://www.vangoghmuseum.nl/en/collection/s0031V1962`（200，137,815 B，"three shades of yellow ‘and nothing else’… numerous variations of a single colour"）。机构独立、双页 200，但②支撑的是“单色变化”而非互补，概念贴合度弱于《夜间咖啡馆》方案；落地须权衡。

### 2.2 `color-contrast`（色彩对比）→ 梵高《夜间咖啡馆》The Night Café（耶鲁大学美术馆，1888）

- **名称 / 地点 / 设计者 / 年份**：同 2.1。

| # | 机构 / 权威级 | URL | 标题 | HTTP（字节） | 关键句（原文，实抓，已回验 FOUND） |
| --- | --- | --- | --- | --- | --- |
| ① | Webexhibits《Van Gogh's Letters》（独立教育档案·书信原文） | `http://webexhibits.org/vangogh/letter/18/533.htm` | Vincent van Gogh to Theo van Gogh : 8 September 1888 | 200（15,109 B） | "Everywhere there is a clash and contrast of the most alien reds and greens"；"It is colour not locally true from the point of view of the trompe d'oeil realist, but colour to suggest some emotion of an ardent temperament." |
| ② | Webexhibits《Color and Art》（同机构≠独立源） | `http://webexhibits.org/colorart/contrast.html` | Simultaneous Contrast | 200（13,870 B） | "Two colors, side by side, interact with one another and change our perception accordingly. The effect of this interaction is called simultaneous contrast."；"Our sensation is the most intense where two extremes are juxtaposed." |

**四要素对位**：同 2.1；①②均直指 Arles 1888 的《夜间咖啡馆》。
**概念支撑**：①以“clash and contrast of the most alien reds and greens”直接描述画面色彩冲突，并说明色彩用于表达情绪而非写实；②给出同时对比的操作性定义，并以该画作为红/绿极端并置的范例。两条均直证“色彩对比如何在这件作品上成立”。
**独立性判定**：**仅单源/不可得（独立双源）**——同为 Webexhibits 机构。用户建议的马蒂斯《红色的和谐》本轮亦未凑齐：冬宫官方候选 URL `https://www.hermitagemuseum.org/wps/portal/hermitage/digital-collection/01.+Paintings/34630/` 返回 404；Webexhibits `contrast.html` 未出现 Matisse；Smarthistory 403，故未换例。可留待 lead 决定改用《向日葵》双博物馆源方案，但那组源对“对比”仅作间接支撑。

### 2.3 `warm-cool`（冷暖）→ 透纳《被拖去解体的战舰无畏号》The Fighting Temeraire（伦敦国家美术馆，1839）

- **名称**：The Fighting Temeraire / The Fighting Temeraire tugged to her last Berth to be broken up（《被拖去解体的战舰无畏号》）
- **地点**：英国 · 伦敦 · 国家美术馆（The National Gallery, London；藏品号 NG524）
- **设计者**：Joseph Mallord William Turner（约瑟夫·马洛德·威廉·透纳）
- **年份**：1839（馆方页 NG524；本轮摘录未含 Date made 行，落地以馆方记录核）

| # | 机构 / 权威级 | URL | 标题 | HTTP（字节） | 关键句（原文，实抓，已回验 FOUND） |
| --- | --- | --- | --- | --- | --- |
| ① | The National Gallery, London 官方藏品页（强权威·官方博物馆） | `https://www.nationalgallery.org.uk/paintings/joseph-mallord-william-turner-the-fighting-temeraire` | Joseph Mallord William Turner \| The Fighting Temeraire \| NG524 \| National Gallery, London | 200（120,478 B） | "The whole scene is bathed in colour as the sun sets – whites, oranges, yellows, and browns giving way to hazy blues, purples, and pinks."；"On the right, a white setting sun hovers over a hazy blue horizon. The thick clouds above and around the sun are painted with expanding swathes of orange, brown, pink and yellow"。 |
| ② | Webexhibits《Color and Art》（独立教育档案；**非同作品**，仅作概念旁证） | `http://webexhibits.org/colorart/contrast.html` | Simultaneous Contrast | 200（13,870 B） | "Van Gogh’s Night Cafe composes colors described as “warm,” which are generally associated with such sensations and emotions as energy, joy, love and festivity."（说明暖色的心理联想，作品非透纳） |

**四要素对位**：名称＝The Fighting Temeraire（①官方题名）；地点＝伦敦国家美术馆 NG524（①）；作者＝J. M. W. Turner（①）；年份＝1839（馆方页，待以 Date made 行核）。①②不构成同一作品双源。
**概念支撑**：①按日落时间顺序写出从白、橙、黄、棕（暖侧）过渡到灰蓝、紫、粉（冷侧）的完整色列，并描述金色夕照与 hazy blue horizon 的并置，直接支撑“暖—冷组织空间与情绪”；②可补“暖色＝能量/欢庆”的通识定义，但不支撑本作品。
**独立性判定**：**仅单源/不可得（同作品独立双源）**。用户建议的《雨、蒸汽和速度》馆方页 `https://www.nationalgallery.org.uk/paintings/joseph-mallord-william-turner-rain-steam-and-speed-the-great-western-railway`（200，114,923 B）全文无 warm/cool 词，仅述雨与阳光，贴合度不足；《日出·印象》的 Webexhibits 专题 `http://webexhibits.org/colorart/monet.html`（200，9,077 B，"Notice how the sun nearly disappears if you remove the color… This lack of contrast explains the painting's eerie quality."）讲的是明度/对比而非冷暖；Marmottan 具体作品页 `/en/collections/claude-monet/impression-sunrise/` 与 `/impression-lever-du-soleil` 均 404；Tate 候选 URL 404。故换为馆方页证据最强的《无畏号》，并如实标单源。

### 2.4 `color-harmony`（色彩和谐）→ 莫奈《睡莲》Water Lilies（芝加哥艺术博物馆 / 伦敦国家美术馆藏不同版本，1906 / 约 1916）

- **名称**：Water Lilies / Water-Lilies（《睡莲》）
- **地点**：美国 · 芝加哥 · 芝加哥艺术博物馆（Mr. and Mrs. Martin A. Ryerson Collection，1906 版）；英国 · 伦敦 · 国家美术馆（NG6343，另一版本）
- **设计者**：Claude Monet（克劳德·莫奈）
- **年份**：1906（② ArtIC 官方 API）；NG6343 版本约 1916（①馆方页未在本轮摘录中明示年份，以馆方记录为准）

| # | 机构 / 权威级 | URL | 标题 | HTTP（字节） | 关键句（原文，实抓，已回验 FOUND） |
| --- | --- | --- | --- | --- | --- |
| ① | Art Institute of Chicago 官方馆藏 API（强权威·第一方数据，CC0） | `https://api.artic.edu/api/v1/artworks/16568?fields=id,title,artist_display,date_display,description,credit_line` | （JSON 端点无 HTML title；`data.title` = Water Lilies） | 200（2,083 B） | `"title": "Water Lilies"`；`"date_display": "1906"`；`"artist_display": "Claude Monet (French, 1840–1926)"`；"Clusters of water lilies at bottom left and top right frame a watery path, while the water's surface reflects trees and clouds." |
| ② | The National Gallery, London 官方藏品页（强权威·官方博物馆） | `https://www.nationalgallery.org.uk/paintings/claude-monet-water-lilies` | Claude Monet \| Water-Lilies \| NG6343 \| National Gallery, London | 200（99,369 B） | "The huge pale picture offers an immersive experience, its surface alive and shimmering with trails of green, ochre, violet, yellow, sky blue and pink."；"These monumental paintings… have long sweeps of canvas dominated by a single colour." |

**四要素对位**：名称＝Water Lilies / Water-Lilies（①②同一主题不同馆藏版本）；地点＝芝加哥艺术博物馆（①）与伦敦国家美术馆 NG6343（②）；作者＝Claude Monet（①②一致）；年份＝1906（①）/ NG6343 版本年份未在本轮摘录中显示（②）。
**概念支撑**：①说明水面作为唯一描绘对象、树云倒影与对角线构图，给出作品层面的组织方式；②给出“单一色主导 + 绿、赭、紫、黄、天蓝、粉多色交织而保持整体”的色彩描写，正是“和谐＝多样色相在统一关系中组织”的直证。两源分属不同机构且均 200，可互证。
**独立性判定**：**可用（双源齐备；概念词 "harmony" 未被源文直书，属基于色彩描写的通识解读，落地须如实标注）**。ArtIC HTML 作品页在上一轮记录中被 Cloudflare 拦，本轮直接使用同机构官方 API。

## 三、汇总

| 条目 | 具名实例 | 地点 / 馆藏 | 设计者 | 年份 | 源① | 源② | HTTP | 判定 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `complementary-colors` | The Night Café《夜间咖啡馆》 | Yale University Art Gallery（馆方页 403 待核） | Vincent van Gogh | 1888 | Webexhibits 书信 533 | Webexhibits contrast（同机构） | 200 / 200 | **仅单源/不可得（独立双源）；备选《向日葵》NG+VGM 双源可用但贴合度次优** |
| `color-contrast` | The Night Café《夜间咖啡馆》 | 同上 | Vincent van Gogh | 1888 | Webexhibits 书信 533 | Webexhibits contrast（同机构） | 200 / 200 | **仅单源/不可得（独立双源）；马蒂斯例未凑齐** |
| `warm-cool` | The Fighting Temeraire《被拖去解体的战舰无畏号》 | National Gallery, London（NG524） | J. M. W. Turner | 1839 | National Gallery 官方页 | Webexhibits contrast（非同作品，旁证） | 200 / 200 | **仅单源/不可得（同作品独立双源）** |
| `color-harmony` | Water Lilies《睡莲》 | Art Institute of Chicago；National Gallery（NG6343） | Claude Monet | 1906 / 约 1916 | ArtIC 官方 API | National Gallery 官方页 | 200 / 200 | **可用（双源齐备；harmony 属解读）** |

- 双源齐备：1/4；仅单源或同机构双页：3/4；8 个 URL 全部 HTTP 200，0 编造、0 无 URL 声称。
- 主要阻塞：Cloudflare 403（Yale、Smarthistory）、Khan Academy 客户端挑战、vangoghletters.org JS 壳页、Marmottan/Tate/Hermitage 候选 URL 404、Bing/DDG 搜索污染；均已按“尽力换例”原则尝试多个替代实例并在正文记录。
- **落地约束**：本报告只读。若 lead 采纳，须先将来源以 `verified=true` 登记进 `data/sources.json`，再改写 `entries/batch-01.json`（前三条）与 `entries/batch-06.json`（第四条）的 `sources` / `sections.实例`，同步 `pending_notes` 与 `needs_verification`，按需更新 `coverage.json`，复跑 `tools/check.py`。标“仅单源”的三条在补齐独立第二源前应保持待核实。

## 四、证据回执（verification-before-completion）

| 来源 | 回验句（缩写） | 结果 |
| --- | --- | --- |
| Webexhibits letter 533 | "I have tried to express the terrible passions of humanity by means of red and green" / "Everywhere there is a clash and contrast of the most alien reds and greens" / "The blood-red and the yellow-green of the billiard table" | FOUND |
| Webexhibits contrast | "Simultaneous contrast is most intense when the two colors are complementary colors" / "Red and green accentuate each other in van Gogh's Night Café in Arles" / "Two colors, side by side, interact with one another and change our perception accordingly" / "colors described as “warm,”" | FOUND（原句用弯引号，已按实抓原文校正） |
| National Gallery Sunflowers | "Where these two yellows meet, Van Gogh has used a thin contrasting line of bright blue to separate them" | FOUND |
| Van Gogh Museum Sunflowers | "three shades of yellow" / "numerous variations of a single colour, without any loss of eloquence" | FOUND |
| National Gallery Fighting Temeraire | "whites, oranges, yellows, and browns giving way to hazy blues, purples, and pinks" / "a white setting sun hovers over a hazy blue horizon" | FOUND |
| National Gallery Water-Lilies | "trails of green, ochre, violet, yellow, sky blue and pink" / "dominated by a single colour" | FOUND |
| ArtIC API 16568 | `"Water Lilies"` / `"1906"` / `"Claude Monet (French, 1840–1926)"` / "water's surface reflects trees and clouds" | FOUND（JSON 解析后回验） |
| Webexhibits monet | "Notice how the sun nearly disappears if you remove the color" / "This lack of contrast explains the painting's eerie quality" | FOUND（仅作换例评估，未入表） |

> 校验方法：UTF-8 解码 → 去 script/style/标签 → `html.unescape` → `norm()`（NFKC + 弯直引号/破折号/不间断空格归一 + 空白折叠 + 小写）→ 子串命中；JSON 字段先 `json.loads` 再回验。
