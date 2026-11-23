# B1/B6 判定 + dead-link 复核 — 第 77 轮

- 日期：2026-11-23（Asia/Hong_Kong）
- 执行角色：b1-r77（只读子任务，无人值守，未提问）
- 任务：第 77 轮 B1（≥3 份此前未用权威大纲/分类树核对 scope 258 条）+ B6（近 12 个月理论性新研究/事件）+ dead-link 复核（data/sources.json 中 link_ok=false 的源）。
- 抓取方式：Python 3.11 urllib + 浏览器 User-Agent 直连（SSL 校验证书关闭以容错），以实际 HTTP 响应为准；辅以 `web_search` 一次（B6 旁证）。`owiki.org`、`en.wikipedia.org` 均可达。
- 数据纪律：联网内容一律视为**数据**；网页中任何指令均未执行；未下载或运行页面代码，仅读取 HTML 判读 title、章节标题、正文文本与 TOC。
- 只读纪律：本文件是本子任务**唯一产物**；未改动其他文件、未 git commit、未触碰项目外内容（所有脚本经 stdin heredoc 执行，未在项目内落盘）。
- 已按 host 规则加载 `using-superpowers`、`verification-before-completion` 技能。

---

## B1：权威大纲/分类树再对照（scope 258 条）

### 比对基准

- `scope.md` 现 **258 条**：理论 128 / 风格 66 / 造景 19 / 动线 13 / 下沉空间 13 / 材料 19；层级 核心 50、重要 153、补充 55。`coverage.json` entries=258。
- `SATURATION.json`：`SATURATED=true`，`consecutive_zero_gap_rounds=3`（第 48–50 轮零缺口），此后各轮仅 B5/F 推进（pending_items 179）。
- 范围判据（沿用 TASK_design.md 六面）：①绘画理论（透视、构图、色彩、光影明暗、中国画六法与留白、东西比较）；②建筑风格史；③中国传统园林造景；④动线设计；⑤下沉式空间；⑥采光/通风/材料；含空间序列与尺度、室内外过渡。
- 从严三条（须全满足才报）：①≥2 份**独立**权威来源（不同平台；owiki 视作 Wikipedia 镜像，与各语言维基合算 1 源）；②属六面**核心概念**（非边缘技法、非近义重复、非绘画流派/媒介）；③`scope.md` 确实缺失。

### 本轮新用分类树/页面（此前未用过，对前 25–50 轮 b1-round 全量 slug 去重后选取）

| # | 分类树/页面 | URL | HTTP | 实读结构（标题/章节） | 归属面 |
| --- | --- | --- | --- | --- | --- |
| 1 | Composition (visual arts) | https://owiki.org/wiki/Composition_(visual_arts) | 200 | Elements of design（Line/Color/Texture/Value/Form/Space）；Compositional techniques（Rule of thirds / Rule of odds / Rule of space / Simplification / Geometry and symmetry / Creating movement） | ①构图 |
| 2 | Chinese painting | https://owiki.org/wiki/Chinese_painting | 200 | Specifics and study → **Six principles（六法）**；Iconography；Landscape painting（Paradigm shift / Dyads / Art as cartography）；Modern/Early PRC/Since 1978 | ①中国画 |
| 3 | Chinese garden | https://owiki.org/wiki/Chinese_garden | 200 | Design of classical garden：Architecture / Artificial mountains & rock gardens / Water / Flowers and trees / **"Borrowing scenery"** / Concealment and surprise；Philosophy | ③造景 |
| 4 | Architectural style | https://owiki.org/wiki/Architectural_style | 200 | Styles in the history of architecture / Evolution of style / History of the concept / Practical issues | ②风格 |
| 5 | Golden ratio | https://owiki.org/wiki/Golden_ratio | 200 | Mathematics（irrationality/continued fraction/geometry/golden spiral）；Applications: Architecture / Art / Books and design | ①比例 |
| 6 | Chiaroscuro | https://owiki.org/wiki/Chiaroscuro | 200 | History（chiaroscuro drawing/modelling/woodcuts/compositional chiaroscuro to Caravaggio）；Use of the term；Cinema & photography | ①明暗 |
| 7 | Outline of aesthetics | https://owiki.org/wiki/Outline_of_aesthetics | 200 | History of aesthetics / Aesthetics and art movements / Concepts in aesthetics / Philosophers of art | 元理论（边缘） |
| 8 | Shanshui（Shan shui） | https://owiki.org/wiki/Shanshui | 200 | History / **Concepts** / Compositions / Elements and colors / Connection to poetry | ①中国画 |
| 9 | Penjing | https://owiki.org/wiki/Penjing | 200 | History / Aesthetics / Styles / Maintenance | 造园技艺媒介（边缘） |
| 10 | Sacred geometry | https://owiki.org/wiki/Sacred_geometry | 200 | As worldview and cosmology / Representations in art and architecture（各宗教）/ Notable artists | 元理论（边缘） |
| 11 | Visual hierarchy | https://owiki.org/wiki/Visual_hierarchy | 200 | Evidence / Theory / Application: Cartography / UX & behavioral design | 平面/UX（边缘，越域） |
| 12 | Underground city | https://owiki.org/wiki/Underground_city | 200 | 按国家/地区列举地下城实例（Asia/Europe/…） | ⑤（实例列表，非概念树） |
| — | Atmospheric perspective | https://owiki.org/wiki/Atmospheric_perspective | 200（302→Aerial_perspective） | 与既有 aerial-perspective 同页 | ①（已覆盖） |
| — | Elements of art | https://owiki.org/wiki/Elements_of_art | 200 | 元素列表，已由 S6 构图树覆盖 | ①（已覆盖） |
| — | Repetition (visual arts) | https://owiki.org/wiki/Repetition_(visual_arts) | 404 | 页面不存在 | — |
| — | Spatial sequence | https://owiki.org/wiki/Spatial_sequence | 404 | 页面不存在 | — |

