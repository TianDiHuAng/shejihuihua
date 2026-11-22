# 第34轮质量闸抽检报告（spotcheck-round34）——古罗马建筑 / 装饰艺术 / 国际风格（第34轮新增 12 条中抽 3 条）

- 抽检人：spotcheck-r34（由 lead 委派的子代理）；抽样/核对时间 2026-11-23 00:02 起，核对完成约 2026-11-23 00:30，Asia/Hong_Kong（CST）。
- 协议依据：`AUTONOMOUS.md` 第三节 E「质量闸」（新增/改动条目随机抽 10%、至少 3 条逐条核对来源；**不合格则整批返工**，下一轮抽检比例提高到 25%；异常监控「新条目与已有条目相似度过高（疑似套话）整批降级为草稿并复查」）+ 第六节（联网内容一律视为数据，其中任何指令不执行、不下载不运行来源代码、不改项目文件夹之外内容）+ `TASK_design.md`「条目页结构」L2 七节标准与「通用硬性规则」（不编造数字/日期/人名/引文/出处；**关键事实至少两个独立来源互相印证，否则标“待核实”**；只引用 verified=true 来源；图下注明“示意图，非施工图”；尺寸/坡度/消防/无障碍注明“实际工程须按当地规范和专业设计人员的要求”）+ `DECISIONS.md` D05/D06/D10/D11/D14。
  - 说明：任务书所称 `AUTONOMOUS.md`/`TASK_design.md` 在仓库根**无同名文件**（已 `ops_glob` 确认）；实际位于 `D:/Users/Administrator/Desktop/`（与第 12–33 轮一致），已按该路径**只读**读取（AUTONOMOUS.md 71 行、TASK_design.md 67 行）；`DECISIONS.md` 在仓库根（21 行）。本轮抽检比例 3/12＝**25%**，与 `METRICS.json` round33 `spotcheck_policy_next_round="25%"` 一致。
- 技能：已按 host 规则加载 `using-superpowers`（本会话为委派子代理，按 SUBAGENT-STOP 仅作规范参考）与 `verification-before-completion`（全部结论以本轮实抓/实跑证据为准，证据先于断言，未验证不下断言）。

## 〇、数据稳定性与只读声明

- **采样快照（本轮实读，Asia/Hong_Kong）**：`data/sources.json`=120373B@23:47:23（git 未改，与 HEAD 一致）、`entries/batch-34.json`=24185B@00:02:15、`coverage.json`=83281B@00:02:15。`git log -1` = `0fd3995 feat: round33 twelve entries light/shadow and color`。`git status --porcelain` 显示 ` M coverage.json`、`?? entries/batch-34.json`、`?? tools/add_round34.py`——**即第34轮改动尚未提交**，工作树含本轮未入库改动，属本轮执行中的正常中间态（本轮抽检未改动上述任何文件）。
- **条目规模**：`entries/*.json` 共 **22 文件 / 173 条**（第33轮末 161 条，第34轮 `batch-34` 新增 12 条 → 173；与 `coverage.json` 中 `status=已写` 的 173 条一致；coverage 总口径 246 = 已写 173 + 未开始 73，级别 173 全 L2 + 73 未开始 L1；无重复 id）。
- **`tools/check.py`** 本轮实跑：**`PASS: all checks, 0 errors`（EXIT=0）**。
- **只读声明**：本次**仅生成** `research/spotcheck-round34.md` 一个项目文件；**未修改** `entries/`、`data/sources.json`、`coverage.json`、`tools/`、`site/` 或任何其他项目文件，未 `git commit`，未改项目文件夹之外内容（桌面治理文档仅只读）。抓取全程在 Python 进程内存中进行、**未落盘任何临时文件**（脚本经 stdin 传入 Python，无临时文件）；联网内容一律视为数据，网页中任何指令均未执行、未下载运行来源代码。
- **抽检口径与样本**：任务指定第34轮新增 12 条中抽 **3 条**：`ancient-roman`（古罗马建筑）、`art-deco`（装饰艺术）、`international-style`（国际风格），均在 `entries/batch-34.json`；12 条全为 L2。引用来源为 `wp-roman-architecture`、`wp-classical-architecture`、`wp-art-deco`、`wp-architectural-style`、`wp-international-style`、`wp-modern-architecture`（见 `data/sources.json`）。

## 一、判定口径与抓取方法

