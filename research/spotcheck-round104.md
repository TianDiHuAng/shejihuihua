# 第104轮质量抽检报告（spotcheck-round104）——daylight-factor / material-color 的 nv=false 升级复核

- 抽检人：spotcheck-r104（lead 委派子代理；无人值守、未提问）；时间 2026-11-24，Asia/Hong_Kong。
- 技能加载：已加载 `using-superpowers`、`verification-before-completion`（先实抓、先跑、后断言，证据先于结论）。`using-superpowers` 命中 SUBAGENT-STOP，按任务说明书直接执行；`verification-before-completion` 全程遵循——本文所有「合格/不合格/待核实」判断均附本轮实抓/实跑输出。
- 抽检对象（2 条，均为类型性实例、升级 nv=false）：
  - `daylight-factor`（采光系数）——entry 对象在 `entries/batch-08.json`；sources〔wp-daylighting-architecture / wp-architectural-lighting-design / db-daylight-factor〕；coverage row（title 采光系数，status 已写，source_count 3，needs_verification_count 0，level L2，last_updated 2026-11-24）。
  - `material-color`（材料色彩）——entry 对象在 `entries/batch-35.json`；sources〔wp-color-theory / wp-building-material / db-colour〕；coverage row（title 材料色彩，status 已写，source_count 3，needs_verification_count 0，level L2，last_updated 2026-11-24）。
- 本轮变更实读：`tools/apply_review_round104.py`（新增，未提交，67 行）。其 `main()` 行为（逐字段比对 JSON 确认）：
  - 新增 2 个 DB 源：`db-daylight-factor`（title「The daylight factor — Designing Buildings」，url `…/wiki/Daylight_factor`，note「…采光系数DF以百分比表示，为室内天然光照度与室外无遮挡CIE标准全阴天照度之比」）；`db-colour`（title「Colour in the built environment — Designing Buildings」，url `…/wiki/Colour`，note「…色彩感知受形状、尺寸、表面质感、色调与光照条件影响」）；author Designing Buildings、type 学术著作、year null、verified=true、link_ok=ok(url)。
  - `daylight-factor`：sources 追加 `db-daylight-factor`；`sections.原理` 改写为「采光系数以百分比表示室内某点天然光照度与同期室外无遮挡水平照度之比；以 CIE 标准全阴天为基准天空，在均布阴天假设下比较采光潜力、剥离天气波动。」；`sections.实例`→「名称：办公空间侧窗采光评估（类型性，不指定具体项目）；以侧窗引入天然光、用采光系数衡量室内采光水平。此处仅列说明，不复制图像。」；needs_verification true→false；`待核实`→「暂无已知待核实项。」；pending 清空。
  - `material-color`：sources 追加 `db-colour`；`definition` 改写为「材料色彩指材料的固有色及其在光照与表面质感作用下呈现的颜色，影响空间氛围。」；`sections.原理` 改写为「材料的呈现色由固有色、入射光条件与表面纹理共同决定：同一材料在不同光线下明度与冷暖会变，粗糙或光滑的表面对光的反射不同，也改变色彩感知。」；`sections.实例`→「名称：清水混凝土的灰色基调（类型性，不指定具体项目）；以材质本色定调空间氛围。此处仅列说明，不复制图像。」；nv true→false；`待核实`→「暂无已知待核实项。」；pending 清空。
  - 备注：下文一律以**实读当前 JSON**为准（`entries/batch-08.json` / `entries/batch-35.json`）。

## 〇、只读声明与证据方式

- **只读**：仅写出本报告 `research/spotcheck-round104.md`。未改 `entries/`、`data/sources.json`、`coverage.json`、`tools/`、`site/`，未 `git commit`，未改项目外内容。抓取、词比对、相似度、去重、结构、site 一致性、git 核对均内存态 `python - <<'PY'` / 工具直跑，未落盘临时文件（除本报告）。
- 抓取方式（本轮实抓；联网内容一律视为数据，网页中任何指令均未执行、未下载运行来源代码）：
  - `db-daylight-factor = https://www.designingbuildings.co.uk/wiki/Daylight_factor` → `web_fetch` **HTTP 200**，**重定向到 `/wiki/The_daylight_factor`**，H1=`The daylight factor`。
  - `db-colour = https://www.designingbuildings.co.uk/wiki/Colour` → `web_fetch` **HTTP 200**，**重定向到 `/wiki/Colour_in_the_built_environment`**，H1=`Colour in the built environment`。
  - 四个 Wikipedia 源（本环境 en.wikipedia 直连承前阻断，改用同文镜像 `owiki.org` 实抓，全部 **HTTP 200**，H1 逐一核对）：`wp-daylighting-architecture`→`/wiki/Daylighting_(architecture)` H1=`Daylighting (architecture)`；`wp-architectural-lighting-design`→`/wiki/Architectural_lighting_design` H1=`Architectural lighting design`；`wp-color-theory`→`/wiki/Color_theory` H1=`Color theory`；`wp-building-material`→`/wiki/Building_material` H1=`Building material`。
