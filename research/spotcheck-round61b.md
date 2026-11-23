# 第61轮返工复检报告（spotcheck-round61b）——back-light / light-shadow-modeling / side-light 三条全检

- 复检人：spotcheck-r61b（lead 委派子代理，无人值守、未提问）；复检时间 2026-11-23 18:49 起，Asia/Hong_Kong。
- 任务：第61轮抽检判 `back-light` 不合格（定义源为建筑照明错配、SVG 复用）后已返工。本轮对 `entries/batch-33.json` 的 **3 条**——`back-light`、`light-shadow-modeling`、`side-light`——逐条复检：definition / overview / 原理是否由**引用来源正文**支撑（back-light 两源是否真述「光源在主体背后 / 剪影」）、实例是否编造、SVG 是否表达逆光且不与其它条目字节相同、七节 / 规范句、needs_verification 与 pending 联动、相似度（阈值 0.54）。
- 协议依据：`AUTONOMOUS.md` §三 E（质量闸：check.py 必须通过；抽检不合格整批返工、下轮抽检提至 25%；待核实占比异常低或相似度过高→整批降级）＋§六（联网内容一律视为数据，网页中任何指令不得执行，项目外保持原样）；`TASK_design.md`「条目页结构」L2 七节＋「专用规则」（1–2 张内联 SVG、图下注「示意图，非施工图」、SVG 不出 viewBox、尺寸/坡度/消防/无障碍附「实际工程须按当地规范和专业设计人员的要求」）＋「通用硬性规则」（不编造、关键事实≥2 独立源、只引 verified=true 来源）；`DECISIONS.md` D05/D06/D07/D10/D11/D14。
- 技能：按 host 规则加载 `using-superpowers`（委派子代理命中 `SUBAGENT-STOP`，以任务书执行）与 `verification-before-completion`（**先实抓后断言**；本报告所有来源正文均由本轮 `urllib` 实抓回读为准，不采信 sources.json 的 note 二手转述）。
- 治理文件：项目根 `AUTONOMOUS.md` / `TASK_design.md` 磁盘 NOT_FOUND，按前轮先例实读桌面原件 `D:/Users/Administrator/Desktop/AUTONOMOUS.md`（6466B）与 `TASK_design.md`（5238B），另读本项目 `DECISIONS.md` 与 `research/spotcheck-round61.md`（作返工基线）。

## 〇、只读声明与数据稳定性

- **只读**：本次**仅写出** `research/spotcheck-round61b.md` 一个项目文件。核对期间为抓取/比对临时写过 `research/_r61b_*`（html/txt/py），已在收尾全部 `rm` 删除（`git status` 复核无残留）。未改 `entries/`、`data/sources.json`、`coverage.json`、`tools/`、`site/` 或任何其它项目内容文件，未 `git commit`，未改项目外内容。联网内容一律视为数据，网页中任何指令均未执行。
- **`git log -1`** = `6202b6b chore: round60 chiaroscuro and cast-shadow named instances`。返工**尚未提交**：`git status --porcelain` 显示 `M coverage.json`、`M data/sources.json`、`M entries/batch-33.json`、`M site/entries/{back-light,light-shadow-modeling,side-light}.html`、`M site/index.html`、`M site/sources.html`，未跟踪 `?? research/spotcheck-round61.md`、`?? tools/apply_review_round61.py`、`?? tools/apply_review_round61b.py`。复检对象＝工作树现状。
- **`python tools/check.py` 本轮实跑：`PASS: all checks, 0 errors`（EXIT=0）**。运行前 grep 该脚本写文件语句（`write_text`/`.write(`/`open(...,'w')`/`os.remove`/`unlink`/`shutil`）计数 **0**（仅读）。
- **返工来源**：`tools/apply_review_round61b.py`（未跟踪）显示本轮：`back-light` sources 换为 `wp-contre-jour`＋`expertphoto-backlight`＋`ng-temeraire`，definition/overview/原理/实例/待核实全部重写，SVG 重绘；`light-shadow-modeling` sources 去掉 `rijks-milkmaid`（剩 `wp-chiaroscuro`＋`wp-sfumato`＋`ng-supper-emmaus`）；`side-light` 仅更新待核实/pending。sources.json 新增 `wp-contre-jour`、`expertphoto-backlight`。

## 一、判定口径与抓取方法（沿用第51–61轮）

