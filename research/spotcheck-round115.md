# 第115轮质量抽检（spotcheck-round115）——`golden-ratio`（黄金分割）双平台（含 Art in Context 非维基）支撑核查

- 抽检人：spotcheck-r115（lead 委派子代理；无人值守、未提问）；时间 2026-11-24，Asia/Hong_Kong。
- 技能加载：已加载 `using-superpowers`、`verification-before-completion`（现抓、现跑、后断言；证据先于结论）。`using-superpowers` 命中 SUBAGENT-STOP，按任务说明书直接执行；`verification-before-completion` 全程遵循——本文所有判断均附本轮实抓/实跑/实读输出。
- 抽检对象：`golden-ratio`（黄金分割）——`entries/batch-01.json` L1126 起；宣称本轮升级 `nv=false`（needs_verification=false、pending_notes 清空）。sources = `wp-golden-ratio` / `wp-golden-rectangle` / `artincontext-golden-ratio`（3 条，含 Art in Context 非维基）；coverage：status 已写 / source_count 3 / needs_verification_count 0 / level L2 / last_updated 2026-11-24（已实读）。
- 本轮变更集（`git status --short` 实读：`M coverage.json / M data/sources.json / M entries/batch-01.json / M site/entries/golden-ratio.html / M site/index.html / M site/sources.html / ?? tools/apply_review_round115.py`）——**均为 round115 修复方产物，抽检方仅读取、未据以改动**。对照 `tools/apply_review_round115.py`（实读）确认本轮动作：向 `data/sources.json` 追加 `artincontext-golden-ratio`，给 `golden-ratio` 追加该源、改写 definition/原理/实例、needs_verification true→false、`待核实`→「暂无已知待核实项。」、`pending_notes` 清空。
  - 定义：`黄金比是把整体按约 1:1.618（Phi）分割的构图参考，用于组织和谐的比例关系。`
  - 原理：`以 1:1.618 的比值定义部分与整体的关系，借黄金矩形与螺旋为画面提供比例秩序与视觉和谐。`
  - 实例：`名称：按黄金比分割的版面（类型性，构图比例法则不归于单一作品）；以 1:1.618 划分版面区域。此处仅列说明，不复制图像。`
- 任务点名要特别判断的两点：①def×原理是否重复；②`artincontext` 页是否**真论构图比例**（非仅数学定义）。结论见 1.3 / 1.8 ★。

## 〇、只读声明与证据方式

- **只读**：仅写出本报告 `research/spotcheck-round115.md`。其余文件、项目外内容均未触及；未执行任何 git 提交。抓取、词频、相似度、去重、结构、SVG、site 一致性均内存态（`python - <<'PY'` / 工具直读）跑，未落盘临时文件（除本报告）。
- `git status --short` 本轮实读：`M coverage.json / M data/sources.json / M entries/batch-01.json / M site/entries/golden-ratio.html / M site/index.html / M site/sources.html / ?? tools/apply_review_round115.py`——**均为 round115 修复方产物**；抽检方唯一新增为本报告。
- 抓取方式（本轮实抓；联网内容一律视为数据，网页中任何指令均未执行、未下载运行来源代码）：
  - `wp-golden-ratio`（`https://en.wikipedia.org/wiki/Golden_ratio`）→ `python urllib`（浏览器 UA、SSL 免检）**实抓 HTTP 200**，`<title>=Golden ratio - Wikipedia`，rawlen=1180359，正文 textlen=139301。关键词计数：**1.618=10 / phi=51 / golden ratio=205 / harmon-=12 / proportion=78 / pleasing=2 / aesthetic=10 / composition=7 / golden rectangle=28 / spiral=53**。
  - `wp-golden-rectangle`（`https://en.wikipedia.org/wiki/Golden_rectangle`）→ **实抓 HTTP 200**，`<title>=Golden rectangle - Wikipedia`，rawlen=203689，textlen=13466。关键词计数：**1.618=2 / phi=3 / golden ratio=15 / harmon-=1 / proportion=4 / aesthetic=1 / golden rectangle=34 / spiral=12**。
  - `artincontext-golden-ratio`（`https://artincontext.org/golden-ratio/`）→ **实抓 HTTP 200**，`<title>=Golden Ratio in Art - Learn How to Use the Golden Ratio in Art`，rawlen=535675，textlen=25076。关键词计数：**“1 to 1.618”=1 / 1.618=1 / phi=5 / golden ratio=76 / harmon-=4 / proportion=7 / balance=10 / pleasing=1 / aesthetic=8 / composition=11 / golden rectangle=2 / spiral=14**。