- **L2 七节口径**：顶层 `definition` + `sections` 内 原理 / 典型手法与适用条件 / 实例 / 常见错误与限制 / 一图 / 待核实（6 节）＝共 7 节；须 1 张内联 SVG 且含“示意图，非施工图”；「常见错误与限制」段须含“实际工程须按当地规范和专业设计人员的要求”；SVG 元素不出 `viewBox`（本轮均 `0 0 760 400`）。
- **抓取方法**：Python 3.11 `urllib` + 浏览器 UA（`Chrome/124`，`Accept/Accept-Language` 齐备，`ssl` 不校验证书）。按 URL 记录 HTTP 码、字节数、`<title>`；去 script/style/标签后按关键句检索。`en.wikipedia.org` canonical 本轮仍**超时**（`URLError(TimeoutError)`，与历史 10060 一致），改 **owiki 同源镜像**（`https://owiki.org/wiki/<Title>`）核对标题与正文（DECISIONS D05 允许）。本轮 **3 条共 6 个引用来源 id 全部实抓 HTTP 200**（均经 owiki 镜像），无死链。
- **相似度口径**：`difflib.SequenceMatcher`（去空白）；①短文本＝title+definition+time_or_place+overview；②全字段-不含 SVG 原始标记（definition+time_or_place+overview + 六节正文，`一图`段计入、`svg` 标记不计入）。全库 **173 条**（`entries/*.json` 全部已写条目）逐条扫描，警戒线 **0.54**（与第27–33轮一致的内容层口径②）。
- **“两源互证”判定口径（本轮明确）**：`TASK_design.md` 硬性规则要求“关键事实至少两个独立来源互相印证，否则标待核实”。本轮按“两源并集须覆盖 definition/time/overview 全部要点，且定义主干/核心论断至少获两源之一共同支撑”执行；若第二源与本条主题毫无内容交集、对本条任一具体论断均不构成印证，则该条核心事实实为**单源**，按硬性规则应落「待核实」。

## 二、抽检对象来源清单与完整性

`python tools/check.py` → **PASS, 0 errors**。3 条共引用 **6 个来源 id（去重 6），全部存在、全部 verified=true**：

| 条目 | sources（现状） | 存在/verified | 标题 / 机构 | type | link_ok | 与主题相关性 |
| --- | --- | --- | --- | --- | --- | --- |
| ancient-roman | `wp-roman-architecture` | ✅ / true | Ancient Roman architecture / Wikipedia | 权威百科 | true | **直接**（拱券、穹顶、罗马混凝土、承袭希腊柱式） |
| ancient-roman | `wp-classical-architecture` | ✅ / true | Classical architecture / Wikipedia | 权威百科 | true | 相关/直接（古典传统源自希腊与罗马、柱式比例体系） |
| art-deco | `wp-art-deco` | ✅ / true | Art Deco / Wikipedia | 权威百科 | true | **直接**（几何形态、金属工艺、流线造型、1920s–30s、全球） |
| art-deco | `wp-architectural-style` | ✅ / true | Architectural style / Wikipedia | 权威百科 | true | **泛论伞源**（仅泛述“建筑风格＝建筑分类概念”，正文无 “Deco”/几何/流线内容，见 §3.2、§四） |
| international-style | `wp-international-style` | ✅ / true | International Style / Wikipedia | 权威百科 | true | **直接**（体积非体量、规则立面、无附加装饰三原则） |
| international-style | `wp-modern-architecture` | ✅ / true | Modern architecture / Wikipedia | 权威百科 | true | 相关/直接（明确含 “International Style (1920s–1970s)”、摒弃装饰、玻璃/钢/钢筋混凝土） |

> 关键事实：三条 `sources` 数组长度与 `coverage.source_count` 一致（各 2=2）。6 源均 `year=null`（在线百科条目，D06 允许）、`link_ok=true`。**无死链、无假 id、无 verified=false 被引用。**6 个标题中 `wp-architectural-style`（“Architectural style”）为泛论概念条目，对 art-deco 不构成主题直接相关（详见 §3.2 与 §四）。

## 三、任务 1：来源正文是否支撑 definition / time_or_place / overview 及七节「实例」（实抓逐句比对）

### 3.1 ancient-roman（古罗马建筑）——**合格（Minor）**
- **wp-roman-architecture**（owiki 镜像 HTTP200 92326B，h1「Ancient Roman architecture」）：
  - “The use of **vaults and arches**, together with a sound knowledge of building materials, **enabled them to achieve unprecedented successes**…”（拱券与拱顶直证 definition）
  - “used new materials, particularly **Roman concrete**, and newer technologies such as the **arch and the dome** to make buildings that were typically strong and well engineered.”（**混凝土＋拱＋穹顶**直证）
  - “adopted the **external language of classical Greek architecture** for the purposes of the ancient Romans”（继承希腊柱式语言直证）
  - “The **classical orders now became largely decorative rather than structural**, except in colonnades”（**希腊柱式转为装饰性**＝overview“把希腊柱式转为装饰性立面语言”直证）
  - “…domes for the creation of **large and well-defined interior spaces**.”（**拱与穹顶覆盖大跨度空间**＝overview 直证）
  - “also known as the ‘concrete revolution’ … widespread use in Roman architecture of the previously little-used architectural forms of the **arch, vault, and dome**.”（拱顶体系佐证）
  - “the style used in **Western Europe** … Romanesque…”；“the provinces around the **Mediterranean Sea**”；“Greek colonies in southern **Italy**”（时间/地点“古代、欧洲”支撑）
- **wp-classical-architecture**（HTTP200 22936B，h1「Classical architecture」）：
  - “consciously **derived from the principles of Greek architecture and Roman architecture of classical antiquity**, or more specifically, from *De architectura* by the Roman architect Vitruvius.”（古典传统＝希腊与罗马共同源流，佐证“继承发展希腊柱式”）
  - “…a **systematic order of proportions for columns**…”（柱式体系佐证）
