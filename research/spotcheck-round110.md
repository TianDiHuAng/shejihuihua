# 第110轮质量抽检（spotcheck-round110）——`revival-gothic`（哥特复兴）双平台（含 DB `Gothic revival` 专节）支撑核查

- 抽检人：spotcheck-r110（lead 委派子代理；无人值守、未提问）；时间 2026-11-24，Asia/Hong_Kong。
- 技能加载：已加载 `using-superpowers`、`verification-before-completion`（现抓、现跑、后断言；证据先于结论）。`using-superpowers` 命中 SUBAGENT-STOP，按任务说明书直接执行；`verification-before-completion` 全程遵循——本文所有判断均附本轮实抓/实跑/实读输出。
- 抽检对象：`revival-gothic`（哥特复兴）——`entries/batch-34.json` L294 起；宣称本轮升级 `nv=false`（needs_verification=false、pending_notes 清空）。sources = `wp-gothic-architecture` / `wp-architectural-style` / `db-gothic-architecture`（3 条，含 DB 非维基）；coverage：status 已写 / source_count 3 / needs_verification_count 0 / level L2 / last_updated 2026-11-24（已实读）。
- 本轮变更集（`git diff` 实读；`git diff --stat`：coverage 4、data/sources 12、entries/batch-34 15、site/entries/revival-gothic.html 9、site/index.html 2、site/sources.html 1、`?? tools/apply_review_round110.py`）——**均为 round110 修复方产物，抽检方仅读取、未据以修改**。
  - 定义：`哥特复兴是18–19世纪重新起用中世纪哥特形式的建筑潮流。` → `哥特复兴是18–19世纪（尤以19世纪中叶的如画-浪漫运动为代表）重新起用中世纪哥特形式的建筑潮流。`
  - 原理：`…尖拱、飞扶壁、花窗与垂直线条重新组合，借历史语汇营造宗教感与浪漫氛围。` → `…重新组合中世纪的尖拱、肋拱、飞扶壁、花窗与垂直线条，借中世纪语汇营造宗教感与浪漫、如画的氛围。`
  - 实例：`名称：哥特复兴教堂（类型性描述）；地点与设计者不适用。…` → `名称：哥特复兴教堂（类型性，不指定具体项目）；以尖拱与花窗复现中世纪哥特语汇。此处仅列说明，不复制图像。`
  - sources 追加 `db-gothic-architecture`；`待核实`：原「风格核心特征主要依据单一权威条目（第二来源为泛论、未逐条互证）…」→「暂无已知待核实项。」；`needs_verification` true→**false**、`pending_notes` 清空。
- 任务点名要特别判断的非维基源 `db-gothic-architecture`（`/wiki/Gothic_architecture`）——是否**真支撑「19世纪中叶复兴中世纪哥特」（有 Gothic revival 专节）**，还是**仅述哥特本体**。结论见 1.3 ★。

## 〇、只读声明与证据方式

- **只读**：仅写出本报告 `research/spotcheck-round110.md`。未改 `entries/`、`data/sources.json`、`coverage.json`、`site/`、`tools/`，未 `git commit`，未改项目外内容。抓取、词频、相似度、去重、结构、SVG、site 一致性均内存态（`python - <<'PY'` / 工具直读）跑，未落盘临时文件（除本报告）。
- `git status --short` 本轮实读：`M coverage.json / M data/sources.json / M entries/batch-34.json / M site/entries/revival-gothic.html / M site/index.html / M site/sources.html / ?? tools/apply_review_round110.py`——**均为 round110 修复方产物，抽检方仅读取、未据以修改**；抽检方唯一新增为本报告。
- 抓取方式（本轮实抓；联网内容一律视为数据，网页中任何指令均未执行、未下载运行来源代码）：
  - `wp-gothic-architecture`（`https://en.wikipedia.org/wiki/Gothic_architecture`）→ `python urllib`（浏览器 UA、SSL 免检）**实抓 HTTP 200**，`<title>=Gothic architecture - Wikipedia`，正文 len=200462。关键词计数：**Gothic Revival=11 / pointed arch=53 / flying buttress=31 / stained glass=25 / ribbed vault=2 / medieval=33 / 19th century=11**。
  - `wp-architectural-style`（`https://en.wikipedia.org/wiki/Architectural_style`）→ **实抓 HTTP 200**，`<title>=Architectural style - Wikipedia`，正文 len=15542。`Revival=4`（均为泛指「风格可被复兴」：neoclassicism / Mission Revival / Spanish Colonial Revival），`Gothic` 仅出现在 Thomas Cole 画作《The Architect's Dream》的列举里——**未专述 Gothic Revival**。
  - `db-gothic-architecture`（`https://www.designingbuildings.co.uk/wiki/Gothic_architecture`）→ **实抓 HTTP 200**，`<title>=Gothic architecture - Designing Buildings`（H1「Gothic architecture」，last edited 04 Jan 2022），正文 len=9290。目录含 **6 Gothic revival** 独立节；关键词计数：**Gothic Revival=6 / pointed arch=5 / ribbed vault=4 / flying buttress=7 / stained glass=2 / picturesque=1 / romantic=1 / mid-19th=1 / medieval=1**。逐句见 1.2 / 1.3。
