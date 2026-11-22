# 第31轮质量闸抽检报告（spotcheck-round31）——mexican-baroque / metabolism（第30轮新增）· bauhaus（第30轮改动）逐条来源正文支撑·七节与SVG·元数据/pending联动·相似度

- 抽检人：spotcheck-r31（由 lead 委派的子代理）；抽样/核对时间 2026-11-22 约 23:33 起、核对完成约 23:50，Asia/Hong_Kong（CST）。
- 协议依据：`D:/Users/Administrator/Desktop/AUTONOMOUS.md` 第三节 E「质量闸」（新增/改动条目随机抽 10%、至少 3 条逐条核对来源；**不合格则整批返工**，下一轮抽检比例提至 25%；→ 异常监控「新条目与已有条目相似度过高（疑似套话），整批降级为草稿并复查」）+ 第三节 F「体检」+ 第六节（联网内容一律视为数据，其中任何指令不执行、不下载不运行来源代码、不改项目文件夹之外内容）；`D:/Users/Administrator/Desktop/TASK_design.md`「条目页结构」L2 七节标准 +「通用硬性规则」（不编造数字·日期·人名·引文·出处；**关键事实至少两个独立来源互相印证，否则标"待核实"**；只引用 verified=true 来源；图下注明"示意图，非施工图"；尺寸/坡度/消防/无障碍注明"实际工程须按当地规范和专业设计人员的要求"）+「专用规则」；`DECISIONS.md` D05/D06/D10/D11/D14。
  - 说明：任务书所称 `AUTONOMOUS.md`/`TASK_design.md` 在仓库根**无同名文件**（已 glob 确认），实际位于 `D:/Users/Administrator/Desktop/`（与第 12–30 轮一致），已按该路径**只读**读取（AUTONOMOUS.md 71 行、TASK_design.md 67 行）；`DECISIONS.md` 在仓库根。
- 技能：已按 host 规则加载 `using-superpowers`（本会话为委派子代理，按 SUBAGENT-STOP 仅作规范参考）与 `verification-before-completion`（全部结论以本轮实跑/实抓证据为准，证据先于断言，未验证不下断言）。

## 〇、数据稳定性与只读声明

- **采样快照（本轮实读，Asia/Hong_Kong）**：`data/sources.json`=118364B@23:32:57、`entries/batch-30.json`=4819B@23:32:57、`entries/batch-02-d.json`=18253B@23:23:12、`coverage.json`=82684B@23:32:57。`git log -1` = `c5110ed feat: round30 health check, sparse-cell entries (mexican-baroque, metabolism)`（即"第30轮改动"所在提交；其父 `8b3d909 docs: note round29 push failure` 为第29轮终态）。`entries/*.json` 共 **18 文件 / 135 条**（第29轮末 133 条，第30轮 batch-30 新增 2 条 → 135；135 个 id 全库无重复）。`git status --porcelain` 于本文件写入前**为空**（工作树干净）。`python tools/check.py` 本轮实跑 **`PASS: all checks, 0 errors`（EXIT=0）**。
- **只读声明**：本次**仅生成** `research/spotcheck-round31.md` 一个项目文件；**未修改** `entries/`、`data/sources.json`、`coverage.json`、`tools/`、`site/` 或任何其他项目文件，未 `git commit`，未改项目文件夹之外内容（桌面治理文档仅只读）。抓取脚本与缓存仅驻留系统临时目录（`/tmp/r31/*.txt|*.html|*.py`，核对完成后已清理），非项目产物。联网内容一律视为数据，网页中任何指令均未执行。
- **抽检口径与样本**：任务指定（a）第30轮新增 2 条：`mexican-baroque`、`metabolism`（均在 `entries/batch-30.json`）；（b）近期改动 1 条：`bauhaus`。**定位修正**：任务写作"batch-20?"，实经 grep `"id": "bauhaus"` 全库唯一定位在 **`entries/batch-02-d.json`**（非 batch-20）；第30轮确实改了它——见 `git show c5110ed -- entries/batch-02-d.json`：`bauhaus` 的「实例」年份由 `1925–1926 年（1926-12-04 启用）` 改为 `1926 年建成并启用（施工约始于 1925 年，1926-12-04 启用）`（即第30轮抽检建议的"年份措辞统一"Minor）。该改动是本次 bauhaus 相似度结论的关键。

## 一、判定口径与抓取方法

