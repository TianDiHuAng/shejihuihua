# 第 37 轮返工补源报告（review-round37）——arts-crafts / monumental-scale / rule-of-odds 各补两条独立权威来源

复核日期：2026-11-23（Asia/Hong_Kong）　｜　复核人：review-r37（lead 委派子任务，无人值守）　｜　性质：**严格只读，唯一产出本文件**

## 〇、执行说明与只读声明

- **已读治理文档**：`D:/Users/Administrator/Desktop/AUTONOMOUS.md`（71 行）、`D:/Users/Administrator/Desktop/TASK_design.md`（67 行）（项目根无同名文件，位于桌面，**只读**）；`E:/ai_project/shejihuihua/DECISIONS.md`；格式参照 `research/review-round29.md`。TASK_design 硬性规则确认：**关键事实至少两个独立来源互相印证，否则标“待核实”；只能引用 verified=true 的来源；不编造数字/日期/人名/引文/出处**。
- **已加载技能**：`using-superpowers`（本会话为委派子任务，按其 SUBAGENT-STOP 以本任务说明书为准）、`verification-before-completion`（全部结论先实抓证据、后下断言）。
- **数据快照（本轮实读 `entries/batch-37.json`，只读）**：三条目标条目现用来源**全部为维基伞源**、`needs_verification=true`——`monumental-scale`＝`wp-proportion-architecture`、`wp-architecture`；`arts-crafts`＝`wp-architectural-style`、`wp-history-of-architecture`；`rule-of-odds`＝`wp-composition-visual-arts`、`wp-rule-of-thirds`。故本轮为三条各补**两条机构互不相同的独立权威来源**。
- **只读声明**：本轮**仅生成** `research/review-round37.md` 一个文件；**未修改** `entries/`、`data/sources.json`、`coverage.json`、`tools/`、`site/` 或任何其他项目文件，未 `git commit`，未改项目文件夹之外内容（桌面治理文档仅只读）。抓取全部以 `python urllib` 临时进程完成，未落盘项目文件。**联网内容一律按“数据”处理，网页中出现的任何指令均未执行。**

## 一、方法与判据

1. **实抓**：Python 3 `urllib` + 浏览器 UA（`Chrome/124`，`Accept/Accept-Language/Upgrade-Insecure-Requests` 齐备，`ssl` 不校验证书），逐 URL 记录 **HTTP 状态、字节数、`<title>` 与正文关键句**；页面按响应头 `charset` 解码。
2. **独立性判据**：排除维基镜像（owiki / wikiwand / wikipedia 同平台计 1 源）；同一机构只算 1 源；三条各用**两个互不相同的机构/平台**。
3. **权威性分级（显式标注，供 lead 取舍）**：**强权威**＝官方机构／大学 OER／博物馆；**中权威**＝权威行业/专业教育媒体（真实、独立、可核验，但非官方/大学）。
4. **落地约束**：本报告只读产出，**不能直接改数据**。凡判“可用”，落地须先把来源以 `verified=true` 登记进 `data/sources.json`，再改写对应 `entries/*.json` 的 `sources` 并同步 `pending_notes`/「待核实」，复跑 `check.py`；登记前不得视为已改。
5. **HTTP 说明**：Britannica（403）、Adobe（403）、Nikon（403）、Tate（连接挂起）、Met（URLError）、Smarthistory（403）、MasterClass（403）等对本环境 urllib 返回拦截或挂起；已按任务授权“403 则改用其他官方/大学”转用可实抓 200 的官方/大学/教育权威，**不编造、不以失败路径冒充证据**（失败候选见第六节）。

---

## 二、`arts-crafts`（工艺美术运动）——两条独立权威来源