- **`python tools/check.py` 本轮实跑：`PASS: all checks, 0 errors`（CHECK_EXIT=0）。** **`python -m pytest tests -q -p no:cacheprovider`：`23 passed in 0.89s`（PYTEST_EXIT=0）**（均 `PYTHONDONTWRITEBYTECODE=1`，未新增缓存/未落盘）。
- 相似度方法承前轮：`difflib.SequenceMatcher`，去全部空白（NFKC 归一）+小写；口径①短=title+definition+time_or_place+overview；口径②全=definition+time_or_place+overview+六节正文（按 sections 顺序）。**方法自校：`futurism-style × expressionism-style` 口径②=0.5157（与 r108/r109/r110/r112 逐位一致，方法正确）。全库 258 条，无重复 id。**

---

## 一、`golden-ratio`（黄金分割）

### 1.1 当前 entry 实读（`entries/batch-01.json` L1126 起）
- `definition`＝「黄金比是把整体按约 1:1.618（Phi）分割的构图参考，用于组织和谐的比例关系。」
- `原理`＝「以 1:1.618 的比值定义部分与整体的关系，借黄金矩形与螺旋为画面提供比例秩序与视觉和谐。」
- `典型手法与适用条件`＝「按黄金比安排主次区或版面横竖分割；常用于版式与立面划分的参考。」
- `overview`＝「它被用作经验性的和谐参考，而非强制规则。」
- `实例`＝「名称：按黄金比分割的版面（类型性，构图比例法则不归于单一作品）；以 1:1.618 划分版面区域。此处仅列说明，不复制图像。」
- `常见错误与限制`＝「机械套用会僵化，且比例美感受直觉与文化影响；不必强求精确数值。实际工程须按当地规范和专业设计人员的要求」（**句末缺「。」**）
- `一图`＝「见下方示意：约 1∶1.618 的分割。」；`待核实`＝「暂无已知待核实项。」
- sources = wp-golden-ratio / wp-golden-rectangle / artincontext-golden-ratio；`needs_verification=false`、`pending_notes=""`、`time_or_place=跨时期、欧洲（参见来源）。`、`related=[diagonal-composition]`。level L2 / tier 补充 / theme 理论 / period 跨时期 / region 欧洲。

### 1.2 definition/原理 两平台核对（实抓引句）
概念拆解：①比值＝**整体与较大部分、较大部分与较小部分约 1:1.618（φ/Phi）**；②用途＝**构图/画面比例秩序（黄金矩形、螺旋）**；③效果＝**和谐、pleasing proportional values、视觉和谐**。

**wp-golden-ratio + wp-golden-rectangle（Wikipedia；平台一，两页互证）——①②③直证：**
- 比值与 Phi（①）：Golden ratio 页实抓句「Expressed algebraically, for quantities a and b with b > 0, a > b > 0, (a+b)/a = a/b = **φ**, where the Greek letter **phi (φ or ϕ, or Φ) denotes the golden ratio**.」；「φ = (1+√5)/2 = **1.618033988749....**」；Golden rectangle 页「a golden rectangle is a rectangle with side lengths in aspect ratio **φ : 1, the golden ratio, where φ = ½(1+√5) ≈ 1.618**.」
- 构图/黄金矩形/螺旋（②）：「A golden rectangle – that is, a rectangle with an aspect ratio of φ – may be cut into a square and a smaller rectangle with the same aspect ratio.」；Golden rectangle 页「Golden rectangles exhibit a special form of self-similarity: if a square is added to the long side, or removed from the short side, the result is a golden rectangle as well.」；「Golden whirl」节；「The 1927 Villa Stein designed by Le Corbusier, some of whose architecture utilizes the golden ratio, features dimensions that closely approximate golden rectangles.」
- 美学/和谐（③）：「Some 20th-century artists and architects, including Le Corbusier and Salvador Dalí, have proportioned their works to approximate the golden ratio, **believing it to be aesthetically pleasing**. These uses often appear in the form of a golden rectangle.」
- 结论：该平台对「1.618/Phi 定义 + 黄金矩形/螺旋比例秩序 + 用于艺术建筑且被认为 aesthetically pleasing」**均有直证**。