- **L2 七节口径**：顶层 `definition` + `sections` 内 原理 / 典型手法与适用条件 / 实例 / 常见错误与限制 / 一图 / 待核实（6 节）＝共 7 节；须 1 张内联 SVG 且含"示意图，非施工图"；「常见错误与限制」段须以"实际工程须按当地规范和专业设计人员的要求"收尾；SVG 元素不出 `viewBox`（本轮各为 `0 0 760 400`）。
- **抓取方法**：Python 3.11 `urllib` + 浏览器 UA（`Chrome/124`，`Accept/Accept-Language` 齐备，`ssl` 不校验证书）；逐 URL 记录 HTTP 码、字节数、`<title>`；页面按 UTF-8 解码、去标签后做关键句检索。`en.wikipedia.org` canonical 本轮仍超时（WinError 10060，与历史一致），改 **owiki 同源镜像**（`https://owiki.org/wiki/<Title>`）核对 h1 与正文（DECISIONS D05 允许）。本轮 **8 个引用来源 id 全部实抓 HTTP 200**（3 篇维基经 owiki 镜像 200，5 个独立站点 canonical 200）。
- **第二源相关性判据**：第二源须**正文直接支撑该条核心概念/定义/实例要素**（非泛论伞源、非维基镜像）。
- **相似度口径**：`difflib.SequenceMatcher`（去空白）对全库 **135 条**逐条扫描，警戒线 **0.54**；采用与第27–30轮一致的**内容层口径②（全字段-不含SVG原始标记；`一图`段计入、`svg` 标记不计入）**。本轮已用该口径**复算第29轮 bauhaus** 得 `0.5319`，与第30轮报告 §七所载 `0.5319` **逐位吻合**，证明口径一致、可比。

## 二、抽检对象来源清单与完整性

`python tools/check.py` → **PASS, 0 errors**。3 条共引用 **8 个来源 id，全部存在、全部 verified=true、标题与主题直接相关**：

| 条目 | sources（现状） | 存在/verified | 标题 / 机构 | type | 与主题相关性 | 实例第二源 |
| --- | --- | --- | --- | --- | --- | --- |
| mexican-baroque | `wp-new-spanish-baroque` | ✅ / true | New Spanish Baroque / Wikipedia(owiki) | 权威百科* | 直接（风格定义：Mexican Baroque=New Spanish Baroque） | — |
| mexican-baroque | `designingbuildings-baroque` | ✅ / true | Baroque architecture — Designing Buildings | 学术著作* | 相关（西属美洲晚期巴洛克＝Churrigueresque） | 仅泛证子风格**（非实例主体） |
| metabolism | `wp-metabolism-architecture` | ✅ / true | Metabolism (architecture) / Wikipedia(owiki) | 权威百科* | **直接**（定义＋代表人物＋中银胶囊塔1972） | **①✅（唯一给年份）** |
| metabolism | `designingbuildings-metabolism` | ✅ / true | Metabolism in architecture — Designing Buildings | 学术著作* | **直接**（有机生长/可替换＋中银胶囊塔） | ②✅（塔/黑川，**无年份**） |
| bauhaus | `wp-bauhaus` | ✅ / true | Bauhaus / Wikipedia(owiki) | 权威百科 | 直接（学派定义） | — |
| bauhaus | `wp-modern-architecture` | ✅ / true | Modern architecture / Wikipedia(owiki) | 权威百科 | 相关（现代主义背景） | — |
| bauhaus | `stiftung-bauhaus-dessau` | ✅ / true | Bauhaus Building — Stiftung Bauhaus Dessau | 官方机构 | **直接**（实例主体，官方） | **①✅** |
| bauhaus | `archdaily-bauhaus-dessau` | ✅ / true | Bauhaus Dessau — ArchDaily | 学术著作 | **直接**（实例主体，行业媒体） | **②✅** |

> 关键事实：三条 `sources` 数组长度与 `coverage.source_count` 一致（mexican-baroque 2=2、metabolism 2=2、bauhaus 4=4）。`wp-new-spanish-baroque`/`designingbuildings-baroque`/`wp-metabolism-architecture`/`designingbuildings-metabolism`/`stiftung-bauhaus-dessau`/`archdaily-bauhaus-dessau` 六源 `link_ok=null`（仅"当前可达性未回写"，`verified` 独立表示标题/机构已核对，符合 D11）；本轮对此六 URL 均实抓 HTTP 200，故不存在死链，仅 `link_ok` 字段尚未回填。\* type 字段：两篇维基为"权威百科"，Designing Buildings 系列在库内记为"学术著作"，均与主体相关。

## 三、任务 1：来源正文是否支撑 definition / time_or_place / overview 及七节「实例」（实抓逐句比对）

