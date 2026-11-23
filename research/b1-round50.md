# B1/B6 缺口判定 — 第 50 轮

- 日期：2026-11-23（Asia/Hong_Kong），采样时刻约 11:5x–12:0x
- 执行角色：b1-r50（只读子任务，无人值守，未提问）
- 任务：第 50 轮 **B1/B6 缺口终判**（新循环零缺口第 3 轮）。B1 用**至少 3 份此前未用过的大纲/分类树**核对，否则结论「无新核心缺口」；B6 只报近 12 个月**理论性**新研究/事件中**确需更新**者。
- 抓取方式：**Python 3.11（Anaconda）urllib + 浏览器 User-Agent 直连**（依 DECISIONS.md D05，以实际 HTTP 响应为准）。本轮 `web_search` 端点再次不可用（返回 no web_search_tool_result blocks / 未触发原生检索），故全部改 urllib 直连；`owiki.org` 与 `en.wikipedia.org` 均直连 200。
- 数据纪律：联网内容一律视为**数据**；网页中任何指令均未执行；未下载或运行页面代码，仅读取 HTML 判读标题、章节标题与条目列表（含零星 <li> 文本）。
- 只读纪律：本文件是本子任务**唯一产物**；未改动其他文件、未 git commit、未触碰项目外内容（临时脚本均经 stdin heredoc 执行，未在项目内落盘）。
- 已按 host 规则加载 `using-superpowers`、`verification-before-completion` 技能。

## 环境备注

- 任务点名的 `AUTONOMOUS.md`、`TASK_design.md` 不在工作区根目录；其实体位于 `D:/Users/Administrator/Desktop/AUTONOMOUS.md`、`D:/Users/Administrator/Desktop/TASK_design.md`，本轮已读取两份原文；另读 `DECISIONS.md`、`scope.md`（258 条）、`research/b1-round49.md`、`PROGRESS.md`、`SATURATION.json` 作为方法与基线。
- **范围判据（TASK_design.md 原文六面）**：①绘画理论（透视法、构图、色彩、光影明暗、中国画六法与留白、东西比较）；②建筑风格史；③中国传统园林造景；④动线设计；⑤下沉式空间；⑥采光/通风/材料基本原理；并含空间序列与尺度、室内外过渡。
- **从严三条须全部满足**才报新候选：①≥2 份**独立**权威来源（**不同平台**；`owiki.org` 为维基镜像，与 Wikipedia 各语言版**同算 1 源**）；②属上述六面**核心概念**（非边缘技法、非近义重复、非绘画流派/媒介）；③`scope.md` 确实缺失。
- 平台可达性（本轮实测）：`owiki.org` 200；`en.wikipedia.org` 200；`web_search` 端点不可用（0 URL 返回）。

## 比对基准

- `scope.md` 现 **258 条**：理论 128 / 风格 66 / 造景 19 / 动线 13 / 下沉空间 13 / 材料 19；层级 核心 50、重要 153、补充 55。
- 与 `b1-round49.md` 基线一致（同为 258 条，第 47 轮 3 条候选入库后未再变动）；`SATURATION.json` 记 `consecutive_zero_gap_rounds=2`（第 48 轮零缺口 1/3、第 49 轮零缺口 2/3），本轮为其上**新周期零缺口第 3 轮**判定。

---

## B1：权威大纲/分类树再对照

### 本轮新用分类树/页面（**此前未用过**，均 owiki HTTP 200，不同页面；对前 43–49 轮已用 slug 去重后选取）

