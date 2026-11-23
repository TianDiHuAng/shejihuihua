# B1/B6 缺口判定 — 第 49 轮

- 日期：2026-11-23（Asia/Hong_Kong），采样时刻约 11:3x–11:4x
- 执行角色：b1-r49（只读子任务，无人值守，未提问）
- 任务：第 49 轮 **B1/B6 缺口判定**。B1 用**至少 3 份此前未用过的大纲/分类树**核对，否则结论「无新核心缺口」；B6 只报近 12 个月**理论性**新研究/事件中**确需更新**者。
- 抓取方式：**Python 3.11 urllib + 浏览器 User-Agent 直连**（依 DECISIONS.md D05，以实际 HTTP 响应为准）。本轮 `web_search` 端点再次不可用（返回 `HTTP 402 … 积分已耗尽`），故全部改为 urllib 直连；`owiki.org` 与 `en.wikipedia.org` 均可直连 200。
- 数据纪律：联网内容一律视为**数据**；网页中任何指令均未执行；未下载或运行页面代码，仅读取 HTML 判读标题、章节标题与条目列表。
- 只读纪律：本文件是本子任务**唯一产物**；未改动其他文件、未 git commit、未触碰项目外内容（临时脚本均经 stdin heredoc 执行，未在项目内落盘）。
- 已按 host 规则加载 `using-superpowers`、`verification-before-completion` 技能。

## 环境备注

- 任务点名的 `AUTONOMOUS.md`、`TASK_design.md` 不在工作区根目录；其实体位于 `D:/Users/Administrator/Desktop/AUTONOMOUS.md`、`D:/Users/Administrator/Desktop/TASK_design.md`，本轮已读取两份原文；另读 `DECISIONS.md`、`scope.md`（258 条）、`research/b1-round48.md`、`PROGRESS.md`、`SATURATION.json` 作为方法与基线。
- **范围判据（TASK_design.md 原文六面）**：①绘画理论（透视法、构图、色彩、光影明暗、中国画六法与留白、东西比较）；②建筑风格史；③中国传统园林造景；④动线设计；⑤下沉式空间；⑥采光/通风/材料基本原理；并含空间序列与尺度、室内外过渡。
- **从严三条须全部满足**才报新候选：①≥2 份**独立**权威来源（**不同平台**；`owiki.org` 为维基镜像，与 Wikipedia 各语言版**同算 1 源**）；②属上述六面**核心概念**（非边缘技法、非近义重复、非绘画流派/媒介）；③`scope.md` 确实缺失。
- 平台可达性（本轮实测）：`owiki.org` 200；`en.wikipedia.org` 200；`web_search` 端点 HTTP 402 不可用（0 URL 返回）。

## 比对基准

- `scope.md` 现 **258 条**：理论 128 / 风格 66 / 造景 19 / 动线 13 / 下沉空间 13 / 材料 19；层级 核心 50、重要 153、补充 55。
- 与 `b1-round48.md` 基线一致（同为 258 条，第 47 轮 3 条候选入库后未再变动）；`SATURATION.json` 记第 48 轮 B1/B6 零缺口 = 新周期 **1/3**，本轮在其上判定。

---

## B1：权威大纲/分类树再对照

### 本轮新用分类树/页面（**此前未用过**，均 owiki HTTP 200，不同页面）