- **`python tools/check.py` 本轮实跑：`PASS: all checks, 0 errors`（CHECK_EXIT=0）。** **`python -m pytest tests -q -p no:cacheprovider`：`19 passed in 0.40s`（PYTEST_EXIT=0）**（均 `PYTHONDONTWRITEBYTECODE=1`，未新增缓存/未落盘）。
- 相似度方法承前轮：`difflib.SequenceMatcher`，去全部空白（NFKC 归一）+小写；口径①短=title+definition+time_or_place+overview；口径②全=definition+time_or_place+overview+六节正文（按 sections 顺序）。**方法自校：`futurism-style × expressionism-style` 口径②=0.5157（与 r108/r109 逐位一致，方法正确）。全库 258 条，无重复 id。**

---

## 一、`revival-gothic`（哥特复兴）

### 1.1 当前 entry 实读（`entries/batch-34.json` L294 起）
- `definition`＝「哥特复兴是18–19世纪（尤以19世纪中叶的如画-浪漫运动为代表）重新起用中世纪哥特形式的建筑潮流。」
- `原理`＝「哥特复兴重新组合中世纪的尖拱、肋拱、飞扶壁、花窗与垂直线条，借中世纪语汇营造宗教感与浪漫、如画的氛围。」
- `典型手法与适用条件`＝「按哥特母题设计教堂与校园建筑。」
- `overview`＝「它用尖拱、飞扶壁与花窗唤起对中世纪的浪漫想象，多见于教堂与校园。」
- `实例`＝「名称：哥特复兴教堂（类型性，不指定具体项目）；以尖拱与花窗复现中世纪哥特语汇。此处仅列说明，不复制图像。」
- `常见错误与限制`＝「形式复古而结构未必匹配；需现代加固。实际工程须按当地规范和专业设计人员的要求」（**句末缺「。」**）
- sources = wp-gothic-architecture / wp-architectural-style / db-gothic-architecture；`needs_verification=false`、`pending_notes=""`、`待核实=暂无已知待核实项。`、`time_or_place=文艺复兴至19世纪、欧洲（参见来源）。`、`related=[]`。level L2 / tier 补充 / theme 风格 / period 文艺复兴至19世纪 / region 欧洲。

### 1.2 definition/原理 两平台核对（实抓引句）
概念拆解：①时间跨度＝**18–19世纪**；②代表运动＝**19世纪中叶 picturesque(如画)-romantic(浪漫) 运动**；③核心＝**重新起用/复兴中世纪哥特形式**；④形式特征＝**尖拱/肋拱/飞扶壁/花窗（+垂直线条），营造宗教感与浪漫、如画氛围**。

**wp-gothic-architecture（Wikipedia；en 直连 HTTP200，`<title>=Gothic architecture`）——②③④直证，①直证：**
- 复兴（③①）：实抓句「A series of **Gothic revivals** began in **mid-18th century England, spread through 19th century Europe** and continued, largely for **churches and university buildings**, into the 20th century.」——直证「18–19世纪」「复兴」「多见于教堂与校园」。
- 复兴机制（②③）：「…neo-Gothic began to become promoted … as the preferred style for ecclesiastical… The appeal of this **Gothic Revival** (which after 1837, in Britain, is sometimes termed **Victorian Gothic**)…」；并设「Main article: **Gothic Revival architecture**」。
- 形式特征（④）：正文导语「The style is characterised by **pointed arches, rib vaults, flying buttresses and large, traceried stained glass windows**.」；「The defining characteristic of the Gothic style is the **pointed arch**, which was widely used … giving a sensation of **verticality**.」
- 结论：该源对「18–19世纪复兴中世纪哥特 + 哥特形式特征」**均有直证**。