### 3.1 mexican-baroque（墨西哥巴洛克/新西班牙巴洛克）——**合格**
- **wp-new-spanish-baroque**（owiki 镜像 HTTP200 31520B，title「New Spanish Baroque ::: Open WIKI」，h1「New Spanish Baroque」）：
  - "**New Spanish Baroque, also known as Mexican Baroque**, refers to Baroque art developed in the entire territories that once formed the **Viceroyalty of New Spain**."（定义直证）
  - "**The most emblematic substyle of Mexican Baroque architecture is Churrigueresque.**"（overview 直证）
  - "artists such as Jerónimo de Balbás **decorated churches or facades** with a mixture of stipes, geometric shapes and **altarpieces**."（"装饰繁复"直证）
  - "polychrome sculptures … reflect the expressiveness and the **colour contrasts characteristic of New Spanish Baroque**."（"色彩浓烈"直证）
- **designingbuildings-baroque**（CANONICAL HTTP200 55604B，title「Baroque architecture - Designing Buildings」）："The late Baroque style is often referred to as Rococo or, **in Spain and Spanish America, as Churrigueresque**."；"Baroque architecture is characterised by **dynamic designs and complex architectural plan forms**; intended to heighten feelings of **motion**…"（子风格与曲面/动势直证）
- 逐项：definition"新西班牙（今墨西哥）殖民时期巴洛克建筑与艺术，**装饰繁复、色彩浓烈**"✓（Mexico/New Spain + decorated facades/altarpieces + colour contrasts 逐项对应）；time_or_place"美洲"✓（Viceroyalty of New Spain），"文艺复兴至19世纪"为 scope 分类口径（Minor，见下）；overview"结合本土工艺，子风格 Churrigueresque"✓（两源同证）。
- **实例核对**：`实例`＝"名称：新西班牙巴洛克教堂（**类型性描述**）；地点：墨西哥；设计者：不适用；年份：不适用"。**未点名任何具体教堂、人名或年份 → 无编造风险**；且 `needs_verification=true`、`pending_notes` 与「待核实」均明说"具体实例（名称/地点/设计者/年代）待补充独立来源"，**诚实相符**。此为该条目当前的正确处理（第30轮抽检亦按"稀疏格补条目、实例待核实"口径建立）。
- **Minor**：period 上界"至19世纪"未在两来源逐字出现（db-baroque 明说西属美洲晚期巴洛克延续至 18 世纪），属 scope 层级时段归类，非杜撰年份；`related` 含 `latin-american-colonial`（在 scope.md 第183行，属"scope 内未写条目"，check.py 允许、站内不生成 404 链接），非缺陷。
- `needs_verification=true`、`pending_notes`、正文「待核实」三者语义一致（均指向"具体实例待补独立来源"）。**未发现编造人名、引文、出处或具体年份。结论：合格。**

### 3.2 metabolism（新陈代谢派）——**合格（任务特别核对的"中银胶囊塔/黑川纪章/1972"有来源支撑）**
- **wp-metabolism-architecture**（owiki 镜像 HTTP200 47724B，title「Metabolism (architecture) ::: Open WIKI」，h1「Metabolism (architecture)」）：
  - "**Metabolism was a post-war Japanese biomimetic architectural movement that fused ideas about architectural megastructures with those of organic biological growth.**"（定义直证）
  - "a group of young architects and designers, including **Kiyonori Kikutake, Kisho Kurokawa and Fumihiko Maki**, prepared the publication of the Metabolism manifesto."（代表人物菊竹清训/黑川纪章/槙文彦 三人逐一直证）
  - "**The icon of Metabolism, Kurokawa's Nakagin Capsule Tower was erected in the Ginza district of Tokyo in 1972** and completed in just 30 days."（**实例四要素：中银胶囊塔/东京银座/黑川纪章/1972 — 全部直证，1972 确有明文**）
- **designingbuildings-metabolism**（CANONICAL HTTP200 50970B，title「Metabolism in architecture - Designing Buildings」）："…the **Nakagin Capsule Tower, Tokyo by Kisho Kurokawa**."；"Metabolism represented an urban environment that was **responsive, replaceable and could grow in an organic way**."（塔/黑川/地点 + 有机生长概念直证）
- 逐项：definition"战后日本以巨型结构＋可替换单元主张城市有机生长"✓（post-war Japanese biomimetic + megastructures + organic biological growth + replaceable 逐项对应）；time_or_place"20世纪、东亚"✓（post-war Japan，20th century）；overview"代表人物菊竹清训、黑川纪章、槙文彦"✓（三人名直接列出）。
- **任务特别核对结论**：实例「中银胶囊塔 / 黑川纪章 / 1972」—— **1972 年有来源支撑**：`wp-metabolism-architecture` 明写 "erected … in Tokyo in **1972**"。故**"来源只提该塔未给年份"的假设不成立**（第一源确实给了年份）。但**年份仅此单一来源**：第二源 `designingbuildings-metabolism` 只提"中银胶囊塔、东京、黑川纪章"，**未给年份**（grep "1972" 命中 0）。按 TASK 硬性规则"关键事实至少两个独立来源互相印证，否则标待核实"，此处将条目置 `needs_verification=true`、`pending_notes="中银胶囊塔的年代与现状…待补充独立来源"` 是**正确且诚实**的处理，**无需改为"待核实"字样之外的动作，也无需补源**（现有状态已合规）；若要"合格无待核实"，则应补一条明确写 1972 年份的第二独立来源（可选）。
- **Minor**：`待核实`节写"中银胶囊塔的具体年代与保存现状待补充独立来源"——其中"年代"其实第一源已直证 1972，措辞可更精确为"年代（1972，现仅单一来源）与保存现状待补第二独立来源"；不影响诚实性。`related` 含 `japanese-architecture`（scope.md 第177行，scope 内未写条目），同 mexican-baroque，非 404。
- `needs_verification=true`、`pending_notes`、正文「待核实」三者语义一致。**未发现编造人名、引文、出处或年份。结论：合格。**

