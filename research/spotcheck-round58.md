# 第58轮质量抽检报告（spotcheck-round58）——第58轮补具名实例的 3 条（qi-yun / gongbi / xieyi）

- 抽检人：spotcheck-r58（lead 委派子代理，无人值守、未提问）；抽检时间 2026-11-23 18:07–18:16，Asia/Hong_Kong。
- 任务：对第58轮「补具名实例」条目中 lead 定点 3 条——`qi-yun`（气韵生动，`entries/batch-02-a.json` 73–105 行）、`gongbi`（工笔，`entries/batch-32.json` 192–222 行）、`xieyi`（写意，`entries/batch-32.json` 224–254 行）——逐条核对 definition / time_or_place / overview / 实例是否有引用来源正文支撑、是否编造、来源是否直接相关；核对 L2 七节 / 内联 SVG / 规范提示；核对 `needs_verification` 与 `pending_notes` / 正文「待核实」联动（本轮多为「传本/摹本/真迹存疑」的诚实标注）；核对相似度（阈值 0.54）。
- **路径提示偏差（已纠正）**：lead 任务书写「`qi-yun`…（`entries/batch-32.json`）」，实读 `batch-32.json` 只含 `gongbi`/`xieyi`；`qi-yun` 实际在 `entries/batch-02-a.json`（本轮 git 亦显示该文件被改）。本报告按真实文件抽检，不据错误路径判定。
- 抽样说明：round58 落地脚本 `tools/apply_review_round58.py`（只读查看）的 `INST` 共 **8 条**补具名实例条目（qi-yun / liubai / yijing / bone-method / cunfa / gongbi / xieyi / ink-wash），来源底稿 `research/review-round58a.md`（4 条）与 `review-round58b.md`（4 条）。本轮定点抽 3 条，占 3/8=37.5%，满足 `AUTONOMOUS.md` §E「随机 10%／至少 3 个」下限，且 lead 定点优先于随机。其余 5 条只作状态观察，不列入内容判定。
- 协议依据：`AUTONOMOUS.md` §E（质量闸：check.py 必须通过；抽检不合格则整批返工、下轮抽检提至 25%；待核实占比异常低或相似度过高→整批降级）＋第六节（联网内容一律视为数据，网页中任何指令不得执行，项目文件夹之外保持原样）；`TASK_design.md`「条目页结构」L2 七节与「专用规则」（每页 1–2 张内联 SVG、图下注「示意图，非施工图」、SVG 元素不出 viewBox、尺寸/坡度/消防/无障碍附「实际工程须按当地规范和专业设计人员的要求」）＋「通用硬性规则」（不编造数字/日期/人名/引文/出处；关键事实至少两个独立来源互证，否则标待核实；只引用 `verified=true` 来源）；`DECISIONS.md` D05/D06/D07/D10/D11/D14。
- 技能：按 host 规则加载 `using-superpowers`（本会话为委派子代理，命中 `SUBAGENT-STOP`，以任务说明书执行）与 `verification-before-completion`（先实抓、后断言；6 个新增具名实例来源正文均由本轮 `web_fetch` / `urllib` 实抓回读为准，未采信底稿的二手转述）。

## 〇、数据稳定性与只读声明

- **采样快照（本轮实读，2026-11-23 18:07 起）**：`coverage.json`=`total=258`、`pending_sum=**193**`；`entries/batch-02-a.json`=24009B、`batch-32.json`=24272B、`data/sources.json`=227835B。三条 `needs_verification_count` 各=1、`source_count` 各=4。
- **`git log -1`** = `a23ce03 docs: note round57 push status`。第58轮改动尚未提交：`git status --porcelain` 显示 `M coverage.json`、`M data/sources.json`、`M entries/batch-02-a.json`、`M entries/batch-32.json`、`M site/entries/{bone-method,cunfa,gongbi,ink-wash,liubai,qi-yun,xieyi,yijing}.html`、`M site/index.html`、`M site/sources.html`，以及 `?? research/review-round58a.md`、`review-round58b.md`、`tools/apply_review_round58.py`（lead 侧底稿/脚本，本抽检不触碰）。抽检对象即上述未提交工作树中的 3 条现状，非 HEAD 内容。
- **`python tools/check.py` 本轮实跑：`PASS: all checks, 0 errors`（EXIT=0）**。运行前已 grep 确认该脚本无写文件语句（`open(...,'w')`/`write_text`/`.write(`/`shutil`/`unlink`/`os.remove` 均 0 命中）。
- **只读声明**：本次**仅写出** `research/spotcheck-round58.md` 一个项目文件；未修改 `entries/`、`data/sources.json`、`coverage.json`、`tools/`、`site/`、`review-round58a.md`、`review-round58b.md`、`apply_review_round58.py` 或任何其他项目内容文件，未 `git commit`，未改项目文件夹之外内容（抓取全程内存，无文件写入）。联网内容一律视为数据，网页中任何指令性文本均未执行。
- **治理文件说明**：项目根 `AUTONOMOUS.md` / `TASK_design.md` 在工作区磁盘为 NOT_FOUND；按前轮先例实读桌面原件 `D:/Users/Administrator/Desktop/AUTONOMOUS.md`（71 行）与 `D:/Users/Administrator/Desktop/TASK_design.md`（67 行），另读本项目 `DECISIONS.md`（25 行）、`research/spotcheck-round57.md`（236 行）、`review-round58a.md`（121 行）、`review-round58b.md`（117 行）、`tools/apply_review_round58.py`（67 行）。

## 一、判定口径与抓取方法