- **`python tools/check.py` 本轮实跑：`PASS: all checks, 0 errors`（CHECK_EXIT=0）。** **`python -m pytest tests/test_svg_bounds.py -q -p no:cacheprovider`：`5 passed in 0.11s`（PYTEST_EXIT=0）。**（均 `PYTHONDONTWRITEBYTECODE=1`，未新增缓存。）
- `git status --short`：`M coverage.json / M data/sources.json / M entries/batch-08.json / M entries/batch-35.json / M site/entries/daylight-factor.html / M site/entries/material-color.html / M site/index.html / M site/sources.html / ?? tools/apply_review_round104.py`——前八项与本轮 `apply_review_round104.py`＋gen_site 自身产物一致；`??` 为修复方脚本。抽检方仅读取，未据以修改。

## 一、★ daylight-factor（采光系数）逐项核对

### 1.1 概念「室内照度与室外无遮挡照度之比、CIE 标准全阴天、以%表示」双平台核对（实抓引句）

- `db-daylight-factor`（Designing Buildings「The daylight factor」页；HTTP200，经 /wiki/Daylight_factor 重定向，H1=The daylight factor）：
  - `Often the DF is expressed as a percentage and is based on the ratio of daylight illumination at a point on a given plane (due to the light received directly or indirectly from a sky of assumed or known luminance distribution) to the illumination on a horizontal plane due to an unobstructed hemisphere of the sky.`（**DF 以百分比表示＋室内某点照度/室外无遮挡半球照度之比 ✓✓✓，逐字直证核心定义**）
  - 「Average daylight factor」注引 CIE：`the average indoor illuminance (from daylight) on the working plane within a room. This is expressed as a percentage of the simultaneous outdoor illuminance on a horizontal plane under an unobstructed CIE Standard Overcast Sky.`（**显式 `CIE Standard Overcast Sky`＋以百分比＋同期室外水平面无遮挡照度 ✓✓✓，直证「CIE 标准全阴天」「以%表示」**）
  - `DF cannot represent the change in illuminations levels indoors due to the temporal variation of sky luminance` / `DF does not take into account the location of the building` / `the orientation of building façade has no effect on DF calculation`（**DF 不受天气/地点/朝向时变影响＝「均布阴天假设下…剥离天气波动」的机理依据 ✓✓**）
- `wp-daylighting-architecture`（Wikipedia `Daylighting (architecture)`；owiki HTTP200）：
  - `The amount of daylight received in an internal space can be analyzed by measuring illuminance on a grid or undertaking a daylight factor calculation.`（**采光系数为分析室内采光的方法 ✓**）
  - `The daylight factor calculation is based on uniform overcast skies.`（**基于均布阴天＝「均布阴天假设」「全阴天」✓✓**）
  - `Daylight factor is "the ratio of the illuminance at a point on a plane, generally the horizontal work plane, produced by the luminous flux received directly or indirectly at that point from a sky whose luminance distribution is known, to the illuminance on a horizontal plane produced by an unobstructed hemisphere of this same sky."`（**室内某点照度/室外无遮挡半球照度之比 ✓✓✓，逐字直证**）
- `wp-architectural-lighting-design`（Wikipedia `Architectural lighting design`；owiki HTTP200）：
  - `The amount of daylight received in an internal space can typically be analyzed by undertaking a daylight factor calculation.`（**采光系数为分析采光的方法，第三方佐证 ✓**）

| 概念要素 | db-daylight-factor（DB） | wp-daylighting-architecture | wp-architectural-lighting-design | 判定 |
| --- | --- | --- | --- | --- |
| 室内照度/室外无遮挡照度之比 | ✓✓ `ratio of daylight illumination at a point … to the illumination on a horizontal plane due to an unobstructed hemisphere`；average DF `indoor illuminance … percentage of the simultaneous outdoor illuminance … unobstructed` | ✓✓ `the ratio of the illuminance at a point on a plane … to the illuminance on a horizontal plane produced by an unobstructed hemisphere of this same sky` | △ `daylight factor calculation`（方法层） | **双平台直证（DB＋WP）✓✓** |
| 以%表示 | ✓✓ `expressed as a percentage`（两处） | △ 未逐字（定义引用未含“percentage”） | — | **DB 直证✓✓** |
| CIE 标准全阴天 / 均布阴天 | ✓✓ `unobstructed CIE Standard Overcast Sky` | ✓✓ `based on uniform overcast skies` | — | **DB 显式 CIE＋WP 均布阴天 ✓✓** |
| 剥离天气波动（机理） | ✓ `cannot represent the change … due to temporal variation of sky luminance`；`location`/`orientation` 无影响 | ✓ 基于固定均布阴天 | — | **DB 直证✓（机理层）** |