### 3.3 bauhaus（包豪斯）——**内容/来源/七节/元数据 合格；相似度维度 不合格（详见 §六）**
- **wp-bauhaus**（owiki 镜像 HTTP200 52601B，title/h1「Bauhaus」）："The Staatliches Bauhaus … was a **German art school** operational from **1919 to 1933** that combined **crafts and the fine arts** … founded by architect **Walter Gropius in Weimar** … **emphasis on function** … The Bauhaus **moved to Dessau in 1925** and new facilities there were **inaugurated in late 1926**."（定义/时间/概述直证）
- **wp-modern-architecture**（owiki 镜像 HTTP200 104471B，h1「Modern architecture」）："…prominent in the **20th century** … the principle of **functionalism**; an embrace of **minimalism**; and a **rejection of ornament**."（现代主义背景直证）
- **实例来源① stiftung-bauhaus-dessau**（CANONICAL HTTP200 210827B，title「Bauhaus Building - Locations - Stiftung Bauhaus Dessau」）："**On 4 December 1926, after approximately one year of construction, the building was opened.**"；地址"**Gropiusallee 38 06846 Dessau-Roßlau, Germany**"；旁注"(Walter Gropius, 1926)"。
- **实例来源② archdaily-bauhaus-dessau**（CANONICAL HTTP200 780022B，title「AD Classics: Dessau Bauhaus / Walter Gropius | ArchDaily」）："Dessau, Germany **Architects: Walter Gropius** … **Year: 1926**"。
- 逐项：definition"把艺术、工艺与工业生产结合的设计学派"✓（combined crafts and the fine arts + mass production + emphasis on function）；time_or_place"20世纪、欧洲"✓（1919–1933，Weimar/Dessau/Berlin）；overview"影响建筑与设计教育方法，强调形式服从功能"✓（emphasis on function + influential）。
- **实例四要素核对（第30轮改动后的新措辞）**：名称＝包豪斯德绍校舍 Bauhaus Dessau ✓；地点＝德国德绍-罗斯劳 ✓（Gropiusallee 38 06846 Dessau-Roßlau）；设计者＝瓦尔特·格罗皮乌斯 ✓（两源）；年份＝**"1926 年建成并启用（施工约始于 1925 年，1926-12-04 启用）"** ✓——"1926-12-04 落成启用"由 stiftung 直证、"Year 1926"由 archdaily 直证；"施工约始于 1925"由 stiftung"after **approximately one year** of construction"＋wp-bauhaus"moved to Dessau in **1925**"共同支撑。**第30轮的年份措辞修正（原"1925–1926 年"→"1926 建成启用，施工约始于1925"）在来源层面更精确、更诚实，内容维度合格。**
- `needs_verification=false`、`pending_notes=""`、正文「待核实」="暂无已知待核实项。"三者**完全一致**（内容无未验证断言）。
- **但**：第30轮把 bauhaus 的「实例」段改到与 `modernism` 条目**逐字完全相同**（见 §六），导致**相似度越过 0.54 阈值**——这是本轮唯一实质问题，属**相似度维度不合格**（不是来源/结构/编造问题）。

## 四、任务 2：来源 id 存在性、verified、相关性、可达性（汇总）

