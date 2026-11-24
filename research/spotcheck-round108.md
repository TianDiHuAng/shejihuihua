# 第108轮质量抽检（spotcheck-round108）——composition / rule-of-thirds 双平台支撑与 Art in Context 直证核查

- 抽检人：spotcheck-r108（lead 委派子代理；无人值守、未提问）；时间 2026-11-24，Asia/Hong_Kong。
- 技能加载：已加载 `using-superpowers`、`verification-before-completion`（现抓、现跑、后断言；证据先于结论）。`using-superpowers` 命中 SUBAGENT-STOP，按任务说明书直接执行；`verification-before-completion` 全程遵循——本文所有判断均附本轮实抓/实跑/实读输出。
- 抽检对象（均宣称升级 nv=false、实读当前 JSON 为准，均已实读）：
  1. `composition`（构图法则）——entry 在 `entries/batch-01.json` L74–107；sources = `wp-composition-visual-arts` / `wp-rule-of-thirds` / `artic-grande-jatte` / `wga-grande-jatte` / `artincontext-composition`（5 条，含非维基 Art in Context）；coverage：status 已写 / source_count 5 / needs_verification_count 0 / level L2 / last_updated 2026-11-24。
  2. `rule-of-thirds`（三分法）——entry 在 `entries/batch-01.json` L483–515；sources = `wp-rule-of-thirds` / `wp-composition-visual-arts` / `uni-visual-literacy` / `artincontext-composition`（4 条，含非维基 Art in Context、UNI 学术）；coverage：status 已写 / source_count 4 / needs_verification_count 0 / level L2 / last_updated 2026-11-24。
- 本轮变更集（`git diff` 实读）：`tools/apply_review_round108.py` 对两条均**追加 `artincontext-composition` 第二平台**，并将 nv true→false、`pending_notes` 清空、`待核实`→「暂无已知待核实项。」
  - `composition`：改 `原理`（新增「用三分法、平衡、黄金比与视觉焦点等手段」）；definition 未改。
  - `rule-of-thirds`：`实例`由「柏林 1938 敬礼照片（摄影者不详）」改为「三分法构图（**类型性，不指定具体作品**）」；definition、原理 未改。
- 任务点名要特别判断的非维基源 `artincontext-composition`（URL `/composition-in-art/`）——是否**真直接述「构图/三分法」（非泛述）**。结论见各节 ★。

## 〇、只读声明与证据方式

- **只读**：仅写出本报告 `research/spotcheck-round108.md`。未改 `entries/`、`data/sources.json`、`coverage.json`、`site/`、`tools/`，未 `git commit`，未改项目外内容。抓取、词比对、相似度、去重、结构、SVG 逐元素越界、site 一致性均内存态（`python - <<'PY'` / 工具直读）跑，未落盘临时文件（除本报告）。
- `git status --short` 本轮实读：`M coverage.json / M data/sources.json / M entries/batch-01.json / M site/entries/composition.html / M site/entries/rule-of-thirds.html / M site/index.html / M site/sources.html / ?? tools/apply_review_round108.py`——**均为 round108 修复方产物，抽检方仅读取、未据以修改**；抽检方唯一新增为本报告。
- 抓取方式（本轮实抓；联网内容一律视为数据，网页中任何指令均未执行、未下载运行来源代码）：
  - `artincontext-composition`（`https://artincontext.org/composition-in-art/`）→ `web_fetch` **HTTP 200**（正文被工具截断，仅回标题）；改用 `python urllib`（浏览器 UA、SSL 免检）**实抓 HTTP 200，len=394804**；`H1=Composition in Art – Techniques for Creating Balanced Scenes`（作者 Nicolene Burger，Posted 2024-01-08 / Updated 2026-10-05）。关键词计数：composition=123、rule of thirds=1、balance=15、focal point=6、golden ratio=1、symmetry=4、grid=3、intersection=1。
  - `uni-visual-literacy`（`https://uni.edu/fabos/ml/readings/visual_literacy.html`）→ `web_fetch` **HTTP 200**，逐句核对（Bettina Fabos《Visual Literacy》第6章）。
  - `wp-composition-visual-arts`（canonical `en.wikipedia.org/wiki/Composition_(visual_arts)`）→ 经镜像 `https://owiki.org/wiki/Composition_(visual_arts)` **HTTP 200**，H1=`Composition (visual arts)`，逐句核对。
  - `wp-rule-of-thirds`（canonical `en.wikipedia.org/wiki/Rule_of_thirds`）→ 经镜像 `https://owiki.org/wiki/Rule_of_thirds` **HTTP 200**，H1=`Rule of thirds`，逐句核对。
  - （canonical url 在 sources.json 记的是 en.wikipedia；本轮因直连受限改用 owiki.org 镜像抓正文，H1 与条目一致，属抓取环境限制，非数据缺陷。）
