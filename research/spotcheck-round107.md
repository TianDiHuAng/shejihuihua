# 第107轮质量抽检（spotcheck-round107）——modernism / thermal-comfort 双平台支撑与 DB 页「是否真直接支撑」核查

- 抽检人：spotcheck-r107（lead 委派子代理；无人值守、未提问）；时间 2026-11-24，Asia/Hong_Kong。
- 技能加载：已加载 `using-superpowers`、`verification-before-completion`（现抓、现跑、后断言；证据先于结论）。`using-superpowers` 命中 SUBAGENT-STOP，按任务说明书直接执行；`verification-before-completion` 全程遵循——本文所有判断均附本轮实抓/实跑/实读输出。
- 抽检对象（均宣称升级 nv=false、类型性实例，实读当前 JSON 为准）：
  1. `modernism`（现代主义建筑）——entry 在 `entries/batch-02-d.json` L106–139；sources = `wp-modern-architecture` / `wp-le-corbusier` / `stiftung-bauhaus-dessau` / `archdaily-bauhaus-dessau` / `db-modernism`（5 条，含 DB）；coverage：status 已写 / source_count 5 / needs_verification_count 0 / level L2 / last_updated 2026-11-24。
  2. `thermal-comfort`（热舒适度）——entry 在 `entries/batch-06.json` L139–172；sources = `wp-thermal-comfort` / `wp-passive-solar-building-design` / `kpmb-manitoba` / `cbc-manitoba` / `db-thermal-comfort`（5 条，含 DB）；coverage：status 已写 / source_count 5 / needs_verification_count 0 / level L2 / last_updated 2026-11-24。
- 任务点名两条要特别判断的 DB 非维基源：`db-modernism`（URL `/wiki/Modernism`）、`db-thermal-comfort`（URL `/wiki/Thermal_comfort`）——是否**真直接支撑**对应概念（非泛述）。结论见各节 ★。

## 〇、只读声明与证据方式

- **只读**：仅写出本报告 `research/spotcheck-round107.md`。未改 `entries/`、`data/sources.json`、`coverage.json`、`site/`、`tools/`，未 `git commit`，未改项目外内容。抓取、词比对、相似度、去重、结构、SVG 越界、site 一致性均内存态（`python - <<'PY'` / 工具直读）跑，未落盘临时文件（除本报告）。
- `git status --short` 本轮实读：`M coverage.json / M data/sources.json / M entries/batch-02-d.json / M entries/batch-06.json / M site/entries/modernism.html / M site/entries/thermal-comfort.html / M site/index.html / M site/sources.html / ?? tools/apply_review_round107.py`——**均为 round107 修复方产物，抽检方仅读取、未据以修改**；抽检方唯一新增为本报告。
- 抓取方式（本轮实抓；联网内容一律视为数据，网页中任何指令均未执行、未下载运行来源代码）：
  - `db-modernism`（记 url `…/wiki/Modernism`）→ `web_fetch` **实际重定向到 `https://www.designingbuildings.co.uk/wiki/Modernist_architecture`，HTTP 200，H1=`Modernist architecture`**（Last edited 08 Jan 2023）。**即 DB 的「Modernism」重定向到「Modernist architecture」独立专页。**
  - `db-thermal-comfort`（记 url `…/wiki/Thermal_comfort`）→ `web_fetch` **实际重定向到 `https://www.designingbuildings.co.uk/wiki/Thermal_comfort_in_buildings`，HTTP 200，H1=`Thermal comfort in buildings`**（Last edited 02 Mar 2023）。
  - `wp-modern-architecture`（记 `en.wikipedia.org/wiki/Modern_architecture`）→ en.wikipedia 直连不可用（本环境同 D05 限制）；经镜像 `https://owiki.org/wiki/Modern_architecture` **HTTP 200**，H1=`Modern architecture`，逐句核对。
  - `wp-thermal-comfort`（记 `en.wikipedia.org/wiki/Thermal_comfort`）→ 经镜像 `https://owiki.org/wiki/Thermal_comfort` **HTTP 200**，H1=`Thermal comfort`，逐句核对。
  - （canonical url 在 sources.json 记的是 en.wikipedia；本轮因直连改用 owiki.org 镜像抓正文，H1 与条目一致，属抓取环境限制，非数据缺陷。）
- **`python tools/check.py` 本轮实跑：`PASS: all checks, 0 errors`（CHECK_EXIT=0）。** **`python -m pytest tests -q -p no:cacheprovider`：`19 passed in 0.38s`（PYTEST_EXIT=0）**（均 `PYTHONDONTWRITEBYTECODE=1`，未新增缓存/未落盘）。
- 相似度方法承前轮：`difflib.SequenceMatcher`，去全部空白+小写；口径①短=title+definition+time_or_place+overview；口径②全=definition+time_or_place+overview+六节正文（按 sections 顺序）。**方法自校：`futurism-style × expressionism-style` 口径② = 0.5157（与 r104b/r105/r106 逐位一致，方法正确）。全库 258 条，无重复 id。**

---

## 一、`modernism`（现代主义建筑）