- **L2 七节**：顶层 `definition`＋`sections` 六节（原理 / 典型手法与适用条件 / 实例 / 常见错误与限制 / 一图 / 待核实）＝7 节；1–2 张内联 SVG、含「示意图，非施工图」；SVG 元素不出 viewBox、无 `on*`、无外链图；「常见错误与限制」以规范句收尾。
- **抓取**：`urllib`＋浏览器 UA＋非校验 SSL 实抓并回读，去标签→`html.unescape`→`norm()`（去空白＋小写）子串回验。本轮实抓（HTTP 200）：`wp-contre-jour`(137031B)、`expertphoto-backlight`(110365B)、`ng-temeraire`(120439B)、`wp-architectural-lighting-design`(377024B)、`wp-daylighting-architecture`(56341B, JS 静态壳偏短)、`ng-rembrandt-self63`(128877B)、`tate-chiaroscuro`(103930B)、`wp-chiaroscuro`(264846B)、`wp-sfumato`(127333B)、`ng-supper-emmaus`(125583B，正确 slug `michelangelo-merisi-da-caravaggio-the-supper-at-emmaus`)。
- **三级判定**（沿用第51–61轮）：**合格**＝definition/time/overview/实例均获所引来源正文直接支撑，关键事实≥2 独立源直证或强权威官方源直证＋第二源，无编造，机械项全过或有轻微项；**待核实**＝核心获直接相关源实质支撑，但某关键事实实质单源/无源或为来源未逐字作出的解读，nv=true 且 pending/正文如实披露；**不合格**＝definition/overview 主干被所引来源均不支撑（实质无源）、实例核心四要素无源、或关键结构项（七节/SVG）实质不满足（含 SVG 语义与主题错配）。
- **相似度**：`difflib.SequenceMatcher`；①短文本＝title+definition+time_or_place+overview；②全字段-不含 SVG＝definition+time_or_place+overview＋六节正文（含「一图」解说，不计 svg 标记），去空白＋小写。全库 258 条扫描，阈值 0.54。**方法自校**：`futurism-style vs expressionism-style` 全字段②＝**0.5157**（与第39–61轮逐位一致，口径正确）。

## 二、任务1：definition / overview / 原理 是否由引用来源正文支撑

### 2.1 back-light（逆光）——定义**已获双源直证**（本轮返工核心项）

- 条目现状（batch-33 back-light）：definition＝「逆光指光源位于主体背后、朝向镜头的照明，主体因此变暗成剪影、边缘显出轮廓光。」；overview＝「光源在主体之后，主体大面积处于阴影，边缘被照亮形成轮廓；曝光不当主体会全黑。」；原理＝「当主光位于主体背后并朝向相机，主体迎镜头一面落在背光中而变暗，其轮廓边缘被背后强光照亮，形成剪影与轮廓光。」sources＝`wp-contre-jour`、`expertphoto-backlight`、`ng-temeraire`。
- **wp-contre-jour 实抓逐字直证**：`Contre-jour produces backlighting of the subject. This effect usually hides details, causes a stronger contrast between light and dark, creates silhouettes and emphasizes lines and shapes. The sun, or other light source, is often seen as either a bright spot or as a strong glare behind the subject.` 另有定义句 `a photographic technique in which the camera is pointing directly toward a source of light`。→ 「光源在主体背后」「朝向（镜头/光源）」「剪影」**全部逐字命中** ✓。
- **expertphoto-backlight 实抓逐字直证**：`Backlighting in photography happens when the main light is behind your subject and facing the camera.`；`Backlighting means that you compose your pictures so that the primary light source is behind your subject.`；`creating a silhouette effect`、`You can create silhouettes like this`。→ 「主光在主体背后、朝向相机」「剪影」**逐字命中** ✓。
- **结论**：definition / overview / 原理 的「光源在主体背后、朝向镜头、变暗成剪影、边缘轮廓光」均由 `wp-contre-jour`（百科，silhouette/behind the subject）＋`expertphoto-backlight`（摄影教学，behind your subject and facing the camera/silhouette）**双独立源逐字直证**。上轮「两定义导向源为建筑照明/采光、全文无逆光术语→定义实质无源」的致命缺陷**已消除**。（注：轮廓光「rim」一词 wp-contre-jour 正文未直用 rim light 短语，但「emphasizes lines and shapes / edges of the subject」可支撑「边缘显出轮廓」；「边缘亮廓」为对 edges/lines 的合理表述，非编造。）