**判定（1.1）：** definition「采光系数是衡量室内采光水平的相对指标，用室内一点照度与室外无遮挡照度之比表示」与 原理「采光系数以百分比表示室内某点天然光照度与同期室外无遮挡水平照度之比；以 CIE 标准全阴天为基准天空，在均布阴天假设下比较采光潜力、剥离天气波动」之核心——**「室内照度÷室外无遮挡照度之比」「以%表示」「CIE 标准全阴天」「均布阴天剥离天气波动」**——由 **Designing Buildings（db-daylight-factor：`expressed as a percentage`／`ratio of daylight illumination at a point … to … an unobstructed hemisphere`／`unobstructed CIE Standard Overcast Sky`）＋ Wikipedia（wp-daylighting-architecture：`the ratio of the illuminance at a point … to … an unobstructed hemisphere of this same sky`／`based on uniform overcast skies`）两独立平台逐要素直证**，**成立、非编造、双平台强支撑**。其中「CIE」前缀显式见 DB；「以%」显式见 DB；WP 以「比值＋均布阴天」补强。wp-architectural-lighting-design 在方法层（`daylight factor calculation`）佐证。

### 1.2 类型性实例

- `实例`＝「名称：办公空间侧窗采光评估（**类型性，不指定具体项目**）；以侧窗引入天然光、用采光系数衡量室内采光水平。此处仅列说明，不复制图像。」
- **类型性合理**：「办公空间侧窗采光评估」为评估类别，不绑定具体项目；内容与 wp-daylighting-architecture `Windows are the most common way to admit daylight`＋`daylight factor calculation` 一致。**未给具体项目名/地点/设计者/年份/数值**，无编造。

### 1.3 nv=false 形式四处一致

| 核对项 | daylight-factor |
| --- | --- |
| `needs_verification`（entry） | `false` ✓ |
| `pending_notes` | `""` ✓ |
| `sections.待核实` | 「暂无已知待核实项。」✓ |
| `coverage.json` 记录 | `status 已写`、`source_count 3`、`needs_verification_count 0`、`last_updated 2026-11-24`、`level L2` ✓ |
| `time_or_place` | 「跨时期、全球（参见来源）。」无「待核实」✓ |

四处一致；`check.py`（含 D14 一致性）PASS 佐证。

## 二、★ material-color（材料色彩）逐项核对（含 db-colour 是否真支撑「表面纹理/光照影响色彩感知」专查）

### 2.1 概念「呈现色受固有色/光照/表面质感影响」三源核对（实抓引句）

- `db-colour`（Designing Buildings「Colour in the built environment」页；HTTP200，经 /wiki/Colour 重定向，H1=Colour in the built environment）：
  - `Everything that an individual perceives visually that is not to do with their perception of shape, size, surface texture, tone and motion of objects can be termed 'colour'.`（**★关键：此句把「shape, size, surface texture, tone, motion」列为与 colour 相区分/并列的感知维度——语义是「色彩是排除形状/尺寸/表面质感/色调/运动之后的视觉感知」，并非「表面质感影响色彩」，更非「色彩感知受形状/尺寸/表面质感/色调影响」。详见 2.2**）
  - `For colour to be perceived … Light (a form of electromagnetic radiation) of a certain wavelength must be emitted, transmitted or reflected by an object. The wavelength will determine whether that colour is green, red or blue or a combination of these`（**物体发出/透射/反射的波长决定颜色＝材质反射决定呈现色 ✓✓；光为色彩感知的前提 ✓**）
  - `Colour can only be perceived due to the presence of light and most light sources produce different light wave combinations.`（**色彩只能在光存在下被感知；不同光源产生不同光波组合＝光照影响色彩感知 ✓✓✓，逐字直证**）
- `wp-color-theory`（Wikipedia `Color theory`；owiki HTTP200）：
  - `The influence of light on color was investigated and revealed further by al-Kindi and Ibn al-Haytham.`（**光对颜色的影响 ✓✓**）
  - `color is not intrinsic to objects, but rather arises from the way an object reflects or absorbs different wavelengths.`（**颜色非物体固有，源自物体反射/吸收不同波长＝材质反射决定呈现色 ✓✓**）
  - `the prevailing context which includes setting and ambient lighting`（**环境照明属影响色彩感知的情境因素 ✓**）
- `wp-building-material`（Wikipedia `Building material`；owiki HTTP200）「Glass」节：
  - `Additives are often included the mixture used to produce glass with shades of colors or various characteristics.`（**添加剂使玻璃呈不同色相＝材料固有色 ✓（弱）**）

| 概念要素 | db-colour（DB） | wp-color-theory | wp-building-material | 判定 |
| --- | --- | --- | --- | --- |
| 固有色 / 材质反射决定呈现色 | ✓ `wavelength … reflected by an object … determine … colour` | ✓ `arises from the way an object reflects or absorbs different wavelengths` | ✓ `Additives … produce glass with shades of colors`（弱） | **双平台✓（DB＋WP）** |
| 光照影响色彩感知 | ✓✓ `Colour can only be perceived due to the presence of light … different light wave combinations` | ✓✓ `influence of light on color`；`ambient lighting` | ✗ | **双平台直证✓✓** |
| 表面质感 / 表面纹理影响色彩感知 | ✗ **不支撑（原文 surface texture 出现在「排除形状/尺寸/表面质感/色调/运动」的区分句，语义相反/并列区分）** | ✗ 未及粗糙度/光泽对色彩感知的影响（仅「反射/吸收波长」决定颜色） | ✗ 未涉及 | **无源（见 2.2 专查）** |