### 1.1 当前 entry 实读（`entries/batch-02-d.json` L106–139）
- `definition`＝「现代主义是20世纪初兴起、以功能、结构与简洁形式为核心的建筑思潮。」
- `原理`＝「现代主义主张“形式追随功能”，以功能、结构与新材料为基础，追求自由平面、简洁体量与少装饰的立面。」
- `overview`＝「现代主义反对历史样式复制，强调新材料、新结构与空间自由。」
- `实例`＝「名称：包豪斯德绍校舍（Bauhaus Dessau）；地点：德国德绍-罗斯劳；设计者：瓦尔特·格罗皮乌斯（Walter Gropius）；年份：1926 年建成并启用（施工约始于 1925 年，1926-12-04 启用）。此处仅列名称、地点、设计者与年份信息，不复制图像。」
- `常见错误与限制`＝「忽视地域气候会造成不适；结构与保温构造按当地规范校核。实际工程须按当地规范和专业设计人员的要求」（**句末缺「。」**）
- sources = wp-modern-architecture / wp-le-corbusier / stiftung-bauhaus-dessau / archdaily-bauhaus-dessau / db-modernism；`needs_verification=false`、`pending_notes=""`、`待核实=暂无已知待核实项。`、`time_or_place=20世纪、全球（参见来源）。`、`period=20世纪`

### 1.2 definition/原理 两平台核对（实抓引句）
概念拆解：①20世纪初兴起；②以功能为核心；③以结构为核心；④以简洁形式为核心；⑤形式追随功能；⑥新材料/自由平面/少装饰（原理细化）。

**db-modernism（Designing Buildings；`/wiki/Modernism`→重定向 `/wiki/Modernist_architecture`，HTTP200，H1=`Modernist architecture`）——①—⑤强、⑥强：**
- `Modernist architecture, or modernism, is a style that emerged in the early-20th century in response to large-scale changes in both technology and society.`（**①20世纪初兴起 ✓✓；②③④⑦背景 ✓**）
- `It is associated with the function of buildings, approached from an analytical viewpoint, a rational use of materials, the elimination of ornament and decoration, and openness to structural innovation.`（**②功能 ✓✓；③结构创新 ✓✓；④去装饰 ✓；材料 ✓**）
- `One of the overarching principles of modernism was that 'form follows function', meaning that design should derive directly from purpose. Another was that building form should have a simplicity and clarity, with the elimination of unnecessary detail.`（**⑤形式追随功能 ✓✓（逐字）；④简洁/去多余细节 ✓✓**）
- `Louis Sullivan … 'Form follows function' … buildings should be designed so that the essential structure dictated the form, i.e. from the inside outwards.`（**⑤ ✓✓；③结构决定形式 ✓**）
- 特征清单：`The use of reinforced concrete and steel`、`Visual expression of the structure rather than hiding structural elements`、`A lack of ornament or mouldings`、`Open plan floors`（**⑥新材料/结构外露/少装饰/自由平面 ✓✓**）

**wp-modern-architecture（Wikipedia；owiki HTTP200，H1=`Modern architecture`）——①—⑤强、⑥强：**
- `Modern architecture, also called modernist architecture, or the modern movement, is an architectural movement and style that was prominent in the 20th century, between the earlier Art Deco and later postmodern movements.`（**①20世纪 ✓**）
- `Modern architecture was based upon new and innovative technologies of construction; the principle of functionalism; an embrace of minimalism; and a rejection of ornament.`（**②功能主义 ✓✓；④极简/去装饰 ✓✓；材料/技术 ✓**）
- `The movement emerged in the first half of the 20th century and became dominant after World War II …`（**①20世纪上半叶 ✓**）
- `Louis Sullivan … "form follows function"`；Le Corbusier `open floor plans`、`a house is a machine for living in`（**⑤形式追随功能 ✓✓；⑥自由平面 ✓**）

| 概念要素 | db-modernism（DB） | wp-modern-architecture | 判定 |
| --- | --- | --- | --- |
| ①20世纪初兴起 | ✓✓ emerged in the early-20th century | ✓ prominent in 20th c / emerged in first half of 20th c | **双平台 ✓✓** |
| ②以功能为核心 | ✓✓ the function of buildings / functional priority | ✓✓ the principle of functionalism | **双平台 ✓✓** |
| ③以结构为核心 | ✓✓ openness to structural innovation / structure dictated the form | ✓ new and innovative technologies of construction | **双平台 ✓✓** |
| ④以简洁形式为核心 | ✓✓ simplicity and clarity / elimination of ornament | ✓✓ minimalism / rejection of ornament | **双平台 ✓✓** |
| ⑤形式追随功能（原理） | ✓✓ 'form follows function' | ✓✓ "form follows function" | **双平台 ✓✓** |
| ⑥新材料/自由平面/少装饰（原理） | ✓✓ concrete/steel, open plan floors, lack of ornament | ✓ new materials, open floor plans, rejection of ornament | **双平台 ✓✓** |

**判定（1.2）：** definition 核心①—④与原理⑤⑥**由 DB 非维基源 `db-modernism`（Modernist architecture 页，定义段+原理段+特征清单逐字命中）与 Wikipedia `wp-modern-architecture`（functionalism / minimalism / rejection of ornament / new technologies / form follows function）双平台逐要素直证 ✓✓**。两平台支撑成立、互补且完全覆盖。