- **`python tools/check.py` 本轮实跑：`PASS: all checks, 0 errors`（CHECK_EXIT=0）。** **`python -m pytest tests -q -p no:cacheprovider`：`19 passed in 0.39s`（PYTEST_EXIT=0）**（均 `PYTHONDONTWRITEBYTECODE=1`，未新增缓存/未落盘）。
- 相似度方法承前轮：`difflib.SequenceMatcher`，去全部空白+小写；口径①短=title+definition+time_or_place+overview；口径②全=definition+time_or_place+overview+六节正文（按 sections 顺序）。**方法自校：`futurism-style × expressionism-style` 口径② = 0.5157（与前轮逐位一致，方法正确）。全库 258 条，无重复 id。**

---

## 一、`composition`（构图法则）

### 1.1 当前 entry 实读（`entries/batch-01.json` L74–107）
- `definition`＝「对画面元素的位置、比例与关系进行组织以形成秩序和重点的方法。」
- `原理`＝「构图通过安排元素的位置、比例与相互关系组织画面，用三分法、平衡、黄金比与视觉焦点等手段引导观看顺序、建立主次与秩序。」
- `overview`＝「构图决定观看路径与信息主次，是绘画与视觉设计共通的骨架。」
- `实例`＝「名称：《大碗岛的星期天下午》（A Sunday on La Grande Jatte）；地点：美国芝加哥艺术博物馆；设计者：乔治·修拉（Georges Seurat）；年份：1884–1886 年。以点彩与几何安排组织画面构图。此处仅列名称、地点、设计者与年份信息，不复制图像。」
- `常见错误与限制`＝「元素过多会削弱重点；构图为视觉秩序而非工程尺寸。实际工程须按当地规范和专业设计人员的要求」（**句末缺「。」**）
- sources = wp-composition-visual-arts / wp-rule-of-thirds / artic-grande-jatte / wga-grande-jatte / artincontext-composition；`needs_verification=false`、`pending_notes=""`、`待核实=暂无已知待核实项。`、`time_or_place=跨时期、全球（参见来源）。`

### 1.2 definition/原理 两平台核对（实抓引句）
概念拆解：①画面元素；②位置、比例、关系；③组织；④形成秩序与重点；⑤原理细化四手段：三分法 / 平衡 / 黄金比 / 视觉焦点 + 引导观看顺序、建立主次。

**wp-composition-visual-arts（Wikipedia；owiki HTTP200，H1=`Composition (visual arts)`）——①②③④强、⑤强：**
- `The term composition means "putting together". It can be thought of as the organization of art.`（**③组织 ✓✓；①艺术元素整体 ✓**）
- 元素清单 `elements of design: Line/Shape/Color/Texture/Value/Form/Space`；`These elements … constitute the vocabulary with which the visual artist compose`（**①元素 ✓；③编排 ✓**）
- `a work of art is said to be aesthetically pleasing … if the elements within the work are arranged in a balanced compositional way`（**④平衡有序 ✓✓**）
- 「Rule of thirds」小节：`arranging the important features of an image on or near the horizontal and vertical lines that would divide the image into thirds horizontally and vertically is visually pleasing … ideally near the intersection of those lines.`（**⑤三分法 ✓✓**）
- `The rule of thirds is thought to be a simplification of the golden ratio.`（**⑤黄金比 ✓**）
- `There should be a center of interest or focus in the work`（**⑤视觉焦点 ✓✓**）

**artincontext-composition（Art in Context；`/composition-in-art/`，HTTP200，H1=`Composition in Art – Techniques for Creating Balanced Scenes`）——①②③④强、⑤强：**
- `Artistic composition is the cornerstone of visual art, serving as the unseen architect that guides the viewer's experience.`（**③组织/引导 ✓✓**）
- `By strategically positioning elements, artists direct the observer's gaze toward key focal points within the artwork.`（**②位置 ✓✓；④重点/焦点 ✓✓**）
- `… techniques such as the rule of thirds, which divides the canvas into a grid, with the most important elements placed at the intersections of these lines.`（**⑤三分法 ✓✓（明确点名）**）
- 关键词计数 corroborated：balance=15（含节标题「Creating Balance and Harmony: The Equilibrium of Art」→**⑤平衡 ✓✓**）、focal point=6（**⑤视觉焦点 ✓✓**）、golden ratio 明确提及（**⑤黄金比 ✓**）、intersection=1/grid=3（**⑤三分交点 ✓**）。

| 概念要素 | artincontext-composition（非维基） | wp-composition-visual-arts | 判定 |
| --- | --- | --- | --- |
| ①画面元素 | ✓ cornerstone/positioning elements | ✓ elements of design | **双平台 ✓** |
| ②位置、比例、关系 | ✓ strategically positioning elements；golden ratio（比例） | ✓ arrangement / organization | **双平台 ✓** |
| ③组织 | ✓ unseen architect that guides | ✓ organization of art | **双平台 ✓✓** |
| ④秩序与重点 | ✓ direct gaze toward key focal points；balance/harmony | ✓ balanced compositional way；center of interest | **双平台 ✓✓** |
| ⑤三分法 | ✓ rule of thirds … intersections | ✓ rule of thirds 小节 | **双平台 ✓✓** |
| ⑤平衡 | ✓ balance（15 次，专节） | ✓ balanced compositional way | **双平台 ✓✓** |
| ⑤黄金比 | ✓ golden ratio（明确提及） | ✓ simplification of the golden ratio | **双平台 ✓✓** |
| ⑤视觉焦点 | ✓ focal point（6 次） | ✓ center of interest or focus | **双平台 ✓✓** |