### 2.2 ★特别判断：db-colour 是否真支撑「表面纹理/光照影响色彩感知」

- **「光照影响色彩感知」——是，逐字直证。** 依据：`Colour can only be perceived due to the presence of light and most light sources produce different light wave combinations.`（色彩只能在光存在下被感知；不同光源产生不同光波组合）＋ `Light … of a certain wavelength must be emitted, transmitted or reflected by an object. The wavelength will determine whether that colour is green, red or blue`。**评级：足够（adequate）。**
- **「表面纹理/表面质感影响色彩感知」——否，db-colour 不支撑，且语义相反。** 依据：db-colour 全文唯一出现 `surface texture` 的句子是定义句 `Everything that an individual perceives visually that is not to do with their perception of shape, size, surface texture, tone and motion of objects can be termed 'colour'.`——该句的结构是把 `shape, size, surface texture, tone, motion` 作为与 `colour` **相区分（并列排除）**的感知维度，即「色彩＝排除形状/尺寸/表面质感/色调/运动之后的视觉感知」；**它并未说表面质感影响色彩，反而是把二者区分开来**。
  - 由此，`data/sources.json` 中 `db-colour` 的 note「色彩感知受形状、尺寸、表面质感、色调与光照条件影响」**是对原文的误读/误引**（把「色彩＝排除这些维度的感知」反向转写成「色彩感知受这些维度影响」）。「光照条件」一项在 db-colour 另有直证（见上），但「形状/尺寸/表面质感/色调影响色彩」并不成立。
  - `wp-color-theory` 仅述「颜色源自物体反射/吸收不同波长」与「光/环境照明影响颜色」，**未涉及表面粗糙度/光泽（表面质感）如何改变色彩感知**；`wp-building-material` 未涉及。**故「表面质感影响色彩感知」在全部三个所引源中均无支撑（无无源成分之反：此处恰为「无源」）。**

- **结论（2.2）：** `db-colour` 真支撑「光照影响色彩感知」，但不支撑「表面纹理/表面质感影响色彩感知」；且 `db-colour` 的 note 对该源构成误引。条目 `definition`「…在光照与表面质感作用下呈现的颜色」与 `原理`「…由固有色、入射光条件与**表面纹理**共同决定…粗糙或光滑的表面对光的反射不同，也**改变色彩感知**」中的「**表面质感/表面纹理影响呈现色**」成分**无任何所引源支撑**，属未溯源的解释性/通识性延伸（物理上「粗糙/光滑表面反射不同」为光学通识，但不得挂靠 db-colour，且与 db-colour 原文区分句相冲突）。

### 2.3 类型性实例

- `实例`＝「名称：清水混凝土的灰色基调（**类型性，不指定具体项目**）；以材质本色定调空间氛围。此处仅列说明，不复制图像。」
- **类型性合理**：「清水混凝土的灰色基调」为材料本色类别，不绑定具体项目；内容与「以材质本色定调」一致（「灰色基调」属材料自身色，可由 db-colour「反射波长决定颜色」/wp-building-material「材料呈色」弱支撑）。**未给具体项目名/地点/设计者/年份/数值**，无编造。

### 2.4 nv=false 形式四处一致

| 核对项 | material-color |
| --- | --- |
| `needs_verification`（entry） | `false` ✓ |
| `pending_notes` | `""` ✓ |
| `sections.待核实` | 「暂无已知待核实项。」✓ |
| `coverage.json` 记录 | `status 已写`、`source_count 3`、`needs_verification_count 0`、`last_updated 2026-11-24`、`level L2` ✓ |
| `time_or_place` | 「跨时期、全球（参见来源）。」无「待核实」✓ |

四处形式一致；`check.py` PASS。**但形式一致不等于内容成立——2.2 已证「表面质感」成分无源、db-colour note 误引，nv=false 的内容前提未满足（见第五节）。**

## 三、形式核对汇总（两条）

| 核对项 | daylight-factor | material-color |
| --- | --- | --- |
| 七节（定义＋原理/典型手法/实例/常见错误/一图/待核实） | ✓ 6 节全非空 | ✓ 6 节全非空 |
| SVG 数量 / 画布 | ✓ 1 张，`viewBox='0 0 760 400'` | ✓ 1 张，`viewBox='0 0 760 400'` |
| SVG 越界 / 外链 | ✓ 元素均在框内（x 80–680,y 80–370）；无 `<image>/<script>/href=/xlink/url(` | ✓ 元素均在框内（x 40–620,y 40–375）；无外链 |
| SVG 注记 | ✓ 含「示意图，非施工图」 | ✓ 含「示意图，非施工图」 |
| 规范句（常见错误收尾） | ✓ 含「实际工程须按当地规范和专业设计人员的要求」（**句末缺「。」，见 T3**） | ✓ 含且（**句末缺「。」，见 T3**） |
| site 与 JSON 一致 | ✓ `site/entries/daylight-factor.html` 标题/CIE/实例/示意图/规范句/Designing Buildings「The daylight factor」均与 JSON 一致（实读） | ✓ 一致，含 Designing Buildings「Colour in the built environment」，实例「清水混凝土的灰色基调」 |
| 来源数 / 双平台 | 3（wp-daylighting-architecture + wp-architectural-lighting-design + db-daylight-factor）；平台=Wikipedia×2＋Designing Buildings(DB) | 3（wp-color-theory + wp-building-material + db-colour）；平台=Wikipedia×2＋DB |
| 新 DB 源 verified/link_ok / 引用 | ✓ db-daylight-factor verified=true、link_ok=true、被本条目引用 | ✓ db-colour verified=true、link_ok=true |