- **逐项结论**：
  - definition“拱券、穹顶与混凝土技术著称，并继承发展希腊柱式”——四点**全部有直接来源支撑**（vaults/arches、Roman concrete、arch and dome、external language of classical Greek / orders decorative）。
  - time_or_place“古代、欧洲”——Ancient Roman、Western Europe、Mediterranean、Italy 均见源文，**可接受**（宽范围概括）。
  - overview“拱与穹顶覆盖大跨度空间，把希腊柱式转为装饰性立面语言”——“large and well-defined interior spaces”＋“classical orders largely decorative rather than structural”**双句直证**。
- **实例核对**：`实例`＝“名称：万神殿式穹顶建筑（**类型性描述**）；地点与设计者不适用。看穹顶与拱券如何形成大跨。”**未点名具体作品、人名或年份 → 无编造风险**；`needs_verification=true`、`pending_notes` 与「待核实」三者逐字一致（均“具体实例待补充”）。
- **判定：合格**。附带 **Minor**：`ancient-roman` 的 SVG 字符串与 `rococo`/`neoclassical`/`art-nouveau`/`revival-renaissance` **逐字相同**（见 §五），且该通用图为“基座线＋三根立柱＋三角山花”，与「一图」解说“拱券与穹顶的受力关系”**仅部分对应**（未画出拱券受力路径或穹顶）；属图—文部分脱节的批内同质化问题，非来源/编造缺陷。

### 3.2 art-deco（装饰艺术）——**待核实**
- **wp-art-deco**（owiki 镜像 HTTP200 106428B，h1「Art Deco」）：
  - “It has its origin in the bold **geometric forms** of the Vienna Secession and Cubism.”（“几何化装饰”直证）
  - “French manufacturers of luxury furniture, porcelain, glass, **metalwork**, textiles…”；“Art Deco **represented luxury, glamour, exuberance**”（“金属光泽/奢华材料”支撑）
  - “A sleeker form of the style appeared in the 1930s called **Streamline Moderne, featuring curving forms and smooth, polished surfaces**.”（“流线造型”直证）
  - “first appeared in Paris in the 1910s just before World War I and **flourished internationally during the 1920s to early 1930s**”；“…which was **copied worldwide**”（time_or_place“20世纪、全球”直证；overview“流行于两次大战之间”＝1920s–early1930s 的合理概括）
  - “held in **Paris in 1925**”（Exposition internationale des arts décoratifs et industriels modernes，佐证年代/地点）
- **wp-architectural-style**（HTTP200 21723B，h1「Architectural style」）——**关键问题**：
  - “An architectural style is a **classification of buildings** based on a set of characteristics and features…”（仅泛述“建筑风格”概念）
  - 全文检索 `Deco`=0、`Rococo`=0、`Neoclassical`=0、`Art Nouveau`=0、`De Stijl`=0、`International`=0 → **该文完全不提“装饰艺术”及本条任何具体内容**。作为 art-deco 的第二源，**对本条 definition/time/overview 无任何具体印证**，属**泛论伞源**。
- **逐项结论**：
  - definition/time_or_place/overview：**全部有 wp-art-deco 的直接支撑**（几何/金属/流线、1920s–30s、全球、奢华材料、巴黎 1925）。**无编造年份、人名、引文、出处。**
  - **但按 `TASK_design.md` 硬性规则“关键事实至少两个独立来源互相印证，否则标待核实”**：本条第二源 `wp-architectural-style` 与本条主题**零内容交集**，并未对任一具体论断构成二次印证；即 art-deco 的**核心事实实为单源（仅 wp-art-deco）**。`wp-architectural-style` 在 batch-34 被作为 9 条的第二源重用（见 §七），系**泛论伞源**，不构成有效互证。故核心事实的“两源互证”未满足 → 应落「待核实」。
- **实例核对**：`实例`＝“名称：装饰艺术风格电影院门厅（**类型性描述**）；地点与设计者不适用。看几何母题与金属线条。”**无具名作品/人名/年份 → 无编造**。
- **联动核对（needs_verification↔pending↔待核实）**：三者逐字一致（均“「装饰艺术」的具体实例（名称、地点、设计者、年代）待补充独立来源”）。**但「待核实」只声明了“具体实例”缺口，未声明“第二源为泛论伞源、核心事实单源未互证”这一真实缺口**——即“联动一致但内容不完整”（与第33轮 five-tones 同类）。
- **判定：待核实**。非编造、非假源、非死链，definition/time/overview 由主源 wp-art-deco 充分支撑；但**第二源为泛论伞源、未构成独立互证**，按硬性规则应落待核实。建议把 `wp-architectural-style` 替换为一条真正关于装饰艺术的权威来源（如博物馆/专业机构页面），或把该缺口写入「待核实」并同步 `pending_notes`。附带 **Minor~Medium**：`art-deco` 的 SVG 与 `international-style`/`de-stijl`/`eclecticism` **逐字相同**，且「一图」解说“几何母题与阶梯体量”，而该通用图仅为“矩形＋竖线网格”，**未画出阶梯状体量、也未表现装饰几何母题 → 图文不符**（见 §五）。