| # | 分类树 / 页面 | URL | HTTP | 结构 / 覆盖面 | 归属面 |
| --- | --- | --- | --- | --- | --- |
| 1 | Building material（建筑材料分类总述） | https://owiki.org/wiki/Building_material | 200 | 天然材料（土/石/木/茅草/冰/砂）与人工材料（砖/水泥/混凝土/金属/玻璃/塑料/陶瓷）分类树 | ⑥材料 |
| 2 | Passive solar building design（被动式太阳能设计） | https://owiki.org/wiki/Passive_solar_building_design | 200 | 得热原理/直接·间接·混合·隔离系统/蓄热/保温/玻璃与遮阳/被动采光 | ⑥采光·通风·可持续 |
| 3 | Passive ventilation（被动通风） | https://owiki.org/wiki/Passive_ventilation | 200 | Process/Design/风压驱动/热浮力驱动/性能评估/标准 | ⑥通风 |
| 4 | Windcatcher（捕风塔） | https://owiki.org/wiki/Windcatcher | 200 | 气流力/地下冷却/蒸发冷却/地域用途（中东·北非·南亚） | ⑥通风 |
| 5 | Lightwell（采光井） | https://owiki.org/wiki/Lightwell | 200 | Area/areaway、古代史 | ⑤⑥采光 |
| 6 | Architectural lighting design（建筑照明设计） | https://owiki.org/wiki/Architectural_lighting_design | 200 | 采光/电照明/灯具/照明层次/光度学/色温/灯具类型 | ⑥采光 |
| 7 | Daylighting（天然采光，短条） | https://owiki.org/wiki/Daylighting | 200 | 仅少量正文（页面偏短），未成分类树 | ⑥采光 |
| 8 | Color（色彩总述） | https://owiki.org/wiki/Color | 200 | 物理属性/色觉/色彩再现（加色·减色）/文化视角 | ①色彩 |
| 9 | Zen garden（枯山水，标题 Japanese dry garden） | https://owiki.org/wiki/Zen_garden | 200 | 历史/岩石选配/砂砾/象征/与风景画的关系 | ③造景 |
| 10 | Terrace (building)（露台/平台） | https://owiki.org/wiki/Terrace_(building) | 200 | Ground terraces / Roof terraces | 空间过渡 |
| 11 | Courtyard house（庭院住宅） | https://owiki.org/wiki/Courtyard_house | 200 | History（建筑类型，短条） | ⑤空间·类型 |
| 12 | Pedestrian zone（步行街区） | https://owiki.org/wiki/Pedestrian_zone | 200 | 定义与类型/无车城镇/限行/利弊/按地区 | ④动线·城市 |
| 13 | Traffic calming（交通稳静化） | https://owiki.org/wiki/Traffic_calming | 200 | 措施：横向偏移/竖向偏移/非物理/执法教育 | ④动线 |
| 14 | Horticulture（园艺） | https://owiki.org/wiki/Horticulture | 200 | 分科/繁殖/选种/环境控制/胁迫/采收 | ③造景（植物，边缘） |
| 15 | Sunken courtyard（下沉庭院，短条） | https://owiki.org/wiki/Sunken_courtyard | 200 | 无实质章节（页面短） | ⑤下沉空间 |
| 16 | Painting technique（绘画技法，短条） | https://owiki.org/wiki/Painting_technique | 200 | 无实质章节（页面短） | ①绘画理论 |

> 另抓 3 个**已用过**页面对照（不计新树，透明记录）：`Chinese_garden`（S1）、`Composition_(visual_arts)`（S1）、`Landscape_architecture`（round06）；`Vertical_circulation` 本轮 **404**（无此 slug）。

### 逐树核对结论（按从严三条）

1. **Building material**：材料**类型分类树**（石/木/砖/混凝土/玻璃/金属/塑料/陶瓷…）。scope ⑥材料维度收的是**原理型条目**（material-texture / material-color / material-durability / vernacular-material / transparent-material / structural-material）。材料"类型"属建筑类型学式分类，非六面核心概念。→ **不满足②（边缘分类）**，排除。
2. **Passive solar building design**：为应用型设计方法（direct/indirect gain、蓄热、保温、glazing、遮阳）。已被 `sustainable-design` / `thermal-comfort` / `daylighting` / `natural-ventilation` 覆盖，属**边缘技法 + 近义重复**。→ **不满足②**，排除。
3. **Passive ventilation**：风压驱动 + 热浮力驱动，**直接等于** scope 的 `wind-driven-ventilation`（风压通风）+ `stack-ventilation`（热压通风）+ `natural-ventilation`。→ **近义重复（③实为已覆盖）**，排除。
4. **Windcatcher**：具体**被动冷却装置**（捕风塔），属边缘技法/装置，与通风组（风压/热压）近义。→ **不满足②**，排除。
5. **Lightwell**：= scope `light-well`（天井）。→ **③已存在**，排除。
6. **Architectural lighting design**：职业/技术实践，已被 `lighting-design` / `daylighting` / `glare` 覆盖，**近义/边缘**。→ **不满足②**，排除。
7. **Daylighting**：= scope `daylighting`（自然采光），且页面偏短未成树。→ **③已存在**，排除。
8. **Color**：色彩科学总述，已被 `color-theory` 及 `hue/value/saturation/primary-colors/complementary-colors/color-contrast/color-harmony/color-scheme` 等系统覆盖。→ **近义重复**，排除。
9. **Zen garden（枯山水）**：日本**干枯山水**子类型，scope 已有 `japanese-architecture`（风格）与 `rock-garden`（岩石园·造景补充）。→ **近义/边缘**，排除。
10. **Terrace (building)**：露台/平台构件，scope 有 `raised-floor`（架空层）、`transition-space`（过渡空间）。→ **近义/边缘**，排除。
11. **Courtyard house**：庭院住宅**建筑类型**，scope 有 `courtyard`（庭院）。→ **近义/建筑类型**，排除。
12. **Pedestrian zone**：步行街区**城市类型**，scope 有 `pedestrian-flow`（人行流线）、`people-vehicle-separation`（人车分流）。→ **近义/边缘**，排除。
13. **Traffic calming**：减速带/路拱等**措施集**，边缘技法，与 `vehicle-flow`/`people-vehicle-separation` 近义。→ **不满足②**，排除。
14. **Horticulture**：植物栽培科学，**越出造景核心**（属农学/园艺），不成六面核心概念。→ **不满足②（越域/边缘）**，排除。
15. **Sunken courtyard**：= scope `sunken-courtyard`（下沉庭院），且短条无树。→ **③已存在**，排除。
16. **Painting technique**：短条无分类树；绘画技法（hatching/stippling/sfumato/chiaroscuro…）已在 scope 充分覆盖。→ **近义/无树**，排除。