- **存在性/verified**：8 个来源 id **全部存在、全部 verified=true**（见 §二表）。六个独立站点源 `link_ok=null`（未回写可达性），两篇维基 `link_ok=true`；`verified` 独立表示标题/机构已核对，不受 `link_ok` 影响（符合 D11）。
- **相关性**：metabolism 的 `wp-metabolism`（定义+人物+中银1972）与 `designingbuildings-metabolism`（有机生长+中银/黑川）均为**直接支撑**；bauhaus 的 `stiftung`+`archdaily` 为**实例主体直接支撑**；mexican-baroque 的 `wp-new-spanish-baroque` 定义直接支撑、`designingbuildings-baroque` 佐证 Churrigueresque（实例为类型描述、无第二实例源属正常）。
- **可达性（本轮实抓，全部 HTTP 200）**：`en.wikipedia.org` 三篇 canonical 超时 → 经 owiki 镜像 200（Metabolism 47724B / New Spanish Baroque 31520B / Bauhaus 52601B / Modern architecture 104471B）；`www.designingbuildings.co.uk/wiki/Metabolism`(50970B)、`…/Baroque_architecture`(55604B)、`bauhaus-dessau.de`(210827B)、`archdaily.com/87728`(780022B) 均 canonical 200。**8 个来源 id 全部可达（经 canonical 或同源镜像），无死链。**

## 五、任务 3：L2 七节完整性 + SVG + 风险/规范提示（程序化实核）

| 条目 | level | definition 顶层 | sections 6 节 | 缺节/多节 | SVG 数 | 含"示意图，非施工图" | SVG 元素出界 | viewBox | 风险/规范句 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| mexican-baroque | L2 | ✓ | 6/6 | 无 | 1 | ✓ | 无出界 | 0 0 760 400 | ✓"实际工程须按当地规范和专业设计人员的要求" |
| metabolism | L2 | ✓ | 6/6 | 无 | 1 | ✓ | 无出界 | 0 0 760 400 | ✓ |
| bauhaus | L2 | ✓ | 6/6 | 无 | 1 | ✓ | 无出界 | 0 0 760 400 | ✓ |

> 七节完整（definition + 原理/典型手法与适用条件/实例/常见错误与限制/一图/待核实 全部齐备，无缺节、无多余节）；每条 1 张内联 SVG、viewBox 均 `0 0 760 400`、均含"示意图，非施工图"；逐元素（rect/circle/ellipse/line/polygon 坐标与宽高半径）程序化核验**无出界**；「常见错误与限制」段均以规范提示收尾。**该项三条全部通过。**

## 六、任务 4：元数据一致性 + needs_verification ↔ pending_notes ↔ 正文待核实

- 三条 `title/theme/tier/period/region/level` 与 `coverage.json` 逐字段**一致**；`source_count` 与来源数组长度**一致**：mexican-baroque 2=2、metabolism 2=2、bauhaus 4=4；`needs_verification_count` 与 nv 一致：mexican-baroque 1/true、metabolism 1/true、bauhaus 0/false。

| 条目 | needs_verification | pending_notes（结构化） | 正文「待核实」节 | 一致性 |
| --- | --- | --- | --- | --- |
| mexican-baroque | **true** | 「墨西哥巴洛克」的具体实例（名称、地点、设计者、年代）待补充独立来源。 | 具体教堂的设计者与年代待补充独立来源。 | **语义一致** ✓（均为"具体实例待补源"；措辞略长短不同，Minor） |
| metabolism | **true** | 中银胶囊塔的年代与现状、以及其他实例待补充独立来源。 | 中银胶囊塔的具体年代与保存现状待补充独立来源；其余实例待核实。 | **语义一致** ✓（均为"中银年代/现状+其余实例待补源"；措辞略差，Minor） |
| bauhaus | **false** | （空） | 暂无已知待核实项。 | **完全一致** ✓（false/空/暂无） |

> 结构化标志与两处文本**实质一致**；三条 `related`（latin-american-colonial / japanese-architecture / de-stijl）均为 **scope.md 内但尚未写**的条目，`check.py` 对 scope 内 related 放行、站内不生成 404 链接（非缺陷，仅提示后续可能成"悬空引用"缺口）。

## 七、任务 5：与既有条目相似度（difflib，阈值 0.54，全库 135 条；口径②=全字段-不含SVG，`一图`计入）

| 条目 | ①短文本(标题+定义+时间+概述) | 判 | ②全字段-不含SVG | 判 |
| --- | --- | --- | --- | --- |
| mexican-baroque | **0.2925** vs baroque | <0.54 ✓ | **0.4069** vs renaissance-style | <0.54 ✓ |
| metabolism | **0.2570** vs postmodernism | <0.54 ✓ | **0.3403** vs chinese-architecture-style | <0.54 ✓ |
| bauhaus | **0.3175** vs pattern-language | <0.54 ✓ | **0.5673** vs **modernism** | **>0.54 ✗（触线）** |