**判定（1.2）：** definition ①—④（元素/位置比例关系/组织/秩序重点）与原理⑤（三分法·平衡·黄金比·视觉焦点四手段）**由非维基源 `artincontext-composition`（整篇即论构图："unseen architect that guides"＋"strategically positioning elements… focal points"＋明确 rule of thirds/a balance/golden ratio）与 Wikipedia `wp-composition-visual-arts`（organization of art / balanced compositional way / rule of thirds / golden ratio / center of interest）双平台逐要素直证 ✓✓**。两平台互补且完整覆盖，成立。

### 1.3 ★特别判断：artincontext-composition 是否真直接述「构图/三分法」（非泛述）
**结论：是，真直接支撑（非泛述）。**
- **页面主体即「构图」**：H1=`Composition in Art – Techniques for Creating Balanced Scenes`，正文首段 `Artistic composition is the cornerstone of visual art, serving as the unseen architect that guides the viewer's experience`——对象与 entry 完全同一（构图），不是泛论绘画/艺术史的通页。
- **明确点名三分法**：`… techniques such as the rule of thirds, which divides the canvas into a grid, with the most important elements placed at the intersections of these lines.`——逐字命中「三分法/交点」，非泛述。
- **四手段齐备**：rule of thirds（三分法）、balance（平衡，15 次含专节）、golden ratio（黄金比）、focal point（视觉焦点，6 次）——恰为 entry 原理所列四手段。
- **解决了升级前的缺口**：升级前 pending 记「两来源未逐字讨论『构图法则』」；现由一篇以「composition in art」为题的整篇文章直接讨论构图，缺口消解。**非泛述，直接命中。**

### 1.4 是否编造
- definition（元素位置比例关系的组织→秩序重点）与原理（三分法/平衡/黄金比/视觉焦点四手段）均有实源逐句可溯源（wp 定义段+四手段句；artincontext 首段+三分法句+balance/focal/golden 计数），**非编造 ✓**。`比例`一项由 golden ratio（比例概念）与 arrangement 佐证，属合理表述而非虚构事实。**无编造。**

### 1.5 类型性/具体实例合理性
- 《大碗岛的星期天下午》（A Sunday on La Grande Jatte）；美国芝加哥艺术博物馆；乔治·修拉；1884–1886 年——**事实正确且双源**：`artic-grande-jatte`（Art Institute of Chicago API，source note 记 1884–86）＋`wga-grande-jatte`（Web Gallery of Art，note 记 1884–86）。以点彩与几何安排作为「构图」实例合理。✓（两实例源 `verified=true`，`link_ok=null` 为 canonical 直连待复，属可达性标记，不影响已核标题/正文。）

### 1.6 nv=false 形式
| 项 | 值 | 判定 |
| --- | --- | --- |
| entry.needs_verification | false | ✓ |
| entry.pending_notes | "" | ✓ |
| sections.待核实 | 「暂无已知待核实项。」 | ✓ |
| coverage.needs_verification_count | 0（status 已写 / source_count 5 / L2 / 2026-11-24） | ✓ |
| time_or_place | 「跨时期、全球（参见来源）。」无「待核实」 | ✓ |
- **形式四处一致 ✓，check.py PASS；内容前提（双平台支撑、Art in Context 直证）已满足，nv=false 成立。**

### 1.7 七节 / SVG / 规范句 / site
| 核对项 | 值 | 判定 |
| --- | --- | --- |
| 七节（definition+原理/典型手法与适用条件/实例/常见错误与限制/一图/待核实） | 实读 sections 6 节齐备且非空 + definition，共七节 | ✓ |
| SVG 数量 / viewBox | 1 张，`0 0 760 400` | ✓ |
| SVG 越界 | 逐元素（rect 60–700/60–340；线 x=273/486 y60–340、y=153/246 x60–700；circle cx273 cy153 r14；text x300 y370）均落框内，脚本判定 **OOB=NONE** | ✓ |
| SVG 外链 | 无 `<image>/<script>/xlink/href=/url(`（forbidden=[]） | ✓ |
| SVG 注记 | 含「示意图，非施工图」（含 figcaption「图 1：示意图，非施工图」） | ✓ |
| 规范句 | 「实际工程须按当地规范和专业设计人员的要求」在，**句末缺「。」**（entry L100 与 site L15 均缺；site 页脚 note 处带「。」）——同 r101–r107 T 小疵 | ✓（T 小疵） |
| site 与 JSON 一致 | `site/entries/composition.html`：title/lead(=overview)/核心定义/原理/实例/常见错误 逐句包含比对 **全部 True** | ✓ |