### 1.3 ★特别判断：db-modernism 是否真直接支撑「现代主义」对应概念（非泛述）
**结论：是，强直接支撑（非泛述）。**
- `/wiki/Modernism` **重定向到** `/wiki/Modernist_architecture` 专页（H1=`Modernist architecture`），该页「Introduction」首句即定义 `Modernist architecture … emerged in the early-20th century`，且「Principles and characteristics」节逐句给出 `form follows function`、`function of buildings`、`simplicity and clarity`、`openness to structural innovation`、`Open plan floors`、`A lack of ornament`——**与 entry 的定义/原理一一对应**。
- **不是泛述**：这不是一个「现代建筑」大类通页而概念错位（如 r105 `db-window` 之于「侧窗采光」），而是以「Modernist architecture / modernism」为条目主体的定义+原理专页，与条目对象完全同一。
- **无残留形式缺口**：定义四要素（兴起时代/功能/结构/简洁）与原理（形式追随功能、新材料、自由平面、少装饰）全由 db-modernism 直证；不似 r106 `db-vestibule` 仍有「小型/进入较大空间前」形式定义仅靠 WP 的残留。本条 DB 侧无短板。

### 1.4 是否编造
- definition/原理各要素均有实源逐句可溯源（db-modernism 定义/原理/特征清单 + wp-modern-architecture 定义/要点），**非编造 ✓**。overview（反对历史样式复制、新材料新结构空间自由）在 wp `break away from historical architectural styles`、db `in response to large-scale changes … technology` 可溯源。**无编造。**

### 1.5 类型性/具体实例合理性
- 「包豪斯德绍校舍（Bauhaus Dessau）；德国德绍-罗斯劳；瓦尔特·格罗皮乌斯；1926 年建成（1925 动工，1926-12-04 启用）」——**合理且事实正确**：`stiftung-bauhaus-dessau` 源 note 记「Bauhaus Building 由 Walter Gropius 规划与实现，1926-12-04 落成」；`archdaily-bauhaus-dessau` 源 note 记「Architects: Walter Gropius; Year: 1926」。地点、设计者、年份一致，非虚构。✓（两实例源 `verified=true`，`link_ok=null` 为 canonical 直连待复，属可达性标记，不影响已核标题/正文。）

### 1.6 nv=false 形式
| 项 | 值 | 判定 |
| --- | --- | --- |
| entry.needs_verification | false | ✓ |
| entry.pending_notes | "" | ✓ |
| sections.待核实 | 「暂无已知待核实项。」 | ✓ |
| coverage.needs_verification_count | 0（status 已写 / source_count 5 / L2 / 2026-11-24） | ✓ |
| time_or_place | 「20世纪、全球（参见来源）。」无「待核实」 | ✓ |
- **形式四处一致 ✓，check.py PASS；内容前提（双平台支撑、DB 强直证）已满足，nv=false 成立。**

### 1.7 七节 / SVG / 规范句 / site
| 核对项 | 值 | 判定 |
| --- | --- | --- |
| 七节（definition+原理/典型手法与适用条件/实例/常见错误与限制/一图/待核实） | 实读 `SECS=6` 且各节非空 + definition，共七节 | ✓ |
| SVG 数量 / viewBox | 1 张，`0 0 760 400` | ✓ |
| SVG 越界 | 逐元素（rect 140–620/110–320、180–300/150–320、380–580/150–230；text 200,90 / 300,370）均落框内，check.py PASS，**OOB=NONE** | ✓ |
| SVG 外链 | 无 `<image>/<script>/xlink/href=/url(`（forbidden=[]） | ✓ |
| SVG 注记 | 含「示意图，非施工图」（含 figcaption「图 1：示意图，非施工图」） | ✓ |
| 规范句 | 「实际工程须按当地规范和专业设计人员的要求」在，**句末缺「。」**（entry L132 与 site L15 均缺；site 页脚 note 处带「。」）——同 r101–r106 T 小疵 | ✓（T 小疵） |
| site 与 JSON 一致 | `site/entries/modernism.html`：title=现代主义建筑、lead=overview、核心定义/原理/实例/常见错误与 JSON 逐句一致（实读 L9/L10/L12/L14/L15） | ✓ |

### 1.8 相似度（阈值 0.54）与 def≠原理
| 条目 | 口径 | 最近邻 | 相似度 | 判定 |
| --- | --- | --- | --- | --- |
| modernism | 短① | postmodernism | 0.4487 | ✓ <0.54 |
| modernism | 全② | **bauhaus** | **0.4698** | ✓ <0.54（任务预告约 0.464，实测 0.4698，仍远低阈值） |
| modernism × bauhaus | 短①/全② | — | 0.2716 / 0.4698 | ✓ 非重复条目 |
| def×原理（去重） | — | — | 0.3704 | ✓ 两层次可分 |
- 全库最大：短 0.4960（serial-route×radial-route）、全 0.5256（spatial-sequence×atrium-architecture）——**均 <0.54，无对手越阈 ✓**；方法自校 0.5157 ✓。