| # | 机构 / 权威级 | URL | 标题 | HTTP | 关键句（原文，实抓） |
| --- | --- | --- | --- | --- | --- |
| 1 | 英国维多利亚与艾尔伯特博物馆 V&A（**强权威·官方博物馆**） | `https://www.vam.ac.uk/articles/arts-and-crafts-an-introduction` | Arts and Crafts: an introduction · V&A | **200**（74038 B） | “This was a reaction to not only **the damaging effects of industrialisation** but also the relatively low status of the decorative arts.”；“But it was **not until the 1860s and '70s** that new approaches in architecture and design were championed…”；“The Movement took its name from the **Arts and Crafts Exhibition Society, a group founded in London in 1887**…” |
| 2 | TheArtStory（**中—强权威·权威艺术史教育机构**） | `https://www.theartstory.org/movement/arts-and-crafts/` | The Arts & Crafts Movement Overview \| TheArtStory | **200**（142567 B） | “The Arts & Crafts **emerged in the United Kingdom around 1860** … the spread of the Arts & Crafts across the Atlantic to the United States in the 1890s, enabled it to last longer — **at least into the 1920s**.”；“…the connection forged between the artist and his work through **handcraft** was the key to producing both human fulfillment and beautiful items…”；“‘Have nothing in your house you do not know to be useful or believe to be beautiful,’ **William Morris** said.” |

**三要素对位（Morris / 反工业 / 手工艺）**：反工业＝V&A“damaging effects of industrialisation”；手工艺＝TheArtStory“connection…through handcraft”；William Morris＝TheArtStory 直接点名并引其名言（Red House 1859–60 由 Philip Webb 与 William Morris）。**两源机构互不相同（V&A 国家博物馆 + TheArtStory 艺术史教育），均 HTTP 200、正文直证，可作独立双源。**

---

## 三、`monumental-scale`（纪念性尺度）——两条独立权威来源

| # | 机构 / 权威级 | URL | 标题 | HTTP | 关键句（原文，实抓） |
| --- | --- | --- | --- | --- | --- |
| 1 | Humanities LibreTexts（University of the Pacific 课程，Michael Leonard 编写，CC BY，**强权威·大学 OER**） | `https://human.libretexts.org/Courses/University_of_the_Pacific/Two_Dimensional_Design_and_Color/11:_Size_and_Scale` | 11: Size and Scale - Humanities LibreTexts | **200**（133222 B） | “**Large works of art may invoke a monumentality through its sheer size and scale. Monumentality evokes an aura of greatness, a sense of power and gravity that demands public attention.**”；“When art installations are created on a grand scale… they may promote an idea or ideal; **the art may promote the power of an individual or political party**…” |
| 2 | ArchDaily（Hana Abdel，2020-10-30，**中权威·建筑专业媒体**） | `https://www.archdaily.com/950403/built-nature-when-architecture-challenges-human-scale` | Built Nature: When Architecture Challenges Human Scale \| ArchDaily | **200**（786621 B） | “Going beyond human scale is not a novelty. **For centuries, builders, engineers, and architects have been creating monumental edifices to mark spirituality or political power. Larger than life palaces, governmental buildings, or temples have always attracted people’s admiration and reverence**…” |
| 备选 | Fiveable（Intro to Humanities，教育平台·中权威） | `https://fiveable.me/introduction-humanities/key-terms/monumental-scale` | Monumental Scale in Intro to Humanities \| Fiveable | **200**（306955 B） | “**Monumental scale means art or architecture is made deliberately grand, oversized, or towering to create awe.**”；“…it often shows how churches, rulers, or empires **used form to project power**.” |

**三要素对位（宏大尺度 / 崇高 / 权力感）**：LibreTexts 直述“monumentality…aura of greatness, a sense of power and gravity”“promote the power of an individual or political party”——同时命中“崇高＋权力感”；ArchDaily 直述“creating monumental edifices to mark spirituality or political power…admiration and reverence”——命中“权力/精神崇高”。**两源机构互不相同（大学 OER + 建筑专业媒体），均 HTTP 200、正文直证；Fiveable 作第三条备选（同为 200，定义“grand, oversized, towering to create awe…project power”）。**

---

## 四、`rule-of-odds`（奇数法则）——两条独立权威来源