> **metabolism / mexican-baroque 两档全部 <0.54，无套话超标。**
>
> **bauhaus 触线是本轮核心问题，且可精确定位为第30轮改动引入的回归：**
> 1. 第30轮终态（`c5110ed`）`bauhaus` 的「实例」段与 `modernism` 的「实例」段**逐字完全相同**（程序化比对 `identical == True`）：两者均为"名称：包豪斯德绍校舍…年份：1926 年建成并启用（施工约始于 1925 年，1926-12-04 启用）。…"。
> 2. 用同一口径复算：**第29轮终态（`8b3d909`）bauhaus vs modernism = 0.5319**（<0.54，与第30轮报告 §七所载 0.5319 **逐位吻合**）；**第30轮改动后（`c5110ed`）= 0.5673**（>0.54）。另一口径（含`一图`文本、不含 svg 标记）亦由 0.5226 → **0.5563**，同向越过阈值。
> 3. 归因：第30轮把 bauhaus 年份措辞"统一"成与 modernism 相同的建筑实例描写（本意是修掉"1925 起始年为推算"的 Minor），副作用是把两条目实例段变成同一串文本，使全字段相似度**从 0.5319 抬到 0.5673，越过 0.54 阈值**。
> 4. 性质判断：这是**同一实例建筑（包豪斯德绍校舍）被 baohaus 与 modernism 两个条目合法共用**导致的文本重合，**并非套话造假或抄袭来源**；但客观阈值已被突破，且系本轮受检的"改动条目"直接造成，按 AUTONOMOUS §E「新条目与已有条目相似度过高（疑似套话）→ 整批降级为草稿并复查」应**登记为异常并复查/去重**，不能当作达标放行。

## 八、逐条验收结论

| 条目 | definition / time_or_place / overview / 实例 来源支撑 | 来源存在·verified·相关 | L2 七节/SVG/风险 | 元数据·联动 | 相似度(①②) | 结论 |
| --- | --- | --- | --- | --- | --- | --- |
| **mexican-baroque（墨西哥巴洛克）** | 定义✓（New Spanish Baroque=Mexican Baroque；decorated facades+colour contrasts）；时间✓（美洲·Viceroyalty of New Spain）；概述✓（Churrigueresque 为最典型子风格，双源）；实例＝**类型性描述**无具名/无年份→不编造，且明确标待核实 | 2/2 true；wp 直接、db 佐证子风格 | 七节齐、SVG✓、风险✓ | 全部一致；nv=true/pending/待核实 **语义一致** | 0.293/0.407 | **合格**（Minor：period"至19世纪"为分类口径；实例类型描述属合规待核实） |
| **metabolism（新陈代谢派）** | 定义✓（post-war Japanese biomimetic+megastructure+organic growth）；概述✓（菊竹/黑川/槙文彦三名直证）；实例✓（**中银胶囊塔/东京银座/黑川纪章/1972 — wp 全部直证，1972 有明文**） | 2/2 true；wp 直接（含年份）、db 直接（塔/黑川，无年份） | 七节齐、SVG✓、风险✓ | 全部一致；nv=true/pending/待核实 **语义一致** | 0.257/0.340 | **合格**（年份 1972 仅单一来源→按双源规则标待核实，处理正确） |
| **bauhaus（包豪斯）** | 定义✓（crafts+fine arts+function）；时间✓（1919–1933/欧洲）；概述✓（form follows function）；实例✓（德绍校舍/Dessau-Roßlau/格罗皮乌斯/1926 建成启用，施工约始于1925，双源直证） | 4/4 true；stiftung+archdaily 直接 | 七节齐、SVG✓、风险✓ | 全部一致；nv=false/pending 空/待核实"暂无" **完全一致** | 短 0.318 ✓ / **全字段 0.5673 ✗>0.54** | **内容/来源/七节/元数据 合格；相似度 不合格（0.5673>0.54，round30 改动引入）** |

- **内容与来源维度：3 条全部合格**——`mexican-baroque`、`metabolism`、`bauhaus` 的 definition/time_or_place/overview/实例均有引用来源直接支撑；实例四要素（或 mexican 的类型描述）无编造人名、引文、出处或年份。**硬性"编造" 0 条，假第二源 0 条。**
- **结构与元数据维度：3 条全部通过**——L2 七节齐、各 1 张 SVG 含"示意图，非施工图"且无出界、风险/规范句齐备；元数据逐项一致；`needs_verification↔pending↔待核实` 实质一致；`check.py` PASS 0 errors。
- **相似度维度：2 条合格（mexican-baroque、metabolism）、1 条不合格（bauhaus 0.5673>0.54，round30 改动引入）。**

## 九、总体结论与是否建议整批返工