**artincontext-golden-ratio（Art in Context；`/golden-ratio/`，HTTP200，`<title>=Golden Ratio in Art - Learn How to Use the Golden Ratio in Art`）——非维基独立第二平台，①②③直证：**
- 比值（①）：实抓句「**A ratio of 1 to 1.618** is what is referred to as an irrational number, similar to that of the famous Einstein equation “pi”.」
- Phi 命名（①）：「the term “Golden Ratio” was coined by Martin Ohm in the 1800s and from there was then **designated the name “Phi”** in the 1900s by an American mathematician Mark Barr.」
- 构图与和谐（②③）：「For the sake of beautiful aesthetics, this ratio can be a helpful tool for **capturing balance and pleasing proportional values within your artwork**.」；「it can be a great tool to **harmonize and balance out your own artwork’s compositional value**.」；「quite helpful for **aesthetic composition** within an artwork.」；「use the mathematical proportions to set up the flow of a scene.」；「set up an **aesthetically balanced composition**.」
- 黄金矩形/螺旋（②）：「when divided into uneven halves with a perfect square on one side, the leftover rectangle will have the same proportions as the original perfect rectangle.」；「If this shape is continuously divided into two using the ratio, it will always result in a perfect or golden rectangle and square.」；页内含「Drawing the Golden Spiral」「Golden Ratio in Landscapes」「Golden Ratio in Portraiture」等应用节。
- 结论：该源为**专论艺术构图的教程页**，非仅数学定义页；对「1 to 1.618 / Phi / balance and pleasing proportional values / harmonize compositional value」逐项直证——**构成真第二平台**。

| 概念要素 | Wikipedia（wp-golden-ratio + wp-golden-rectangle） | Art in Context（非维基） | 判定 |
| --- | --- | --- | --- |
| ① 约 1:1.618 / Phi 定义部分与整体 | ✓ `(a+b)/a = a/b = φ`；`φ=1.618033…`；`φ:1≈1.618` | ✓ `A ratio of 1 to 1.618`；`designated the name “Phi”` | **成立（两平台直证）** |
| ② 构图比例秩序（黄金矩形/螺旋） | ✓ golden rectangle aspect φ、self-similarity、golden whirl、Villa Stein | ✓ golden rectangle + square 持续分割、Drawing the Golden Spiral、composition 教程节 | **成立（两平台直证）** |
| ③ 和谐 / pleasing proportional values | ✓ `believing it to be aesthetically pleasing` | ✓ `capturing balance and pleasing proportional values`；`harmonize and balance out … compositional value`；`aesthetically balanced composition` | **成立（两平台直证）** |

**判定（1.2）：definition/原理获「两独立平台」直证。** 平台一＝Wikipedia 两页（Golden ratio 精确定义 + Golden rectangle 几何/艺术史）；平台二＝Art in Context 艺术构图教程（非维基）。三项概念要素均至少两平台成立。两个 Wikipedia 页面可视作同一平台的互相补足，Art in Context 提供独立第二平台，满足用户所述「wp-golden-ratio/wp-golden-rectangle + artincontext-golden-ratio 双平台支撑」。