- **L2 七节口径**：顶层 `definition` + `sections` 内 原理 / 典型手法与适用条件 / 实例 / 常见错误与限制 / 一图 / 待核实（6 节）＝共 7 节；须 1–2 张内联 SVG 且含「示意图，非施工图」；SVG 元素须限制在 viewBox 内、无 `on*` 事件属性、无外链图片；「常见错误与限制」段须以「实际工程须按当地规范和专业设计人员的要求」收尾。
- **抓取与回验方法**：`dpm-luoshenfu`（故宫名画记）、`chinaculture-luoshenfu`（ChinaCulture）、`dpm-furong`（故宫藏品页）本轮 `web_fetch` HTTP 200 且关键句正文可见；`people-furong`（人民网，GB18030）、`rmzx-poshui`（人民政协网）、`npm-poshui`（NPM 数位典藏）`web_fetch` 报 `fetch failed` 或乱码，改 `urllib`+浏览器 UA+非校验 SSL 取正文（分别 41520B / 43817B / 80186B，均 HTTP 200），关键句按去标签→`html.unescape`→`norm()`（去空白＋小写）子串回验，全部 FOUND（见第五节回执）。Wikipedia / 百科镜像按项目既定口径不作证据。
- **三级判定定义（沿用第51–57轮）**：
  - **合格**：definition/time/overview/实例均获所引来源正文直接支撑；关键事实（核心定义或实例四要素）由 ≥2 独立来源直证互证或由强权威官方源直证且第二源覆盖实例结构；无编造；机械项全过或仅有不影响判定的轻微问题。
  - **待核实**：核心获直接相关来源实质支撑，但某关键事实（实例四要素、年份、具体术语或内容映射）实质单源/无源，或为来源未逐字作出的解读/存在来源明确讨论的学术争议；`needs_verification=true` 且 pending/正文如实披露者，属「正确的待核实管理」，判待核实但无治理缺陷。
  - **不合格**：definition/overview 主干被两个引用来源均不支撑（实质无源）；或实例核心四要素无任何来源直证；或关键结构项（七节/SVG）实质不满足 TASK_design 强制要求。
- **相似度口径**：`difflib.SequenceMatcher`；①短文本＝`title+definition+time_or_place+overview`；②全字段-不含 SVG（`definition+time_or_place+overview` + 六节正文，按 `sections` 原始插入顺序、`一图` 解说文字计入、`svg` 标记不计入），归一为去空白＋小写。全库 258 条逐条扫描，警戒线 **0.54**。**方法自校**：`futurism-style vs expressionism-style` 全字段②＝**0.5157**，与第39–57轮报告逐位一致，口径正确。
- **相似度是独立维度**：超线触发 §E「整批降级」，与「不合格（内容无源）→整批返工」是不同触发路径；pending 联动失真单独列为问题，不自动等于内容无源。

## 二、抽检对象来源清单与完整性

3 条共引用 **12 处来源引用（每条 4；6 个新增具名实例来源＋6 个沿用概念来源；无跨条目共用具名源，`wp-chinese-painting` 为三条共用的概念背景源）**。6 个新增来源全部在 `data/sources.json` 登记、`verified=true`、`year=null`（D06 允许）、`link_ok=null`（三态未标）；沿用概念来源按项目既有 `verified=true` 登记，本轮未改。

| 条目 | 来源 id | 机构 / type | 实抓标题或端点（本轮证据） | verified / link_ok | 与主题相关性 |
| --- | --- | --- | --- | --- | --- |
| qi-yun | `wp-six-principles-chinese-painting` | Wikipedia / 概念背景（沿用） | 六法/气韵概念背景（前轮登记） | true / true | 背景（概念主干，本轮未改） |
| qi-yun | `wp-chinese-painting` | Wikipedia / 概念背景（沿用） | 中国画通论（前轮登记） | true / true | 背景（概念主干，本轮未改） |
| qi-yun | `dpm-luoshenfu` | 故宫博物院·故宫名画记 / 官方机构 | `顾恺之洛神赋图卷（宋摹）-故宫名画记`（HTTP 200） | true / null | **直接·实例主证**：「东晋，顾恺之作」「顾恺之（约345—406）」「以形写神」「传神写照，正在阿堵」「学界一般认为是宋摹本」 |
| qi-yun | `chinaculture-luoshenfu` | ChinaCulture 中国文化网英文站 / 官方机构 | `Luoshen Appraisal Painting`（HTTP 200） | true / null | **直接·实例佐证**：`His representative work, Luoshen Appraisal Painting, is now kept at the Palace Museum in Beijing`、`vividly captures the jovial mood… sadness`、`considered a classic` |
| gongbi | `wp-chinese-painting` / `wp-ink-wash-painting` | Wikipedia / 概念背景（沿用） | 中国画／水墨通论（前轮登记） | true / true | 背景（概念主干，本轮未改） |
| gongbi | `dpm-furong` | 故宫博物院藏品页 / 官方机构 | `赵佶芙蓉锦鸡图轴 - 故宫博物院`（HTTP 200） | true / null | **直接·实例主证**：「《芙蓉锦鸡图》轴，（传）北宋徽宗赵佶绘」「工致细丽者如《芙蓉锦鸡图》」「双钩法……多用于工笔花鸟画」「徐邦达先生指出……画院画家的作品」 |
| gongbi | `people-furong` | 人民网文化频道 / 中央级官方媒体 | `宋元书画缘何令人追慕至今--文化--人民网`（urllib HTTP 200，GB18030） | true / null | **直接·实例佐证**：「宋徽宗《芙蓉锦鸡图》 现藏于北京故宫博物院」「这幅作品可谓宋徽宗工笔花鸟画的代表作，绢本立轴，双勾重彩」 |
| xieyi | `wp-chinese-painting` / `wp-ink-wash-painting` | Wikipedia / 概念背景（沿用） | 中国画／水墨通论（前轮登记） | true / true | 背景（概念主干，本轮未改） |
| xieyi | `npm-poshui` | 国立故宫博物院（台北）数位典藏 / 官方机构 | `名畫琳瑯　冊　宋梁楷潑墨仙人`（urllib HTTP 200） | true / null | **直接·实例主证**：「作者 梁楷」「人物衣紋描法(減筆) 寫意」「48.7x27.7」「國立故宮博物院，台北」 |
| xieyi | `rmzx-poshui` | 人民政协网·人民政协报社 / 中央级官方媒体 | `笔墨风格考证：台北故宫藏《泼墨仙人图》是真迹吗`（urllib HTTP 200） | true / null | **直接·实例佐证**：`《泼墨仙人图》是梁楷减笔画的代表作`、`纸本，纵48.7厘米，横27厘米，水墨画`、`成为后代画家大写意追捧的楷模`、`写意画技法`、真迹归属争议 |