### 3.3 international-style（国际风格）——**合格（Minor）**
- **wp-international-style**（owiki 镜像 HTTP200 47698B，h1「International Style」）：
  - 三项原则原文：“**Architecture as volume** – thin planes or surfaces create the building's form, **as opposed to a solid mass**; **Regularity in the facade**, as opposed to building symmetry; and **No applied ornament**.”（**体积而非体量、规则立面、少装饰**＝definition 逐项直证）
  - “modular and rectilinear forms, flat surfaces **devoid of ornamentation and decoration**, **open and airy interiors** … the use of **glass, steel, and concrete**.”（弱化装饰＋轻盈＋玻璃钢混凝土）
  - “began in **western Europe in the 1920s** and dominated modern architecture until the 1970s”；“brought to the **United States** by European architects in the **1930s**”（time_or_place“20世纪、全球”直证）
  - “the creation of a **standard architectural product**”；“steel frame structures employing **glass curtain walls**”（overview“标准化与轻盈感”支撑）
  - “first used in **1932** by the historian Henry-Russell Hitchcock and architect Philip Johnson”（术语年代，佐证 20 世纪）
- **wp-modern-architecture**（HTTP200 104471B，h1「Modern architecture」）：
  - “**International Style (1920s–1970s)**”；“**rejection of ornament**”；“the use of cast iron, drywall, plate glass, and **reinforced concrete**”；“form follows function”（**第二源直接点名 International Style 并印证“少装饰/现代”核心**，两源互证成立）
- **逐项结论**：
  - definition“体积而非体量、规则立面与少装饰，是现代主义的国际化表达”——三项原则**近乎逐字直证**；第二源 modern-architecture 同证“International Style”与摒弃装饰。
  - time_or_place“20世纪、全球”——1920s 西欧诞生→1930s 传入美国→主导至 1970s，**直接支撑**。
  - overview“标准化与轻盈感，弱化地方装饰”——“standard architectural product”（标准化）＋“open and airy interiors”（轻盈）＋“No applied ornament / devoid of ornamentation”（弱化装饰）**有支撑**；“地方装饰”为对 “applied ornament” 的近似改写（Minor）。
- **实例核对**：`实例`＝“名称：国际风格办公楼（**类型性描述**）；地点与设计者不适用。看规则网格与玻璃立面。”**无具名作品/人名/年份 → 无编造**；三者逐字一致。
- **判定：合格**。附带 **Minor**：`international-style` 的 SVG 与 `art-deco`/`de-stijl`/`eclecticism` **逐字相同**（同一“矩形＋网格线”模版），「一图」解说“规则网格与通透立面”，网格可见但**“通透/玻璃”未表现**（`fill='none'` 仅为空框，未画玻璃/透明）→ 轻微信图脱节；相似度全字段 0.5011（vs de-stijl）接近但未越 0.54（见 §七）。

## 四、任务 2：来源 id 存在性、verified、相关性、可达性（汇总）

- **存在性/verified**：6 个来源 id **全部存在、全部 verified=true**（见 §二表），`year=null`（D06 允许）、`link_ok=true`。
- **相关性**：
  - `wp-roman-architecture`（拱券/穹顶/罗马混凝土/承袭希腊柱式）与 `wp-classical-architecture`（古典传统源自希腊与罗马、柱式比例）——**均与 ancient-roman 直接相关**，两源并集覆盖其全部要点。
  - `wp-international-style`（三原则直证）与 `wp-modern-architecture`（点名 International Style、摒弃装饰）——**均与 international-style 直接相关**，两源互证成立。
  - `wp-art-deco`（几何/金属/流线/1920s–30s/全球）——**与 art-deco 直接相关**（主源充分）。
  - `wp-architectural-style`（仅泛述“建筑风格＝分类概念”，正文检索 `Deco`=0、`Rococo`=0、`Neoclassical`=0、`Art Nouveau`=0、`De Stijl`=0、`International`=0）——**与 art-deco 主题非直接相关，属泛论伞源，不构成互证**（本轮唯一直接相关性缺陷）。
- **可达性（本轮实抓，全部 HTTP 200，经 owiki 同源镜像）**：`wp-roman-architecture`（http://en.wikipedia.org/wiki/Roman_architecture→owiki 200 92326B）/ `wp-classical-architecture`（22936B）/ `wp-art-deco`（106428B）/ `wp-architectural-style`（21723B）/ `wp-international-style`（47698B）/ `wp-modern-architecture`（104471B）。**6 个来源 id 全部可达，无死链。**

## 五、任务 3：L2 七节完整性 + SVG + 风险/规范提示（程序化实核）

| 条目 | level | definition 顶层 | sections 6 节 | 缺节/多节 | SVG 数 | 含“示意图，非施工图” | SVG 元素出界 | viewBox | 风险/规范句 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ancient-roman | L2 | ✓ | 6/6 | 无 | 1 | ✓ | 无出界（程序化核验 line/rect/polygon/circle/text） | 0 0 760 400 | ✓“实际工程须按当地规范和专业设计人员的要求” |
| art-deco | L2 | ✓ | 6/6 | 无 | 1 | ✓ | 无出界 | 0 0 760 400 | ✓ |
| international-style | L2 | ✓ | 6/6 | 无 | 1 | ✓ | 无出界 | 0 0 760 400 | ✓ |