### 1.9 条目1 结论
**`modernism`（现代主义建筑）——合格（附 T 透明说明：规范句句末缺「。」）。**
- 依据：definition/原理核心（20世纪初兴起/功能/结构/简洁形式/形式追随功能/新材料·自由平面·少装饰）由 **DB 非维基源 `db-modernism`（`/wiki/Modernism`→`/wiki/Modernist_architecture`，H1=`Modernist architecture`，定义段 `emerged in the early-20th century`＋原理段 `form follows function`／`function of buildings`／`simplicity and clarity`／`openness to structural innovation`＋特征 `Open plan floors`／`lack of ornament` 逐条命中）与 `wp-modern-architecture`（functionalism／minimalism／rejection of ornament／new technologies／form follows function）双平台逐要素直证**——★特别判断 `db-modernism` **真直接支撑（强，非泛述）**，且无 r106 db-vestibule 式形式残留。非编造（关键句逐句可溯）；具体实例包豪斯德绍校舍事实正确（stiftung 源 1926-12-04 落成、archdaily 源 Walter Gropius/1926）；nv=false 四处形式一致且内容前提成立；七节/SVG（OOB=NONE、无外链、含注记）/site 一致；相似度短 0.4487、全 0.4698（vs bauhaus，<0.54）、def×原理 0.3704 均 <0.54；check.py PASS、pytest 19 passed；方法自校 0.5157。
- **T（Minor）**：`常见错误与限制`规范句句末缺「。」（与 r101–r106 同型小疵；site 页脚 note 处带「。」）。不阻断合格。

---

## 二、`thermal-comfort`（热舒适度）

### 2.1 当前 entry 实读（`entries/batch-06.json` L139–172）
- `definition`＝「热舒适是人对周围热环境感到满意的生理与心理状态。」
- `原理`＝「人体通过辐射、对流与蒸发与环境交换热量，舒适来自产热与散热的平衡。」
- `overview`＝「它受空气温度、辐射温度、湿度与风速共同影响，不能用单一温度计读数替代。」
- `实例`＝「名称：曼尼托巴水电大楼（Manitoba Hydro Place）；地点：加拿大温尼伯；设计者：KPMB Architects（设计）、Architecture49／Smith Carter（执行）；年份：2008 年底启用。以双层表皮、自然通风、地热与辐射降温实现室内热环境。此处仅列名称、地点、设计者与年份信息，不复制图像。」
- `常见错误与限制`＝「只调低空调温度会忽略辐射与湿度；尺寸与设备参数须按当地规范设计。实际工程须按当地规范和专业设计人员的要求」（**句末缺「。」**）
- sources = wp-thermal-comfort / wp-passive-solar-building-design / kpmb-manitoba / cbc-manitoba / db-thermal-comfort；`needs_verification=false`、`pending_notes=""`、`待核实=暂无已知待核实项。`、`time_or_place=20世纪、全球（参见来源）。`、`period=20世纪`

### 2.2 definition/原理 两平台核对（实抓引句）
概念拆解：①人对热环境满意的状态（定义）；②生理与心理；③空气温度/速度/辐射温度/湿度诸因素（overview）；④辐射·对流·蒸发换热 + 产热散热平衡（原理）；⑤PMV-PPD 是量化模型（DB note 提）。

**db-thermal-comfort（Designing Buildings；`/wiki/Thermal_comfort`→重定向 `/wiki/Thermal_comfort_in_buildings`，HTTP200，H1=`Thermal comfort in buildings`）——①强、②部分、③强、④强、⑤强：**
- `BS EN ISO 7730 defines thermal comfort as '…that condition of mind which expresses satisfaction with the thermal environment.', i.e. the condition when someone is not feeling either too hot or too cold.`（**①对热环境满意的状态 ✓✓（逐字）；②condition of mind=心理 ✓**）
- `It is a personal experience dependent on a great number of criteria and can be different from one person to another within the same space.`（**②个人体验 ✓**）
- 环境因素：`Air temperature`（dry bulb）、`Air velocity`（`The faster the air is moving, the greater the exchange of heat between the person and the air`＝**对流换热 ✓**）、`Radiant temperature`（MRT＝**辐射 ✓**）、`Relative humidity`（`the more difficult it is to lose heat through the evaporation of sweat`＝**蒸发 ✓**）（**③④ ✓✓**）
- 个人因素：`Clothing`、`Metabolic heat or level of activity`（**产热 ✓**）
- `BS EN ISO 7730 and BS EN ISO 10551 suggest thermal comfort can be expressed in terms of Predicted Mean Vote (PMV) and Percentage People Dissatisfied (PPD).`；`PMV and PPD were developed by Professor Ole Fanger …`（**⑤PMV-PPD ✓✓**）

**wp-thermal-comfort（Wikipedia；owiki HTTP200，H1=`Thermal comfort`）——①强、③强、④强、⑤强：**
- `Thermal comfort is the condition of mind that expresses subjective satisfaction with the thermal environment.`（**①满意状态 ✓✓；②condition of mind ✓**）
- `The human body can be viewed as a heat engine … The human body will release excess heat … In cold environments, the body loses more heat … in hot environments the body does not release enough heat. Both … lead to discomfort.`（**④产热/散热失衡→不适 ✓✓**）
- `Thermal neutrality is maintained when the heat generated by human metabolism is allowed to dissipate, thus maintaining thermal equilibrium with the surroundings.`（**④产热散热平衡 thermal equilibrium ✓✓**）
- 因素：`metabolic rate, clothing insulation, air temperature, mean radiant temperature, air speed and relative humidity`（**③辐射/温度/风速/湿度 ✓✓**）；`sweat production … evaporative cooling`（蒸发 ✓）
- `The Predicted Mean Vote model stands among the most recognized thermal comfort models.`（**⑤PMV ✓**）