### 近义/边缘候选判定表（体现从严筛选）

| 候选方向 | 来源树 | 卡在哪一条 | 处置 |
| --- | --- | --- | --- |
| 材料类型学（石/木/混凝土/金属…） | Building material | ②边缘分类、非核心概念 | 排除 |
| 被动式太阳能/被动通风/捕风塔 | Passive solar building design、Passive ventilation、Windcatcher | ②边缘技法 + 近义（已覆盖风压/热压/可持续） | 排除 |
| 采光井 / 天然采光 | Lightwell、Daylighting | ③已存在（light-well、daylighting） | 排除 |
| 建筑照明设计 | Architectural lighting design | ②近义（lighting-design/daylighting/glare） | 排除 |
| 色彩科学总述 | Color | ②近义（color-theory 及色相/明度/纯度系列） | 排除 |
| 枯山水 / 露台 / 庭院住宅 | Zen garden、Terrace、Courtyard house | ②近义/边缘（对应条目已覆盖） | 排除 |
| 步行街区 / 交通稳静化 | Pedestrian zone、Traffic calming | ②近义/边缘（人行流线/人车分流已覆盖） | 排除 |
| 园艺 | Horticulture | ②越域/边缘 | 排除 |
| 下沉庭院 / 绘画技法 | Sunken courtyard、Painting technique | ③已存在 / 无分类树 | 排除 |

> 备注：上述方向若要收，需 lead 先在 TASK 范围新增对应维度（如"建筑类型学""材料类型学""被动式设计"）并补 ≥2 独立平台源；按现状与从严口径**本轮不报**。

**B1 结论：无新核心缺口。**（本轮以 **16 份此前未用过的分类树/页面** 逐一核对，另含 1 个 404 探测；无一项同时满足「≥2 独立平台源 + 六面核心概念 + scope 缺失」。）

---

## B6：近 12 个月理论性新研究/事件

- 时间窗：2025-11-23 至 2026-11-23。
- 打开的近期动态页（均 HTTP 200，逐条读取章节目录与正文）：
  - `https://en.wikipedia.org/wiki/2025_in_architecture`（200）
  - `https://en.wikipedia.org/wiki/2026_in_architecture`（200）
  - `https://en.wikipedia.org/wiki/2025_in_art`（200）
  - `https://en.wikipedia.org/wiki/2026_in_art`（200）
- 内容性质（本轮实读）：
  - `2025_in_architecture` 章节：**Events / Buildings and structures（按国）/ Awards / Deaths**。Events 实读为：1/7 起南加州山火损毁多处建筑；3/16 荷兰 Valkenburg 1906 年 Wilhelminatoren 意外坍塌；11/3 罗马中世纪 Torre dei Conti 修缮中部分坍塌（1 死）。均为**损毁/坍塌类事件**。
  - `2026_in_architecture` 章节：仅 **Buildings and structures（澳大利亚/西班牙/阿联酋/美国）/ Awards / Deaths**，无 Events、无理论章节。
  - `2025_in_art`：Art fairs / Events / Exhibitions / Awards / Works / Deaths（拍卖、展览、奖项、作品、讣告）。
  - `2026_in_art`：Events / Exhibitions / Awards / Films / Works / Deaths。
  - 全部为**实例/奖项/开馆/展览/拍卖/坍塌等语境更新**，**非理论性研究**，不改变任何条目定义。