> 七节完整（definition + 原理/典型手法与适用条件/实例/常见错误与限制/一图/待核实 齐备，无缺节、无多余节）；每条 1 张内联 SVG、viewBox 均 `0 0 760 400`、均含“示意图，非施工图”；逐元素（line/rect/polygon/circle/text 坐标）程序化核验**无出界**；「常见错误与限制」段均以规范提示收尾。**机械项三条全部通过。**
>
> **但存在严重“图示同质化 + 图文脱节”缺陷（Minor～Medium，非机械项判负，需定向整改；且较第33轮恶化）**——**batch-34 全 12 条仅用 3 套 SVG 模版**，逐字相同分组如下（程序化比对）：
> 1. **模版A（SVG 长度 548，基座线＋三立柱＋三角山花）逐字相同**：`ancient-roman`、`rococo`、`neoclassical`、`art-nouveau`、`revival-renaissance`（5 条）。
> 2. **模版B（SVG 长度 468，矩形＋竖线网格）逐字相同**：`art-deco`、`international-style`、`de-stijl`、`eclecticism`（4 条）。
> 3. **模版C（SVG 长度 468，另一通用模版）逐字相同**：`romanesque`、`organic-architecture`、`revival-gothic`（3 条）。
> - 抽检 3 条中：**`art-deco` 与 `international-style` 的 SVG 字符串逐字相同**；`art-deco` 解说“几何母题与阶梯体量”但图为“矩形＋网格”，**未画阶梯体量/装饰几何母题 → 图文不符**；`international-style` 解说“规则网格与通透立面”，网格可见但**通透/玻璃未表现**；`ancient-roman` 解说“拱券与穹顶的受力关系”但图为立柱＋山花，**未画拱券受力/穹顶**（部分脱节）。
> - 该缺陷与第32、33轮已记的“本批 SVG 大量复用同一通用模版”**同类且范围更广（12 条全部落入 3 套模版）**，说明**图示去同质化仍未落实**。

## 六、任务 4：元数据一致性 + needs_verification ↔ pending_notes ↔ 正文待核实

- 三条 `title/theme/tier/period/region/level` 与 `coverage.json` 逐字段**一致**；`source_count` 与来源数组长度**一致**（各 2=2）；`needs_verification_count`：各 1/true；`related` 均为空数组（无悬空引用）。

| 条目 | needs_verification | pending_notes（结构化） | 正文「待核实」节 | 一致性 |
| --- | --- | --- | --- | --- |
| ancient-roman | true | 「古罗马建筑」的具体实例（名称、地点、设计者、年代）待补充独立来源。 | （同左，逐字相同） | **完全一致** ✓ |
| art-deco | true | 「装饰艺术」的具体实例（名称、地点、设计者、年代）待补充独立来源。 | （同左，逐字相同） | **完全一致** ✓（但未覆盖伞源缺口） |
| international-style | true | 「国际风格」的具体实例（名称、地点、设计者、年代）待补充独立来源。 | （同左，逐字相同） | **完全一致** ✓ |

> 结构化标志与两处文本**逐字一致**（程序化 `pending_notes == sections.待核实` 三条全部 True）。
> **注意**：如上 §3.2 所述，art-deco 的「待核实」**只声明了“具体实例”缺口，未声明“第二源为泛论伞源、核心事实单源未互证”这一真实缺口**——即 `needs_verification` 与正文声明虽“互相一致”，但**均未覆盖真实存在的来源支撑缺口**，属“联动一致但内容不完整”，已按 §3.2 判为待核实。

## 七、任务 5：与既有条目相似度（difflib，阈值 0.54；全库 173 条；口径②=全字段-不含 SVG，`一图`计入）

| 条目 | ①短文本(标题+定义+时间+概述) | 判 | ②全字段-不含SVG | 判 |
| --- | --- | --- | --- | --- |
| ancient-roman | **0.3974** vs ancient-greek | <0.54 ✓ | **0.4535** vs romanesque | <0.54 ✓ |
| art-deco | **0.3939** vs art-nouveau | <0.54 ✓ | **0.4852** vs art-nouveau | <0.54 ✓ |
| international-style | **0.4060** vs de-stijl | <0.54 ✓ | **0.5011** vs de-stijl | <0.54 ✓（近阈） |

> **三条两档全部 <0.54，无套话越线。** 最近邻多落在**同批 sibling 条目**（ancient-roman→romanesque/ancient-greek、art-deco→art-nouveau/international-style、international-style→de-stijl/art-deco），反映本批条目模板化程度偏高但**尚未越线**；`international-style` 全字段 0.5011 已接近阈值（余量 0.039）。
>
> **补充：batch-34 批内 12 条两两相似度**（口径②全字段）最高为 **revival-gothic vs revival-renaissance＝0.5198**（short 0.4741），次高 international-style vs de-stijl＝0.5011、art-deco vs international-style＝0.4890、de-stijl vs art-deco 等，均在 0.54 以下；即整批 new-entry 之间**无套话越线**，不触发 AUTONOMOUS §E“相似度过高→整批降级”。但批内最高 0.5198 亦近阈，与“SVG 三模版复用”一致地说明本批**模板化偏高**。