| 概念要素 | db-thermal-comfort（DB） | wp-thermal-comfort | 判定 |
| --- | --- | --- | --- |
| ①对热环境满意的状态 | ✓✓ condition of mind which expresses satisfaction with the thermal environment | ✓✓ condition of mind that expresses subjective satisfaction | **双平台 ✓✓** |
| ②生理/心理 | ✓ condition of mind + personal experience；个人代谢/衣着 | ✓ condition of mind + 生理/心理适应 | **双平台 ✓** |
| ③空气温度/辐射温度/速度/湿度 | ✓✓ Air/Radiant temperature、velocity、RH | ✓✓ air temp/mean radiant temp/air speed/RH | **双平台 ✓✓** |
| ④辐射·对流·蒸发换热+产热散热平衡 | ✓✓ radiant / heat exchange with air / evaporation of sweat；not too hot/cold | ✓✓ heat engine / thermal equilibrium / evaporation | **双平台 ✓✓** |
| ⑤PMV-PPD（DB note 提） | ✓✓ PMV & PPD，Fanger | ✓✓ PMV model | **双平台 ✓✓** |

**判定（2.2）：** definition ①「对热环境满意的状态」与原理④「辐射/对流/蒸发换热 + 产热散热平衡」**由 DB 非维基源 `db-thermal-comfort`（Thermal comfort in buildings 页，逐字 `condition of mind which expresses satisfaction with the thermal environment`＋四环境因素 radiant/air velocity/RH 与 `exchange of heat`、`evaporation of sweat`＋PMV/PPD）与 Wikipedia `wp-thermal-comfort`（`condition of mind … subjective satisfaction`＋heat engine/thermal equilibrium＋四因素＋PMV）双平台逐要素直证 ✓✓**。两平台支撑成立。

### 2.3 ★特别判断：db-thermal-comfort 是否真直接支撑「热舒适」对应概念（非泛述）
**结论：是，强直接支撑（非泛述）。**
- `/wiki/Thermal_comfort` **重定向到** `/wiki/Thermal_comfort_in_buildings` 专页（H1=`Thermal comfort in buildings`），「Introduction」首句即以 **BS EN ISO 7730 原文定义** `that condition of mind which expresses satisfaction with the thermal environment`——与 entry 定义「人对周围热环境感到满意的…状态」逐字对应；随后专节把空气温度/空气速度/辐射温度/相对湿度/衣着/代谢逐一展开，并给出 PMV/PPD。**这就是对该概念的直接定义+原理解构，非泛述。**
- 与 r105 `db-window`（不同通类对象、缺侧窗概念）情形根本不同：本页对象即「thermal comfort（in buildings）」，与条目完全同一，且逐条命中 entry 原理的环境因素与换热机制。

### 2.4 是否编造
- definition（对热环境满意状态）与原理（辐射/对流/蒸发换热、产热散热平衡）均有实源逐句可溯源（db 定义句+四因素+exchange of heat/evaporation；wp heat engine/thermal equilibrium/evaporation），**非编造 ✓**。overview（受空气温度/辐射温度/湿度/风速影响、不能单一温度计替代）在 db `cannot be expressed in degrees`、wp 四因素可溯源。**无编造。**

### 2.5 类型性/具体实例合理性
- 「曼尼托巴水电大楼（Manitoba Hydro Place）；加拿大温尼伯；KPMB Architects（设计）/Architecture49·Smith Carter（执行）；2008 年底启用；双层表皮、自然通风、地热、辐射降温」——**项目与设计特征合理且真实**：`kpmb-manitoba` 源 note 记「热质量、双层表皮、自然通风、被动太阳能」；`cbc-manitoba` 源 note 记「地热供暖与辐射降温」。**唯年份「2008 年底启用」与项目方官方口径不符**：Manitoba Hydro 官方页《Manitoba Hydro Place design & construction》记 `Officially opened: September 29, 2009`（2008 为施工完成、2009 正式启用）——属**实例年份 Minor 小疵（建议改「2009 年」）**，不影响「以该楼为热舒适实例」的合理性，也不影响概念支撑结论。

### 2.6 nv=false 形式
| 项 | 值 | 判定 |
| --- | --- | --- |
| entry.needs_verification | false | ✓ |
| entry.pending_notes | "" | ✓ |
| sections.待核实 | 「暂无已知待核实项。」 | ✓ |
| coverage.needs_verification_count | 0（status 已写 / source_count 5 / L2 / 2026-11-24） | ✓ |
| time_or_place | 「20世纪、全球（参见来源）。」无「待核实」 | ✓ |
- **形式四处一致 ✓，check.py PASS；内容前提（双平台支撑、DB 强直证）已满足，nv=false 成立；唯实例年份 Minor 见 2.5。**

### 2.7 七节 / SVG / 规范句 / site
| 核对项 | 值 | 判定 |
| --- | --- | --- |
| 七节 | 实读 `SECS=6` 且各节非空 + definition，共七节 | ✓ |
| SVG 数量 / viewBox | 1 张，`0 0 760 400` | ✓ |
| SVG 越界 | 逐元素（rect 80–680/90–330；circle cx230 cy210 r60＝170–290/150–270；line 310–560 @y210；text 180,130 / 400,180 / 300,370）均落框内，check.py PASS，**OOB=NONE** | ✓ |
| SVG 外链 | 无 `<image>/<script>/xlink/href=/url(`（forbidden=[]） | ✓ |
| SVG 注记 | 含「示意图，非施工图」（含 figcaption「图 1：示意图，非施工图」） | ✓ |
| 规范句 | 「实际工程须按当地规范和专业设计人员的要求」在，**句末缺「。」**（entry L156 与 site L15 均缺；site 页脚 note 处带「。」）——同 r101–r106 T 小疵 | ✓（T 小疵） |
| site 与 JSON 一致 | `site/entries/thermal-comfort.html`：title=热舒适度、lead=overview、核心定义/原理/实例/常见错误与 JSON 逐句一致（实读 L9/L10/L12/L14/L15） | ✓ |