### 2.2 light-shadow-modeling（光影塑形）——定义双源直证（沿用上轮合格口径，rijks 泛源已删）

- definition＝「光影塑形指用受光与背光的明暗过渡表现物体的体积与转折。」；overview＝「光线落在形体上形成亮部、暗部与过渡，体积因明暗梯度而被感知。」sources＝`wp-chiaroscuro`＋`wp-sfumato`＋`ng-supper-emmaus`（**已删去上轮判为「偏泛」的 rijks-milkmaid**）。
- **支撑**：`wp-chiaroscuro` `sense of volume in modelling three-dimensional objects and figures`→「体积」直证；`wp-sfumato` `softening the transition between colours`→「明暗过渡」直证。双独立权威源 ✓。
- 实例《以马忤斯的晚餐》NG 页实抓逐字：`chiaroscuro`×3、`contrasts of light`、`strong light from the left`、`NG172`、`1601`、`Caravaggio`——四要素＋「明暗对比塑形」由 NG 官方源直证 ✓（上轮「实例『体积』为概念层补述」的轻微项仍在：NG 原文用 `heighten the drama`，未出现 `volume`）。**无编造。** rijks 泛源删除后，来源相关性收紧，上轮问题⑤已解决 ✓。

### 2.3 side-light（侧面光）——定义**实质无源**（两建筑照明源仍在，且与概念错配）

- 条目现状：definition＝「侧面光从约九十度横向打来，凸处迎光、凹处落影，最能把表面质感拉出来。」；overview＝「明暗各半、戏剧性强，适合表现纹理与体积，暗部需补光。」sources＝`wp-architectural-lighting-design`、`wp-daylighting-architecture`、`ng-rembrandt-self63`、`tate-chiaroscuro`（**两建筑照明源仍在，本轮返工未处理**）。
- **wp-architectural-lighting-design 实抓**：`side light` 仅 1 次，且为路灯透镜描述 `a type II lens (side to side light distribution pattern)`——**与「对主体的侧向照明」概念无关**；`side lighting`/`from the side`/`from one side`/`silhouette`/`rim light` 全部 **0 次** → 不支撑侧面光定义。
- **wp-daylighting-architecture 实抓**：`side light`/`from the side`/`side lighting` 等**全部 0 次**（页面仅 2319B 纯静态壳，正文 JS 渲染，不足以支撑）。
- **ng-rembrandt-self63 实抓**：`lit dramatically from one side` 出现 1 次，但**该句描述的是另一幅画《A Seated Man with a Stick》（Follower of Rembrandt，同页相关作品轮播），并非《63岁自画像》**；NG 对《63岁自画像》正文只述「面部肌理/油彩/衰老面容/笔触」，及对相关作品泛述 `dramatic, shadowy light effects`，**未断言该自画像「面部受一侧光照、背衬深影」** → 实例「一侧光照」为推断，且挂靠的是另一幅画的描述。
- **tate-chiaroscuro**：`side light`/`from one side` 均 0 次，仅 4 次 `chiaroscuro`——概念背景源，不直述侧光。
- **结论**：side-light 的 definition 主干（「约九十度横向打光、明暗各半」）被所引两个定义导向源（建筑照明/采光，全文无侧光术语且其一 `side light` 为路灯透镜巧合）**实质无源**；实例「一侧光照」为据**另一幅画**描述的推断。**与第61轮 back-light 完全同型的「定义源错配＋实例挂靠」缺陷在本条重现。** 依第61轮口径，definition 主干被所引来源均不支撑→判**不合格**。（注：侧光为摄影通识，但项目规则要求来源直证，通识不能替代署名来源。）

## 三、任务2：来源 id 存在性 / verified / 相关性 / 可达性

- 涉及 10 个 id 全部存在、`verified=true`、`year=null`（D06 允许）。**新增两源 `wp-contre-jour`、`expertphoto-backlight`：verified=true、link_ok=true**。本轮实抓全部 HTTP 200 取得正文。`ng-temeraire.link_ok` 仍为 `null`（apply 未记 true），但实抓 200 可达（维护·轻微，建议补记）。
- **相关性结论**：
  - `back-light`：`wp-contre-jour`、`expertphoto-backlight` **直接相关且逐字直证逆光定义**（上轮建筑照明错配问题已修复）；`ng-temeraire` 支撑实例四要素与「blazing sunset/glowing orange」，不直用「逆光」字样（实例层推断，已入待核实）。
  - `light-shadow-modeling`：`wp-chiaroscuro`＋`wp-sfumato` 直证定义、`ng-supper-emmaus` 直证实例，相关性收紧。
  - `side-light`：`wp-architectural-lighting-design`、`wp-daylighting-architecture` **为建筑照明/采光，与「摄影侧光」错配（挂名不相关源）**；`ng-rembrandt-self63` 的「一侧光照」实指另一幅画；`tate` 仅概念背景。