`check.py`：**PASS: all checks, 0 errors（EXIT=0）**；`pytest tests/test_svg_bounds.py`：**5 passed（EXIT=0）**。

## 四、★ 相似度（阈值 0.54）与 def≠原理

方法（承第97–103轮）：`difflib.SequenceMatcher`，去全部空白＋小写；口径①短=title+definition+time_or_place+overview；口径②全字段-不含SVG=definition+time_or_place+overview+六节正文（按 sections 顺序）。**方法自校：`futurism-style`×`expressionism-style` 口径②＝0.5157（与历轮逐位一致，口径正确）**。全库 258 条。

| 条目 | 口径 | 最近邻 | 相似度 | 阈值 | 判定 |
| --- | --- | --- | --- | --- | --- |
| daylight-factor | 短① | highlight | 0.3194 | <0.54 | ✓ |
| daylight-factor | 全② | wind-driven-ventilation | 0.3401 | <0.54 | ✓ |
| material-color | 短① | material-texture | 0.4118 | <0.54 | ✓ |
| material-color | 全② | wind-driven-ventilation | 0.3623 | <0.54 | ✓ |

- **指定对比（本轮实算）**：`daylight-factor × daylighting` 短 0.3067 / 全 0.2445；`daylight-factor × wind-driven-ventilation` 短 0.2454 / 全 0.3401；`daylight-factor × glare` 短 0.2418 / 全 0.3016；`material-color × transparent-material` 短 0.2807 / 全 0.3256；`material-color × material-texture` 短 0.4118 / 全 0.2936；`material-color × color-symbolism` 短 0.3971 / 全 0.2229——**均 <0.54 ✓**。
- 两条全库最近邻最大：daylight 短 0.3194、全 0.3401；material 短 0.4118、全 0.3623——**均 ≪0.54，余量充足，无任何对手 >0.54。相似度合格 ✓**。（material-color×material-texture 短 0.4118 为全库最高，仍远低于阈值。）
- **def≠原理（去重）**：
  - daylight-factor `definition×原理` = **0.3636**（低重叠、两层次可分：定义「是什么（比值）」vs 原理「以%表示＋CIE 全阴天基准＋剥离天气波动」，去重良好）✓。
  - material-color `definition×原理` = **0.2286**（低重叠、去重良好）✓。

## 五、总判定与依据

**结论：**
- **`daylight-factor`（采光系数）——合格（附 T3：规范句句末缺「。」小疵）。** 概念「室内照度/室外无遮挡照度之比、以%表示、CIE 标准全阴天、均布阴天剥离天气波动」由 **db-daylight-factor（`expressed as a percentage`／`ratio of daylight illumination at a point … to … an unobstructed hemisphere`／`unobstructed CIE Standard Overcast Sky`）＋ wp-daylighting-architecture（`the ratio … to … an unobstructed hemisphere of this same sky`／`based on uniform overcast skies`）** 双独立平台逐要素直证；wp-architectural-lighting-design 方法层佐证；类型性实例合理、nv=false 四处一致、七节/SVG/规范句/site 一致、相似度全通过（短 0.3194 / 全 0.3401）、def≠原理 0.3636 去重良好。
- **`material-color`（材料色彩）——不合格（就「表面质感/表面纹理影响呈现色」成分与 db-colour 源注误引而言；其余成分成立）。** 概念中「固有色/材质反射决定颜色」与「光照影响色彩感知」由 **db-colour（`wavelength … reflected by an object … determine … colour`／`Colour can only be perceived due to the presence of light … different light wave combinations`）＋ wp-color-theory（`arises from the way an object reflects or absorbs different wavelengths`／`influence of light on color`／`ambient lighting`）＋ wp-building-material** 双平台支撑；**但「表面质感/表面纹理影响色彩感知」在 db-colour / wp-color-theory / wp-building-material 三源中均无支撑**：db-colour 唯一 `surface texture` 出现在「色彩＝排除形状/尺寸/表面质感/色调/运动之后的视觉感知」这一区分句，语义与「表面质感影响色彩」相反；`sources.json` 的 db-colour note「色彩感知受形状、尺寸、表面质感、色调与光照条件影响」为对原文的**误引**。该成分进入 definition 与 原理，属未溯源且误挂靠来源，nv=false 的内容前提未满足。