> 6 个新增来源 id 全部存在、`verified=true`、`year=null`、`link_ok=null`，无假 id、无 `link_ok=false`。关键相关性结论：三条 definition/overview 由沿用概念背景源支撑，实例四要素由**两个不同机构的具名实例来源**直证互证；`qi-yun` 的「气韵生动↔该作品」归属为解读（两源未逐字用该术语），`gongbi` 的作者归属争议、`xieyi` 的真迹归属争议均为来源明确讨论且如实披露。

## 三、任务 1：来源正文是否支撑 definition / time_or_place / overview 及七节「实例」

### 3.1 qi-yun（气韵生动，第58轮改动）——**待核实（正确的待核实管理）**

- 条目现状（实读 `entries/batch-02-a.json` 73–105 行）：`definition`＝「六法之首，强调作品的精神气息与生动韵致。」；`time_or_place`＝「古代中国（参见来源）。」；`overview`＝「气韵生动关注整体生命感，而非单一物象的精确再现。」；`实例`＝「名称：顾恺之《洛神赋图》（现存宋摹本）；地点：北京故宫博物院藏；作者：顾恺之（约 345–406）；年代：东晋（现存宋摹）。以形写神、传神写照。……」
- **definition / overview 支撑（概念背景·沿用源）**：`wp-six-principles-chinese-painting`、`wp-chinese-painting` 支撑「六法之首」「整体生命感」的概念主干，属前轮已验证的概念背景，本轮未改，无具体数字/引文，可接受。非编造。
- **实例四要素（双源直证）**：
  - **名称**：故宫名画记标题「顾恺之洛神赋图卷（宋摹）」 + ChinaCulture `Luoshen Appraisal Painting` → 双源直证 ✓。
  - **地点**：「北京故宫博物院藏」由 ChinaCulture `now kept at the Palace Museum in Beijing` + 故宫名画记（故宫藏品语境）→ 双源直证 ✓。
  - **作者/年代**：故宫名画记「东晋，顾恺之作」「顾恺之（约345—406）」「学界一般认为是宋摹本」 + ChinaCulture `Gu Kaizhi (346-407)`、`Eastern Jin Dynasty` → 双源直证，条目采用故宫「约345–406」并标注「现存宋摹」，诚实 ✓。
  - **「以形写神、传神写照」**：故宫名画记逐字「以形写神」「传神写照，正在阿堵」直证 ✓。
- **关键缺口（判待核实主因·已如实披露）**：两源均未逐字写出中文「气韵生动」四字，也未直接说「此画气韵生动」；「按谢赫六法第一法归入气韵生动实例」是条目的解读性映射。条目 `needs_verification=true`、`pending_notes` 与正文「待核实」同为「两源直证"以形写神"与代表作，但未逐字使用"气韵生动"；概念归属为解读。」→ 该解读性质已如实披露，不构成隐瞒。
- **七节其他内容**：`原理`「六法之首、整体气脉」与概念背景源相容；`典型手法与适用条件`「用笔连贯、虚实相生、经营位置」为一般性说明，附规范句。
- **无编造**：instance 四要素均由引用来源正文支撑；不复制图像。
- **问题**：
  - ① **（判待核实主因·已披露）** 概念归属为解读，两源未逐字用「气韵生动」；保持待核实正确，升级需补一源直接把该作品与「气韵生动」挂钩。
  - ② **（轻微）** 生卒年两源小差：故宫「约345–406」vs ChinaCulture「346–407」，条目取前者并加「约」，可接受；若要极致严谨可写「约345–407（各源略异）」。
  - ③ 两个 `wp-*` 概念源为沿用背景源，`link_ok=true`；新增两源 `link_ok=null` 已标。
- **内容判定：待核实（正确的待核实管理）**。`needs_verification=true` ↔ pending ↔ 正文「待核实」三者一致且披露诚实；无治理缺陷。

### 3.2 gongbi（工笔，第58轮改动）——**待核实（正确的待核实管理，内容四要素双源扎实）**