## 四、任务3：L2 七节 + SVG + 规范提示（程序化实核）

| 条目 | def 顶层 | sections 6 节 | SVG 数 | viewBox | 「示意图，非施工图」 | on*/外链图 | 规范句收尾 | SVG 几何越界 | SVG 语义贴合 | 与他条字节相同 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| back-light | ✓ | 6/6 | 1 | `0 0 760 400` | ✓ | 无/无 | ✓ | 无（min≥0,max≤580） | ✓ **表达逆光**（circle cx=580 光源在右后、ellipse cx=300 fill=muted 暗剪影、两 arcs 轮廓亮线、文字「光源在主体背后」「主体成剪影、边缘亮线（轮廓光）」） | **无**（已重绘，唯一） |
| light-shadow-modeling | ✓ | 6/6 | 1 | `0 0 760 400` | ✓ | 无/无 | ✓ | 无（max≤480） | ✓（circle cx=150 正面/侧前光→椭圆形体，标「光源/形体与明暗」，贴合体积塑形） | **有：与 cast-shadow / highlight / reflected-light / core-shadow / front-light / top-light 6 条字节完全相同（通用图复用）** |
| side-light | ✓ | 6/6 | 1 | `0 0 760 400` | ✓ | 无/无 | ✓ | 无（max≤375） | ✓（rect 主体、箭头 x=80→290 侧向光源，标「侧向光源/明暗各半」） | **无**（唯一） |

- 七节完整（定义＋原理/典型手法与适用条件/实例/常见错误与限制/一图/待核实，无缺无余）；三条各 1 张内联 SVG、含「示意图，非施工图」、无 `on*`、无 `<image>`/外链、几何均在 0–760×400 内；「常见错误与限制」三条均以「实际工程须按当地规范和专业设计人员的要求」收尾；`check.py` PASS 0 errors。
- **SVG 语义/复用结论**：
  - **back-light：上轮「与 light-shadow-modeling 复用同一正面照明图、未表达逆光」缺陷已修复** ✓——本轮 SVG 唯一，且几何确表达「光源在主体背后、主体成暗剪影、边缘亮线（轮廓光）」，与「一图」文字一致。
  - **新发现：light-shadow-modeling 的 SVG 与全库 6 条（cast-shadow/highlight/reflected-light/core-shadow/front-light/top-light）字节完全相同**，属通用图复用。上轮报告只指出它「与 back-light 复用」；back-light 重绘后不再共用，但该图本身仍是多条目共享的通用「光源→椭圆」示意。此为机械可渲染、语义尚可（光源→形体与明暗），但**图未针对「光影塑形的明暗过渡/转折」专属绘制**，属轻微-中等（TASK_design 要求图示表达本条设计意图；本图偏泛用）。不单独构成不合格，但记录为批内通用图复用待整改项。

## 五、任务4：元数据一致性 + needs_verification ↔ pending ↔ 正文待核实 + 相似度

- `title/theme/tier/period/region/level/status/source_count` 与 `coverage.json` 逐字段一致：back-light cov（L2/已写/src=3/nvc=1）↔ entry（src=3/nv=True）；light-shadow-modeling cov（L2/已写/src=3/nvc=0）↔ entry（src=3/nv=False）；side-light cov（L2/已写/src=4/nvc=1）↔ entry（src=4/nv=True）。全部匹配 ✓。