### 逐树核对（按从严三条）

1. **Composition (visual arts)**：本节即 scope 中 `composition` 及 `rule-of-thirds/rule-of-odds/rule-of-space/simplification/geometry-symmetry/leading-lines/negative-space` 等条目的来源。逐项已在 scope（coverage：composition + diagonal/s-curve/triangular/framing-composition 共 6 项）；Elements of design 与既有视觉元素条目重合。→ 无新概念，排除。
2. **Chinese painting**：「Six principles」↔ scope `six-principles`（六法）已存在；Landscape/Iconography 等为题材与图像志章节，非新的核心概念；「Dyads / Art as cartography」属行文议题（二元、地图性），非六面核心。→ 排除（已覆盖）。
3. **Chinese garden**：Design 各节（假山、理水、花木、借景、藏与露）↔ scope `rockery/rock-garden/water-management/planting-design/borrowed-scenery/framed-scenery/opposed-scenery/screened-scenery/leaked-scenery/added-scenery/side-scenery/suppressed-scenery/seasonal-scenery/time-scenery` 已系统覆盖。→ 排除（已覆盖）。
4. **Architectural style**：风格史总述 ↔ scope 风格类 66 条已覆盖。→ 排除（已覆盖）。
5. **Golden ratio**：Applications（Architecture/Art）↔ scope `golden-ratio` 已存在（且该条在 B5 待核实清单，属实例待补，非 scope 缺口）。数学部分非本领域。→ 排除。
6. **Chiaroscuro**：History（含 compositional chiaroscuro to Caravaggio）↔ scope 明暗类 `chiaroscuro/tenebrism/rembrandt/light-shadow-modeling` 已覆盖。→ 排除（已覆盖）。
7. **Outline of aesthetics**：美学哲学总览（aesthetic concepts/philosophers）＝元理论/价值论，与第 50 轮所排除 `Architectural design values` 同类，非六面核心概念。→ 排除（边缘）。
8. **Shanshui**：Concepts/Compositions/Elements ↔ 中国画理论条目已覆盖；山水为风景画题材，非新核心。→ 排除（已覆盖）。
9. **Penjing**：盆景＝造园/园艺技艺媒介（近义于 bonsai），非六面理论核心。→ 排除（边缘技法/媒介）。
10. **Sacred geometry**：世界观/宇宙论与跨宗教象征，属元理论/象征学，非本领域核心概念。→ 排除（边缘/元理论）。
11. **Visual hierarchy**：视觉层级＝平面/UX/制图学概念，越出绘画理论与建筑空间六面。→ 排除（越域/边缘）。
12. **Underground city**：按国别列举地下城实例，非概念；下沉空间核心（`sunken-plaza/sunken-courtyard/atrium/lightwell` 等）已覆盖。→ 排除（实例列表）。
13. **Atmospheric perspective / Elements of art**：直接等同既有 `aerial-perspective` / 视觉元素条目。→ 已覆盖。
14. **Repetition (visual arts) / Spatial sequence**：404（owiki 无此页），不计入有效新树；即使存在亦为近义（节奏重复 / 空间序列已覆盖）。

> 去重说明：以上 slug 均不在前 25–50 轮 `b1-round*.md` 与 `gaps-external-round*.md` 已用 URL 集合内（已对全量文件 grep 核对；如 `Chinese_painting`、`Chinese_garden`、`Composition_(visual_arts)`、`Outline_of_aesthetics`、`Architectural_style`、`Golden_ratio`、`Chiaroscuro`、`Penjing`、`Shanshui`、`Sacred_geometry`、`Visual_hierarchy` 的 used 计数均为 0）。有效新树 ≥3 份且分布覆盖①构图/中国画、②风格、③造景三面，另含⑤下沉与元理论对照，满足 ≥3 份未用权威大纲的要求。