- **抽样结果**：3 条中 **2 条完全合格**（mexican-baroque、metabolism），**1 条仅"相似度"维度不合格**（bauhaus：全字段 0.5673 vs modernism > 0.54，由第30轮"年份措辞统一"把实例段改成与 modernism 逐字相同所致）；**内容/来源/编造维度 0 不合格、0 编造、0 假第二源**。
- **来源层面**：8 个引用来源 id 全部存在、verified=true、主题相关；3 条定义/实例均有直接来源支撑（metabolism 中银胶囊塔 1972 由 wp 明证；bauhaus 德绍校舍 1926 由官方+ArchDaily 双源明证；mexican-baroque 为类型性描述待核实、诚实）；8 个 URL 实抓（canonical 或 owiki 同源镜像）**全部 HTTP 200，无死链**。
- **结构/治理层面**：七节/SVG/规范提示全过、元数据与 pending 联动三条实质一致、`check.py` PASS 0 errors。
- **相似度层面**：**bauhaus 越线（0.5673>0.54）**，且经同一口径复算第29轮为 0.5319（证明是第30轮改动把它推过阈值），属 AUTONOMOUS §E 的"相似度过高（疑似套话）"异常，需处理。
- **是否建议整批返工**：
  - **不建议"整批返工"（不回炉重写 3 条内容）。** 依据：①源核对维度不合格 0 条、无任何编造或假第二源；②mexican-baroque、metabolism 两条完全合格；③三楼七节/元数据/check.py 全部通过。按 §E，"不合格则整批返工"针对的是**源核对不合格**，本轮为 0，不触发。
  - **但须对 bauhaus 做"定向去重"修复（相似度异常），并按其性质按 §E 登记复查。** 具体：把 `bauhaus` 的「实例」措辞与 `modernism` 差异化（二者改用不同表述或 bauhaus 侧重"作为设计学派/学校的实例"、或另择一具名实例；modernism 保留德绍校舍建筑实例与现年份口径），使全字段相似度回落 <0.54，复跑 `tools/check.py` 与相似度脚本确认。此修复为 1–2 处文字改动，不涉及重写其它内容。
  - **流程建议**：因本轮出现相似度触线（若 lead 将其计为"不合格"），按 §E 下一轮抽检比例提至 **25%**；并将 `bauhaus↔modernism` 去重项写入 BACKLOG 随访。若严格套用 §E"相似度过高→整批降级为草稿并复查"，可将第30轮批次作"降级草稿+复查"，其代价远小于全量返工，二者择一即可，**内容无需重写**。

---

### 机器可读汇总