| 条目 | needs_verification | pending_notes | 正文「待核实」节 | 联动一致性 |
| --- | --- | --- | --- | --- |
| back-light | **true** | 「实例“逆光”解读基于馆方夕阳/暖色描述；概念已双源。」 | 「逆光概念由 Contre-jour 与 ExpertPhotography 双源直证；实例《无畏号》的夕阳逆光为据馆方“blazing sunset/glowing orange”解读，作品未直言“逆光”。」 | **结构一致 ✓、披露准确**：如实区分「概念双源直证」与「实例逆光为解读」，与上轮「定义无源」缺陷已消相符；nv=True 保留合理（实例确为推断） |
| light-shadow-modeling | **false** | ""（空） | 「暂无已知待核实项。」 | **结构一致 ✓**：nv=False 无 pending、声明「暂无」为正确约定；有 wp+NG 直证支撑清零 |
| side-light | **true** | 「侧光为据馆方描述的解读；概念有 Tate 背景。」 | 「“一侧光照”由馆方对该像的描述解读（伦勃朗自画像面部受光、背景深影）；Tate 为明暗对照概念源。」 | **结构一致，但披露不完整/不准确**：nv=True 且自称「概念有 Tate 背景」，然 **Tate 并不直述侧光**、两建筑照明源与侧光概念错配、实例「一侧光照」实指另一幅画——这些更根本缺口未如实披露，反把错配源当作「背景」 |

### 相似度（difflib 去空白＋小写，阈值 0.54；全库 258 条；口径②全字段-不含 SVG）

| 条目 | ①短文本 max | ②全字段 max | 判 |
| --- | --- | --- | --- |
| back-light | 0.3333 vs highlight | **0.4123 vs warm-cool** | 均 <0.54 ✓（较上轮 0.4735 更低） |
| light-shadow-modeling | 0.3810 vs core-shadow | **0.5233 vs chiaroscuro** | <0.54 ✓（裕度 0.0167，逼近；共用《以马忤斯的晚餐》实例） |
| side-light | 0.3946 vs top-light | 0.3725 vs cast-shadow | 均 <0.54 ✓ |

- **批内两两（全字段）**：back-light vs light-shadow-modeling 0.3081、back-light vs side-light 0.3289、light-shadow-modeling vs side-light 0.3432，均远低于 0.54 ✓。
- **方法自校**：`futurism vs expressionism` 全字段＝**0.5157**，与第39–61轮一致，口径正确。
- 三条对全库与批内均 PASS（<0.54）；light-shadow-modeling↔chiaroscuro 0.5233 贴近阈值需记录关注（共享实例所致，非降级）。

## 六、逐条验收结论

| 条目 | definition/overview/原理 来源支撑 | 来源存在·verified·相关·可达 | 七节/规范/SVG | nv·pending 联动 | 相似度(①②) | 结论 |
| --- | --- | --- | --- | --- | --- | --- |
| **back-light（逆光）** | **双源逐字直证**：wp-contre-jour（behind the subject/silhouettes/backlighting）＋expertphoto（main light behind your subject and facing the camera/silhouette）→「光源在主体背后、剪影、边缘轮廓」全部支撑；实例四要素 NG 直证、「逆光」为解读（已披露）；无编造 | 3/3 存在且 true；新两源 200 可达、直接相关；ng-temeraire 仅支撑夕阳 | 七节齐、规范句✓；**独立 SVG 表达逆光、唯一、无越界** | nv=True↔pending↔待核实**结构一致且披露准确** | ✓（0.3333/0.4123） | **合格**（上轮不合格缺陷已修复） |
| **light-shadow-modeling（光影塑形）** | definition 双源（wp-chiaroscuro 体积/ wp-sfumato 过渡）直证；实例 NG-supper 逐字直证并点名 chiaroscuro；rijks 泛源已删；「体积」概念层补述（轻微） | 3/3 存在且 true；相关性收紧 | 七节齐、规范句✓；1 SVG 语义尚可但**与 6 条字节相同（通用图复用）** | nv=False↔pending=""↔「暂无」正确约定 | ✓（0.3810/0.5233 贴近） | **合格（含轻微项：SVG 通用图复用待整改；0.5233 贴近阈值）** |
| **side-light（侧面光）** | **definition 主干实质无源**：两建筑照明/采光源全文无侧光术语（wp-arch `side light` 系路灯透镜巧合）、Tate 概念背景；实例「一侧光照」实指另一幅画《A Seated Man with a Stick》 | 4 个存在且 true、200 可达；**两定义导向源与摄影侧光错配（挂名不相关）** | 七节齐、规范句✓；1 SVG 唯一、语义贴合 | nv=True↔pending↔待核实结构一致，**但披露不完整/不准确（把错配源当背景、漏报定义无源）** | ✓（0.3946/0.3725） | **不合格** |

### 问题清单