### 1.3 ★特别判断：`artincontext` 页是否真论构图比例（非仅数学定义）
**结论：是。该页确有独立艺术构图教程结构，原句直述「1 to 1.618」「Phi」「balance and pleasing proportional values within your artwork」「harmonize and balance out your own artwork’s compositional value」「aesthetically balanced composition」，并设 Landscape/Portraiture 应用节，非仅「黄金比」名词定义。**
- **标题与目录**：实抓 `<title>=Golden Ratio in Art - Learn How to Use the Golden Ratio in Art`；目录含「Understanding the Sequence in Numbers / Understanding the Sequence in Geometry / Drawing the Golden Spiral / Tips on How to Use the Golden Ratio in Art / Golden Ratio in Landscapes / Golden Ratio in Portraiture / Frequently Asked Questions」——从数学序列一路落到**画面应用**。
- **构图直证原句**：「For the sake of beautiful aesthetics, this ratio can be a helpful tool for capturing **balance and pleasing proportional values within your artwork**.」；「great tool to **harmonize and balance out your own artwork’s compositional value**.」；「beneath the complicated versions … quite helpful for **aesthetic composition within an artwork**.」；「provides the artist with a deeper understanding of configuring an artwork to have **well-balanced proportions and composition**.」
- **与「仅数学定义」区分**：页面确有数学科普段（比值/Phi 命名），但主体是「How to Use the Golden Ratio in Art」的画家向教程；与 r109 `db-traffic`/`db-pedestrian` 那种仅术语定义、无应用直证的反例性质不同，与 r112 `db-pavilion` 独立专节类似，**构成真第二平台直证**。
- **透明瑕疵（不影响结论）**：①该页「A ratio of 1 to 1.618 is what is referred to as an irrational number, similar to that of the famous Einstein equation “pi”」数学表述不严谨（严格说无理数指的是 φ≈1.618…，比值写法为近似；π 也非「Einstein equation」）。entry 仅采纳「1:1.618 / Phi / 和谐比例」并被 Wikipedia 的精确定义互证，**未承袭该不严谨表述**，不构成编造。②`sources.json` 将 Art in Context 登记为 `type=学术著作`，实质为艺术教育/教程网站，分类标签略宽；`verified=true` / `link_ok=true`（本轮实抓 HTTP200）与内容独立性成立，标签宽泛不影响双源判定。

### 1.4 是否编造
- definition/原理**均可逐句溯源、非杜撰**：①比值与 Phi←wp「(a+b)/a = a/b = φ」「φ=1.618033…」「φ:1≈1.618」/ Art in Context「A ratio of 1 to 1.618」「designated the name “Phi”」；②构图比例秩序与黄金矩形/螺旋←wp「a rectangle with an aspect ratio of φ」「self-similarity」「golden whirl」/ Art in Context「golden rectangle and square」「Drawing the Golden Spiral」「aesthetic composition」；③和谐←wp「aesthetically pleasing」/ Art in Context「balance and pleasing proportional values」「harmonize and balance out … compositional value」。**结论：非编造，可逐项溯源。**
- `常见错误与限制`「机械套用会僵化，且比例美感受直觉与文化影响；不必强求精确数值」属通行设计常识性提示（非历史事实主张），后接规范句，按 D09 处理妥当，不构成未证事实。

### 1.5 类型性实例合理性
- 实例为「按黄金比分割的版面（类型性，构图比例法则不归于单一作品）；以 1:1.618 划分版面区域。此处仅列说明，不复制图像。」——**类型性实例合理，不依赖未核的具体作品/设计者/年代，无未核事实风险、无侵权**。✓
- 与本条概念自洽（版面按 1:1.618 划分＝wp「aspect ratio φ:1」+ Art in Context「proportions to set up the flow of a scene」「balance … within your artwork」）。