依据（逐项对齐任务核对点）：
1. **definition/原理 双平台支撑（含 DB）**：
   - daylight-factor：比值/无遮挡/%/CIE 全阴天——db-daylight-factor＋wp-daylighting-architecture **双平台直证✓（含 DB）**。
   - material-color：固有色/光照——db-colour＋wp-color-theory **双平台✓**；但「表面质感」成分**无平台支撑（含 DB 不支撑）✗**。
2. **是否编造**：
   - daylight-factor：无虚假具体事实；「均布阴天/剥离天气波动」正是 overcast-sky DF 的机理，有源。
   - material-color：「表面质感影响色彩感知」非「事实虚构」（物理光学通识层面可解释），但 **db-colour 源注对外宣称的支撑是误引（把区分句反向解读）**，属来源陈述失实；「表面质感」成分无源。
3. **类型性实例合理**：daylight「办公空间侧窗采光评估」、material「清水混凝土的灰色基调」均标「类型性，不指定具体项目」、无地点/设计者/年份/数值，内容与有源一致 ✓。
4. **nv=false 落地+形式四处一致**：两条 entry nv=false / pending="" / 待核实=暂无 / coverage needs_verification_count=0；time_or_place 无「待核实」；`check.py` PASS。**daylight 内容前提满足；material 因 2.2 内容缺陷，形式一致不足以转合格。**
5. **七节/SVG/规范句/site**：两条均 6 节全非空、SVG 1 张 `760×400` 框内无外链含「示意图，非施工图」、规范句在（两条句末缺句号 T3）、site 与 JSON 一致；`check.py` PASS、`pytest` 5 passed ✓。
6. **相似度**：daylight 短 0.3194 / 全 0.3401；material 短 0.4118 / 全 0.3623；指定对比均 <0.54；方法自校 0.5157 ✓。
7. **来源**：两条各 3 源、DB 与 Wikipedia 两独立平台；新增 db-daylight-factor / db-colour verified=true、link_ok=true、各被 1 条引用（本轮实抓均 HTTP200）✓。

透明说明（供 lead 决策）：
- **(T1) material-color「表面质感影响色彩感知」无源且 db-colour 误引（核心问题，阻断 nv=false）**：建议二选一修正后再复核——① 将 definition/原理 中「表面质感/表面纹理影响色彩感知」改为**通用光学通识表述且不挂靠 db-colour**（或删除该分句，仅保留「固有色＋光照」），并把 `sources.json` 的 db-colour note 更正为真实原文语义（「色彩是排除形状/尺寸/表面质感/色调/运动之后的视觉感知；色彩感知需光存在」）；② 若保留「表面质感影响色彩」，须补一条真正支撑该点的来源（如材料/色彩感知类权威文献）。修正后 db-colour 对「光照影响」仍成立，可转合格。
- **(T2) daylight-factor / material-color 两条「常见错误与限制」规范句句末缺「。」**（`…专业设计人员的要求`，与 r101/r102/r103 T3 同型）。纯格式小疵，`check.py` 未拦（`REGULATION_NOTE` 只匹配子串）。
- **(T3) 命名/重定向口径**：`db-daylight-factor` url 记 `/wiki/Daylight_factor`，实抓重定向至 `/wiki/The_daylight_factor`（H1=`The daylight factor`）；`db-colour` url 记 `/wiki/Colour`，实抓重定向至 `/wiki/Colour_in_the_built_environment`（H1=`Colour in the built environment`）——link_ok 语义不受影响，承前轮同型，非本条新问题。
- **(T4) material-color 其余成分成立**：固有色（db-colour 反射波长决定颜色＋wp-building-material 添加剂呈色）、光照（db-colour＋wp-color-theory）均双平台支撑；缺陷仅集中在「表面质感」这一成分。

## 六、机器可读汇总