- 条目现状（实读 `entries/batch-32.json` 192–222 行）：`definition`＝「工笔是以精细勾勒与层层设色为特征的中国画法。」；`time_or_place`＝「古代中国（参见来源）。」；`overview`＝「它工整细腻，常用于人物、花鸟。」；`实例`＝「名称：《芙蓉锦鸡图》轴；地点：北京故宫博物院藏；作者：（传）赵佶／画院画家御题画；年代：北宋 12 世纪初。以双钩重彩、工致细丽著称。……」
- **definition / overview 支撑（概念背景·沿用源）**：`wp-chinese-painting`、`wp-ink-wash-painting` 支撑「中国画法」概念背景，本轮未改；「工整细腻、常用于人物花鸟」为一般性说明。非编造。
- **实例四要素（双源直证）**：
  - **名称**：故宫藏品页「《芙蓉锦鸡图》轴」 + 人民网「宋徽宗《芙蓉锦鸡图》」→ 双源 ✓。
  - **地点**：故宫藏品页（故宫藏品语境、文物号故00005872） + 人民网「现藏于北京故宫博物院」→ 双源 ✓。
  - **作者**：故宫藏品页「（传）北宋徽宗赵佶绘」＋「徐邦达先生指出……画院画家的作品」＋《南宋馆阁续录》「御题画」 + 人民网「宋徽宗工笔花鸟画的代表作」→ 双源合证「（传）赵佶／画院画家御题画」，条目如实并列两说，不写「徽宗亲笔」✓。
  - **年代**：「北宋 12 世纪初」为约数（底稿据赵佶 1082–1135 推定），来源未给绝对纪年，条目写约数不写死，可接受 ✓。
  - **「双钩重彩、工致细丽」**：人民网「绢本立轴，双勾重彩」+ 故宫藏品页「工致细丽者如《芙蓉锦鸡图》」「双钩法……多用于工笔花鸟画」→ 双源逐字支撑 ✓。
- **关键标注（判待核实主因·已如实披露）**：作者归属存在真实学术争议（亲笔 vs 画院御题画），来源明确讨论；条目 `needs_verification=true`、`pending_notes` 与正文「待核实」同为「作者不可写徽宗亲笔（故宫引徐邦达说为画院御题画），已按传本标注。」→ 争议与处置如实披露，不构成隐瞒。
- **七节其他内容**：`原理`「勾线立骨、罩染求润」、`典型手法与适用条件`「先勾线定形，再淡彩多次罩染」与故宫藏品页「双钩法线条细劲」「色彩晕染得层次清晰」相容。
- **无编造**：四要素与术语均由引用来源正文支撑；作者争议如实并列；不复制图像。
- **问题**：
  - ① **（判待核实主因·已披露）** 作者归属争议属来源明确讨论的未决学术分歧，条目以「（传）赵佶／画院画家御题画」并列并标 pending，方向正确；若 lead 认为该表述已充分解决争议，可评估清零（见第九节建议）。
  - ② **（轻微）** 年代「北宋 12 世纪初」为据作者生卒的约数，来源无绝对纪年，建议保持「约」表述。
  - ③ 两个 `wp-*` 概念源为背景；新增两源 `link_ok=null` 已标。
- **内容判定：待核实（正确的待核实管理；内容四要素双源扎实）**。三者一致、披露诚实；无治理缺陷。按内容实质，本条接近「合格」，唯一保留 nv 的理由是来源中真实存在的作者归属争议。

### 3.3 xieyi（写意，第58轮改动）——**待核实（正确的待核实管理，内容四要素双源扎实）**

- 条目现状（实读 `entries/batch-32.json` 224–254 行）：`definition`＝「写意是以简练笔墨抒写意趣的中国画法。」；`time_or_place`＝「古代中国（参见来源）。」；`overview`＝「它重神韵与笔势，不拘形似细节。」；`实例`＝「名称：梁楷《泼墨仙人图》；地点：国立故宫博物院（台北）藏；作者：传梁楷；年代：南宋约 13 世纪初。以减笔泼墨的大写意著称。……」
- **definition / overview 支撑（概念背景·沿用源）**：`wp-chinese-painting`、`wp-ink-wash-painting` 支撑概念背景，本轮未改；「重神韵与笔势、不拘形似」为一般性说明。非编造。
- **实例四要素（双源直证）**：
  - **名称**：NPM 数位典藏「名畫琳瑯　冊　宋梁楷潑墨仙人」 + 人民政协网「《泼墨仙人图》」→ 双源 ✓。
  - **地点**：NPM「國立故宮博物院，台北」 + 人民政协网「现藏于台北故宫博物院」「现存于台北故宫博物院」→ 双源 ✓。
  - **作者**：NPM「作者 梁楷」+ 人民政协网「梁楷为南宋画院画家」→ 双源；条目写「传梁楷」保守 ✓。
  - **年代**：「南宋约 13 世纪初」由人民政协网「主要活动在孝、光、宁三朝」「嘉泰年间（1201-1204）……年过五十」「生活时间约1140-1228」支撑，为约数 ✓。
  - **「减笔泼墨的大写意」**：NPM 技法栏逐字「人物衣紋描法(減筆) 寫意」 + 人民政协网「减笔画的代表作」「成为后代画家大写意追捧的楷模」「写意画技法」→ 双源逐字支撑 ✓。