**db-gothic-architecture（Designing Buildings；`/wiki/Gothic_architecture`，HTTP200，H1「Gothic architecture」）——②③专节直证、④直证：**
- 复兴（②③）——**独立节「6 Gothic revival」逐句**：「**The Gothic Revival style is part of the mid-19th century picturesque and romantic movement in architecture, reflecting the public's taste for buildings inspired by medieval design.**」——直证「19世纪中叶」「picturesque & romantic 运动」「以中世纪设计为灵感（复兴中世纪哥特）」。
- 形式特征（④）：该页把「**Ribbed vault / Pointed arch / Flying buttress**」列为「The three defining features of the Gothic style」，并述「…what was new was the way they were combined」；「Other features」列「**Stained glass windows** (particularly rose windows) to filter light」「Large windows」。
- 结论：该源既有 **Gothic revival 专节**（支撑复兴概念），又有 **哥特本体形式节**（支撑尖拱/肋拱/飞扶壁/花窗）——**两用直证**。

**wp-architectural-style（Wikipedia；HTTP200）——泛论「风格可被复兴」，无 Gothic Revival 专述：**
- 仅「After an architectural style has gone out of fashion, revivals and re-interpretations may occur… classicism… Mission Revival… Spanish Colonial Revival」等**一般性论述**；`Gothic` 仅出现在 Thomas Cole 画作列举里。**不专述 Gothic Revival，属泛论性第三源**（旧「待核实」所称「第二来源为泛论」即指此）。

| 概念要素 | wp-gothic-architecture | db-gothic-architecture（非维基） | wp-architectural-style | 判定 |
| --- | --- | --- | --- | --- |
| ① 18–19世纪 | ✓「Gothic revivals… mid-18th century England, spread through 19th century Europe」 | ✓「mid-19th century」 | ✗（泛论） | **成立** |
| ② 19世纪中叶 picturesque-romantic 运动 | △「19th century… Victorian Gothic」（未点 picturesque/romantic） | ✓ 专节原句「mid-19th century picturesque and romantic movement」 | ✗ | **成立（DB 直证，wp 佐证）** |
| ③ 重新起用/复兴中世纪哥特形式 | ✓「Gothic revivals / neo-Gothic / Gothic Revival architecture」 | ✓「buildings inspired by medieval design」 | ✗ | **成立** |
| ④ 尖拱/肋拱/飞扶壁/花窗（+垂直线条） | ✓「pointed arches, rib vaults, flying buttresses, traceried stained glass windows」 | ✓「Ribbed vault/Pointed arch/Flying buttress」+「Stained glass windows」 | ✗ | **成立** |

**判定（1.2）：definition/原理 获「两独立平台」直证。** 两平台＝Wikipedia `Gothic architecture`（②③④直证、①直证）与 DB `Gothic architecture`（②③专节直证、④直证）；四项概念要素**均至少两平台成立**（②核心 picturesque-romantic 由 DB 专节原句直证，wp 佐证 19 世纪复兴语境）。`wp-architectural-style` 为泛论性第三源、不专述 Gothic Revival，但两平台直证已由前两者满足。

### 1.3 ★特别判断：`db-gothic-architecture` 的 "Gothic revival" 专节是否真支撑「19世纪中叶复兴中世纪哥特」
**结论：是。DB 页确有独立「Gothic revival」专节，逐句直述「19世纪中叶 + picturesque/romantic 运动 + 复兴中世纪设计」，非仅述哥特本体。**
- **专节存在**：页面目录列举「1 Introduction / 2 Plan form / 3 Ribbed vaults and pointed arches / 4 Flying buttresses / 5 Other features / **6 Gothic revival** / 7 Related articles」，第 6 节为**独立成节**，非附注一句。
- **专节原句直证三维**：「**The Gothic Revival style is part of the mid-19th century picturesque and romantic movement in architecture, reflecting the public's taste for buildings inspired by medieval design.**」
  - 时间＝**mid-19th century**（19世纪中叶）✓；
  - 运动性质＝**picturesque and romantic movement**（如画-浪漫运动）✓；
  - 概念＝**buildings inspired by medieval design**（复兴中世纪哥特设计）✓。