### 1.8 相似度（阈值 0.54）与 def≠原理
| 条目 | 口径 | 最近邻 | 相似度 | 判定 |
| --- | --- | --- | --- | --- |
| composition | 短① | s-curve-composition | 0.3910 | ✓ <0.54 |
| composition | 全② | hierarchy | 0.4018 | ✓ <0.54 |
| composition × rule-of-thirds | 短①/全② | — | 0.3262 / 0.2794 | ✓ 非重复条目 |
| def×原理（去重） | — | — | 0.3636 | ✓ 两层次可分 |
- 全库最大：短 0.4960（serial-route×radial-route）、全 0.5256（spatial-sequence×atrium-architecture）——**均 <0.54 ✓**；方法自校 0.5157 ✓；258 条无重复 id。

### 1.9 条目1 结论
**`composition`（构图法则）——合格（附 T 透明说明：规范句句末缺「。」）。**
- 依据：definition ①—④（元素/位置比例关系/组织/秩序重点）与原理⑤（三分法·平衡·黄金比·视觉焦点）由 **非维基源 `artincontext-composition`（`/composition-in-art/`，H1=`Composition in Art – Techniques for Creating Balanced Scenes`，"unseen architect that guides"＋"strategically positioning elements… focal points"＋明确 `rule of thirds … intersections`＋balance/focal/golden 计数）与 `wp-composition-visual-arts`（organization of art / balanced compositional way / rule of thirds / golden ratio / center of interest）双平台逐要素直证**——★特别判断 `artincontext-composition` **真直接述构图并点名三分法（非泛述）**，升级前「未逐字讨论构图法则」缺口消解。非编造；实例《大碗岛》双源（artic+wga，1884–86）事实正确；nv=false 四处形式一致且内容前提成立；七节/SVG（OOB=NONE、无外链、含注记）/site 一致；相似度短 0.3910、全 0.4018、def×原理 0.3636、composition×rule-of-thirds 0.3262 均 <0.54；check.py PASS、pytest 19 passed；方法自校 0.5157。
- **T（Minor）**：`常见错误与限制`规范句句末缺「。」（同 r101–r107 小疵；site 页脚 note 处带「。」）。不阻断合格。

---

## 二、`rule-of-thirds`（三分法）

### 2.1 当前 entry 实读（`entries/batch-01.json` L483–515）
- `definition`＝「将画面横竖各三等分并把主体置于交点或分割线上的构图方法。」
- `原理`＝「三分法把画面横竖各三等分，主体置于交点或分割线上以获得偏离中心的均衡。」
- `overview`＝「它让主体偏离几何中心，产生更自然的视觉平衡。」
- `实例`＝「名称：三分法构图（类型性，不指定具体作品）；把主体或关键线置于横竖三分线的交点或分割线上，使画面偏离中心而取得均衡。此处仅列说明，不复制图像。」
- `常见错误与限制`＝「机械套用会导致构图僵硬；主体位置应结合视线方向调整。实际工程须按当地规范和专业设计人员的要求」（**句末缺「。」**）
- sources = wp-rule-of-thirds / wp-composition-visual-arts / uni-visual-literacy / artincontext-composition；`needs_verification=false`、`pending_notes=""`、`待核实=暂无已知待核实项。`、`time_or_place=跨时期、全球（参见来源）。`

### 2.2 definition/原理 两平台核对（实抓引句）
概念拆解：①横竖各三等分（两横两竖，九格）；②主体置交点或分割线；③构图方法；④原理增量：获得偏离中心的均衡。

**wp-rule-of-thirds（Wikipedia；owiki HTTP200，H1=`Rule of thirds`）——①②③④强（逐字）：**
- `The rule of thirds is a rule of thumb for composing visual art such as designs, films, paintings, and photographs.`（**③构图方法 ✓✓**）
- `an image should be imagined as divided into nine equal parts by two equally spaced horizontal lines and two equally spaced vertical lines, and that important compositional elements should be placed along these lines or their intersections.`（**①九格三等分 ✓✓；②交点/分割线 ✓✓（逐字）**）
- `… aligning a subject with these points creates more tension, energy and interest in the composition than simply centering the subject.`（**④偏离中心的张力/均衡 ✓✓**）
- `The main reason for observing the rule of thirds is to discourage placement of the subject at the center, or prevent a horizon from appearing to divide the picture in half.`（**④偏离中心 ✓✓**）

**wp-composition-visual-arts（Wikipedia；owiki HTTP200）——①②强：**
- `The rule of thirds is a composition guide that states that arranging the important features of an image on or near the horizontal and vertical lines that would divide the image into thirds horizontally and vertically is visually pleasing. … ideally near the intersection of those lines.`（**①三等分 ✓✓；②分割线/交点 ✓✓**）

**uni-visual-literacy（University of Northern Iowa；uni.edu HTTP200）——①②③④强：**
- `Composition is the creative activity of placing objects within a frame.`（③构图 ✓）
- `Another is "rule of thirds," a well-known principle of photographic and image composition. By breaking an image down into thirds (both horizontally and vertically), and by placing elements on the points of intersection, we can avoid both the uncomfortable pulling when the form is too close to the frame, and the boring inertia when the form is too central.`（**①横竖三等分 ✓✓；②交点 ✓✓；④偏离中心的均衡 ✓✓**）
- `Knowing the rule of thirds is to create images that are balanced yet interesting.`（④均衡 ✓✓）