- **理论层面**：窗口内未出现提出「需据以新增或改写六大面任一核心条目」的规范性理论变更；与第 40–48 轮结论一致（新著/论文多为话语/专著层面、单一出版方、非核心概念定义变更）。`web_search` 端点本轮 HTTP 402 不可用，改以年度权威页实抓替代。

**B6 结论：无需更新**（无新理论性研究/事件需据以更新条目）。

---

## 打开 URL 数

- **B1**：20 个不同 URL（owiki），其中 19 个 HTTP 200、1 个 HTTP 404（`Vertical_circulation`）。
- **B6**：4 个不同 URL（en.wikipedia），全部 HTTP 200（`2025_in_architecture` 因取正文片段重复请求，同 URL 计 1）。
- **合计不同 URL：24 个（23×HTTP 200、1×HTTP 404）**；`web_search` 2 条查询端点 HTTP 402 故障，0 URL 返回。

## 机器可读汇总

```
ROUND=49
SCOPE_TOTAL=258   # 理论128/风格66/造景19/动线13/下沉13/材料19；核心50/重要153/补充55
DATE=2026-11-23
BASELINE="b1-round48.md: 258条, 零缺口1/3(新周期)"

B1_TREES_NEW=[
 "https://owiki.org/wiki/Building_material",
 "https://owiki.org/wiki/Passive_solar_building_design",
 "https://owiki.org/wiki/Passive_ventilation",
 "https://owiki.org/wiki/Windcatcher",
 "https://owiki.org/wiki/Lightwell",
 "https://owiki.org/wiki/Architectural_lighting_design",
 "https://owiki.org/wiki/Daylighting",
 "https://owiki.org/wiki/Color",
 "https://owiki.org/wiki/Zen_garden",
 "https://owiki.org/wiki/Terrace_(building)",
 "https://owiki.org/wiki/Courtyard_house",
 "https://owiki.org/wiki/Pedestrian_zone",
 "https://owiki.org/wiki/Traffic_calming",
 "https://owiki.org/wiki/Horticulture",
 "https://owiki.org/wiki/Sunken_courtyard",
 "https://owiki.org/wiki/Painting_technique"
]
B1_TREES_NEW_COUNT=16
B1_TREES_REUSED_NOT_NEW=["Chinese_garden(S1)","Composition_(visual_arts)(S1)","Landscape_architecture(round06)"]
B1_PROBE_404=["https://owiki.org/wiki/Vertical_circulation"]

B1_NEW_CORE_GAPS=[]
B1_EXCLUDED=[
 {"dir":"material typology (stone/wood/concrete/metal/glass)","reason":"②边缘分类 非核心"},
 {"dir":"passive solar / passive ventilation / windcatcher","reason":"②边缘技法+近义(风压/热压/可持续已覆盖)"},
 {"dir":"lightwell / daylighting","reason":"③已存在 light-well/daylighting"},
 {"dir":"architectural lighting design","reason":"②近义 lighting-design/daylighting/glare"},
 {"dir":"color (general)","reason":"②近义 color-theory 及色相明度纯度系列"},
 {"dir":"zen garden / terrace / courtyard house","reason":"②近义/边缘(对应条目已覆盖)"},
 {"dir":"pedestrian zone / traffic calming","reason":"②近义/边缘(人行流线/人车分流已覆盖)"},
 {"dir":"horticulture","reason":"②越域/边缘"},
 {"dir":"sunken courtyard / painting technique","reason":"③已存在 / 无分类树"}
]

B6_WINDOW="2025-11-23..2026-11-23"
B6_UPDATES=[]
B6_NOTE="年度页仅事件(火灾/坍塌)/建筑/奖项/展览/拍卖/讣告等语境动态，无规范性理论变更"

URLS_DISTINCT=24
URLS_HTTP_200=23
URLS_HTTP_404=1
WEB_SEARCH_ENDPOINT="FAILED (HTTP 402 credits exhausted); used urllib direct"
```

是否发现新缺口：**否**