- **关键标注（判待核实主因·已如实披露）**：尺寸两源略出入（NPM 48.7×27.7 vs 人民政协网 48.7×27）且真迹归属有学术争议（人民政协网整篇讨论「是真迹吗」，列中日学者分歧）；条目写「约 48.7×27cm」并入「传本/争议」标注，`needs_verification=true`、`pending_notes` 与正文「待核实」同为「尺寸两源略有出入（约 48.7×27cm），真迹归属有争议，已按传本标注。」→ 出入与争议如实披露，不构成隐瞒。
- **七节其他内容**：`原理`「以少胜多、笔势与留白」、`典型手法与适用条件`「阔笔泼墨、一次成形、重气势虚实」与人民政协网「粗笔横扫，笔简而意到」「泼墨」相容。
- **无编造**：四要素与术语均由引用来源正文支撑；真迹争议如实并列；不复制图像。
- **问题**：
  - ① **（判待核实主因·已披露）** 真迹归属争议与尺寸出入为来源明确讨论，条目已按传本/约数处理；若 lead 认为披露充分可评估清零。
  - ② **（轻微）** NPM 宽度 27.7cm、人民政协网 27cm，条目取「约 27cm」合理；来源 `rmzx-poshui` 系人民政协网转载新浪收藏稿，底稿按「中央级官方媒体发布页」采用，若需更硬来源可补 NPM Style 专页。
  - ③ 两个 `wp-*` 概念源为背景；新增两源 `link_ok=null` 已标。
- **内容判定：待核实（正确的待核实管理；内容四要素双源扎实）**。三者一致、披露诚实；无治理缺陷。按内容实质，本条接近「合格」，唯一保留 nv 的理由是来源中真实存在的真迹归属争议与尺寸出入。

## 四、任务 2：来源 id 存在性、verified、相关性、可达性（汇总）

- **存在性/verified/link_ok**：新增 6 个来源 id 全部存在、`verified=true`、`year=null`（D06 允许）、`link_ok=null`；沿用 6 处概念源前轮登记 `verified=true`。无假 id，无 `link_ok=false`。
- **可达性（本轮实抓）**：6 个新增来源本轮全部取得正文——3 个 `web_fetch` 200，3 个 `urllib` 200（people-furong GB18030、rmzx-poshui、npm-poshui）。`link_ok=null` 未标 true 属三态保守，不影响证据效力。
- **相关性结论**：
  - `qi-yun`：概念背景源支撑定义/overview；故宫名画记 + ChinaCulture 双源直证《洛神赋图》四要素；「气韵生动」归属为解读（已披露）。
  - `gongbi`：概念背景源支撑定义；故宫藏品页 + 人民网双源直证《芙蓉锦鸡图》四要素与工笔术语；作者归属争议双源并列（已披露）。
  - `xieyi`：概念背景源支撑定义；NPM 数位典藏 + 人民政协网双源直证《泼墨仙人图》四要素与写意术语；真迹争议/尺寸出入双源披露。

## 五、任务 3：L2 七节完整性 + SVG + 风险/规范提示（程序化实核）

| 条目 | level | definition 顶层 | sections 6 节 | SVG 数 | viewBox | 含「示意图，非施工图」 | on* 事件 / 外链图 | 规范句收尾 | SVG 几何越界 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| qi-yun | L2 | ✓ | 6/6 | 1 | `0 0 760 400` | ✓ | 无 / 无 | ✓ | NONE |
| gongbi | L2 | ✓ | 6/6 | 1 | `0 0 760 400` | ✓ | 无 / 无 | ✓ | NONE |
| xieyi | L2 | ✓ | 6/6 | 1 | `0 0 760 400` | ✓ | 无 / 无 | ✓ | NONE |

> 七节完整（定义 + 原理/典型手法与适用条件/实例/常见错误与限制/一图/待核实，无缺节无多余节）；每条 1 张内联 SVG、`viewBox='0 0 760 400'`、含「示意图，非施工图」、无 `on*`、无 `<image>`/外链；三条「常见错误与限制」均以「实际工程须按当地规范和专业设计人员的要求」收尾；`check.py` PASS。**机械项三条形式层面全部通过。**
>
> **几何实核（本轮新增，针对第57轮 acoustic 越界缺陷的同类检查）**：用脚本按 `x/y/width/height` 与 `cx/cy/rx/ry` 复算三条 SVG 元素包围盒，全部落在 0–760 × 0–400 内，**无第57轮 acoustic 那种越出 viewBox 的缺陷**。三条均含 `<text>` 设计意图文字（qi-yun「笔势贯通而气脉生动」、gongbi/xieyi「笔墨层次与气脉」）。
>
> **SVG 质量观察（系统性次要项，延续第44–57轮）**：gongbi 与 xieyi 的 SVG **完全相同**（同一「笔墨层次与气脉」通用图），且均未标注具体尺寸关系，`TASK_design` 要求「图中标注设计意图或尺寸关系」的语义项未被 `check.py` 覆盖；建议为两条换用更贴实例的示意图并补尺寸/意图标注。此为本轮引入的通用图复用（非存量），不影响内容判定，列为次要问题。

## 六、任务 4：元数据一致性 + needs_verification ↔ pending_notes ↔ 正文待核实

- 三条 `title/tier/theme/period/region/level` 与 `coverage.json` 逐字段**一致**（程序化比对 `mismatch=[]`，无 MISMATCH）；`source_count` 与来源数组长度一致（4=4、4=4、4=4）；`coverage.needs_verification_count` 三条各=1，与条目 `needs_verification=true` 逐条对应。
- `pending_sum`=**193**，与第57轮报告记录持平（194→193→193），本轮 8 条补实例条目 `keep=True` 全保留待核实，无清零；存量待核实占比 193/258≈74.8%，处历史高位，**不触发「待核实占比异常低（疑似硬写）」降级**。