**artincontext-composition（Art in Context；HTTP200）——①②补充：**
- `… techniques such as the rule of thirds, which divides the canvas into a grid, with the most important elements placed at the intersections of these lines.`（**①三等分/网格 ✓；②交点 ✓**）

| 概念要素 | wp-rule-of-thirds | wp-composition / uni / artincontext | 判定 |
| --- | --- | --- | --- |
| ①横竖各三等分（九格） | ✓✓ nine equal parts, two horizontal + two vertical lines | ✓✓ thirds horizontally and vertically（wp-comp/uni）；divides into grid（actic） | **双平台以上 ✓✓** |
| ②主体置交点/分割线 | ✓✓ along these lines or their intersections | ✓✓ intersection of those lines（wp-comp/uni）；intersections（actic） | **双平台以上 ✓✓** |
| ③构图方法 | ✓✓ rule of thumb for composing visual art | ✓ composition guide（wp-comp）/ principle of composition（uni） | **双平台以上 ✓✓** |
| ④获得偏离中心的均衡（原理） | ✓✓ more tension/interests than centering；discourage center | ✓✓ balanced yet interesting / avoid boring central inertia（uni） | **双平台 ✓✓** |

**判定（2.2）：** definition ①③「横竖各三等分＋主体置交点/分割线」**由 Wikipedia `wp-rule-of-thirds` 逐字直证（`nine equal parts by two equally spaced horizontal lines and two equally spaced vertical lines … placed along these lines or their intersections`），并获 `wp-composition-visual-arts`、`uni-visual-literacy`（academic）、`artincontext-composition` 一致复证**；原理④「偏离中心的均衡」由 `wp-rule-of-thirds`（more tension than centering／discourage center）＋`uni`（avoid boring central inertia／balanced yet interesting）双平台直证 ✓✓。两平台以上支撑成立。

### 2.3 ★特别判断：artincontext-composition 对「三分法」是否真直接述（非泛述）
**结论：是（对「构图」为整篇直述；对「三分法」为明确点名的一条技术，属直接陈述而非泛述）。**
- 页面主体是「构图」，`rule of thirds` 在其中被**明确点名并给出定义性描述**（`divides the canvas into a grid, with the most important elements placed at the intersections of these lines`），逐字命中「三等分网格/交点」——非泛述。
- 需如实说明粒度差异：该文对「三分法」仅约 1 处点名（计数=1），主体展开在「构图」总体；故 `rule-of-thirds` 的核心直证主力是 `wp-rule-of-thirds`（逐字）与 `uni-visual-literacy`（整段讲解），`artincontext-composition` 为**补充第二平台**而非唯一支柱。这不影响「两平台支撑」成立：概念由 Wikipedia（wp-rule-of-thirds / wp-composition）＋ UNI 学术（uni-visual-literacy）＋ Art in Context 三方共同直证。

### 2.4 是否编造
- definition（横竖三等分、主体置交点/分割线）与原理（偏离中心的均衡）均有实源逐句可溯源（wp-rule-of-thirds 定义句＋centering 句；uni 整段；wp-comp/actic 复证），**非编造 ✓**。overview（主体偏离中心→更自然视觉平衡）在 wp「more tension… than centering」/uni「balanced yet interesting」可溯源。**无编造。**

### 2.5 类型性/具体实例合理性
- 实读实例为「**三分法构图（类型性，不指定具体作品）**；把主体或关键线置于三分线交点/分割线上……」——**已改为类型性实例，不再依赖未署摄影者的具体照片（柏林 1938 敬礼照）**。类型性说明准确对应定义与原理，合理且无侵权/无未核事实风险。✓
- （对比：变更前为「柏林奥林匹克体育场敬礼照片／摄影者不详」——本轮 `apply_review_round108.py` 已替换，正是任务所述「实例已改类型性」。）

### 2.6 nv=false 形式
| 项 | 值 | 判定 |
| --- | --- | --- |
| entry.needs_verification | false | ✓ |
| entry.pending_notes | "" | ✓ |
| sections.待核实 | 「暂无已知待核实项。」 | ✓ |
| coverage.needs_verification_count | 0（status 已写 / source_count 4 / L2 / 2026-11-24） | ✓ |
| time_or_place | 「跨时期、全球（参见来源）。」无「待核实」 | ✓ |
- **形式四处一致 ✓，check.py PASS；内容前提（多平台支撑）已满足，nv=false 成立。**

### 2.7 七节 / SVG / 规范句 / site
| 核对项 | 值 | 判定 |
| --- | --- | --- |
| 七节 | sections 6 节齐备且非空 + definition，共七节 | ✓ |
| SVG 数量 / viewBox | 1 张，`0 0 760 400` | ✓ |
| SVG 越界 | 逐元素（rect 60–700/60–340；线 x=273/486、y=153/246；circle cx486 cy153 r16；text x300 y370）均落框内，脚本判定 **OOB=NONE** | ✓ |
| SVG 外链 | 无 `<image>/<script>/xlink/href=/url(`（forbidden=[]） | ✓ |
| SVG 注记 | 含「示意图，非施工图」（含 figcaption「图 1：示意图，非施工图」） | ✓ |
| 规范句 | 「实际工程须按当地规范和专业设计人员的要求」在，**句末缺「。」**（entry L508 与 site L15 均缺；site 页脚 note 处带「。」）——同 r101–r107 T 小疵 | ✓（T 小疵） |
| site 与 JSON 一致 | `site/entries/rule-of-thirds.html`：title/lead(=overview)/核心定义/原理/实例/常见错误 逐句包含比对 **全部 True** | ✓ |