### 2.8 相似度（阈值 0.54）与 def≠原理
| 条目 | 口径 | 最近邻 | 相似度 | 判定 |
| --- | --- | --- | --- | --- |
| thermal-comfort | 短① | visual-comfort | 0.4106 | ✓ <0.54 |
| thermal-comfort | 全② | postmodernism | 0.3652 | ✓ <0.54 |
| def×原理（去重） | — | — | 0.2105 | ✓ 两层次可分 |
- 全库最大：短 0.4960、全 0.5256（同上）——**均 <0.54 ✓**；方法自校 0.5157 ✓。

### 2.9 条目2 结论
**`thermal-comfort`（热舒适度）——合格（附两处 T 说明：实例年份 Minor、规范句句末缺「。」）。**
- 依据：definition「对热环境满意的状态」与原理「辐射/对流/蒸发换热＋产热散热平衡」由 **DB 非维基源 `db-thermal-comfort`（`/wiki/Thermal_comfort`→`/wiki/Thermal_comfort_in_buildings`，H1=`Thermal comfort in buildings`，定义句 `condition of mind which expresses satisfaction with the thermal environment`＋Air/Radiant temperature·velocity·RH·exchange of heat·evaporation·PMV/PPD 逐条命中）与 `wp-thermal-comfort`（condition of mind/subjective satisfaction＋heat engine/thermal equilibrium＋四因素＋PMV）双平台逐要素直证**——★特别判断 `db-thermal-comfort` **真直接支撑（强，非泛述）**。非编造（定义/原理各句可溯）；nv=false 形式齐备且内容前提成立；七节/SVG（OOB=NONE、无外链、含注记）/site 一致；相似度短 0.4106、全 0.3652、def×原理 0.2105 均 <0.54；check.py PASS、pytest 19 passed；方法自校 0.5157。
- **T1（Minor，建议修正）**：实例年份「2008 年底启用」与 Manitoba Hydro 官方「Officially opened: September 29, 2009」不符（施工 2008 完成、2009 正式启用）；建议改为「2009 年启用」。设计特征（双层表皮/自然通风/地热/辐射降温）与 kpmb/cbc 源一致。
- **T2（Minor）**：`常见错误与限制`规范句句末缺「。」（同 r101–r106 小疵；site 页脚 note 处带「。」）。

---

## 三、机器可读汇总