- **与「仅述哥特本体」区分**：DB 页第 1–5 节确述哥特本体（12世纪起源、平面、肋拱/尖拱/飞扶壁、花窗等）；但第 6 节是**专门讲「复兴」这件 19 世纪的事**，与本体分开成节。故该源**同时**支撑「哥特形式特征」（本体节→原理）与「19世纪中叶复兴中世纪哥特」（专节→定义）——**正是本条定义/原理所需的双要素，非仅本体**。
- **对照第109轮反例**：r109 的 `db-traffic`/`db-pedestrian` 只是**词义术语定义（泛述交通/行人）**、无「流线组织」直证，故不合格；本条 `db-gothic-architecture` 有**独立复兴专节 + 形式定义要素**，性质不同，**构成真第二平台直证**。
- **附（源数据极小疵，可忽略）**：sources.json 标题记「Gothic architecture — Designing Buildings」，实页 `<title>=Gothic architecture - Designing Buildings`（破折号 em-dash vs hyphen 差异），标题实质一致；`note` 所述「含尖拱/肋拱/飞扶壁/花窗与 Gothic Revival=19世纪中叶 picturesque-romantic 运动专节」与实页**逐项相符**。

### 1.4 是否编造
- definition/原理**均可逐句溯源、非杜撰**：①18–19世纪←wp「mid-18th century…19th century」/DB「mid-19th century」；②如画-浪漫运动←DB 专节原句；③复兴中世纪哥特←wp「Gothic revivals/neo-Gothic」/DB「inspired by medieval design」；④尖拱/肋拱/飞扶壁/花窗/垂直线条←wp 导语与「defining characteristic…pointed arch…verticality」/DB「three defining features…Ribbed vault/Pointed arch/Flying buttress」+「Stained glass windows」。**结论：非编造，可溯源。**
- `常见错误与限制`「形式复古而结构未必匹配；需现代加固」属通行专业常识性提示（非历史事实主张），且后接规范句，按 D09 处理妥当，不构成未证事实。

### 1.5 类型性实例合理性
- 实例已改为「哥特复兴教堂（类型性，不指定具体项目）；以尖拱与花窗复现中世纪哥特语汇。此处仅列说明，不复制图像。」——**类型性实例合理，不依赖未核的具体项目/设计者/年代，无未核事实风险、无侵权**。✓
- 与本条概念自洽（教堂＝DB「mainly to religious buildings」、wp「largely for churches」；尖拱/花窗＝形式特征直证）。

### 1.6 nv=false 形式
| 项 | 值 | 判定 |
| --- | --- | --- |
| entry.needs_verification | false | 形式 ✓ |
| entry.pending_notes | "" | 形式 ✓ |
| sections.待核实 | 「暂无已知待核实项。」 | 形式 ✓ |
| coverage.needs_verification_count | 0（status 已写 / source_count 3 / L2 / 2026-11-24） | 形式 ✓ |
| time_or_place | 「文艺复兴至19世纪、欧洲（参见来源）。」无「待核实」 | 形式 ✓ |
- **形式五处一致 ✓，check.py PASS；且内容前提（两独立平台直证概念，见 1.2/1.3）成立 → nv=false 实质成立。**

### 1.7 七节 / SVG / 规范句 / site
| 核对项 | 值 | 判定 |
| --- | --- | --- |
| 七节（definition+原理/典型手法与适用条件/实例/常见错误与限制/一图/待核实） | sections 6 节齐备且非空 + definition，共七节 | ✓ |
| SVG 数量 / viewBox | 1 张，`0 0 760 400` | ✓ |
| SVG 越界 | check.py `validate_svg` 通过（PASS 0 errors）；逐元素（path M220,300→220,180 Q380,40→540,180→540,300；line 160,300→600,300；text x250 y350；text x40 y40）均落框内 | ✓ |
| SVG 外链 | 无 `<image>/<script>/<iframe>/href=/url(`（forbidden=[]） | ✓ |
| SVG 注记 | 含「示意图，非施工图」（figcaption 亦「图 1：示意图，非施工图」） | ✓ |
| 规范句 | 「实际工程须按当地规范和专业设计人员的要求」在，**entry 句末缺「。」**（`常见错误与限制` 以「要求」收尾；site 页脚 note 处带「。」）——同 r101–r109 T 小疵 | ✓（T 小疵） |
| site 与 JSON 一致 | `site/entries/revival-gothic.html`：title/definition/overview(lead)/time_or_place/原理/典型手法/实例/常见错误/一图/待核实 逐句 `in html=True`；JSON `<svg>` 串 `in html=True`；源三行（Gothic architecture / Architectural style / Gothic architecture — Designing Buildings）一致 | ✓ |