### 2.8 相似度（阈值 0.54）与 def≠原理
| 条目 | 口径 | 最近邻 | 相似度 | 判定 |
| --- | --- | --- | --- | --- |
| rule-of-thirds | 短① | rule-of-odds | 0.4511 | ✓ <0.54 |
| rule-of-thirds | 全② | rule-of-odds | 0.3953 | ✓ <0.54 |
| rule-of-thirds × composition | 短①/全② | — | 0.3262 / 0.2794 | ✓ 非重复条目 |
| def×原理（去重） | — | — | **0.6667** | ⚠ 偏高（见 T） |
- 全库最大：短 0.4960、全 0.5256（同上）——**均 <0.54 ✓**；方法自校 0.5157 ✓。
- **T（def×原理 0.6667，偏高；属本条目固有、非本轮引入）**：definition「将画面横竖各三等分并把主体置于交点或分割线上的构图方法」与 原理「三分法把画面横竖各三等分，主体置于交点或分割线上以获得偏离中心的均衡」共享同一程序性长句，原理相对定义的增量仅为「以获得偏离中心的均衡」这一目的句，故文本重合度显著高于 r104–r107 同项（0.21–0.37）。**非跨条目重复（跨条目最高 0.4511<0.54），check.py 0 errors，不阻断合格**；建议后续在原理中补入机制说明（如「三分交点把画面张力引向主体、与黄金比同源」）以差异化两层次。

### 2.9 条目2 结论
**`rule-of-thirds`（三分法）——合格（附 T 说明：def×原理 0.6667 偏高建议差异化原理；规范句句末缺「。」）。**
- 依据：definition「横竖各三等分＋主体置交点/分割线」由 **Wikipedia `wp-rule-of-thirds` 逐字直证（nine equal parts / two horizontal + two vertical lines / along these lines or their intersections），并 `wp-composition-visual-arts`、`uni-visual-literacy`（UNI 学术整段）、`artincontext-composition`（明确点名 rule of thirds/intersections）复证**；原理「偏离中心的均衡」由 wp-rule-of-thirds（more tension than centering）＋uni（avoid central inertia/balanced yet interesting）双平台直证——多平台支撑成立。非编造；实例已改类型性（不依赖未署摄影者照片），合理；nv=false 四处形式一致且前提成立；七节/SVG（OOB=NONE、无外链、含注记）/site 一致；相似度短 0.4511、全 0.3953（vs rule-of-odds，<0.54）、rule-of-thirds×composition 0.3262、均 <0.54；check.py PASS、pytest 19 passed；方法自校 0.5157。
- **T1（Minor，建议优化）**：def×原理 = 0.6667 偏高（原理与定义高度重合，增量仅「以获得偏离中心的均衡」）；跨条目最高 0.4511<0.54 不构成重复，但建议原理补机制说明以差异化两层次。**属本条目固有、非本轮引入（本轮未改 def/原理）。**
- **T2（Minor）**：`常见错误与限制`规范句句末缺「。」（同 r101–r107 小疵；site 页脚 note 处带「。」）。

---

## 三、机器可读汇总