## 八、逐条验收结论

| 条目 | definition / time_or_place / overview / 实例 来源支撑 | 来源存在·verified·相关 | L2 七节/SVG/风险 | 元数据·联动 | 相似度(①②) | 结论 |
| --- | --- | --- | --- | --- | --- | --- |
| **ancient-roman（古罗马建筑）** | definition✓（vaults/arches＋Roman concrete＋arch & dome＋Greek 柱式 external language，直证）；time✓（Ancient Roman/Western Europe/Mediterranean/Italy 见源）；overview✓（“large and well-defined interior spaces”＋“orders largely decorative”）；实例＝类型性描述无具名/年份→不编造 | 2/2 true；两源均直接相关（roman 主证、classical 佐证古典/柱式） | 七节齐、SVG✓（但与另 4 条逐字同图、图文部分脱节）、风险✓ | 全部一致；nv=true/pending/待核实 逐字一致 | 0.397 / 0.454 | **合格**（Minor：SVG 同质化＋图文部分脱节） |
| **art-deco（装饰艺术）** | definition/time/overview 均由 wp-art-deco **直接支撑**（几何/金属/流线、1920s–30s、全球、奢华材料、巴黎1925）→**无编造**；实例＝类型性描述无具名/年份→不编造；**但第二源 wp-architectural-style 为泛论伞源（Deco=0，零具体印证），核心事实实为单源→未达两源互证** | 2/2 true；wp-art-deco 直接、**wp-architectural-style 非直接相关（伞源，不互证）** | 七节齐、SVG✓（与另 3 条逐字同图、图文不符）、风险✓ | 全部一致；nv=true/pending/待核实 逐字一致（但未覆盖伞源缺口） | 0.394 / 0.485 | **待核实**（非编造；建议换真第二源或扩写待核实） |
| **international-style（国际风格）** | definition✓（volume vs mass/regular facade/no ornament 三原则近逐字直证）；time✓（1920s 西欧→1930s 美国→至1970s）；overview✓（standard product＋open and airy＋no applied ornament）；实例＝类型性描述无具名/年份→不编造 | 2/2 true；两源均直接相关且互证（modern 明文 International Style） | 七节齐、SVG✓（与另 3 条逐字同图、“通透”未表现）、风险✓ | 全部一致；nv=true/pending/待核实 逐字一致 | 0.406 / 0.501（近阈） | **合格**（Minor：SVG 同质化＋“通透”未表现） |

- **内容与来源维度**：**2 合格 + 1 待核实 + 0 不合格**。definition/time_or_place/overview 全部有直接或强支撑；实例三条均为**类型性描述**、无具名作品/作者/年份；**硬性“编造年份/人名/引文/出处”0 条、假第二源 0 条、死链 0 条**。唯一实质缺口在 **art-deco 第二源为泛论伞源、核心事实单源未互证**（属来源互证缺口，非编造，按硬性规则应落「待核实」）。
- **结构与元数据维度**：三条 L2 七节齐、各 1 张 SVG 含“示意图，非施工图”且无出界、风险/规范句齐备；元数据逐项一致；`needs_verification↔pending↔待核实` 三条**逐字一致**；`check.py` PASS 0 errors。但**图示同质化严重（batch-34 全 12 条仅 3 套模版，art-deco≡international-style 逐字同图）且多图与解说脱节**，为需整改的质量缺陷（较第33轮扩大）。
- **相似度维度**：三条两档全部 <0.54（短文本最大 0.4060、全字段最大 0.5011），批内 12 条两两最高 0.5198，亦 <0.54，**无套话异常**（但接近阈值，模板化偏高需关注）。

## 九、总体结论与是否建议整批返工