### 1.8 相似度（阈值 0.54）与 def≠原理
| 条目 | 口径 | 最近邻 | 相似度 | 判定 |
| --- | --- | --- | --- | --- |
| revival-gothic | 短① | revival-renaissance | 0.4398 | ✓ <0.54 |
| revival-gothic | 全② | eclecticism | 0.3525 | ✓ <0.54 |
| revival-gothic × revival-renaissance（短① Top5） | — | revival-renaissance 0.4398 / renaissance-style 0.3605 / rococo 0.3146 / light-shadow-modeling 0.2919 / neoclassical 0.2889 | 均 <0.54 | ✓ 非重复条目 |
| def×原理（去重） | — | — | 0.2178 | ✓ 两层次可分 |
- 全库最大：短 0.4960（serial-route×radial-route）、全 0.5256（spatial-sequence×atrium-architecture）——**均 <0.54 ✓**；方法自校 0.5157 ✓；258 条无重复 id。**相似度非本条问题。**

### 1.9 条目结论
**`revival-gothic`（哥特复兴）——合格（本轮 nv=false 升级成立）。**
- 依据：definition/原理四项要素（①18–19世纪 ②19世纪中叶 picturesque-romantic 运动 ③重新起用中世纪哥特形式 ④尖拱/肋拱/飞扶壁/花窗+垂直线条）**获「Wikipedia Gothic architecture + DB Gothic architecture」两独立平台直证**——★特别判断 `db-gothic-architecture`（`/wiki/Gothic_architecture`，HTTP200）**有独立「6 Gothic revival」专节**，原句「The Gothic Revival style is part of the mid-19th century picturesque and romantic movement in architecture, reflecting the public's taste for buildings inspired by medieval design」**直证「19世纪中叶复兴中世纪哥特」**（非仅述本体），且本体节列「Ribbed vault / Pointed arch / Flying buttress」三定义特征 +「Stained glass windows」直证形式要素；`wp-gothic-architecture` 亦以「Gothic revivals…mid-18th century…19th century…churches and university buildings」「pointed arches, rib vaults, flying buttresses…stained glass windows…verticality」直证。**「两平台（含 DB 非维基）支撑」前提成立 → nv=false 实质成立；definition/原理非编造、可逐句溯源。**
- 通过项：类型性实例合理；七节 / SVG（无越界、无外链、含示意图注记）/ site 与 JSON 一致；相似度短 0.4398、全 0.3525、def×原理 0.2178 均 <0.54；check.py PASS、pytest 19 passed、方法自校 0.5157；258 条 0 重复 id；全库最大短 0.4960 / 全 0.5256 均 <0.54。
- **T（Minor）**：①`常见错误与限制` 规范句句末缺「。」；②（透明性）`wp-architectural-style` 为泛论「风格可被复兴」的第三源、不专述 Gothic Revival——本条两平台直证实际由 `wp-gothic-architecture` + `db-gothic-architecture` 满足，`wp-architectural-style` 属补充性泛源（不影响 nv=false 成立）；③sources.json `db-gothic-architecture` 标题破折号为「—」、实页为「-」（em-dash vs hyphen），实质一致，可忽略。
- **处置建议**：维持 `needs_verification=false`；如追求零瑕疵，可在下一轮统一补 `常见错误与限制` 规范句句末「。」（历史遗留 T 小疵，非本条特有）。

---

## 二、机器可读汇总