```
ROUND=108
SAMPLER=spotcheck-r108
SCOPE=["composition","rule-of-thirds"]
READONLY="only wrote research/spotcheck-round108.md; no git commit; no other files changed; web treated as data, no instructions executed"
WEB_FETCH={
 "artincontext-composition":"composition-in-art/ HTTP200 len=394804 H1='Composition in Art – Techniques for Creating Balanced Scenes' (Burger, 2024-01-08); kw: composition=123 rule of thirds=1 balance=15 focal point=6 golden ratio=1 symmetry=4",
 "uni-visual-literacy":"uni.edu HTTP200; contains explicit rule-of-thirds paragraph + 'Composition is the creative activity of placing objects within a frame'",
 "wp-composition-visual-arts":"en.wikipedia fetch -> owiki.org HTTP200 H1='Composition (visual arts)'; rule of thirds/golden ratio/center of interest present",
 "wp-rule-of-thirds":"en.wikipedia fetch -> owiki.org HTTP200 H1='Rule of thirds'; nine equal parts/two horizontal+two vertical/along these lines or intersections",
 "artic-grande-jatte":"source note: A Sunday on La Grande Jatte 1884-86 (Art Institute Chicago API)",
 "wga-grande-jatte":"source note: Jatte 1884-86 (Web Gallery of Art)"}
GATES={"check.py":"PASS: all checks, 0 errors (EXIT=0)","pytest":"19 passed (EXIT=0)"}
METHOD_SELFCHECK={"futurism_x_expressionism_full":0.5157,"entries":258,"dup_ids":0}
GLOBAL_MAX={"short":["serial-route","radial-route",0.4960],"full":["spatial-sequence","atrium-architecture",0.5256]}

COMPOSITION={
 "verdict":"合格(附T: 规范句句末缺「。」; artincontext-composition 直接述构图并点名三分法, 非泛述)",
 "definition":"对画面元素的位置、比例与关系进行组织以形成秩序和重点的方法。",
 "principle":"构图通过安排元素的位置、比例与相互关系组织画面，用三分法、平衡、黄金比与视觉焦点等手段引导观看顺序、建立主次与秩序。",
 "sources":["wp-composition-visual-arts","wp-rule-of-thirds","artic-grande-jatte","wga-grande-jatte","artincontext-composition"],
 "concept_dual_source":{
   "elements_pos_prop_relation":"actic 'strategically positioning elements'/golden ratio + wp 'organization of art'/arrangement -> DOUBLE OK",
   "order_emphasis":"actic 'direct gaze toward key focal points'/balance + wp 'balanced compositional way'/'center of interest or focus' -> DOUBLE OK",
   "rule_of_thirds":"actic 'rule of thirds ... intersections' + wp 'rule of thirds' subsection -> DOUBLE OK",
   "balance":"actic 'balance'(15x, dedicated section) + wp 'balanced compositional way' -> DOUBLE OK",
   "golden_ratio":"actic 'golden ratio' + wp 'simplification of the golden ratio' -> DOUBLE OK",
   "focal_point":"actic 'focal point'(6x) + wp 'center of interest or focus' -> DOUBLE OK",
   "db_nonwiki_supports_concept":true,
   "holds_two_platform_for_concept":true},
 "artincontext_direct_vs_generic":"DIRECT: 整篇以 'Composition in Art' 为题, 'unseen architect that guides', 'strategically positioning elements... focal points', 明确点名 'rule of thirds ... intersections'; 非泛述; 消解升级前'未逐字讨论构图法则'缺口",
 "fabrication":"no; definition/principle quote-traceable to artincontext + wp-composition",
 "instance":"大碗岛 A Sunday on La Grande Jatte; 美国芝加哥艺术博物馆; Georges Seurat; 1884-1886 -- 事实正确, artic+wga 双源",
 "type_instance_ok":true,
 "nv_false_form":"four-place consistent (nv=false/pending=''/待核实=暂无/coverage nv_count=0); time_or_place clean; check.py PASS",
 "structure":{"seven_sections":true,"sections_with_def":7,"svg_count":1,"viewBox":"0 0 760 400","svg_in_bounds":true,"external_ref":false,"caption":"示意图，非施工图","reg_sentence":true,"reg_period":false,"site_consistent":true,"sources":5},
 "similarity":{"threshold":0.54,"nearest_short":"s-curve-composition 0.3910","nearest_full":"hierarchy 0.4018","x_rule_of_thirds":"short 0.3262 / full 0.2794","def_vs_principle":0.3636,"lt_0.54":true},
 "transparency":["T(Minor): 常见错误与限制 规范句句末缺「。」(同r101-r107). Non-blocking."]}

RULE_OF_THIRDS={
 "verdict":"合格(附T1 def×原理0.6667偏高建议差异化原理[固有/非本轮引入]; T2 规范句句末缺「。」)",
 "definition":"将画面横竖各三等分并把主体置于交点或分割线上的构图方法。",
 "principle":"三分法把画面横竖各三等分，主体置于交点或分割线上以获得偏离中心的均衡。",
 "sources":["wp-rule-of-thirds","wp-composition-visual-arts","uni-visual-literacy","artincontext-composition"],
 "concept_dual_source":{
   "nine_thirds":"wp-rule-of-thirds 'nine equal parts by two equally spaced horizontal lines and two equally spaced vertical lines' + wp-comp/uni 'thirds horizontally and vertically' + actic 'divides into grid' -> DOUBLE-PLUS OK",
   "subject_on_intersection":"wp-rule-of-thirds 'along these lines or their intersections' + wp-comp/uni 'intersection of those lines' + actic 'intersections' -> DOUBLE-PLUS OK",
   "composition_method":"wp-rule-of-thirds 'rule of thumb for composing visual art' + wp-comp 'composition guide'/uni 'principle of ... composition' -> DOUBLE-PLUS OK",
   "off_center_balance":"wp-rule-of-thirds 'more tension than centering'/'discourage center' + uni 'avoid central inertia'/'balanced yet interesting' -> DOUBLE OK",
   "holds_two_platform_for_concept":true},
 "artincontext_direct_vs_generic":"DIRECT for composition (整篇主题); DIRECT mention for rule-of-thirds ('divides the canvas into a grid ... important elements at intersections'); 粒度: actic 对三分法约1处点名, 主力直证为 wp-rule-of-thirds + uni; actic 为补充第二平台, 不影响两平台成立",
 "fabrication":"no; definition/principle quote-traceable to wp-rule-of-thirds + uni + wp-comp + actic",
 "instance":"三分法构图 (类型性, 不指定具体作品) -- 已由柏林1938敬礼照改写为类型性, 不依赖未署摄影者照片; 合理",
 "type_instance_ok":true,
 "nv_false_form":"four-place consistent (nv=false/pending=''/待核实=暂无/coverage nv_count=0); time_or_place clean; check.py PASS",
 "structure":{"seven_sections":true,"sections_with_def":7,"svg_count":1,"viewBox":"0 0 760 400","svg_in_bounds":true,"external_ref":false,"caption":"示意图，非施工图","reg_sentence":true,"reg_period":false,"site_consistent":true,"sources":4},
 "similarity":{"threshold":0.54,"nearest_short":"rule-of-odds 0.4511","nearest_full":"rule-of-odds 0.3953","x_composition":"short 0.3262 / full 0.2794","def_vs_principle":0.6667,"entry_vs_entry_lt_0.54":true},
 "transparency":["T1(Minor, recommend): def×原理=0.6667 偏高(原理与定义高度重合, 增量仅'以获得偏离中心的均衡'); 跨条目最高0.4511<0.54 非重复; 属本条目固有(本轮未改def/原理).","T2(Minor): 规范句句末缺「。」(同r101-r107)."]}

VERDICT={"composition":"合格(artincontext-composition=/composition-in-art/ HTTP200 H1='Composition in Art – Techniques for Creating Balanced Scenes' 整篇述构图并明确点名 rule of thirds ... intersections + balance/golden ratio/focal point, 非泛述; wp-composition-visual-arts organization/balanced/rule-of-thirds/golden-ratio/center-of-interest 双平台; 实例大碗岛双源(artic+wga)事实正确; 相似度短0.3910全0.4018 def×原理0.3636 均<0.54; 附T规范句缺句号)","rule-of-thirds":"合格(wp-rule-of-thirds 逐字 nine equal parts/two horizontal+two vertical/along these lines or intersections + wp-composition/uni-visual-literacy/artincontext 复证; 原理偏离中心均衡 wp+uni; 实例已改类型性; 相似度短0.4511全0.3953(vs rule-of-odds<0.54); 附T1 def×原理0.6667偏高建议差异化原理[固有/非本轮引入], T2规范句缺句号)"}
KEY_FINDING="两条均升级 nv=false、七节/SVG(OOB=NONE,无外链,含示意图注记)/site一致、check.py PASS+pytest 19 passed、方法自校0.5157、全库最大相似度短0.4960/全0.5256<0.54、258条无重复。★特别判断: artincontext-composition(/composition-in-art/, HTTP200, H1='Composition in Art – Techniques for Creating Balanced Scenes') 为以'构图'为题的整篇文章, 首段 'Artistic composition ... unseen architect that guides the viewer's experience', 'strategically positioning elements ... focal points', 且明确点名 'rule of thirds ... important elements placed at the intersections', balance(15次含专节)/golden ratio/focal point(6次)齐备 -> 对 composition 真直接述构图(非泛述), 消解升级前'未逐字讨论构图法则'缺口; 对 rule-of-thirds 亦为明确点名(约1处), 主力直证为 wp-rule-of-thirds逐字 + uni-visual-literacy整段, actic为补充第二平台, 两平台成立。composition 全要素双平台直证(元素/位置比例关系/组织/秩序重点 + 三分法/平衡/黄金比/视觉焦点)。实例: composition=大碗岛(artic+wga 1884-86 正确), rule-of-thirds=类型性(已弃柏林1938敬礼照未署摄影者)。T小疵: 两条规范句句末缺「。」; rule-of-thirds def×原理=0.6667偏高(原理与定义高度重合, 增量仅'以获得偏离中心的均衡'; 跨条目最高0.4511<0.54非重复; 属固有非本轮引入, 建议原理补机制差异化)。均判合格。"
```