### 1.6 nv=false 形式
| 项 | 值 | 判定 |
| --- | --- | --- |
| entry.needs_verification | false | 形式 ✓ |
| entry.pending_notes | "" | 形式 ✓ |
| sections.待核实 | 「暂无已知待核实项。」 | 形式 ✓ |
| coverage.needs_verification_count | 0（status 已写 / source_count 3 / L2 / 2026-11-24） | 形式 ✓ |
| time_or_place | 「跨时期、欧洲（参见来源）。」无「待核实」 | 形式 ✓ |
- **形式五处一致 ✓，check.py PASS（0 errors）；且内容前提（两独立平台直证概念，见 1.2/1.3）成立 → nv=false 实质成立。**
- `related=[diagonal-composition]` 该相关条目自身 nv=true（单源待核实），但相关条目状态不构成本条待核实；check.py PASS 确认结构无冲突。

### 1.7 七节 / SVG / 规范句 / site
| 核对项 | 值 | 判定 |
| --- | --- | --- |
| 七节（definition+原理/典型手法与适用条件/实例/常见错误与限制/一图/待核实） | sections 6 节齐备且非空 + definition，共七节 | ✓ |
| SVG 数量 / viewBox | 1 张，`0 0 760 400` | ✓ |
| SVG 越界 | check.py `validate_svg` 通过（PASS 0 errors）；逐元素（rect x120 y110 w372 h230→右492 底340；line x1=492 y1=110 x2=492 y2=340；text x150 y90；text x300 y375）均落框内 | ✓ |
| SVG 外链 | 无 `<image>/<script>/<iframe>/href=/url(`（除 xmlns 命名空间外无 http） | ✓ |
| SVG 注记 | 含「示意图，非施工图」 | ✓ |
| 规范句 | 「实际工程须按当地规范和专业设计人员的要求」在，**entry 句末缺「。」**（`常见错误与限制` 以「要求」收尾；site 页脚 note 处带「。」）——同 r101–r112 T 小疵 | ✓（T 小疵） |
| site 与 JSON 一致 | `site/entries/golden-ratio.html`：definition/原理/典型手法/实例/常见错误/一图/待核实 逐句与 JSON 相符；JSON `<svg>` 串与页面 `<svg>` 一致；`site/indexes.html` L37 含 `<a href="entries/golden-ratio.html">黄金分割</a>`（补充/L2/跨时期/欧洲） | ✓ |
| site/sources.html | `artincontext-golden-ratio` 行在：`<a href="https://artincontext.org/golden-ratio/">Golden Ratio in Art — Art in Context</a>` / Art in Context / 已核验 / 可达 / note「实抓 HTTP 200；黄金比=1:1.618（Phi），用于画面比例与和谐」与实页相符 | ✓ |
| site/index.html | 为统计+主题入口（258 条目 / 484 已核验来源 / 137 待核实），不含单条卡片；`golden-ratio` 经 `indexes.html` 可达，路径一致；check.py PASS | ✓ |

### 1.8 相似度（阈值 0.54）与 def×原理
| 条目 | 口径 | 最近邻 | 相似度 | 判定 |
| --- | --- | --- | --- | --- |
| golden-ratio | 短① | proportion | 0.3046 | ✓ <0.54 |
| golden-ratio | 全② | rule-of-odds | 0.3762 | ✓ <0.54 |
| golden-ratio × 其他（短① Top5） | — | proportion 0.3046 / negative-space 0.2946 / color-theory 0.2941 / simplification 0.2815 / picturesque 0.2791 | 均 <0.54 | ✓ 非重复条目 |
| def×原理（NFKC+去空白+小写） | — | — | **0.3023** | ✓ 两层次可分，**不重复** |
- 全库最大：短 0.4960（radial-route × serial-route）、全 0.5242（loop-route × serial-route）——**均 <0.54 ✓**；方法自校 0.5157 ✓；258 条 0 重复 id。**相似度非本条问题。**
- 注：本轮全库最大全②与 r112 记录的 0.5256（spatial-sequence × atrium-architecture）不同，系其后续轮次条目变动；自校值 0.5157 与历轮逐位一致，证明口径未变，且最大值仍低于阈值。