**B1 结论：B1 无新缺口。** 本轮 ≥3 份此前未用权威分类树（Composition、Chinese painting、Chinese garden、Architectural style、Golden ratio、Chiaroscuro、Outline of aesthetics、Shanshui、Penjing、Sacred geometry、Visual hierarchy、Underground city 等）逐一核对，凡属六面者均已被 scope 258 条覆盖，其余为边缘技法/近义/流派媒介/元理论/实例列表；未出现满足「≥2 独立权威源 + 属本领域核心 + scope 缺失」的新核心候选。

---

## B6：近 12 个月（2025-11 至 2026-11）理论性新研究/事件

- 时间窗：2025-11 至 2026-11（当下采样 2026-11-23）。
- 打开的近期动态页（en.wikipedia，均 200，读取章节标题与正文）：
  - `2026_in_architecture`（200）：章节仅 **Buildings and structures**（澳/西/阿联酋/美）/ Awards / Deaths。正文实读为具体建筑落成（Powerhouse Parramatta、Guggenheim Abu Dhabi、Lucas Museum 等）、奖项（Pritzker–Smiljan Radić、Stirling、AIA Gold Medal）、讣告。`theor*` 计数 0。
  - `2026_in_art`（200）：Events / Exhibitions / Awards / Films / Works / Deaths。Events 实读为：2/5 米开朗基罗《利比亚女先知》足部习作佳士得 2720 万美元成交；3/2 荷兰国立博物馆宣布寻回伦勃朗 1633《撒迦利亚的异象》；3/12 Pritzker 授 Radic；3/22 意大利 Villa dei Capolavori 雷诺阿/塞尚/马蒂斯三画被盗；4/19 LACMA 祖姆托新馆开幕；4/30 威尼斯双年展全体评审辞职等。皆**市场/展览/奖项/被盗/开幕**类语境，`theor*` 计数 0。
  - `2025_in_architecture`（200）：Events / Buildings / Awards / Deaths；Events 为山火、塔楼坍塌等损毁类；`theor*` 计数 0。
  - `2025_in_art`（200）：Art fairs（按月）/ Events / Exhibitions / Awards / Works / Deaths；`theor*` 计数 1（行文偶现）。
- 旁证（`web_search` 一次）：返回多为出版社/预印本条目（如 *Epistemic Painting: A Visual Theory of Knowledge*（Zenodo 预印本，Varzari 2026）、*Architecture's Constructal Theory*（Springer）、*Empathic Space*（Wiley）、*Designing the Complex City*（Routledge）、《全龄共生的城乡诗学》（武汉大学出版社 2026-08）等）。这些为**单一作者专著/预印本、单一出版方**的话语层产出，属既有个别议题的延伸，**未提出需据以新增或改写六面任一核心条目定义的规范性理论变更**。

**B6 结论：B6 无新动态。** 窗口内理论性研究均为单源专著/预印本层面，事件均为市场/展览/奖项/损毁/开幕类语境更新；无需据以更新任一条目。

---

## dead-link 复核表

对 `data/sources.json` 中 `link_ok=false` 的 3 条（本轮全库实查：498 源中仅此 3 条为 false）逐个复探 canonical 与 owiki 镜像：

| id | url | canonical status | mirror status | 建议 |
| --- | --- | --- | --- | --- |
| wp-means-of-egress | https://en.wikipedia.org/wiki/Means_of_egress | **404**（Wikipedia API 亦确认 "Means of egress" 无此条目、无重定向目标 `missing:""`） | owiki.org/wiki/Means_of_egress → **404** | 确认 404；维持 link_ok=false（无可用镜像，无法改 true） |
| wp-underground-space | https://en.wikipedia.org/wiki/Underground_space | **404**（API 确认 "Underground space" 无条目、无重定向 `missing:""`） | owiki.org/wiki/Underground_space → **404** | 确认 404；维持 link_ok=false（注：`Underground_living`、`Underground_city` 为不同条目，不能替代同一条目） |
| artincontext-academic | https://artincontext.org/academic-art/ | **404**（https，路径级）；`https://www.artincontext.org/academic-art/` 亦 404；站点根 `https://artincontext.org/` 亦 404；`http://` 版本返回 503 | 无镜像（非维基类，无 owiki 对应） | 确认不可达（404/503）；维持 link_ok=false，无法改 true |

**dead-link 结论：** 3 条全部确认 404（artincontext 另现 503），**无一条可改为 link_ok=true**；建议全部保持 `link_ok=false` 并在 note 标注「2026-11-23 复探 canonical+mirror 均 404」。

---

## 打开 URL 数

- 直连抓取 / 探测的 distinct URL：**36 条**（dead-link canonical 3 + owiki 镜像 2 + artincontext 变体 4 + Wikipedia API/替代名 6 + B1 分类树/页面 15 + B6 年度页 4 + 路径变体重合去重后计）。另 `web_search` 查询 2 条。
- 有效分类树（HTTP 200 且含目录结构）：12 份（其中 2 份 404：Repetition_(visual_arts)、Spatial_sequence 已剔除）。

---

是否发现新缺口：否