- **① back-light 定义无源→已修复（验证通过）**：`wp-contre-jour`＋`expertphoto-backlight` 逐字直证「光源在主体背后 / 朝向镜头 / 剪影」，上轮致命缺陷消除。**结论：合格。**
- **② back-light SVG 复用→已修复（验证通过）**：重绘独立逆光 SVG，唯一、表达「光源背后＋暗剪影＋轮廓亮线」，图文一致。**结论：合格。**
- **③-side-light 定义主干无源（严重·强制项·新）**：`wp-architectural-lighting-design`、`wp-daylighting-architecture` 为建筑照明/采光，全文无侧光/明暗半侧术语（wp-arch 的 `side light` 系路灯 `side to side light distribution pattern` 巧合），`tate` 仅概念背景 → definition「约九十度横向打光、明暗各半」实质无源；与第61轮 back-light 同型错配。**结论：不合格。**
- **④ side-light 实例挂靠另一幅画（严重·强制项·新）**：`ng-rembrandt-self63` 的 `lit dramatically from one side` 描述的是同页相关作品《A Seated Man with a Stick》（Follower of Rembrandt），非《63岁自画像》；NG 对该自画像正文未断言「一侧光照」→ 实例「一侧光照」为挂错对象之推断。
- **⑤ side-light pending 披露不完整/误导（治理·中等）**：nv=True 但把错配的 Tate 写作「概念背景」，未披露两建筑照明源与侧光错配、实例实指另一幅画。
- **⑥ light-shadow-modeling SVG 通用图复用（中等·新发现）**：其 SVG 与 cast-shadow/highlight/reflected-light/core-shadow/front-light/top-light **6 条字节完全相同**（上轮仅记与 back-light 复用；back-light 重绘后不再共用，但该图本身仍是共享通用「光源→椭圆」示意，未针对「明暗过渡/转折」专属绘制）。语义尚可、机械合规，判轻微-中等，记录待整改。
- **⑦ light-shadow-modeling 实例「体积」为概念层补述（轻微·延续）**：NG 原文 `heighten the drama`，无 `volume`；「塑造体积」为 wp-chiaroscuro 概念层补述，非该作官网判断。
- **⑧ light-shadow-modeling↔chiaroscuro 相似度 0.5233 贴近阈值（关注·非降级）**：共用《以马忤斯的晚餐》实例所致，裕度 0.0167，仍在 0.54 内。
- **⑨ ng-temeraire.link_ok=null（维护·轻微）**：实抓 200 可达，建议补记 true。

## 七、总体结论

- **抽样 3 条全检结果：2 合格 + 0 待核实 + 1 不合格。**
  - `back-light`：**合格**——上轮判不合格的两项致命缺陷（定义源建筑照明错配、SVG 复用正面照明图未表达逆光）**均已实质修复**：定义改用 `wp-contre-jour`＋`expertphoto-backlight` 双源，二者正文逐字直证「光源在主体背后、朝向镜头、剪影」；SVG 已重绘为独立、表达「光源背后＋暗剪影＋轮廓亮线」的逆光图且唯一。nv=True↔pending↔待核实结构一致且披露准确。
  - `light-shadow-modeling`：**合格**（含轻微项）——定义/实例来源直证，rijks 泛源已删除（上轮问题⑤解决）；仍存「体积」概念层补述（轻微）、SVG 与 6 条通用图复用（中等·新发现）、相似度 0.5233 贴近阈值（关注）。
  - `side-light`：**不合格**——**本轮返工未处理 side-light 的来源**，仍保留与「摄影侧光」概念错配的两个建筑照明/采光源（`wp-architectural-lighting-design`/`wp-daylighting-architecture`，全文无侧光术语或系路灯巧合），definition 主干实质无源；实例「一侧光照」实指同页另一幅画《A Seated Man with a Stick》。此与第61轮 back-light 属完全同型缺陷。