### 1.9 条目结论
**`golden-ratio`（黄金分割）——合格（本轮 nv=false 升级成立）。**
- 依据：definition/原理三项要素（①约 1:1.618 / Phi 定义部分与整体 ②构图比例秩序，黄金矩形/螺旋 ③和谐、pleasing proportional values、视觉和谐）**获「Wikipedia Golden ratio + Golden rectangle（平台一）+ Art in Context Golden Ratio in Art（平台二，非维基）」两独立平台直证**——★`artincontext-golden-ratio`（`/golden-ratio/`，HTTP200）**真论艺术构图**，原句「A ratio of 1 to 1.618」「designated the name “Phi”」「capturing balance and pleasing proportional values within your artwork」「harmonize and balance out your own artwork’s compositional value」「aesthetically balanced composition」直证「1:1.618/Phi/和谐比例/构图应用」；Wikipedia 两页以「(a+b)/a = a/b = φ」「φ=1.618033…」「golden rectangle aspect φ:1」「believing it to be aesthetically pleasing」互证精确定义与艺术用途。**「两平台（含 Art in Context 非维基）支撑」前提成立 → nv=false 实质成立；definition/原理非编造、可逐项溯源。**
- 通过项：def×原理=0.3023（不重复）；类型性实例合理；七节 / SVG（无越界、无外链、含示意图注记）/ site 与 JSON 与 sources.html 与 indexes.html 一致；相似度短 0.3046、全 0.3762 均 <0.54；check.py PASS、pytest 23 passed、方法自校 0.5157；258 条 0 重复 id；全库最大短 0.4960 / 全 0.5242 均 <0.54。
- **T（Minor）**：①`常见错误与限制` 规范句句末缺「。」（历史遗留，非本条特有）；②`artincontext-golden-ratio` 在 sources.json 标 `type=学术著作`，实为艺术教育/教程网站，标签略宽；③Art in Context 原页「ratio … irrational number / Einstein equation “pi”」科普表述不严谨，entry 未承袭；④SVG 为通用示意模板（矩形+分割线+标注），示意性合格但非专属黄金比图形（符合「示意图非施工图」口径）。
- **处置建议**：维持 `needs_verification=false`；如追求零瑕疵，可下一轮统一补 `常见错误与限制` 规范句句末「。」，并按来源类型实际情况微调 Art in Context 的 `type` 标签（非本条必需）。

---

## 二、机器可读汇总