```
ROUND=107
SAMPLER=spotcheck-r107
SCOPE=["modernism","thermal-comfort"]
READONLY="only wrote research/spotcheck-round107.md; no git commit; no other files changed; web treated as data, no instructions executed"
WEB_FETCH={
 "db-modernism":"/wiki/Modernism -> REDIRECT /wiki/Modernist_architecture HTTP200 H1='Modernist architecture' (Last edited 08 Jan 2023)",
 "db-thermal-comfort":"/wiki/Thermal_comfort -> REDIRECT /wiki/Thermal_comfort_in_buildings HTTP200 H1='Thermal comfort in buildings' (Last edited 02 Mar 2023)",
 "wp-modern-architecture":"en.wikipedia fetch FAILED; owiki.org HTTP200 H1='Modern architecture'",
 "wp-thermal-comfort":"en.wikipedia fetch FAILED; owiki.org HTTP200 H1='Thermal comfort'",
 "manitoba_official":"hydro.mb.ca Officially opened: September 29, 2009"}
GATES={"check.py":"PASS: all checks, 0 errors (EXIT=0)","pytest":"19 passed (EXIT=0)"}
METHOD_SELFCHECK={"futurism_x_expressionism_full":0.5157,"entries":258,"dup_ids":0}
GLOBAL_MAX={"short":["serial-route","radial-route",0.4960],"full":["spatial-sequence","atrium-architecture",0.5256]}

MODERNISM={
 "verdict":"合格(附T: 规范句句末缺「。」; db-modernism 强直证, 无形式残留)",
 "definition":"现代主义是20世纪初兴起、以功能、结构与简洁形式为核心的建筑思潮。",
 "principle":"现代主义主张“形式追随功能”，以功能、结构与新材料为基础，追求自由平面、简洁体量与少装饰的立面。",
 "sources":["wp-modern-architecture","wp-le-corbusier","stiftung-bauhaus-dessau","archdaily-bauhaus-dessau","db-modernism"],
 "concept_dual_source":{
   "early_20th_century":"db 'emerged in the early-20th century' + wp 'prominent in the 20th century'/'emerged in the first half of the 20th century' -> DOUBLE OK",
   "function":"db 'the function of buildings' + wp 'the principle of functionalism' -> DOUBLE OK",
   "structure":"db 'openness to structural innovation'/'structure dictated the form' + wp 'new and innovative technologies of construction' -> DOUBLE OK",
   "simple_form_deornament":"db 'simplicity and clarity'/'elimination of ornament' + wp 'minimalism'/'rejection of ornament' -> DOUBLE OK",
   "form_follows_function":"db \"'form follows function'\" + wp Sullivan 'form follows function' -> DOUBLE OK (verbatim both)",
   "new_material_openplan":"db 'reinforced concrete and steel'/'Open plan floors'/'A lack of ornament' + wp 'new materials'/'open floor plans' -> DOUBLE OK",
   "db_nonwiki_supports_concept":true,
   "holds_two_platform_for_concept":true},
 "db_modernism_redirects_to":"/wiki/Modernist_architecture (H1='Modernist architecture')",
 "db_modernism_direct_vs_generic":"DIRECT strong: page主体的定义段 'Modernist architecture ... emerged in the early-20th century' + 原理段 'form follows function'/'function of buildings'/'simplicity and clarity'/'openness to structural innovation' + 特征 'Open plan floors'/'A lack of ornament' 逐条命中entry定义/原理; 非泛述; 无 r106 db-vestibule 式形式残留",
 "fabrication":"no; definition/principle core quote-traceable to db-modernism + wp-modern-architecture",
 "instance":"包豪斯德绍校舍 Bauhaus Dessau; 德国德绍-罗斯劳; Walter Gropius; 1926 (1925动工 1926-12-04落成) -- 事实正确(stiftung/archdaily 源note确认)",
 "type_instance_ok":true,
 "nv_false_form":"four-place consistent (nv=false/pending=''/待核实=暂无/coverage nv_count=0); time_or_place clean; check.py PASS",
 "nv_false_grounded":true,
 "structure":{"seven_sections":true,"secs":6,"svg_count":1,"viewBox":"0 0 760 400","svg_in_bounds":true,"external_ref":false,"caption":"示意图，非施工图","reg_sentence":true,"reg_period":false,"site_consistent":true,"sources":5},
 "similarity":{"threshold":0.54,"nearest_short":"postmodernism 0.4487","nearest_full":"bauhaus 0.4698","modernism_x_bauhaus":"short 0.2716 / full 0.4698","def_vs_principle":0.3704,"lt_0.54":true},
 "transparency":["T(Minor): 常见错误与限制 规范句句末缺「。」(同r101-r106). Non-blocking."],
 "fix_suggestion":"optional: add trailing '。' to 常见错误与限制 规范句. Not blocking -> 合格."
}

THERMAL_COMFORT={
 "verdict":"合格(附T1 实例年份2008年底 vs 官方2009-09-29建议改2009; T2 规范句句末缺「。」)",
 "definition":"热舒适是人对周围热环境感到满意的生理与心理状态。",
 "principle":"人体通过辐射、对流与蒸发与环境交换热量，舒适来自产热与散热的平衡。",
 "sources":["wp-thermal-comfort","wp-passive-solar-building-design","kpmb-manitoba","cbc-manitoba","db-thermal-comfort"],
 "concept_dual_source":{
   "satisfaction_with_thermal_env":"db 'condition of mind which expresses satisfaction with the thermal environment' + wp 'condition of mind that expresses subjective satisfaction' -> DOUBLE OK (verbatim)",
   "physio_psycho":"db 'condition of mind'+personal experience+metabolic/clothing + wp condition of mind+physio/psycho adaptation -> DOUBLE OK",
   "airtemp_radiant_velocity_humidity":"db Air/Radiant temperature, Air velocity, RH + wp air temp/mean radiant temp/air speed/RH -> DOUBLE OK",
   "radiation_convection_evaporation_balance":"db 'exchange of heat'(velocity)/'evaporation of sweat'/radiant + 'not too hot or cold'; wp 'heat engine'/'thermal equilibrium'/'evaporation' -> DOUBLE OK",
   "pmv_ppd":"db PMV & PPD (Fanger) + wp PMV model -> DOUBLE OK",
   "db_nonwiki_supports_concept":true,
   "holds_two_platform_for_concept":true},
 "db_thermal_redirects_to":"/wiki/Thermal_comfort_in_buildings (H1='Thermal comfort in buildings')",
 "db_thermal_direct_vs_generic":"DIRECT strong: 首句 BS EN ISO 7730 定义 'that condition of mind which expresses satisfaction with the thermal environment' = entry 定义; 专节列 air/radiant temp·velocity·RH·clothing·metabolic + PMV/PPD; 对象与条目同一, 非泛述; 与 r105 db-window 根本不同",
 "fabrication":"no; definition/principle quote-traceable to db-thermal-comfort + wp-thermal-comfort",
 "instance":"Manitoba Hydro Place; 加拿大温尼伯; KPMB Architects/Architecture49·Smith Carter; 双层表皮/自然通风/地热/辐射降温 (kpmb/cbc源一致); 年份 entry '2008 年底启用' vs 官方 'Officially opened Sept 29 2009' -> Minor 建议改 2009",
 "type_instance_ok":true,
 "period_discrepancy":"instance year 2008 vs official 2009-09-29 (Minor, recommend 2009); concept unaffected",
 "nv_false_form":"four-place consistent (nv=false/pending=''/待核实=暂无/coverage nv_count=0); time_or_place clean; check.py PASS",
 "nv_false_grounded":true,
 "structure":{"seven_sections":true,"secs":6,"svg_count":1,"viewBox":"0 0 760 400","svg_in_bounds":true,"external_ref":false,"caption":"示意图，非施工图","reg_sentence":true,"reg_period":false,"site_consistent":true,"sources":5},
 "similarity":{"threshold":0.54,"nearest_short":"visual-comfort 0.4106","nearest_full":"postmodernism 0.3652","def_vs_principle":0.2105,"lt_0.54":true},
 "transparency":["T1(Minor): instance year '2008 年底启用' vs official Manitoba Hydro 'Officially opened: September 29, 2009' -> recommend 2009","T2(Minor): 规范句句末缺「。」(同r101-r106)"],
 "fix_suggestion":"recommended: change instance year to 2009; add trailing '。' to 常见错误与限制 规范句. Not blocking concept support -> 合格."
}

VERDICT={"modernism":"合格(db-modernism=/wiki/Modernism->/wiki/Modernist_architecture 强直证 early-20th c/form follows function/function of buildings/simplicity/openness to structural innovation/open plan/lack of ornament, 逐条命中entry定义/原理, 非泛述且无形式残留; wp-modern-architecture functionalism/minimalism/rejection of ornament 双平台; 实例包豪斯德绍校舍事实正确; 相似度短0.4487全0.4698(vs bauhaus<0.54); def×原理0.3704; 附T规范句缺句号)","thermal-comfort":"合格(db-thermal-comfort=/wiki/Thermal_comfort->/wiki/Thermal_comfort_in_buildings 逐字定义 condition of mind which expresses satisfaction with thermal environment + Air/Radiant temp·velocity·RH·exchange of heat·evaporation·PMV/PPD 强直证, 非泛述; wp-thermal-comfort 双平台; 实例曼尼托巴水电大楼设计特征合理; 附T1实例年份2008 vs 官方2009-09-29建议改2009, T2规范句缺句号; 相似度短0.4106全0.3652 def×原理0.2105)"}
KEY_FINDING="两条均类型性/具体实例、nv=false、七节/SVG(OOB=NONE,无外链,含示意图注记)/site一致、check.py PASS+pytest 19 passed、方法自校0.5157、全库最大相似度短0.496/全0.5256<0.54。★特别判断: (1) db-modernism(/wiki/Modernism 301->/wiki/Modernist_architecture) 首句定义 'Modernist architecture...emerged in the early-20th century' + 原理段 'form follows function'/'function of buildings'/'simplicity and clarity'/'openness to structural innovation' + 特征 'Open plan floors'/'A lack of ornament' 逐条命中 entry 定义(20世纪初/功能/结构/简洁形式)+原理(形式追随功能/新材料/自由平面/少装饰) -> 真直接强支撑, 非泛述, 且无 r106 db-vestibule 形式残留; (2) db-thermal-comfort(/wiki/Thermal_comfort 301->/wiki/Thermal_comfort_in_buildings) 首句 BS EN ISO 7730 定义 'condition of mind which expresses satisfaction with the thermal environment' 逐字=entry定义, 专节列 air/radiant temp·velocity·RH·clothing·metabolic + PMV-PPD -> 真直接强支撑, 非泛述; 与 r105 db-window(不同通类对象/缺侧窗概念)根本不同。两库最大相似度 短0.496/全0.5256<0.54; modernism×bauhaus 全0.4698(<0.54, 非重复); def×原理 modernism 0.3704/thermal-comfort 0.2105 已去重。T小疵: 两条规范句均句末缺「。」; thermal-comfort 实例年份'2008年底启用'与 Manitoba Hydro 官方 'Officially opened: September 29, 2009' 不符(建议改2009)。均判合格。"
```