| 条目 | needs_verification | pending_notes（结构化） | 正文「待核实」节 | 联动一致性 |
| --- | --- | --- | --- | --- |
| qi-yun | true（保持） | 「两源直证"以形写神"与代表作，但未逐字使用"气韵生动"；概念归属为解读。」 | 同 pending 逐字一致 | **结构一致 ✓、内容恰当 ✓**：解读性质已披露，保持待核实正确。 |
| gongbi | true（保持） | 「作者不可写徽宗亲笔（故宫引徐邦达说为画院御题画），已按传本标注。」 | 同 pending 逐字一致 | **结构一致 ✓、内容恰当 ✓**：作者归属争议双源并列并披露。 |
| xieyi | true（保持） | 「尺寸两源略有出入（约 48.7×27cm），真迹归属有争议，已按传本标注。」 | 同 pending 逐字一致 | **结构一致 ✓、内容恰当 ✓**：尺寸出入与真迹争议如实披露。 |

> **异常监控（§E）**：全库 `pending_sum` 193，与第57轮持平（0 变化）。本轮 8 条补实例条目统一 `keep=True`，无硬写清零；无「占比异常低」触发。

## 七、任务 5：相似度（difflib 去空白＋小写，阈值 0.54；全库 258 条；口径②=全字段-不含 SVG）

### 7.1 对既有库（排除自身）逐条扫描

| 条目 | ①短文本 max（vs 全库除自身） | 判 | ②全字段 max（vs 全库除自身） | 判 |
| --- | --- | --- | --- | --- |
| qi-yun | **0.3429** vs composition-placement | <0.54 ✓ | **0.3642** vs yijing | <0.54 ✓ |
| gongbi | **0.4583** vs xieyi | <0.54 ✓ | **0.4644** vs xieyi | <0.54 ✓ |
| xieyi | **0.4583** vs gongbi | <0.54 ✓ | **0.4682** vs gongbi | <0.54 ✓ |

> 三条两档均 **<0.54**，未越线。最高为 xieyi 全字段 0.4682 / gongbi 全字段 0.4644（均指向彼此，两条同为「古代中国画法 + 工笔/写意对称句式 + 传本实例」结构，属正常近邻；实例分别为《芙蓉锦鸡图》与《泼墨仙人图》，内容分化明显）。

### 7.2 第58轮批内 3 条两两（全字段② / 短文本①）

- qi-yun vs gongbi：全字段 **0.3568**、短文本 0.3119。
- qi-yun vs xieyi：全字段 **0.3511**、短文本 0.3048。
- gongbi vs xieyi：全字段 **0.4644**、短文本 0.4583。
- → 批内两两均低于 0.54，无套话/模板姊妹风险。

### 7.3 方法自校

- `futurism-style vs expressionism-style` 全字段②＝**0.5157**，与第39–57轮报告逐位一致，口径正确。

> **文本相似度判定：三条对全库与批内均 PASS（<0.54）；无相似度降级触发。**

## 八、逐条验收结论

| 条目 | definition / time / overview / 实例 来源支撑 | 来源存在·verified·相关·可达 | 七节 / 规范 / SVG | 元数据·pending 联动 | 相似度(①②) | 结论 |
| --- | --- | --- | --- | --- | --- | --- |
| **qi-yun（气韵生动）** | 概念背景源支撑定义/overview；《洛神赋图》四要素双源（故宫+ChinaCulture）直证；「气韵生动」归属为解读且已披露；无编造 | 新增 2/2 存在且 true；本轮 200；实例源直接相关 | 七节齐、规范句✓；1 SVG 含「示意图，非施工图」、无越界 | 全部一致；nv=true↔pending↔「待核实」披露诚实 | 全库 ✓（0.3429/0.3642）；批内 ✓ | **待核实** |
| **gongbi（工笔）** | 概念背景源支撑定义；《芙蓉锦鸡图》四要素双源（故宫+人民网）直证，工笔术语逐字；作者归属争议双源并列；无编造 | 新增 2/2 存在且 true；本轮 200；实例源直接相关 | 七节齐、规范句✓；1 SVG 含「示意图，非施工图」、无越界（图与 xieyi 重复，次要） | 全部一致；nv=true↔pending↔「待核实」披露诚实 | 全库 ✓（0.4583/0.4644）；批内 ✓ | **待核实** |
| **xieyi（写意）** | 概念背景源支撑定义；《泼墨仙人图》四要素双源（NPM+人民政协网）直证，写意术语逐字；真迹争议/尺寸出入双源披露；无编造 | 新增 2/2 存在且 true；本轮 200；实例源直接相关 | 七节齐、规范句✓；1 SVG 含「示意图，非施工图」、无越界（图与 gongbi 重复，次要） | 全部一致；nv=true↔pending↔「待核实」披露诚实 | 全库 ✓（0.4583/0.4682）；批内 ✓ | **待核实** |

### 问题清单