- **抽样结果**：3 条中 **2 条合格（ancient-roman、international-style）+ 1 条待核实（art-deco）+ 0 条不合格**；**内容/来源/编造维度：0 编造、0 假第二源、0 死链**。
- **来源层面**：6 个引用来源 id 全部存在、verified=true；定义/概述/实例总体有直接或强支撑；6 个 URL 实抓（owiki 同源镜像）**全部 HTTP 200，无死链**。唯一相关性缺陷：art-deco 的第二源 `wp-architectural-style` 为泛论伞源、零具体印证（→ 该条判待核实）。
- **结构/治理层面**：七节/SVG/规范提示机械项全过、元数据与 pending 联动三条**逐字一致**、`check.py` PASS 0 errors；但**图示同质化严重（12 条仅 3 套模版）＋图文脱节**需整改。
- **相似度层面**：三条两档全部 <0.54（最高全字段 0.5011），批内两两最高 0.5198，**无套话越线**（异常监控未触发，但接近阈值）。
- **是否建议整批返工**：**不建议整批返工。** 依据：①源核对维度**不合格 0 条、编造 0、假第二源 0、死链 0**——按 AUTONOMOUS §E，“不合格则整批返工”针对的是**源核对不合格/编造/假源**，本轮为 0，不触发；②三条七节/元数据/`check.py` 全部通过；③相似度全部 <0.54（含批内 0.5198），异常监控未越线。art-deco 属“**待核实**”（第二源伞源、核心事实单源未互证，而非编造），按项目规则应由**补真第二源/补待核实**解决，不构成整批返工理由。
- **必须的定向整改（不触发整批返工，但建议下一轮优先，并写入 BACKLOG）**：
  1. **art-deco 换真第二源或扩「待核实」**：现第二源 `wp-architectural-style` 为泛论伞源，正文无任何装饰艺术内容（`Deco`=0），未构成独立互证。建议补一条真正关于装饰艺术的权威来源（博物馆/专业机构页面或权威百科专条），或把“核心事实第二源待补充/单源未互证”写入该条「待核实」并同步 `pending_notes`。
  2. **图示去同质化＋修图文脱节（本批最突出）**：batch-34 全 12 条仅 3 套 SVG 模版，且 `art-deco≡international-style`（另含 de-stijl、eclecticism）、`ancient-roman≡rococo/neoclassical/art-nouveau/revival-renaissance` 逐字同图；`art-deco`“几何母题与阶梯体量”、`international-style`“通透立面”、`ancient-roman`“拱券与穹顶受力关系”均与其通用图不符。建议逐条按概念重绘贴合示意图（阶梯体量/拱券受力路径/玻璃通透立面等），并核对全 12 条不重复。**该问题第32、33轮已记、本轮未改且范围扩大，应作为下轮首要整改项。**
  3. **批内相似度贴阈监测**：`revival-gothic vs revival-renaissance` 全字段 0.5198、`international-style vs de-stijl` 0.5011，虽 <0.54 但余量小；建议后续批次对同类风格条目做区分化改写，防止下次越过 0.54 触发降级。
- **流程记录**：本轮抽检 3/12＝25%（与 METRICS round33 `spotcheck_policy_next_round=25%` 一致）；结果 **2 合格 + 1 待核实 + 0 不合格、0 编造、0 假第二源、0 死链、无套话越线**；按 §E 不因“不合格”提至更高比例；鉴于 art-deco 待核实来源互证缺口与本批 SVG 去同质化未落实，建议下轮对 batch-34 其余 9 条做一次**定向来源相关性复核**（尤其核查作第二源的 `wp-architectural-style` 在 rococo/neoclassical/art-nouveau/de-stijl/revival-gothic/revival-renaissance/eclecticism 等条目上是否同样“泛论伞源未互证”）与**全批 SVG 去同质化**。

---

### 机器可读汇总