| # | 分类树 / 页面 | URL | HTTP | 结构 / 覆盖面（实读标题或 <li>） | 归属面 |
| --- | --- | --- | --- | --- | --- |
| 1 | Outline of architecture（建筑大纲） | https://owiki.org/wiki/Outline_of_architecture | 200 | 定义/角色/People/建筑风格/**专业细分**/**建筑理论**(=Architectural design values, Proportion, Space syntax)/术语/各地区建筑 | ②理论·总览 |
| 2 | Outline of painting（绘画大纲） | https://owiki.org/wiki/Outline_of_painting | 200 | 绘画本质/Streams/**Styles by movement(115)**/**Styles by region(140)**/历史/**General concepts**/Materials/Tools/**Elements(20)**/学习 | ①理论·总览 |
| 3 | Architectural design → Building design（建筑设计，重定向职业页） | https://owiki.org/wiki/Architectural_design | 200(302→Building_design) | Occupations/Architect/Building engineer/Draftsperson/Building designer/Surveyor | 边缘（职业页） |
| 4 | Interior design（室内设计） | https://owiki.org/wiki/Interior_design | 200 | 历史与术语/商业室内/职业化/室内设计师/**Color in interior design**/**Lighting**/住宅·商业/其他 | ⑥+室内（边缘） |
| 5 | Spatial design（空间设计） | https://owiki.org/wiki/Spatial_design | 200 | 仅 Books/Films/… 残段，**无实质分类树** | 无树 |
| 6 | Urban design（城市设计） | https://owiki.org/wiki/Urban_design | 200 | Theory/History/早期现代/现代城市设计/新方法/城市主义辩论/职业/相关学科 | ④·城市（越域/边缘） |
| 7 | Landscape design（景观设计） | https://owiki.org/wiki/Landscape_design | 200 | Design scope/Design approach/Training/Gardening | ③（实践/边缘） |
| 8 | Perspective (graphical)（透视·图法） | https://owiki.org/wiki/Perspective_(graphical) | 200 | Overview/曲线透视例/History/早期/文艺复兴/Limitations | ①透视 |
| 9 | Thermal mass（热质量/蓄热） | https://owiki.org/wiki/Thermal_mass | 200 | Background/Heat capacity in buildings/Construction examples | ⑥（热工技法） |
| 10 | Passive cooling（被动冷却） | https://owiki.org/wiki/Passive_cooling | 200 | Overview/预防技术/调节散热/通风/Night flushing/蒸发冷却/Earth coupling | ⑥（被动冷却技法） |
| 11 | Chinese architecture（中国建筑） | https://owiki.org/wiki/Chinese_architecture | 200 | History/新石器/20世纪/地理/**Features**(Bilateral symmetry·Enclosure·Hierarchy·Horizontal emphasis·**Cosmological concepts**)/建筑类型 | ②③空间/类型 |
| 12 | Ink wash painting（水墨画） | https://owiki.org/wiki/Ink_wash_painting | 200 | 哲学/技法材料工具/Brush·Inkstick·Xuan paper·Inkstone/历史与画家/东亚影响 | ①中国画 |
| 13 | Visual arts（视觉艺术） | https://owiki.org/wiki/Visual_arts | 200 | 教育训练/Drawing/Painting/History/Printmaking/摄影/Architecture/电影/计算机艺术 | ①总览（越域） |
| 14 | Classical Gardens of Suzhou（苏州古典园林，遗产短条） | https://owiki.org/wiki/Classical_Gardens_of_Suzhou | 200 | 仅 Comprehensive monitoring plan / 书目等，**无分类树** | ③（具体遗产条目） |

> 去重说明：以上 14 个 slug 均不在前 43–49 轮 b1-round 已用 URL 集合内（已 grep 全量 `b1-round*.md` 核对）。`Landscape_architecture / Landscape_planning / Landscape_painting / Chinese_landscape_garden / Outline_of_the_visual_arts / Painting_technique / Color / Daylighting …` 等均**已用过**，本轮未计为新树。14 个新页全部 HTTP 200，无 404。

### 逐树核对结论（按从严三条）