- **① qi-yun 概念归属为解读（判待核实主因·已如实披露）**：两源未逐字用「气韵生动」，「按六法第一法归入」为解读；已标 nv=true 并披露，属「正确的待核实管理」；升级需补一源直接挂钩该术语与该作品。
- **② qi-yun 生卒年两源小差（轻微）**：故宫「约345–406」vs ChinaCulture「346–407」，条目取前者并加「约」，可接受。
- **③ gongbi 作者归属争议（判待核实主因·已如实披露）**：亲笔 vs 画院御题画为来源明确讨论的学术分歧，条目以「（传）赵佶／画院画家御题画」并列并披露；内容四要素双源扎实，实质接近合格；如需升级，可评估清零或补一源定论。
- **④ gongbi 年代约数（轻微）**：「北宋 12 世纪初」据作者生卒推定，来源无绝对纪年，保持「约」表述即可。
- **⑤ xieyi 真迹争议/尺寸出入（判待核实主因·已如实披露）**：48.7×27.7 vs 48.7×27、真迹归属争议，条目按传本/约数披露；内容四要素双源扎实，实质接近合格；`rmzx-poshui` 为转载稿，如需更硬来源可补 NPM Style 专页。
- **⑥ 概念源背景定位（轻微）**：`wp-six-principles-chinese-painting` / `wp-chinese-painting` / `wp-ink-wash-painting` 为概念背景源，建议注明为背景而非实例主证；新增 6 源 `link_ok=null` 已标。
- **⑦ SVG 通用图复用（次要·本轮引入）**：gongbi 与 xieyi 使用完全相同的「笔墨层次与气脉」SVG，且缺尺寸/设计意图标注；建议换用贴实例的示意图并补标注（延续第44–57轮系统性方向）。
- **⑧ 三态与可达性（轻微）**：人民政协网、NPM、人民网 `web_fetch` 失败/乱码经 urllib 200（NPM UTF-8、人民网 GB18030），按连接/编码异常处理、非死链；`link_ok=null` 未标 true 属三态保守。

## 九、总体结论与建议

- **抽样结果**：第58轮补具名实例条目中定点抽检 3 条——`qi-yun`、`gongbi`、`xieyi`。**内容维度：0 合格（3 条均待核实，其中 gongbi/xieyi 内容实质接近合格）＋3 待核实＋0 不合格；实例层面 0 编造、0 假 id、0 死链证据。** 三条实例四要素均由两个不同机构的具名来源双源直证，争议/解读均如实披露。
- **来源层面**：6 个新增来源全部存在、`verified=true`、本轮全部取得正文（3 个 web_fetch 200 + 3 个 urllib 200）。三条实例四要素双源扎实；`qi-yun` 概念归属为解读，`gongbi` 作者归属争议、`xieyi` 真迹争议均为来源明确讨论并披露。
- **结构/治理层面**：七节/规范提示机械项三条全过、SVG 唯一性与几何检查通过（无第57轮 acoustic 式越界）、元数据逐项一致、`check.py` PASS 0 errors。**pending 联动**：三条结构一致、披露诚实；`pending_sum`=193 与第57轮持平，无硬写清零，存量占比 74.8% 处高位，不触发降级。
- **相似度层面**：三条对全库与批内均 <0.54（短文本最高 0.4583、全字段最高 0.4682）；方法自校 0.5157 与第39–57轮一致。
- **是否整批返工 / 降级（结论）**：
  1. **§E「抽检不合格→整批返工（25%）」路径：不成立**——0 不合格（3 待核实），0 实例编造/假 id/死链。
  2. **§E「相似度过高（疑似套话）→整批降级」路径：不成立**——三条对全库与批内均 <0.54。
  3. **§E「待核实占比异常低（疑似硬写）→整批降级」路径：不成立**——存量待核实占比 74.8% 处高位，本轮无清零。
  4. **结论：本轮 3 条待核实、0 不合格，不触发整批返工/降级。** 三条待核实均为「解读/来源争议需披露」而非编造，`needs_verification` 联动方向正确、披露诚实。
- **返工/修复建议（定向、非整批）**：
  1. **（问题⑥，优先·概念支撑）** 为三条注明 `wp-*` 为概念背景源；如需提升证据硬度，为 qi-yun 补一源直接把《洛神赋图》与「气韵生动」挂钩。
  2. **（问题③⑤，可选升级）** gongbi / xieyi 内容四要素已双源扎实，若 lead 判断「（传）赵佶／画院御题画」「传梁楷／约数尺寸」已充分解决争议，可评估 `needs_verification` true→false 清零（须同步 `pending_notes`、正文「待核实」、`coverage.needs_verification_count` 与 `pending_sum`）；否则维持现状（当前披露已诚实，无需回滚）。
  3. **（问题⑦，次要）** 为 gongbi / xieyi 更换不重复的 SVG 并补「设计意图/尺寸关系」标注；建议全站统一补强该语义项。
  4. **（问题②④⑧）** 保持「约」数表述；概念源注明背景、三态 `link_ok=null` 维持保守；无需因 period 与实例朝代差异改动。

### 机器可读汇总