```
ROUND=34
SAMPLER=spotcheck-r34
SCOPE=["ancient-roman","art-deco","international-style"]
FILES={"ancient-roman":"entries/batch-34.json","art-deco":"entries/batch-34.json","international-style":"entries/batch-34.json"}
STATE={"sources.json":"120373B@23:47:23 (git-unmodified)","batch-34.json":"24185B@00:02:15","coverage.json":"83281B@00:02:15","total_written_entries":173,"scope_total":246,"written":173,"not_started":73,"files":22}
GIT_HEAD="0fd3995 feat: round33 twelve entries light/shadow and color"; GIT_STATUS="dirty: M coverage.json; ?? entries/batch-34.json; ?? tools/add_round34.py (round34 not yet committed)"
CHECK_PY="PASS: all checks, 0 errors (EXIT=0)"
SAMPLE_RATIO="3/12 = 25% (matches METRICS round33 spotcheck_policy_next_round=25%)"
FETCH_METHOD="urllib+ChromeUA; en.wikipedia TIMEOUT -> owiki.org mirror HTTP200; 6/6 sources HTTP200; no temp files written"
FETCH={
 "wp-roman-architecture":"OWIKI 200 92326B h1 Ancient Roman architecture; 'vaults and arches ... enabled unprecedented successes'; 'Roman concrete ... arch and the dome'; 'adopted the external language of classical Greek architecture'; 'classical orders now became largely decorative rather than structural'; 'domes for the creation of large and well-defined interior spaces'; 'Western Europe/Mediterranean/Italy'",
 "wp-classical-architecture":"OWIKI 200 22936B h1 Classical architecture; 'derived from the principles of Greek architecture and Roman architecture of classical antiquity ... De architectura by Vitruvius'; 'systematic order of proportions for columns'",
 "wp-art-deco":"OWIKI 200 106428B h1 Art Deco; 'bold geometric forms'; 'luxury furniture, porcelain, glass, metalwork'; 'Streamline Moderne ... curving forms and smooth, polished surfaces'; 'first appeared in Paris in the 1910s ... flourished internationally during the 1920s to early 1930s'; 'copied worldwide'; 'Paris in 1925'",
 "wp-architectural-style":"OWIKI 200 21723B h1 Architectural style; GENERIC: 'An architectural style is a classification of buildings...'; SEARCH Deco=0,Rococo=0,Neoclassical=0,Art Nouveau=0,De Stijl=0,International=0 -> NO Art Deco content; UMBRELLA SOURCE, no corroboration",
 "wp-international-style":"OWIKI 200 47698B h1 International Style; three principles: 'Architecture as volume ... as opposed to a solid mass'; 'Regularity in the facade'; 'No applied ornament'; 'open and airy interiors ... glass, steel, and concrete'; 'began in western Europe in the 1920s ... until the 1970s'; 'brought to the United States ... in the 1930s'; 'standard architectural product'; '1932 Hitchcock & Johnson'",
 "wp-modern-architecture":"OWIKI 200 104471B h1 Modern architecture; 'International Style (1920s-1970s)'; 'rejection of ornament'; 'cast iron, drywall, plate glass, and reinforced concrete'; 'form follows function'"
}
SOURCES={"count_distinct":6,"all_exist":true,"all_verified_true":true,"all_urls_reachable_200":"yes (owiki mirror)","relevance_defect":"wp-architectural-style is a generic umbrella source with zero Art Deco content -> not directly relevant to art-deco, no independent corroboration"}
BODY_SUPPORT={
 "ancient-roman":"definition(time/overview) fully supported by primary (vaults/arches, Roman concrete, arch+dome, Greek external language, orders decorative, large interior spaces); classical-architecture corroborates Greek/Roman classical orders; instance=type-description honest; VERDICT=合格",
 "art-deco":"definition/time/overview fully supported by wp-art-deco (direct); but 2nd source wp-architectural-style is generic umbrella (Deco=0) -> no independent corroboration -> key facts effectively single-source -> violates two-source rule -> VERDICT=待核实 (not fabrication); pending/待核实 only covers '具体实例', not umbrella-source gap",
 "international-style":"definition exact (volume vs mass / regular facade / no ornament); time 1920s Europe->US 1930s->1970s; overview standard/airy/no ornament; modern-architecture corroborates International Style -> VERDICT=合格"
}
L2_CHECK={"seven_sections":"definition+6/6 x3, no missing/extra","svg":"1 each, all 示意图非施工图, viewBox 0 0 760 400, no overflow (programmatic)","risk_note":"实际工程须按当地规范和专业设计人员的要求 x3","defect":"batch-34 uses ONLY 3 SVG templates across 12 entries; identical-SVG groups: A(548B)={ancient-roman,rococo,neoclassical,art-nouveau,revival-renaissance}; B(468B)={art-deco,international-style,de-stijl,eclecticism}; C(468B)={romanesque,organic-architecture,revival-gothic}; art-deco/international-style captions mismatch diagrams"}
METADATA={"title/theme/tier/period/region/level":"ALL OK x3","source_count":"2=2 x3","nvc":"1/true x3","needs_verification/pending_notes/待核实":"逐字一致 x3 (art-deco 待核实未覆盖伞源缺口)","related":"[] (no dangling)"}
SIMILARITY={
 "ancient-roman":{"short":0.3974,"vs_short":"ancient-greek","full_no_svg":0.4535,"vs_full":"romanesque","verdict":"PASS<0.54"},
 "art-deco":{"short":0.3939,"vs_short":"art-nouveau","full_no_svg":0.4852,"vs_full":"art-nouveau","verdict":"PASS<0.54"},
 "international-style":{"short":0.4060,"vs_short":"de-stijl","full_no_svg":0.5011,"vs_full":"de-stijl","verdict":"PASS<0.54 (near threshold)"},
 "intra_batch_34_max":{"full_no_svg":0.5198,"pair":["revival-gothic","revival-renaissance"],"short":0.4741},
 "threshold":0.54
}
VERDICT={"ancient-roman":"合格","art-deco":"待核实","international-style":"合格"}
HARD_FABRICATION=0
HARD_FAIL_FALSE_SOURCE=0
LINK_FAIL=0
MINOR=[
 "art-deco 2nd source wp-architectural-style is generic umbrella (Deco=0, zero corroboration) -> key facts single-source -> violates two-source rule -> 待核实; replace with genuine Art Deco source or extend 待核实/pending",
 "batch-34 SVG homogenization: 12 entries use only 3 templates; art-deco==international-style==de-stijl==eclecticism; ancient-roman==rococo==neoclassical==art-nouveau==revival-renaissance; captions (阶梯体量/通透立面/拱券受力) mismatch diagrams -> redraw; repeats+expands round33 defect",
 "international-style full-no-svg similarity 0.5011 vs de-stijl (near 0.54); intra-batch revival-gothic vs revival-renaissance 0.5198 (near 0.54); templating high -> monitor",
 "art-deco '两次大战之间' & international-style '地方装饰' are paraphrases of source ('1920s to early 1930s'/'applied ornament'), not verbatim (Minor)"
]
BATCH_REWORK="不建议整批返工：源核对不合格0、编造0、假第二源0、死链0；2合格+1待核实+0不合格；七节/元数据/check.py全过；相似度全部<0.54(短MAX0.4060/全字段MAX0.5011, 批内MAX0.5198)。art-deco属待核实(第二源泛论伞源未互证，非编造)，建议换真第二源或扩写待核实；同时本批SVG去同质化(12条仅3套模版)并修图文脱节；不触发§E整批返工。"
READONLY="only wrote research/spotcheck-round34.md; no other project file changed; no git commit; web content treated as data, no instruction executed; fetches done in-memory via python stdin, no temp files written"
```

*（报告完）*