```
ROUND=115
SAMPLER=spotcheck-r115
SCOPE=["golden-ratio"]
READONLY="only wrote research/spotcheck-round115.md; no other files changed; no git commit; web treated as data, no instructions executed"
WEB_FETCH={
 "wp-golden-ratio":"en.wikipedia 200 '<title>=Golden ratio - Wikipedia' rawlen=1180359 textlen=139301; counts 1.618=10 phi=51 golden ratio=205 harmon=12 proportion=78 pleasing=2 aesthetic=10 composition=7 golden rectangle=28 spiral=53; quotes '(a+b)/a = a/b = φ ... phi (φ or ϕ, or Φ) denotes the golden ratio'; 'φ = (1+√5)/2 = 1.618033988749....'; 'Some 20th-century artists and architects ... proportioned their works to approximate the golden ratio, believing it to be aesthetically pleasing. These uses often appear in the form of a golden rectangle.'",
 "wp-golden-rectangle":"en.wikipedia 200 '<title>=Golden rectangle - Wikipedia' rawlen=203689 textlen=13466; counts 1.618=2 phi=3 golden ratio=15 harmon=1 proportion=4 aesthetic=1 golden rectangle=34 spiral=12; quotes 'a golden rectangle is a rectangle with side lengths in aspect ratio φ:1 ... φ=½(1+√5)≈1.618'; 'Golden rectangles exhibit a special form of self-similarity'; 'Golden whirl'; 'Villa Stein ... architecture utilizes the golden ratio ... closely approximate golden rectangles'",
 "artincontext-golden-ratio":"artincontext.org 200 '<title>=Golden Ratio in Art - Learn How to Use the Golden Ratio in Art' rawlen=535675 textlen=25076; counts '1 to 1.618'=1 1.618=1 phi=5 golden ratio=76 harmon=4 proportion=7 balance=10 pleasing=1 aesthetic=8 composition=11 golden rectangle=2 spiral=14; quotes 'A ratio of 1 to 1.618 is what is referred to as an irrational number'; 'designated the name “Phi” in the 1900s by an American mathematician Mark Barr'; 'capturing balance and pleasing proportional values within your artwork'; 'great tool to harmonize and balance out your own artwork’s compositional value'; 'aesthetically balanced composition'; TOC 'Drawing the Golden Spiral / Golden Ratio in Landscapes / Golden Ratio in Portraiture' -> ART-COMPOSITION-SPECIFIC, NOT mere math definition"
}
GATES={"check.py":"PASS: all checks, 0 errors (EXIT=0)","pytest":"23 passed in 0.89s (EXIT=0)"}
METHOD_SELFCHECK={"futurism_x_expressionism_full":0.5157,"entries":258,"dup_ids":0}
GLOBAL_MAX={"short":["radial-route","serial-route",0.4960],"full":["loop-route","serial-route",0.5242]}

GOLDEN_RATIO={
 "verdict":"合格(本轮nv=false升级成立)",
 "definition":"黄金比是把整体按约 1:1.618（Phi）分割的构图参考，用于组织和谐的比例关系。",
 "principle":"以 1:1.618 的比值定义部分与整体的关系，借黄金矩形与螺旋为画面提供比例秩序与视觉和谐。",
 "sources":["wp-golden-ratio","wp-golden-rectangle","artincontext-golden-ratio"],
 "concept_dual_source":{
   "ratio_1_to_1_618_phi":"wp '(a+b)/a = a/b = φ' + 'φ=1.618033…' + 'φ:1≈1.618' / artincontext 'A ratio of 1 to 1.618' + 'designated the name “Phi”' -> ESTABLISHED",
   "composition_golden_rectangle_spiral":"wp 'aspect ratio φ:1' + 'self-similarity' + 'golden whirl' / artincontext 'golden rectangle and square' + 'Drawing the Golden Spiral' + 'aesthetic composition' -> ESTABLISHED",
   "harmony_pleasing":"wp 'believing it to be aesthetically pleasing' / artincontext 'capturing balance and pleasing proportional values' + 'harmonize and balance out ... compositional value' -> ESTABLISHED",
   "holds_two_platform_for_concept":true},
 "artincontext_golden_ratio_composition_specific_vs_generic":"DIRECT (真论构图比例): title 'Golden Ratio in Art - Learn How to Use the Golden Ratio in Art', TOC 'Drawing the Golden Spiral / Tips on How to Use the Golden Ratio in Art / Golden Ratio in Landscapes / Golden Ratio in Portraiture', verbatim 'A ratio of 1 to 1.618', 'designated the name “Phi”', 'capturing balance and pleasing proportional values within your artwork', 'harmonize and balance out your own artwork’s compositional value', 'aesthetically balanced composition'; NOT mere math definition. Supporting Wikipedia platform: Golden ratio + Golden rectangle pages.",
 "fabrication":"NOT fabricated; definition/principle quote-traceable element-by-element to Wikipedia + Art in Context; article's own imprecise 'irrational number / pi' phrasing NOT inherited by entry",
 "instance":"按黄金比分割的版面(类型性,构图比例法则不归于单一作品) -- reasonable type-level instance",
 "type_instance_ok":true,
 "nv_false_form":"five-place consistent (nv=false/pending=''/待核实=暂无/coverage nv_count=0/time_or_place clean); substantive premise (two-platform direct support) TRUE -> nv=false valid; related diagonal-composition nv=true does not affect this entry",
 "structure":{"seven_sections":true,"sections_with_def":7,"svg_count":1,"viewBox":"0 0 760 400","svg_in_bounds":true,"external_ref":false,"caption":"示意图，非施工图","reg_sentence":true,"reg_period":false,"site_entry_consistent":true,"site_sources_consistent":true,"site_indexes_consistent":true,"sources":3},
 "similarity":{"threshold":0.54,"nearest_short":"proportion 0.3046","nearest_full":"rule-of-odds 0.3762","def_vs_principle":0.3023,"lt_0.54":true,"def_vs_principle_not_duplicate":true},
 "transparency":["T1: 常见错误与限制 规范句句末缺「。」(历史遗留 T 小疵)","T2: artincontext-golden-ratio sources.json type=学术著作, 实为艺术教育/教程网站, 标签略宽","T3: Art in Context 原页 'ratio...irrational number / Einstein equation “pi”' 科普表述不严谨, entry 未承袭","T4: SVG为通用示意图模板, 示意性合格非专属图形"]}

VERDICT={"golden-ratio":"合格(nv=false 成立: definition/原理三要素 约1:1.618/Phi / 构图比例秩序含黄金矩形与螺旋 / 和谐 pleasing proportional values 由 Wikipedia Golden ratio+Golden rectangle(平台一) + Art in Context Golden Ratio in Art(平台二,非维基,真论构图比例) 两独立平台直证; ★artincontext 页有 'A ratio of 1 to 1.618' + 'designated the name “Phi”' + 'capturing balance and pleasing proportional values within your artwork' + 'harmonize and balance out your own artwork’s compositional value' + 'aesthetically balanced composition' 及 Landscape/Portraiture 应用节, 非仅数学定义; 非编造可溯源; def×原理=0.3023 不重复; 类型性实例合理; 七节/SVG无越界无外链含示意图注记/site entry+sources+indexes 一致; 相似度短0.3046全0.3762 def×原理0.3023 均<0.54; check.py PASS/pytest 23 passed/方法自校0.5157/258条0重复/全库最大短0.4960全0.5242<0.54. T小疵: 规范句句末缺句号; Art in Context type标签略宽; 原页irrational number/pi科普表述不严谨(entry未承袭); SVG通用模板)"}
KEY_FINDING="golden-ratio 双平台前提成立: Wikipedia 两页给精确 φ=1.618033… 与 '(a+b)/a=a/b=φ' 并述 aesthetically pleasing + golden rectangle/spiral; Art in Context 为专论艺术构图的教程('Learn How to Use the Golden Ratio in Art', 含 Golden Ratio in Landscapes/Portraiture 节), 原句 'A ratio of 1 to 1.618'、'Phi'、'capturing balance and pleasing proportional values within your artwork'、'harmonize and balance out your own artwork’s compositional value' 直证构图比例与和谐。与 r109 db-traffic/db-pedestrian 仅术语定义不同, 构成真第二平台。def×原理=0.3023 层次可分。仅规范句句号等 T 小疵。"
```