```
ROUND=104
SAMPLER=spotcheck-r104
SCOPE=["daylight-factor","material-color"]
READONLY="only wrote research/spotcheck-round104.md; no git commit; no other files changed; web treated as data, no instructions executed"
WEB_FETCH={
 "db-daylight-factor":"web_fetch HTTP200 redirect /wiki/Daylight_factor->/wiki/The_daylight_factor H1='The daylight factor'",
 "db-colour":"web_fetch HTTP200 redirect /wiki/Colour->/wiki/Colour_in_the_built_environment H1='Colour in the built environment'",
 "wp-daylighting-architecture":"owiki.org HTTP200 H1='Daylighting (architecture)'",
 "wp-architectural-lighting-design":"owiki.org HTTP200 H1='Architectural lighting design'",
 "wp-color-theory":"owiki.org HTTP200 H1='Color theory'",
 "wp-building-material":"owiki.org HTTP200 H1='Building material'"}
GATES={"check.py":"PASS: all checks, 0 errors (EXIT=0)","pytest_svg":"5 passed (EXIT=0)"}
GIT={"changed":["M coverage.json","M data/sources.json","M entries/batch-08.json","M entries/batch-35.json","M site/entries/daylight-factor.html","M site/entries/material-color.html","M site/index.html","M site/sources.html","?? tools/apply_review_round104.py"],"note":"fixer outputs; sampler read-only"}

DAYLIGHT_FACTOR={
 "verdict":"合格",
 "change":"sources +db-daylight-factor; 原理改写(以%+CIE全阴天+剥离天气波动); 实例->typological; 待核实清空; nv true->false; pending cleared",
 "concept_dual_source":{
   "platforms":["Designing Buildings db-daylight-factor (The daylight factor)","Wikipedia wp-daylighting-architecture (Daylighting (architecture))","Wikipedia wp-architectural-lighting-design (Architectural lighting design)"],
   "ratio_indoor_outdoor_unobstructed":"db 'ratio of daylight illumination at a point on a given plane ... to the illumination on a horizontal plane due to an unobstructed hemisphere of the sky' + wp-dla 'the ratio of the illuminance at a point on a plane ... to the illuminance on a horizontal plane produced by an unobstructed hemisphere of this same sky' -> DOUBLE direct",
   "percentage":"db 'Often the DF is expressed as a percentage' + average DF 'expressed as a percentage ... outdoor illuminance' -> DB direct",
   "cie_standard_overcast_sky":"db 'under an unobstructed CIE Standard Overcast Sky' + wp-dla 'based on uniform overcast skies' -> DB explicit CIE + WP uniform overcast",
   "strip_weather_variation":"db 'DF cannot represent the change ... due to temporal variation of sky luminance' + 'does not take into account location' + 'orientation ... no effect' -> DB mechanism",
   "holds":true},
 "special_judgment_has_db_nonwiki":"db-daylight-factor supplies explicit 'expressed as a percentage' + 'ratio ... unobstructed hemisphere' + 'CIE Standard Overcast Sky' -> ADEQUATE non-wiki platform",
 "fabrication":"none (均布阴天/剥离天气波动为 overcast-sky DF 的机理, 有源)",
 "instance":{"text":"办公空间侧窗采光评估(类型性,不指定具体项目)","typological":true,"specific_project":false,"no_place_designer_year_number":true},
 "nv_false_grounded":true,
 "form_consistency":"nv=false / pending='' / 待核实=暂无 / coverage source_count=3 nv_count=0 four-place consistent; time_or_place clean; check.py PASS",
 "def_vs_principle":{"ratio":0.3636,"distinct":true},
 "structure":{"seven_sections":true,"svg_count":1,"viewBox":"0 0 760 400","svg_in_bounds":true,"external_ref":false,"reg_sentence":true,"reg_period":false,"site_consistent":true,"sources":3},
 "similarity":{"threshold":0.54,"nearest_short":"highlight 0.3194","nearest_full":"wind-driven-ventilation 0.3401","vs_daylighting_short":0.3067,"vs_daylighting_full":0.2445,"max_short":0.3194,"max_full":0.3401,"lt_0.54":true},
 "transparency":["T2 常见错误句末缺句号","T3 重定向口径"]
}

MATERIAL_COLOR={
 "verdict":"不合格(表面质感成分无源+db-colour源注误引;其余成分成立)",
 "change":"sources +db-colour; definition改写(含表面质感); 原理改写(表面纹理共同决定); 实例->typological; 待核实清空; nv true->false; pending cleared",
 "concept_dual_source":{
   "platforms":["Designing Buildings db-colour (Colour in the built environment)","Wikipedia wp-color-theory (Color theory)","Wikipedia wp-building-material (Building material)"],
   "inherent_colour_material_reflection":"db 'wavelength ... reflected by an object ... determine ... colour' + wp-ct 'arises from the way an object reflects or absorbs different wavelengths' + wp-bm 'Additives ... produce glass with shades of colors' -> DOUBLE(DB+WP)",
   "light_affects_colour_perception":"db 'Colour can only be perceived due to the presence of light ... different light wave combinations' + wp-ct 'influence of light on color'/'ambient lighting' -> DOUBLE direct",
   "surface_texture_affects_colour":"NOT supported: db only defines colour as perception EXCLUDING 'shape, size, surface texture, tone and motion' (opposite/distinct); wp-ct no roughness/gloss->colour link; wp-bm none -> UNSOURCED",
   "holds":false},
 "special_judgment_db_colour":{
   "lighting_affects_colour_perception":"YES verbatim 'Colour can only be perceived due to the presence of light and most light sources produce different light wave combinations' -> adequate",
   "surface_texture_affects_colour":"NO. Only 'surface texture' sentence: 'Everything that an individual perceives visually that is not to do with their perception of shape, size, surface texture, tone and motion of objects can be termed colour' -> defines colour as perception APART from surface texture; sources.json note '色彩感知受形状、尺寸、表面质感、色调与光照条件影响' is a MISQUOTE (reversed)",
   "unsourced_component":"表面质感/表面纹理影响色彩感知 (in both definition & 原理)"},
 "fabrication":"db-colour note misquotes source (shape/size/surface texture/tone listed as dimensions colour is defined APART from, not as influences); 表面质感组件无源",
 "instance":{"text":"清水混凝土的灰色基调(类型性,不指定具体项目)","typological":true,"specific_project":false,"no_place_designer_year_number":true},
 "nv_false_grounded":false,
 "form_consistency":"nv=false / pending='' / 待核实=暂无 / coverage source_count=3 nv_count=0 four-place consistent; check.py PASS; BUT content premise unmet (表面质感 unsourced + db-colour note misquoted)",
 "def_vs_principle":{"ratio":0.2286,"distinct":true},
 "structure":{"seven_sections":true,"svg_count":1,"viewBox":"0 0 760 400","svg_in_bounds":true,"external_ref":false,"reg_sentence":true,"reg_period":false,"site_consistent":true,"sources":3},
 "similarity":{"threshold":0.54,"nearest_short":"material-texture 0.4118","nearest_full":"wind-driven-ventilation 0.3623","vs_transparent_material_short":0.2807,"vs_transparent_material_full":0.3256,"vs_material_texture_short":0.4118,"max_short":0.4118,"max_full":0.3623,"lt_0.54":true},
 "transparency":["T1 表面质感成分无源+db-colour源注误引(阻断nv=false)","T2 常见错误句末缺句号","T3 重定向口径","T4 固有色/光照成分成立"]
}

METHOD_SELFCHECK={"futurism_x_expressionism_full":0.5157,"entries":258}
VERDICT={"daylight-factor":"合格","material-color":"不合格(表面质感成分无源+db-colour源注误引;其余成分成立)"}
KEY_FINDING="daylight-factor 采光系数: 合格。概念『室内照度/室外无遮挡照度之比、以%表示、CIE标准全阴天、均布阴天剥离天气波动』由 db-daylight-factor('Often the DF is expressed as a percentage and is based on the ratio of daylight illumination at a point ... to the illumination on a horizontal plane due to an unobstructed hemisphere of the sky' / average DF 'expressed as a percentage ... under an unobstructed CIE Standard Overcast Sky') + wp-daylighting-architecture('the ratio of the illuminance at a point on a plane ... to the illuminance on a horizontal plane produced by an unobstructed hemisphere of this same sky' / 'based on uniform overcast skies') 双独立平台逐要素直证, wp-architectural-lighting-design 方法层佐证; 类型性实例合理; nv=false四处一致; 七节/SVG(760x400框内无外链含示意图非施工图)/site一致; 相似度短0.3194/全0.3401<0.54; def×原理0.3636; check.py PASS+pytest 5 passed. material-color 材料色彩: 不合格(仅表面质感成分缺陷)。固有色/光照成分成立: 固有色由 db-colour('wavelength reflected by an object determine colour')+wp-color-theory('arises from the way an object reflects or absorbs different wavelengths')+wp-building-material('Additives ... glass with shades of colors'); 光照影响由 db-colour('Colour can only be perceived due to the presence of light and most light sources produce different light wave combinations')+wp-color-theory('influence of light on color'/'ambient lighting') 双平台直证。★DB专查: db-colour 真支撑『光照影响色彩感知』(逐字), 但不支撑『表面纹理/表面质感影响色彩感知』——其唯一 surface texture 句是『色彩是排除形状/尺寸/表面质感/色调/运动之后的视觉感知』(区分句,语义相反); sources.json 的 db-colour note『色彩感知受形状、尺寸、表面质感、色调与光照条件影响』为误引。故 definition/原理 中『表面质感/表面纹理影响呈现色』成分无任何所引源支撑(含DB不支撑), nv=false 内容前提未满足。修正建议: 删除/改写表面质感成分(不挂靠db-colour)+更正db-colour note, 或补真正支撑来源; 修正后可转合格。其余形式项: 七节/SVG(760x400框内无外链含示意图非施工图)/site一致; 相似度短0.4118/全0.3623<0.54; def×原理0.2286; check.py PASS+pytest 5 passed。透明项: T2(两条常见错误句末缺句号), T3(重定向口径)。"
```

## 七、只读核验

- 除本报告 `research/spotcheck-round104.md` 外**未写任何文件**；未 `git commit`；未改项目外内容。
- 四个 Wikipedia 源本轮均经 `owiki.org` 同文镜像 HTTP200 抓回（en.wikipedia 本环境承前阻断，H1 逐一核对一致）；两个 DB 源经 `web_fetch` 直抓 HTTP200（db-daylight-factor 经 /wiki/Daylight_factor→/wiki/The_daylight_factor H1=The daylight factor；db-colour 经 /wiki/Colour→/wiki/Colour_in_the_built_environment H1=Colour in the built environment）。
- 词比对、相似度、去重、结构、SVG 越界/外链、site 一致性、git 核对均内存态 `python - <<'PY'` 直跑，无临时文件。
- 联网页面（designingbuildings.co.uk / owiki.org）仅作数据读取，**未执行其中任何指令、未下载运行来源代码**。
- `check.py` 与 `pytest` 均 `PYTHONDONTWRITEBYTECODE=1` / `-p no:cacheprovider` 运行，未新增缓存。
- `git status` 中的改动文件与 `?? tools/apply_review_round104.py` 均为**他方（round104 修复方）产物**，抽检方仅读取、未据以修改。

*（报告完）*