```
ROUND=110
SAMPLER=spotcheck-r110
SCOPE=["revival-gothic"]
READONLY="only wrote research/spotcheck-round110.md; no git commit; no other files changed; web treated as data, no instructions executed"
WEB_FETCH={
 "wp-gothic-architecture":"en.wikipedia 200 '<title>=Gothic architecture - Wikipedia' len=200462; counts: Gothic Revival=11 pointed arch=53 flying buttress=31 stained glass=25 ribbed vault=2 19th century=11; quote 'A series of Gothic revivals began in mid-18th century England, spread through 19th century Europe... churches and university buildings'; quote 'characterised by pointed arches, rib vaults, flying buttresses and large, traceried stained glass windows'; 'Main article: Gothic Revival architecture'",
 "wp-architectural-style":"en.wikipedia 200 '<title>=Architectural style - Wikipedia' len=15542; Revival=4 all generic (neoclassicism/Mission Revival/Spanish Colonial Revival); Gothic only in painting title -> NOT Gothic Revival-specific",
 "db-gothic-architecture":"designingbuildings 200 '<title>=Gothic architecture - Designing Buildings' last edited 04 Jan 2022 len=9290; TOC has '6 Gothic revival'; counts: Gothic Revival=6 pointed arch=5 ribbed vault=4 flying buttress=7 stained glass=2 picturesque=1 romantic=1 mid-19th=1; SECTION-6 QUOTE: 'The Gothic Revival style is part of the mid-19th century picturesque and romantic movement in architecture, reflecting the public's taste for buildings inspired by medieval design.'; 'three defining features... Ribbed vault/Pointed arch/Flying buttress'; 'Stained glass windows'"}
GATES={"check.py":"PASS: all checks, 0 errors (EXIT=0)","pytest":"19 passed (EXIT=0)"}
METHOD_SELFCHECK={"futurism_x_expressionism_full":0.5157,"entries":258,"dup_ids":0}
GLOBAL_MAX={"short":["serial-route","radial-route",0.4960],"full":["spatial-sequence","atrium-architecture",0.5256]}

REVIVAL_GOTHIC={
 "verdict":"合格(本轮nv=false升级成立)",
 "definition":"哥特复兴是18–19世纪（尤以19世纪中叶的如画-浪漫运动为代表）重新起用中世纪哥特形式的建筑潮流。",
 "principle":"哥特复兴重新组合中世纪的尖拱、肋拱、飞扶壁、花窗与垂直线条，借中世纪语汇营造宗教感与浪漫、如画的氛围。",
 "sources":["wp-gothic-architecture","wp-architectural-style","db-gothic-architecture"],
 "concept_dual_source":{
   "time_18_19c":"wp-gothic 'mid-18th century...19th century' / db 'mid-19th century' -> ESTABLISHED",
   "mid19c_picturesque_romantic":"db section-6 verbatim 'mid-19th century picturesque and romantic movement' (primary) + wp '19th century/Victorian Gothic' (support) -> ESTABLISHED",
   "reuse_medieval_gothic_form":"wp 'Gothic revivals/neo-Gothic/Gothic Revival architecture' / db 'buildings inspired by medieval design' -> ESTABLISHED",
   "form_features_pointed_ribbed_flying_stained_vertical":"wp 'pointed arches, rib vaults, flying buttresses, traceried stained glass windows...verticality' / db 'Ribbed vault/Pointed arch/Flying buttress'+'Stained glass windows' -> ESTABLISHED",
   "holds_two_platform_for_concept":true},
 "db_gothic_revival_section_direct_vs_generic":"DIRECT (真支撑): DB /wiki/Gothic_architecture has dedicated section '6 Gothic revival' verbatim 'The Gothic Revival style is part of the mid-19th century picturesque and romantic movement in architecture, reflecting the public's taste for buildings inspired by medieval design' -> supports mid-19th-century revival of medieval Gothic, NOT merely describing Gothic proper; plus form-feature section (Ribbed vault/Pointed arch/Flying buttress/Stained glass) supports 原理. Unlike r109 db-traffic/db-pedestrian which were generic term definitions.",
 "fabrication":"NOT fabricated; definition/principle quote-traceable element-by-element to wp-gothic + db-gothic",
 "instance":"哥特复兴教堂(类型性,不指定具体项目) -- reasonable type-level instance",
 "type_instance_ok":true,
 "nv_false_form":"five-place consistent (nv=false/pending=''/待核实=暂无/coverage nv_count=0/time_or_place clean); substantive premise (two-platform direct support) TRUE -> nv=false valid",
 "structure":{"seven_sections":true,"sections_with_def":7,"svg_count":1,"viewBox":"0 0 760 400","svg_in_bounds":true,"external_ref":false,"caption":"示意图，非施工图","reg_sentence":true,"reg_period":false,"site_consistent":true,"sources":3},
 "similarity":{"threshold":0.54,"nearest_short":"revival-renaissance 0.4398","nearest_full":"eclecticism 0.3525","def_vs_principle":0.2178,"lt_0.54":true},
 "transparency":["T1: 常见错误与限制 规范句句末缺「。」","T2: wp-architectural-style 为泛论第三源(不专述Gothic Revival), 两平台直证实由 wp-gothic-architecture + db-gothic-architecture 满足","T3: sources.json db 标题破折号 — vs 实页 - (实质一致, 可忽略)"]}

VERDICT={"revival-gothic":"合格(nv=false 成立: definition/原理四要素 18–19世纪/19世纪中叶 picturesque-romantic/复兴中世纪哥特/尖拱肋拱飞扶壁花窗+垂直线条 由 wp-gothic-architecture(Wikipedia) + db-gothic-architecture(DB非维基) 两独立平台直证; ★db-gothic-architecture 有独立'6 Gothic revival'专节原句'mid-19th century picturesque and romantic movement...buildings inspired by medieval design'直证19世纪中叶复兴中世纪哥特(非仅述本体), 本体节列Ribbed vault/Pointed arch/Flying buttress+Stained glass直证形式; 非编造可溯源; 类型性实例合理; 七节/SVG无越界无外链含示意图注记/site与JSON一致; 相似度短0.4398全0.3525 def×原理0.2178 均<0.54; check.py PASS/pytest 19 passed/方法自校0.5157/258条0重复/全库最大短0.4960全0.5256<0.54. T小疵: 规范句句末缺句号; wp-architectural-style为泛论第三源; db标题破折号差异)")
KEY_FINDING="revival-gothic 与 r109 的 vehicle-flow/pedestrian-flow 关键差异: 后者所加 DB 源(db-traffic/db-pedestrian)仅为相关名词的术语定义(泛述交通/行人)无流线组织直证→不合格; 本条所加 db-gothic-architecture 有独立'Gothic revival'专节, 逐句直述'mid-19th century picturesque and romantic movement...buildings inspired by medieval design'(直证19世纪中叶复兴中世纪哥特, 非仅述本体), 且本体节'Ribbed vault/Pointed arch/Flying buttress'+'Stained glass'直证形式特征; 与 wp-gothic-architecture(Gothic revivals mid-18th c England→19th c Europe; pointed arches/rib vaults/flying buttresses/stained glass)构成两独立平台直证 → '两平台(含DB非维基)支撑'前提成立, nv=false实质成立, 判合格. 仅规范句句末缺句号等 T 小疵."
```