```
ROUND=31
SAMPLER=spotcheck-r31
SCOPE=["mexican-baroque","metabolism","bauhaus"]
FILES={"mexican-baroque":"entries/batch-30.json","metabolism":"entries/batch-30.json","bauhaus":"entries/batch-02-d.json"}  # bauhaus 非 batch-20，grep 唯一命中 batch-02-d.json
STATE={"sources.json":"118364B@23:32:57","batch-30.json":"4819B@23:32:57","batch-02-d.json":"18253B@23:23:12","coverage.json":"82684B@23:32:57","total_entries":135,"files":18}
GIT_HEAD="c5110ed feat: round30 health check, sparse-cell entries (mexican-baroque, metabolism)"; GIT_STATUS="clean(写入前)"
CHECK_PY="PASS: all checks, 0 errors (EXIT=0)"
FETCH_METHOD="urllib+ChromeUA; en.wikipedia TIMEOUT -> owiki.org mirror; designingbuildings/bauhaus-dessau/archdaily canonical HTTP200"
FETCH={
 "wp-metabolism":"OWIKI 200 47724B h1 'Metabolism (architecture)'; 'post-war Japanese biomimetic ... megastructures ... organic biological growth'; 'Kiyonori Kikutake, Kisho Kurokawa and Fumihiko Maki'; 'Kurokawa Nakagin Capsule Tower was erected in ... Tokyo in 1972'",
 "designingbuildings-metabolism":"200 50970B 'Metabolism in architecture - Designing Buildings'; 'Nakagin Capsule Tower, Tokyo by Kisho Kurokawa' (NO 1972); 'responsive, replaceable ... organic way'",
 "wp-new-spanish-baroque":"OWIKI 200 31520B h1 'New Spanish Baroque'; 'New Spanish Baroque, also known as Mexican Baroque ... Viceroyalty of New Spain'; 'most emblematic substyle ... Churrigueresque'; 'colour contrasts characteristic of New Spanish Baroque'",
 "designingbuildings-baroque":"200 55604B 'Baroque architecture - Designing Buildings'; 'in Spain and Spanish America, as Churrigueresque'; 'dynamic designs and complex architectural plan forms ... motion'",
 "stiftung-bauhaus-dessau":"200 210827B 'Bauhaus Building - Stiftung Bauhaus Dessau'; 'On 4 December 1926, after approximately one year of construction, the building was opened'; 'Gropiusallee 38 06846 Dessau-Rosslau'; '(Walter Gropius, 1926)'",
 "archdaily-bauhaus-dessau":"200 780022B 'AD Classics: Dessau Bauhaus / Walter Gropius | ArchDaily'; 'Architects: Walter Gropius'; 'Year: 1926'; 'Dessau, Germany'",
 "wp-bauhaus":"OWIKI 200 52601B 'Bauhaus'; 'German art school operational from 1919 to 1933 that combined crafts and the fine arts'; 'founded by Walter Gropius in Weimar'; 'emphasis on function'; 'moved to Dessau in 1925 ... inaugurated in late 1926'",
 "wp-modern-architecture":"OWIKI 200 104471B 'Modern architecture'; 'prominent in the 20th century ... functionalism ... minimalism ... rejection of ornament'"
}
SOURCES={"count_distinct":8,"all_exist":true,"all_verified_true":true,"all_urls_reachable_200":"yes (canonical or owiki mirror)"}
BODY_SUPPORT={
 "mexican-baroque":"def(New Spanish Baroque=Mexican Baroque + decorated facades/altarpieces + colour contrasts)+overview(Churrigueresque dual-source)+instance=type-description(no name/year, needs_verification honest); minor period upper-bound 19c=classification",
 "metabolism":"def(post-war Japanese biomimetic+megastructure+organic growth)+overview(Kikutake/Kurokawa/Maki verbatim)+instance(Nakagin/ Tokyo Ginza / Kurokawa / 1972 ALL verbatim in wp-metabolism). YEAR 1972 SOURCE-SUPPORTED but SINGLE-SOURCE (db-metabolism lacks year) -> needs_verification=true correct",
 "bauhaus":"def(crafts+fine arts+function)+time(1919-1933/Europe)+overview(form follows function)+instance(Dessau Bauhaus/Dessau-Rosslau/Gropius/opened 1926-12-04, construction ~1925 dual-source)"
}
L2_CHECK={"seven_sections":"definition+6/6 x3, no missing/extra","svg":"1 each, all 示意图非施工图","svg_bounds":"no overflow (760x400)","risk_note":"实际工程须按当地规范和专业设计人员的要求 x3"}
METADATA={"title/theme/tier/period/region/level":"ALL OK x3","source_count":"mexican-baroque 2=2, metabolism 2=2, bauhaus 4=4","nvc":"mexican-baroque 1/true, metabolism 1/true, bauhaus 0/false","related_dangling":"latin-american-colonial/japanese-architecture/de-stijl 均在 scope.md 内未写；check.py scope 内放行，无404"}
SIMILARITY={
 "mexican-baroque":{"short":0.2925,"vs_short":"baroque","full_no_svg":0.4069,"vs_full":"renaissance-style","verdict":"PASS<0.54"},
 "metabolism":{"short":0.2570,"vs_short":"postmodernism","full_no_svg":0.3403,"vs_full":"chinese-architecture-style","verdict":"PASS<0.54"},
 "bauhaus":{"short":0.3175,"vs_short":"pattern-language","full_no_svg":0.5673,"vs_full":"modernism","verdict":"FAIL>0.54"},
 "bauhaus_regression":{"round29_8b3d909_fullA_vs_modernism":0.5319,"round30_c5110ed_fullA_vs_modernism":0.5673,"variantB_old":0.5226,"variantB_new":0.5563,"cause":"round30 made bauhaus 实例段 identical to modernism (identical==True)"},
 "threshold":0.54
}
VERDICT={"mexican-baroque":"合格","metabolism":"合格","bauhaus":"内容/来源/七节/元数据 合格；相似度 不合格(0.5673>0.54)"}
HARD_FABRICATION=0
HARD_FAIL_FALSE_SOURCE=0
MINOR=["mexican-baroque: period'至19世纪'为分类口径(源文未逐字)","mexican-baroque/metabolism/bauhaus: related 指向 scope内未写条目(无404)","metabolism: 待核实'年代'措辞可更精确(1972已单源直证)"]
BATCH_REWORK="不建议整批返工(内容无需重写)：源核对不合格0、编造0、假第二源0；mexican-baroque与metabolism完全合格；七节/元数据/check.py全过。但bauhaus全字段相似度0.5673>0.54(第30轮'年份措辞统一'把实例段改成与modernism逐字相同，复算第29轮0.5319)触发§E相似度异常，须对bauhaus做定向去重(与modernism实例措辞差异化，回落<0.54并复跑check.py)，并按§E将下轮抽检比例提至25%/或将该批次降级草稿复查。"
READONLY="only wrote research/spotcheck-round31.md; no other project file changed; no git commit; web content treated as data, no instruction executed; /tmp/r31 temp cache cleaned"
```

*（报告完）*