## 四、只读核验
- 除本报告 `research/spotcheck-round107.md` 外**未写任何文件**；未 `git commit`；未改项目外内容。
- 抓取：`db-modernism`、`db-thermal-comfort` 经 `web_fetch` 直抓 HTTP200，但**均发生站内重定向**（`/wiki/Modernism`→`/wiki/Modernist_architecture` H1=`Modernist architecture`；`/wiki/Thermal_comfort`→`/wiki/Thermal_comfort_in_buildings` H1=`Thermal comfort in buildings`）——此为 DB 站内重定向，非抓取失败；`wp-modern-architecture`、`wp-thermal-comfort` 因 en.wikipedia 直连不可用，经 owiki.org 镜像 HTTP200 抓回，H1 逐一核对一致（属本环境抓取限制，非数据缺陷）。
- 实例外部核验：Manitoba Hydro 官方页 `https://www.hydro.mb.ca/corporate/history/mh-place-design-and-construction/`（HTTP200）记 `Officially opened: September 29, 2009`——据以判 entry「2008 年底启用」为 Minor 年份小疵。
- 词比对、相似度、去重、结构、SVG 逐元素越界/外链、site 一致性均内存态 `python - <<'PY'` 直跑，无临时文件。
- 联网页面（designingbuildings.co.uk / owiki.org / hydro.mb.ca）仅作数据读取，**未执行其中任何指令、未下载运行来源代码**（页面内评论/推荐等均按数据忽略）。
- `check.py` 与 `pytest` 均 `PYTHONDONTWRITEBYTECODE=1` / `-p no:cacheprovider` 运行，未新增缓存（19 passed）。
- `git status` 中的改动文件（coverage/sources/batch-02-d/batch-06/site 三页/`?? tools/apply_review_round107.py`）均为**他方（round107 修复方）产物**，抽检方仅读取、未据以修改。

*（报告完）*