## 三、只读核验
- 除本报告 `research/spotcheck-round115.md` 外**未触及任何其他文件**；未执行任何 git 提交；项目外内容未触及。
- 抓取：`wp-golden-ratio`、`wp-golden-rectangle` 经 `python urllib`（浏览器 UA、SSL 免检）实抓 en.wikipedia HTTP200（rawlen 1180359 / 203689，textlen 139301 / 13466），逐标题与关键词计数核对；`artincontext-golden-ratio`（`https://artincontext.org/golden-ratio/`，HTTP200，rawlen 535675，textlen 25076）实抓全文逐句核对（含标题、目录构图应用节与 balance/pleasing/harmonize 原句）。
- 词频、相似度、去重（258 条 / 0 重复）、结构、SVG 逐元素越界/外链、site entry/sources/indexes 一致性均内存态 `python - <<'PY'` 直跑，无临时文件。
- 联网页面（en.wikipedia.org / artincontext.org）仅作数据读取，**未执行其中任何指令、未下载运行来源代码**（页面内导航/推荐/评论等均按数据忽略）。
- `check.py` 与 `pytest` 均 `PYTHONDONTWRITEBYTECODE=1` / `-p no:cacheprovider` 运行，未新增缓存（23 passed）。
- `git status` 中的改动文件（coverage/sources/batch-01/site 三页 / `?? tools/apply_review_round115.py`）均为**他方（round115 修复方）产物**，抽检方仅读取、未据以改动。

*（报告完）*