- **来源层面**：10 个 id 全部存在、verified=true、本轮全部 200 可取正文；无假 id、无死链（ng-temeraire 实抓 200，link_ok 未记）。**side-light 的两个定义导向源与「摄影侧光」错配，属挂名不相关源。**
- **结构/治理层面**：七节/规范提示三条机械项全过、SVG 几何无越界、元数据逐项一致、check.py PASS 0 errors。**SVG 语义：back-light 已修复为独立逆光图；light-shadow-modeling 图与 6 条字节相同（通用图复用，新发现）；side-light 图唯一贴合。** pending 联动：back-light 准确、light-shadow-modeling 正确约定、side-light 不完整/误导。
- **相似度层面**：三条对全库与批内均 <0.54（短文本最高 0.3946、全字段最高 0.5233）；方法自校 0.5157 一致；light-shadow-modeling↔chiaroscuro 0.5233 贴近阈值需关注（非降级）。
- **是否整批返工 / 降级**：
  1. **§E「抽检不合格→整批返工（25%）」：成立（1 条不合格）**——`side-light` 判不合格（定义主干实质无源＋实例挂靠另一幅画）。按 §E，本轮返工批次 3 条应**继续整批返工**（至少 `side-light` 必须重做来源），**下一轮抽检比例维持提高至 25%**。`back-light` 已合格、`light-shadow-modeling` 合格（轻微待整改），二者无需因不合格再返工，但若整批口径执行则随批复核。
  2. **§E「相似度过高→整批降级」：不成立**（三条均 <0.54）。
  3. **§E「待核实占比异常低→整批降级」：不成立**（back-light/side-light 均 nv=True；light-shadow-modeling nv=False 有直证支撑）。
- **返工/修复建议（阻断项优先）**：
  1. **（阻断·side-light 定义无源）** 将 `side-light` 的两个建筑照明源替换为**直述「摄影侧光 / side lighting / from the side」的权威源**（如摄影用光源、百科 sidelight 条目），或在无法取得时改写定义并如实标注「侧光机制为通识、来源未直述」入 pending。
  2. **（阻断·side-light 实例挂靠）** 实例《63岁自画像》「一侧光照」若馆方该页未直述，应改引**直述该自画像侧向光/明暗的馆方或权威源**，或改换一幅馆方明文描述侧光的作品；不得挂靠同页另一作品《A Seated Man with a Stick》的描述。
  3. **（治理·side-light pending）** 重做来源后 pending/正文须如实反映定义来源强度与实例是否为推断，勿把错配源写作「概念背景」。
  4. **（中等·light-shadow-modeling SVG）** 该条 SVG 与 6 条通用图复用，建议为「明暗过渡/转折」专属重绘（体现受光面—明暗交界—暗部的渐变转折），使之与主题意图一致（同类通用图复用建议全库体检时一并排查）。
  5. **（轻微/维护）** light-shadow-modeling 实例「体积」宜以 NG 原文「强化戏剧性」为准或注明「（体积判断参见明暗法原理源）」；补记 `ng-temeraire.link_ok=true`；关注 light-shadow-modeling↔chiaroscuro 0.5233。

### 机器可读汇总