```
ROUND=58
SAMPLER=spotcheck-r58
MODE=第58轮补具名实例条目中lead定点抽3条（qi-yun / gongbi / xieyi）
SCOPE=["qi-yun","gongbi","xieyi"]
FILES={"qi-yun":"entries/batch-02-a.json","gongbi":"entries/batch-32.json","xieyi":"entries/batch-32.json"}
PATH_CORRECTION="lead 任务书注 qi-yun 在 batch-32.json；实读 batch-32.json 仅 gongbi/xieyi，qi-yun 真实位于 batch-02-a.json；按真实文件抽检"
GIT_HEAD="a23ce03 docs: note round57 push status"; ROUND58_COMMITTED=false; GIT_STATUS="round58 changes UNCOMMITTED as found (M coverage/data/sources/entries/batch-02-a+batch-32 + site/*; ?? review-round58a.md, review-round58b.md, apply_review_round58.py - lead notes, untouched)"
STATE={"coverage.json":"total=258, pending_sum=193","batch-02-a.json":"24009B","batch-32.json":"24272B","sources.json":"227835B","nvc_per_entry":1,"src_count_per_entry":4}
CHECK_PY="PASS: all checks, 0 errors (EXIT=0); no file-write statements; SVG geometry recheck: 0 out-of-viewBox across 3 svgs"
SAMPLE_RATIO="3/8 (37.5%, lead 定点; 8 landed named-instance entries per apply_review_round58.py INST)"
FETCH_METHOD="web_fetch 200 for dpm-luoshenfu,chinaculture-luoshenfu,dpm-furong; urllib+UA+unverified-SSL 200 for people-furong(GB18030),rmzx-poshui,npm-poshui(UTF-8); norm() substring readback; all FOUND; in-memory; only this report written"
SOURCES={"new_named_ids":6,"all_exist":true,"all_verified_true":true,"all_year_null":true,"link_ok_null":6,"link_ok_false":0,"concept_sources_reused":6,"fake_id":0}
BODY_SUPPORT={
 "qi-yun":"concept source backs definition/overview; instance Luoshen Fu Tu four facts dual (dpm-luoshenfu '顾恺之洛神赋图卷（宋摹）/东晋顾恺之作/约345-406/以形写神/传神写照/学界一般认为是宋摹本' + chinaculture-luoshenfu 'Luoshen Appraisal Painting...kept at the Palace Museum in Beijing / vividly captures / considered a classic'); '气韵生动' attribution is interpretation (neither source uses term literally), disclosed; VERDICT=待核实 (proper disclosure); minor: birth-year diff 345-406 vs 346-407",
 "gongbi":"concept source backs definition; instance Furong Jinji Tu four facts dual (dpm-furong '（传）北宋徽宗赵佶绘/工致细丽者如《芙蓉锦鸡图》/双钩法多用于工笔花鸟画/徐邦达画院画家作品' + people-furong '现藏于北京故宫博物院/宋徽宗工笔花鸟画的代表作，绢本立轴，双勾重彩'); authorship dispute dual-listed as '（传）赵佶／画院画家御题画'; VERDICT=待核实 (dispute disclosed; content four-fact dual-source, close to 合格); minor: 12世纪初 approximate year",
 "xieyi":"concept source backs definition; instance Pomo Xianren Tu four facts dual (npm-poshui '作者梁楷/人物衣紋描法(減筆)寫意/48.7x27.7/國立故宮博物院台北' + rmzx-poshui '泼墨仙人图梁楷减笔画代表作/纸本48.7×27cm/大写意楷模/写意画技法/真迹争议'); size 27.7 vs 27 and authenticity dispute disclosed as '传梁楷/约48.7×27cm'; VERDICT=待核实 (dispute disclosed; content four-fact dual-source, close to 合格); source rmzx is reprint"}
L2_CHECK={"seven_sections":"definition+6/6 x3","svg_count":"1 each","svg_phrase":"示意图，非施工图 x3","viewBox":"0 0 760 400 x3; 无on*/无外链图","risk_note":"实际工程须按当地规范和专业设计人员的要求 x3","svg_out_of_viewbox":0,"svg_issue":"gongbi 与 xieyi SVG identical generic '笔墨层次与气脉', no dimension annotation (systemic minor, introduced this round)"}
METADATA={"field_match_coverage":"ALL OK x3 (mismatch=[])","source_count":"4=4 x3","nvc":"nvc=1 x3; pending_sum=193 (same as round57, 0 change); stock ratio 193/258=74.8% high -> no anomalous-low downgrade","needs_verification":"all true, proper; pending==待核实节 verbatim x3"}
SIMILARITY={
 "qi-yun":{"vs_all_short":0.3429,"short_entry":"composition-placement","vs_all_full":0.3642,"full_entry":"yijing","verdict":"PASS<0.54"},
 "gongbi":{"vs_all_short":0.4583,"short_entry":"xieyi","vs_all_full":0.4644,"full_entry":"xieyi","verdict":"PASS<0.54"},
 "xieyi":{"vs_all_short":0.4583,"short_entry":"gongbi","vs_all_full":0.4682,"full_entry":"gongbi","verdict":"PASS<0.54"},
 "intrabatch_full_max":0.4644,"intrabatch_full_max_pair":"gongbi vs xieyi",
 "method_selfcheck":"futurism vs expressionism full=0.5157 matches round39-57 -> method validated",
 "threshold":0.54}
VERDICT_CONTENT={"qi-yun":"待核实","gongbi":"待核实","xieyi":"待核实"}
VERDICT_PENDING={"qi-yun":"proper (nv=true, interpretation disclosed)","gongbi":"proper (nv=true, authorship dispute dual-listed; content four-fact dual-source close to 合格)","xieyi":"proper (nv=true, authenticity dispute + size variance disclosed; content four-fact dual-source close to 合格)"}
HARD_FABRICATION_INSTANCE=0
UNSOURCED_CLAIM=0
FAKE_ID=0
LINK_FAIL=0
SVG_OUT_OF_VIEWBOX=0
ANOMALY_NVC="pending_sum=193 unchanged from round57; stock ratio 74.8% high -> no anomalous-low downgrade; no hard-clear"
BATCH_ACTION="No rollback/downgrade: 0 不合格 (3 待核实), 0 instance fabrication/0 fake id/0 dead link; similarity all <0.54; pending stock high. Targeted fixes: (1) mark wp-* concept sources as background, optionally add source directly linking Luoshen Fu Tu to 气韵生动; (2) gongbi/xieyi content four facts dual-source close to 合格 - optionally evaluate nv clear if lead deems disputes adequately disclosed (sync pending/待核实/coverage.nvc/pending_sum), else keep; (3) de-duplicate gongbi/xieyi SVG and add intent/dimension annotation site-wide."
READONLY="only wrote research/spotcheck-round58.md; no other project content file changed; no git commit; round58 work remains uncommitted as found; web content treated as data, no instruction executed; in-memory fetch, no files written outside deliverable"
```

*（报告完）*