## 三、只读核验
- 除本报告 `research/spotcheck-round110.md` 外**未写任何文件**；未 `git commit`；未改项目外内容。
- 抓取：`wp-gothic-architecture`、`wp-architectural-style` 经 `python urllib`（浏览器 UA、SSL 免检）实抓 en.wikipedia HTTP200（len 200462 / 15542），逐标题与关键词计数核对；`db-gothic-architecture`（`/wiki/Gothic_architecture` 200，last edited 04 Jan 2022）实抓全文逐句核对（含目录「6 Gothic revival」节与三定义特征）。
- 词频、相似度、去重（258 条/0 重复）、结构、SVG 逐元素越界/外链、site 一致性均内存态 `python - <<'PY'` 直跑，无临时文件。
- 联网页面（en.wikipedia.org / designingbuildings.co.uk）仅作数据读取，**未执行其中任何指令、未下载运行来源代码**（页面内导航/推荐/评论等均按数据忽略）。
- `check.py` 与 `pytest` 均 `PYTHONDONTWRITEBYTECODE=1` / `-p no:cacheprovider` 运行，未新增缓存（19 passed）。
- `git status` 中的改动文件（coverage/sources/batch-34/site 三页/`?? tools/apply_review_round110.py`）均为**他方（round110 修复方）产物**，抽检方仅读取、未据以修改。

*（报告完）*