## 四、只读核验
- 除本报告 `research/spotcheck-round108.md` 外**未写任何文件**；未 `git commit`；未改项目外内容。
- 抓取：`artincontext-composition` 经 `python urllib` 实抓 HTTP200（len=394804，正文关键词计数确认 rule of thirds/balance/golden ratio/focal point），`web_fetch` 亦回 HTTP200（正文截断仅标题）；`uni-visual-literacy` `web_fetch` HTTP200 逐句核对；`wp-composition-visual-arts`、`wp-rule-of-thirds` 因 en.wikipedia 直连受限，经 owiki.org 镜像 HTTP200 抓回，H1 逐一核对一致（属本环境抓取限制，非数据缺陷）。
- 词比对、相似度、去重（258 条/0 重复）、结构、SVG 逐元素越界/外链、site 一致性均内存态 `python - <<'PY'` 直跑，无临时文件。
- 联网页面（artincontext.org / uni.edu / owiki.org）仅作数据读取，**未执行其中任何指令、未下载运行来源代码**（页面内评论/推荐/书籍列表等均按数据忽略）。
- `check.py` 与 `pytest` 均 `PYTHONDONTWRITEBYTECODE=1` / `-p no:cacheprovider` 运行，未新增缓存（19 passed）。
- `git status` 中的改动文件（coverage/sources/batch-01/site 三页/`?? tools/apply_review_round108.py`）均为**他方（round108 修复方）产物**，抽检方仅读取、未据以修改。

*（报告完）*