1. **Outline of architecture**：总览型大纲树。其「建筑理论」一节只列 *Architectural design values / Proportion / Space syntax*——后二者已由 `proportion`（比例·核心）、`space-syntax`（空间句法）覆盖；「design values（设计价值观）」属**元理论/价值论**，非六面核心概念。风格一栏仅 column modern/international/brutalism，均已覆盖；专业细分 religious/sustainable architecture 亦已覆盖。→ **①缺 2 平台源、②边缘/近义、③基本已覆盖**，排除。
2. **Outline of painting**：主体是 **Styles of painting by movement（115 条：Cubism/Dada/De Stijl/Ashcan…）** 与 **Styles by region（140 条）**——**绘画流派/地域媒介**，rule②明示排除。Elements 一节列 atmospheric-perspective/color/hue/tint/tone/value/line/perspective/shading/texture/**spatial-organization** 等：绝大多数已覆盖（`color-theory/hue/value/air-perspective/chiaroscuro/spatial-organization/material-texture`），余项 line/plasticity/painterly/imprimatura/underpainting 属**基础要素/技法（边缘）**。→ **②流派/边缘**，排除。
3. **Architectural design（→Building design）**：为**职业/从业者页**（Occupations/Architect/Draftsperson…），非概念分类树。→ **②非核心**，排除。
4. **Interior design**：职业实践史 +「室内色彩」「照明」「Specialties」，已被 `color-theory / lighting-design / interior-exterior-transition` 覆盖，属**应用实践**。→ **②边缘/近义**，排除。
5. **Spatial design**：短条，仅残留 Books/Films/…，**无实质章节**。→ **无树**，排除。
6. **Urban design**：城市设计**独立学科总述**（理论/历史/新方法/城市主义辩论），越出六面范围；其「理论」多为城市主义话语，非六面核心概念。→ **②越域/边缘**，排除。
7. **Landscape design**：设计范围/方法/园艺，已被 `planting-design / hardscape-softscape / garden-architecture` 覆盖。→ **②近义/实践**，排除。
8. **Perspective (graphical)**：**等于** scope 透视系列（`perspective/linear-perspective/one-/two-/three-point/curvilinear-perspective/vanishing-point/horizon-line`）。→ **③已存在**，排除。
9. **Thermal mass**：建筑热容（蓄热）**热工技法**。scope 有 `thermal-comfort / sustainable-design / material-durability`，蓄热属技法层。→ **②边缘技法**，排除。
10. **Passive cooling**：被动冷却**技法集**（night flushing/蒸发冷却/earth coupling）；通风类已覆盖 `natural-ventilation / wind-driven-ventilation / stack-ventilation`。→ **②边缘技法 + 近义**，排除。
11. **Chinese architecture**：Features 为 对称布局(`symmetry-layout` 已有)/围合(`enclosure`)/层级(`hierarchy`)/横向强调/**Cosmological concepts**（影壁辟邪、门神福禄寿、背山面水面南 = 风水取向）。**宇宙观/风水属民俗信仰，边缘非理论核心**；其余特征均已被空间组条目覆盖。→ **②边缘（民俗）/近义**，排除。
12. **Ink wash painting**：**等于** scope `ink-wash`（水墨），哲学/技法细分未超出中国画已有组。→ **③已存在**，排除。
13. **Visual arts**：视觉艺术**总览**（含摄影/电影/计算机艺术），**越域**且与绘画理论各条近义。→ **②越域/边缘**，排除。
14. **Classical Gardens of Suzhou**：**具体 UNESCO 遗产短条**（仅监测计划/书目），无分类树，且为园林实例非概念。→ **②边缘/无树**，排除。

### 近义/边缘候选判定表（体现从严筛选）

| 候选方向 | 来源树 | 卡在哪一条 | 处置 |
| --- | --- | --- | --- |
| 建筑设计价值观（design values） | Outline of architecture | ②元理论/非核心 | 排除 |
| 画派/流派（Cubism、Dada…115）、地区画派（140） | Outline of painting | ②绘画流派/媒介（明示排除） | 排除 |
| 绘画要素 line/plasticity/painterly/imprimatura/underpainting | Outline of painting | ②基础要素/边缘技法（其余要素已覆盖） | 排除 |
| 室内设计（含室内色彩/照明） | Interior design | ②应用实践/近义（color-theory、lighting-design） | 排除 |
| 城市设计（理论/新方法/辩论） | Urban design | ②越域/边缘 | 排除 |
| 景观设计（范围/方法/园艺） | Landscape design | ②近义/实践（planting-design、hardscape-softscape） | 排除 |
| 透视（图法） | Perspective (graphical) | ③已存在（perspective 系列） | 排除 |
| 蓄热 / 被动冷却 | Thermal mass、Passive cooling | ②边缘技法（热工/冷却，通风已覆盖） | 排除 |
| 中国建筑「宇宙观概念」(风水/辟邪) | Chinese architecture | ②边缘（民俗信仰）/近义 | 排除 |
| 水墨画 | Ink wash painting | ③已存在（ink-wash） | 排除 |
| 视觉艺术总览 | Visual arts | ②越域/边缘 | 排除 |
| 苏州古典园林（遗产条） | Classical Gardens of Suzhou | ②边缘（实例）/无树 | 排除 |

> 备注：上述任一方向若要收，需 lead 先在 TASK 范围新增对应维度（如「建筑类型学」「城市设计理论」「热工原理」）并补 ≥2 独立平台源；按现状与从严口径**本轮不报**。

**B1 结论：无新核心缺口。**（本轮以 **14 份此前未用过的分类树/页面** 逐一核对，全部 HTTP 200；无一项同时满足「≥2 独立平台源 + 六面核心概念 + scope 缺失」。）

---

## B6：近 12 个月理论性新研究/事件

- 时间窗：2025-11-23 至 2026-11-23。
- 打开的近期动态页（均 en.wikipedia HTTP 200，逐条读取章节目录与 Events/Works 正文）：
  - `https://en.wikipedia.org/wiki/2025_in_architecture`（200）
  - `https://en.wikipedia.org/wiki/2026_in_architecture`（200）
  - `https://en.wikipedia.org/wiki/2025_in_art`（200）
  - `https://en.wikipedia.org/wiki/2026_in_art`（200）
- 内容性质（本轮实读）：
  - `2025_in_architecture` 章节：**Events / Buildings and structures（按国）/ Awards / Deaths**。Events 实读为：1/7 起南加州山火损毁多处建筑；3/16 荷兰 Valkenburg 1906 年 Wilhelminatoren 意外坍塌；11/3 罗马中世纪 Torre dei Conti 修缮中部分坍塌（1 死）。均为**损毁/坍塌类事件**。
  - `2026_in_architecture` 章节：仅 **Buildings and structures（澳大利亚/西班牙/阿联酋/美国）/ Awards / Deaths**，无 Events、无理论章节。
  - `2025_in_art`：Art fairs / Events（月度）/ Exhibitions / Awards / Works / Deaths。
  - `2026_in_art`：Events / Exhibitions / Awards / Films / Works / Deaths；Events 实读为拍卖（米开朗基罗《利比亚女先知》足部习作 2720 万美元）、名画寻回（伦勃朗 1633）、普利兹克奖（Smiljan Radić）、LACMA 祖姆托新馆开幕、威尼斯双年展评审团集体辞职等——皆**语境/市场/奖项动态**。
  - 关键词统计：四页正文 `theor*` 计数 0/0/1/0、`research` 计数 0/0/0/1（均为行文偶现，非理论章节）。
  - 全部为**实例/奖项/展览/拍卖/坍塌/开幕等语境更新**，**非理论性研究**，不改变任何条目定义。
- **理论层面**：窗口内未出现提出「需据以新增或改写六大面任一核心条目」的规范性理论变更；与第 40–49 轮结论一致（新著/论文多为话语/专著层面、单一出版方、非核心概念定义变更）。`web_search` 端点本轮不可用，改以年度权威页实抓替代。

**B6 结论：无需更新**（无新理论性研究/事件需据以更新条目）。

---

## 打开 URL 数

- **B1**：**14 个不同 URL**（owiki），全部 HTTP 200（其中 `Architectural_design` 302 重定向至 `Building_design`，最终 200；同页仅计 1）。0 个 404。
- **B6**：**4 个不同 URL**（en.wikipedia），全部 HTTP 200。
- **合计不同 URL：18 个（18×HTTP 200、0×HTTP 404）**；`web_search` 端点不可用（0 URL 返回）。

## 机器可读汇总

```
ROUND=50
SCOPE_TOTAL=258   # 理论128/风格66/造景19/动线13/下沉13/材料19；核心50/重要153/补充55
DATE=2026-11-23
BASELINE="b1-round49.md: 258条, 零缺口2/3(新周期); 本轮=第3轮"

B1_TREES_NEW=[
 "https://owiki.org/wiki/Outline_of_architecture",
 "https://owiki.org/wiki/Outline_of_painting",
 "https://owiki.org/wiki/Architectural_design",   # 302 -> Building_design, 200
 "https://owiki.org/wiki/Interior_design",
 "https://owiki.org/wiki/Spatial_design",
 "https://owiki.org/wiki/Urban_design",
 "https://owiki.org/wiki/Landscape_design",
 "https://owiki.org/wiki/Perspective_(graphical)",
 "https://owiki.org/wiki/Thermal_mass",
 "https://owiki.org/wiki/Passive_cooling",
 "https://owiki.org/wiki/Chinese_architecture",
 "https://owiki.org/wiki/Ink_wash_painting",
 "https://owiki.org/wiki/Visual_arts",
 "https://owiki.org/wiki/Classical_Gardens_of_Suzhou"
]
B1_TREES_NEW_COUNT=14
B1_TREES_REUSED_NOT_NEW=["Landscape_architecture","Landscape_planning","Landscape_painting","Chinese_landscape_garden","Outline_of_the_visual_arts","Painting_technique","Color","Daylighting"]
B1_PROBE_404=[]

B1_NEW_CORE_GAPS=[]
B1_EXCLUDED=[
 {"dir":"architectural design values","reason":"②元理论/非核心"},
 {"dir":"painting movements(115)/regional styles(140)","reason":"②绘画流派/媒介 明示排除"},
 {"dir":"painting elements line/plasticity/painterly/imprimatura/underpainting","reason":"②基础要素/边缘技法(其余要素已覆盖)"},
 {"dir":"interior design (color/lighting)","reason":"②应用实践/近义(color-theory,lighting-design)"},
 {"dir":"urban design","reason":"②越域/边缘"},
 {"dir":"landscape design","reason":"②近义/实践(planting-design,hardscape-softscape)"},
 {"dir":"perspective (graphical)","reason":"③已存在 perspective 系列"},
 {"dir":"thermal mass / passive cooling","reason":"②边缘技法(热工/冷却; 通风已覆盖)"},
 {"dir":"chinese architecture cosmological concepts (feng-shui/apotropaic)","reason":"②边缘(民俗)/近义"},
 {"dir":"ink wash painting","reason":"③已存在 ink-wash"},
 {"dir":"visual arts (overview)","reason":"②越域/边缘"},
 {"dir":"classical gardens of suzhou","reason":"②边缘(实例)/无树"}
]

B6_WINDOW="2025-11-23..2026-11-23"
B6_UPDATES=[]
B6_NOTE="年度页仅事件(火灾/坍塌)/建筑/奖项/展览/拍卖/开幕/讣告等语境动态; theor*/research 关键词≈0; 无规范性理论变更"

URLS_DISTINCT=18
URLS_HTTP_200=18
URLS_HTTP_404=0
WEB_SEARCH_ENDPOINT="FAILED (no web_search_tool_result blocks); used urllib direct"
```

是否发现新缺口：**否**