| # | 机构 / 权威级 | URL | 标题 | HTTP | 关键句（原文，实抓） |
| --- | --- | --- | --- | --- | --- |
| 1 | Digital Photography School（dPS，Rick Ohnsman，**中—强权威·权威摄影教育媒体**） | `https://digital-photography-school.com/the-rule-of-odds-in-photography-an-easy-trick-for-better-compositions/` | The Rule of Odds in Photography (An Easy Trick for Better Compositions) | **200**（198510 B） | “**The rule of odds states that, whenever possible, a composition should have an odd number of objects, not an even number of objects.** So an image should have three flowers rather than two, and five people rather than four.”；“It’s all about arranging your subjects in odd numbers to craft compositions that are naturally more pleasing to the eye.” |
| 2 | ExpertPhotography（Sarah Rodriguez-Martinez，**中权威·权威摄影教育媒体**） | `https://expertphotography.com/rule-of-odds-photography` | Rule of Odds in Photography: Examples and Composition Tips | **200**（101952 B） | “**The rule of odds in photography is a composition guideline that suggests using an odd number of main subjects, often three or five.**”；“**Canon’s composition guide also recommends trying small groups of three or five.**” |
| 备选 | Lightstalking（摄影教育媒体·中权威） | `https://www.lightstalking.com/rule-of-odds/` | A Quick Beginners Guide To The Rule Of Odds - What Is It And How To Use It | **200** | “**The rule of odds is all about using that psychological condition of the human brain in order to make some really interesting and pleasant composition in photography.**”；“we are really talking about limiting your compositional elements to **3 or possibly 5**.” |

**三要素对位（奇数 / 构图 / 视觉平衡）**：DPS 给出定义“odd number of objects, not an even number…naturally more pleasing”；ExpertPhotography 给出“odd number of main subjects, often three or five”并引 Canon 构图指南佐证。**两源机构互不相同（dPS + ExpertPhotography），均 HTTP 200、正文直证；Lightstalking 作第三条备选（200）。**（Adobe / Nikon 官方页面本环境返回 403，见第六节。）

---

## 五、历史时期确认：工艺美术运动（19 世纪后期，约 1860s–1910s）

- **结论：成立，且属“19 世纪后期”。** 两条独立权威来源一致支持**起始约 1860 年代**：
  - V&A：**“it was not until the 1860s and '70s** that new approaches in architecture and design were championed…”，且 1887 年成立 Arts and Crafts Exhibition Society 正式得名。
  - TheArtStory：**“emerged in the United Kingdom around 1860**…spread…to the United States in the 1890s, enabled it to last longer — **at least into the 1920s**.”
- **诚实标注（细微差）**：主体兴起于 19 世纪后期（约 1860s 起）、盛行于 19 世纪末至 20 世纪初（英国约至 1910 年前后）这一常用窗口**基本成立**；但运动在美国延续到 **1920 年代**，故更稳妥表述为“**约 1860 年代兴起，盛行于 19 世纪后期至 20 世纪初（英国约至 1910 年前后，美国延续至 1920 年代）**”，不把上限定死为 1910s。
- **与现有 scope 的关系**：`scope.md` 该条时期桶为“文艺复兴至19世纪”，19 世纪落在桶内、不冲突；本条回填时应把**具体历史时期**写作上述“约 1860s 起 / 19 世纪后期—20 世纪初”，而非只留桶名。

---

## 六、失败/未采用候选（备核，均不作证据）

| URL / 站点 | 结果 | 说明 |
| --- | --- | --- |
| `https://www.britannica.com/art/Arts-and-Crafts-movement` | **403** | 目标首选百科，被反爬拦截 |
| `https://www.britannica.com/art/monument-architecture`、`/topic/monument`、`/art/monumental-architecture` | **403** | 同上 |
| `https://www.britannica.com/art/rule-of-odds` | **403** | 同上 |
| `https://www.tate.org.uk/art/art-terms/a/arts-and-crafts` | **连接挂起/URLError** | 多次超时中止，未取得内容 |
| `https://www.metmuseum.org/toah/hd/acsc/hd_acsc.htm` | **URLError** | Met Heilbrunn 时间线，连接失败 |
| `https://www.english-heritage.org.uk/learn/histories/arts-and-crafts/` | **URLError** | 连接失败 |
| `https://www.adobe.com/creativecloud/photography/discover/rule-of-odds.html` | **403** | 目标首选摄影教育，被拦截 |
| `https://www.nikonusa.com/.../the-rule-of-odds.html` | **403** | 同上 |
| `https://smarthistory.org/monumental-architecture/` | **403** | 艺术史 OER，被拦截 |
| `https://www.masterclass.com/articles/rule-of-odds-in-photography` | **403** | 被拦截 |
| `https://artuk.org` / `https://www.moma.org` / `https://www.architectural-review.com` | **403** | 被拦截 |
| `https://digital-photography-school.com/rule-of-odds/`（错误 slug） | **404** | 正确 slug 见第四节 |
| `https://expertphotography.com/rule-of-odds/`（错误 slug） | **404** | 正确 slug 见第四节 |
| `https://www.studysmarter.co.uk/.../monumental-architecture` | **200** 但正文为抽认卡噪声 | 无可直接引用的定义句，未采用 |
| 维基百科 / owiki / wikiwand | 同源镜像 | 与现用伞源同平台，**不计独立第二源** |