```
ROUND=61b
SAMPLER=spotcheck-r61b
MODE=第61轮返工后复检3条全检（back-light / light-shadow-modeling / side-light）
SCOPE=["back-light","light-shadow-modeling","side-light"]
FILES={"back-light":"entries/batch-33.json back-light","light-shadow-modeling":"entries/batch-33.json light-shadow-modeling","side-light":"entries/batch-33.json side-light"}
GIT_HEAD="6202b6b chore: round60 chiaroscuro and cast-shadow named instances"; REWORK_COMMITTED=false
CHECK_PY="PASS: all checks, 0 errors (EXIT=0); no file-write statements (grep count=0)"
FETCH_METHOD="urllib+UA+unverified-SSL HTTP200 readback: wp-contre-jour(137031B),expertphoto-backlight(110365B),ng-temeraire(120439B),wp-architectural-lighting-design(377024B),wp-daylighting-architecture(56341B),ng-rembrandt-self63(128877B),tate-chiaroscuro(103930B),wp-chiaroscuro(264846B),wp-sfumato(127333B),ng-supper-emmaus(125583B)"
BODY_SUPPORT={
 "back-light":"definition/overview/原理 DIRECTLY supported by TWO sources verbatim: wp-contre-jour 'Contre-jour produces backlighting...creates silhouettes...light source...behind the subject' + 'camera pointing directly toward a source of light'; expertphoto-backlight 'main light is behind your subject and facing the camera' + 'creating a silhouette effect'. Fixed previous unsourced defect. Instance four facts NG verbatim, '逆光' is inference (disclosed). VERDICT=合格",
 "light-shadow-modeling":"definition dual DIRECT (wp-chiaroscuro volume modelling + wp-sfumato transition); instance Supper at Emmaus NG verbatim + chiaroscuro; rijks generic source removed. minor: 'volume' not on NG page (heighten the drama). VERDICT=合格(轻微)",
 "side-light":"definition backbone (90-degree side light / half light-half dark) NOT supported: wp-architectural-lighting-design has 'side light' only as street-lamp lens 'side to side light distribution pattern' coincidence (side lighting/from the side/silhouette/rim=0); wp-daylighting-architecture all 0 (2319B JS shell); tate-chiaroscuro side-light terms 0, only concept. Instance '一侧光照' from ng-rembrandt-self63 actually describes OTHER work 'A Seated Man with a Stick', not the Self Portrait. DEFINITION ESSENTIALLY UNSOURCED + two building-lighting sources mismatch. VERDICT=不合格"}
SOURCES={"ids_involved":10,"all_exist":true,"all_verified_true":true,"new_sources":["wp-contre-jour(link_ok=true)","expertphoto-backlight(link_ok=true)"],"reachable_200_this_round":true,"fake_id":0,"ng_temeraire_link_ok_field":null,"irrelevant_source":["wp-architectural-lighting-design (side-light: no side-lighting terms, coincidence phrase)","wp-daylighting-architecture (side-light: JS shell, no terms)"]}
L2_CHECK={"seven_sections":"definition+6/6 x3","svg_count":"1 each","svg_phrase":"示意图，非施工图 x3","viewBox":"0 0 760 400 x3; 无on*/无外链","risk_note":"实际工程须按当地规范和专业设计人员的要求 x3","svg_out_of_viewbox":0,
 "svg_semantic":{"back-light":"FIXED: unique SVG expressing back-light (circle cx=580 light behind, ellipse cx=300 muted silhouette, arcs rim highlight, text 光源在主体背后/主体成剪影、边缘亮线)","light-shadow-modeling":"acceptable semantics BUT byte-identical to 6 entries (cast-shadow/highlight/reflected-light/core-shadow/front-light/top-light) = generic graph reuse (NEW finding)","side-light":"unique, acceptable (rect subject + arrow side light)"}}
BYTE_IDENTICAL={"back-light":{"count":1,"same_as":[]},"light-shadow-modeling":{"count":7,"same_as":["cast-shadow","highlight","reflected-light","core-shadow","front-light","top-light"]},"side-light":{"count":1,"same_as":[]}}
METADATA={"field_match_coverage":"ALL OK x3","source_count":"back-light 3=3, lsm 3=3, side-light 4=4","nvc":"back-light=1,lsm=0,side-light=1; matches needs_verification (true/false/true)"}
SIMILARITY={
 "back-light":{"vs_all_short":0.3333,"short_entry":"highlight","vs_all_full":0.4123,"full_entry":"warm-cool","verdict":"PASS<0.54"},
 "light-shadow-modeling":{"vs_all_short":0.3810,"short_entry":"core-shadow","vs_all_full":0.5233,"full_entry":"chiaroscuro","note":"margin 0.0167 near threshold, shared instance","verdict":"PASS<0.54"},
 "side-light":{"vs_all_short":0.3946,"short_entry":"top-light","vs_all_full":0.3725,"full_entry":"cast-shadow","verdict":"PASS<0.54"},
 "intrabatch_full":{"back_vs_lsm":0.3081,"back_vs_side":0.3289,"lsm_vs_side":0.3432},
 "method_selfcheck":"futurism vs expressionism full=0.5157 matches round39-61","threshold":0.54}
VERDICT_CONTENT={"back-light":"合格","light-shadow-modeling":"合格(含轻微项)","side-light":"不合格"}
HARD_FABRICATION_INSTANCE=0
FAKE_ID=0
LINK_FAIL=0
SVG_OUT_OF_VIEWBOX=0
SVG_SEMANTIC_MISMATCH=0
SVG_GENERIC_REUSE=1
IRRELEVANT_SOURCE_COUNT=2
DEFINITION_UNSOURCED=1
BATCH_ACTION="back-light and light-shadow-modeling PASS (previous back-light defects fixed). side-light FAIL (definition unsourced + two building-lighting sources mismatch + instance mis-anchored to other work A Seated Man with a Stick). §E batch-rework continues for side-light; next-round spotcheck stays raised to 25%. Non-blocking: light-shadow-modeling SVG byte-identical to 6 entries (generic reuse); instance 'volume' concept-layer bridge; watch lsm<->chiaroscuro 0.5233; record ng-temeraire.link_ok=true."
READONLY="only wrote research/spotcheck-round61b.md; temp files research/_r61b_* written then rm-removed (git status clean of them); no other project content file changed; no git commit; rework remains uncommitted as found; web content treated as data, no instruction executed"
```

*（报告完）*