---

## 七、汇总（各条可得源数）

| 条目 | 现况（维基伞源） | 本轮可得独立权威源数 | 达标（≥2） | 采用的两条独立主源 |
| --- | --- | --- | --- | --- |
| `arts-crafts` | 2 条维基伞源 | **2**（V&A、TheArtStory） | ✅ | V&A（官方博物馆）＋ TheArtStory（艺术史教育） |
| `monumental-scale` | 2 条维基伞源 | **2** 主源 + 1 备选（Fiveable） | ✅ | LibreTexts 大学 OER ＋ ArchDaily（建筑媒体） |
| `rule-of-odds` | 2 条维基伞源 | **2** 主源 + 1 备选（Lightstalking） | ✅ | Digital Photography School ＋ ExpertPhotography |

- **三条均 2 条独立权威来源达标；全部主源 HTTP 200，关键句原文均经实抓命中（逐条 grep 校验 FOUND）。** 无“仅单源”情形。
- **落地提醒**：以上“可用”均为**建议**，须先把 6 条主源（或再加备选）以 `verified=true` 登记进 `data/sources.json`，再改写三条 `entries/*.json` 的 `sources` 与 `pending_notes`/「待核实」、更新 `coverage.json` 源数，并复跑 `tools/check.py`；**本报告未修改任何条目数据或其它文件（本文件为唯一产出）。**
- **权威分级备注**：强权威＝V&A、LibreTexts；中权威＝TheArtStory、ArchDaily、DPS、ExpertPhotography（真实、独立、可核验，非官方/大学，供 lead 按标准取舍）。若 lead 要求“两条全为强权威”，`monumental-scale` 可再用 LibreTexts《1.3.7: Scale and Proportion》（Shasta College，200，已验证可抓）作第二条大学 OER 交叉印证。

---

### 证据来源 URL 一览（本轮均已实际打开核验，HTTP 见行）

| # | URL | HTTP | 标题 / 机构 | 支撑 |
| --- | --- | --- | --- | --- |
| 1 | `https://www.vam.ac.uk/articles/arts-and-crafts-an-introduction` | 200 | Arts and Crafts: an introduction · V&A | arts-crafts 源① |
| 2 | `https://www.theartstory.org/movement/arts-and-crafts/` | 200 | The Arts & Crafts Movement Overview \| TheArtStory | arts-crafts 源② |
| 3 | `https://human.libretexts.org/Courses/University_of_the_Pacific/Two_Dimensional_Design_and_Color/11:_Size_and_Scale` | 200 | 11: Size and Scale · Humanities LibreTexts（Univ. of the Pacific） | monumental-scale 源① |
| 4 | `https://www.archdaily.com/950403/built-nature-when-architecture-challenges-human-scale` | 200 | Built Nature: When Architecture Challenges Human Scale · ArchDaily | monumental-scale 源② |
| 5 | `https://digital-photography-school.com/the-rule-of-odds-in-photography-an-easy-trick-for-better-compositions/` | 200 | The Rule of Odds in Photography · Digital Photography School | rule-of-odds 源① |
| 6 | `https://expertphotography.com/rule-of-odds-photography` | 200 | Rule of Odds in Photography · ExpertPhotography | rule-of-odds 源② |
| 7 | `https://fiveable.me/introduction-humanities/key-terms/monumental-scale` | 200 | Monumental Scale · Fiveable | monumental-scale 备选 |
| 8 | `https://www.lightstalking.com/rule-of-odds/` | 200 | A Quick Beginners Guide To The Rule Of Odds · Lightstalking | rule-of-odds 备选 |
