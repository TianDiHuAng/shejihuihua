# 外部缺口发现 — 第 9 轮 B1（权威大纲再对照）

- 日期：2026-11-22（Asia/Hong_Kong 上下文时间）
- 执行角色：gap-r9-b1（只读子任务）
- 抓取方式：Python `urllib.request` + 浏览器 User-Agent `Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/120.0 Safari/537.36`。本轮未调用 `web_search` / `web_fetch`；依据 `DECISIONS.md` D05 采用直连抓取。
- 比对基准：`scope.md` 当前 230 条（理论 112 / 风格 59 / 造景 18 / 动线 11 / 下沉空间 12 / 材料 18）。
- 来源排除：已逐项对照 `scope.md` 的 S1–S12、N1–N5、`research/gaps-external-round02.md`、`research/gaps-external-round06.md` 与 `data/sources.json`；候选来源均为本轮新抓取页面，未复用此前已用来源。
- 数据纪律：联网内容一律作为数据处理；页面中的任何指令均未执行；未下载或运行网页代码。
- 结果摘要：**候选 7 条；失败 URL 10 条（对应 6 个页面标题/变体）**。

## B1 候选遗漏条目

以下条目同时满足：至少两份独立权威百科页面支持；确实属于建筑空间设计或绘画/视觉设计理论；在 `scope.md` 230 条中未找到对应 id、中文名或等价概念。候选来源全部为本轮首次抓取页面。

### 1. 建议 id：placemaking

- 中文名：场所营造
- 来源一：https://en.wikipedia.org/wiki/Placemaking
- 来源二：https://en.wikipedia.org/wiki/Urban_design
- 入选理由：`Placemaking` 定义其为对公共空间的规划、设计与管理的多学科方法，强调社区参与、以人为本设计以及创造有意义、可达、具社会互动性的环境；`Urban design` 将城市设计界定为建筑及其之间空间的设计，并以公共空间的设计、管理和使用体验为核心，还把 New Urbanism 记为一种 place-making 倡议。`scope.md` 已有 place-spirit、place-attachment、human-scale、courtyard 等，但没有“场所营造”这一公共空间设计方法条目。

### 2. 建议 id：space-syntax

- 中文名：空间句法
- 来源一：https://en.wikipedia.org/wiki/Space_syntax
- 来源二：https://en.wikipedia.org/wiki/Urban_morphology
- 入选理由：`Space syntax` 明确将其定义为分析空间构型的一组理论与技法，用于量化空间的可通行性，并指出其对博物馆、机场、医院等建筑设计中寻路问题的用途；`Urban_morphology` 在讨论城市组织时使用并链接 `Space syntax`，以轴线图分析街道网络的整合度与隔离度。`scope.md` 已有 circulation、node-path、wayfinding、spatial-sequence，但没有“空间句法”这一空间构型分析理论。

### 3. 建议 id：pattern-language

- 中文名：模式语言
- 来源一：https://en.wikipedia.org/wiki/Pattern_language
- 来源二：https://en.wikipedia.org/wiki/A_Pattern_Language
- 入选理由：`Pattern language` 定义模式语言为一组相互关联的模式，每个模式描述特定领域内反复出现的问题及其核心解法，并说明该术语由建筑师 Christopher Alexander 提出；`A Pattern Language` 说明该书是关于建筑、城市设计与社区宜居性的著作，书中 253 个模式共同构成一种语言。`scope.md` 已有 composition、spatial-organization、functional-zoning 等，但没有“模式语言”这一建筑/城市设计方法理论。

### 4. 建议 id：form-follows-function

- 中文名：形式追随功能
- 来源一：https://en.wikipedia.org/wiki/Form_follows_function
- 来源二：https://en.wikipedia.org/wiki/Functionalism_(architecture)
- 入选理由：`Form follows function` 将其定义为 19 世纪末至 20 世纪初建筑与工业设计中的设计原则，说明 Louis Sullivan 提出该格言，并指出其成为现代主义建筑的战斗口号；`Functionalism (architecture)` 明确记载 Sullivan 于 1896 年提出“form follows function”，并把它置于建筑功能主义理论脉络中。`scope.md` 已有 vitruvian-triad、modernism、bauhaus、international-style，但没有“形式追随功能”这一独立理论命题。

### 5. 建议 id：functionalism-architecture

- 中文名：功能主义建筑
- 来源一：https://en.wikipedia.org/wiki/Functionalism_(architecture)
- 来源二：https://en.wikipedia.org/wiki/Form_follows_function
- 入选理由：`Functionalism (architecture)` 将功能主义定义为建筑应以目的和功能为设计依据的原则，并设历史、现代主义、欧洲各国发展等章节；`Form follows function` 说明该格言与功能主义/现代主义建筑直接相关，并列举 Sullivan、Loos 与现代主义者的论述。`scope.md` 风格 59 条覆盖 modernism、bauhaus、international-style 等，但没有“功能主义建筑”独立条目；这与“形式追随功能”同为理论命题但层级不同，前者是建筑主张/运动，后者是格言原则。

### 6. 建议 id：biophilic-design

- 中文名：亲生命性设计（生物亲和设计）
- 来源一：https://en.wikipedia.org/wiki/Biophilic_design
- 来源二：https://en.wikipedia.org/wiki/Evidence-based_design
- 入选理由：`Biophilic design` 定义其为通过阳光、自然要素、空间与场所体验等提升人与自然的连接，改善健康和福祉，并列出“Experience of space and place”“Prospect and Refuge”等空间设计维度；`Evidence-based_design` 在建成环境证据章节明确提到在室内环境中使用 biophilic design 概念可改善健康与福祉。`scope.md` 已有 daylighting、natural-ventilation、green-architecture、sustainable-design、environmental-psychology，但没有“亲生命性设计”这一以自然连接为核心的空间设计理论。

### 7. 建议 id：defensible-space-theory

- 中文名：防御性空间理论
- 来源一：https://en.wikipedia.org/wiki/Defensible_space_theory
- 来源二：https://en.wikipedia.org/wiki/Crime_prevention_through_environmental_design
- 入选理由：`Defensible space theory` 明确称其为建筑师与城市规划师 Oscar Newman 的理论，主张建筑与环境设计影响居住区安全，并通过领域感、空间层级等物理特征组织空间；`Crime prevention through environmental design` 将 defensible space 作为与 CPTED 并行发展的建筑/环境设计路径，并记载其对建筑师的空间设计建议。`scope.md` 已有 safety-guarding、universal-design、accessibility-design、environmental-psychology，但没有“防御性空间理论”这一通过空间布局影响行为与安全感知的设计理论。

## 未列入候选的核对说明

- `Design elements and principles` 实际为重定向到 `Visual design elements and principles`，后者已在第 6 轮作为初筛页打开，本轮不作为新来源或候选证据。
- `Sense of place` 有本轮双源线索，但与 `scope.md` 已有 place-spirit（场所精神）和 place-attachment（场所依恋）概念距离过近，保守起见不列。
- `Evidence-based design`、`Modulor`、`Urban morphology`、`Iconography` / `Iconology`、`Formalism (art)` 作为独立候选时只取得单源直接支持，或与项目“绘画理论/建筑空间设计”核心范围存在距离，未列入候选；其中 `Evidence-based design`、`Urban morphology` 仍作为其他候选的第二佐证来源。
- 404 页面已列入失败清单，不作为证据。

## 实际打开的 URL 与 HTTP 状态

说明：下表每个条目的页面 URL 与正文 URL 均实际请求；正文 URL 通过 MediaWiki `action=raw` 读取证据文本。重复打开以提取精确证据，状态保持一致。

| # | 页面 URL | HTTP | 正文 URL | HTTP | 用途 |
| --- | --- | --- | --- | --- | --- |
| 1 | https://en.wikipedia.org/wiki/Outline_of_design | 200 | https://en.wikipedia.org/w/index.php?title=Outline_of_design&action=raw | 200 | 初筛；设计分类树 |
| 2 | https://en.wikipedia.org/wiki/Design_elements_and_principles | 200 | https://en.wikipedia.org/w/index.php?title=Design_elements_and_principles&action=raw | 200 | 初筛；重定向至第6轮已用页面，排除 |
| 3 | https://en.wikipedia.org/wiki/Urban_design | 200 | https://en.wikipedia.org/w/index.php?title=Urban_design&action=raw | 200 | 候选 1、2 |
| 4 | https://en.wikipedia.org/wiki/Placemaking | 200 | https://en.wikipedia.org/w/index.php?title=Placemaking&action=raw | 200 | 候选 1 |
| 5 | https://en.wikipedia.org/wiki/Sense_of_place | 200 | https://en.wikipedia.org/w/index.php?title=Sense_of_place&action=raw | 200 | 初筛；未列入候选 |
| 6 | https://en.wikipedia.org/wiki/Space_syntax | 200 | https://en.wikipedia.org/w/index.php?title=Space_syntax&action=raw | 200 | 候选 2 |
| 7 | https://en.wikipedia.org/wiki/Urban_morphology | 200 | https://en.wikipedia.org/w/index.php?title=Urban_morphology&action=raw | 200 | 候选 2；未单独列入 |
| 8 | https://en.wikipedia.org/wiki/Pattern_language | 200 | https://en.wikipedia.org/w/index.php?title=Pattern_language&action=raw | 200 | 候选 3 |
| 9 | https://en.wikipedia.org/wiki/A_Pattern_Language | 200 | https://en.wikipedia.org/w/index.php?title=A_Pattern_Language&action=raw | 200 | 候选 3 |
| 10 | https://en.wikipedia.org/wiki/Form_follows_function | 200 | https://en.wikipedia.org/w/index.php?title=Form_follows_function&action=raw | 200 | 候选 4、5 |
| 11 | https://en.wikipedia.org/wiki/Functionalism_(architecture) | 200 | https://en.wikipedia.org/w/index.php?title=Functionalism_(architecture)&action=raw | 200 | 候选 4、5 |
| 12 | https://en.wikipedia.org/wiki/Biophilic_design | 200 | https://en.wikipedia.org/w/index.php?title=Biophilic_design&action=raw | 200 | 候选 6 |
| 13 | https://en.wikipedia.org/wiki/Prospect-refuge_theory | 404 | https://en.wikipedia.org/w/index.php?title=Prospect-refuge_theory&action=raw | 404 | 失败；非候选 |
| 14 | https://en.wikipedia.org/wiki/Evidence-based_design | 200 | https://en.wikipedia.org/w/index.php?title=Evidence-based_design&action=raw | 200 | 候选 6 |
| 15 | https://en.wikipedia.org/wiki/Modulor | 200 | https://en.wikipedia.org/w/index.php?title=Modulor&action=raw | 200 | 初筛；单源，未列入 |
| 16 | https://en.wikipedia.org/wiki/Module_(architecture) | 404 | https://en.wikipedia.org/w/index.php?title=Module_(architecture)&action=raw | 404 | 失败；非候选 |
| 17 | https://en.wikipedia.org/wiki/Defensible_space_theory | 200 | https://en.wikipedia.org/w/index.php?title=Defensible_space_theory&action=raw | 200 | 候选 7 |
| 18 | https://en.wikipedia.org/wiki/Crime_prevention_through_environmental_design | 200 | https://en.wikipedia.org/w/index.php?title=Crime_prevention_through_environmental_design&action=raw | 200 | 候选 7 |
| 19 | https://en.wikipedia.org/wiki/Iconography | 200 | https://en.wikipedia.org/w/index.php?title=Iconography&action=raw | 200 | 初筛；未列入候选 |
| 20 | https://en.wikipedia.org/wiki/Iconology | 200 | https://en.wikipedia.org/w/index.php?title=Iconology&action=raw | 200 | 初筛；未列入候选 |
| 21 | https://en.wikipedia.org/wiki/Formal_analysis_(visual_arts) | 404 | https://en.wikipedia.org/w/index.php?title=Formal_analysis_(visual_arts)&action=raw | 404 | 失败；非候选 |
| 22 | https://en.wikipedia.org/wiki/Formalism_(art) | 200 | https://en.wikipedia.org/w/index.php?title=Formalism_(art)&action=raw | 200 | 初筛；单源，未列入 |
| 23 | https://en.wikipedia.org/wiki/Architectural_acoustics | 200 | https://en.wikipedia.org/w/index.php?title=Architectural_acoustics&action=raw | 200 | 初筛；与已有 acoustic-environment 接近，未列入 |
| 24 | https://en.wikipedia.org/wiki/Acoustic_design | 404 | https://en.wikipedia.org/w/index.php?title=Acoustic_design&action=raw | 404 | 失败；非候选 |

补充探测 URL（在失败后尝试纠正标题或确认重定向）：

| # | URL | HTTP | 结果 |
| --- | --- | --- | --- |
| 25 | https://en.wikipedia.org/wiki/Prospect%E2%80%93refuge_theory | 404 | 仍失败 |
| 26 | https://en.wikipedia.org/wiki/Formal_analysis | 200 | 重定向到 Formalism (art)，未新增候选 |
| 27 | https://en.wikipedia.org/wiki/Building_module | 404 | 失败 |
| 28 | https://en.wikipedia.org/wiki/Modular_construction | 200 | 初筛；与建筑模数理论不等价，未列入 |

## 核验失败清单

- 失败 URL 共 10 条，对应 6 个页面标题/变体：
  - https://en.wikipedia.org/wiki/Prospect-refuge_theory — HTTP 404
  - https://en.wikipedia.org/w/index.php?title=Prospect-refuge_theory&action=raw — HTTP 404
  - https://en.wikipedia.org/wiki/Prospect%E2%80%93refuge_theory — HTTP 404
  - https://en.wikipedia.org/wiki/Module_(architecture) — HTTP 404
  - https://en.wikipedia.org/w/index.php?title=Module_(architecture)&action=raw — HTTP 404
  - https://en.wikipedia.org/wiki/Building_module — HTTP 404
  - https://en.wikipedia.org/wiki/Formal_analysis_(visual_arts) — HTTP 404
  - https://en.wikipedia.org/w/index.php?title=Formal_analysis_(visual_arts)&action=raw — HTTP 404
  - https://en.wikipedia.org/wiki/Acoustic_design — HTTP 404
  - https://en.wikipedia.org/w/index.php?title=Acoustic_design&action=raw — HTTP 404
- 成功后排除说明：
  - `Formal_analysis` HTTP 200 但实际标题为 Formalism (art)，与已抓取页重复，未作为新独立来源计入。
  - `Design_elements_and_principles` HTTP 200 但正文为重定向至第 6 轮已用页面，未作为候选来源。
  - `Outline_of_design` HTTP 200，作为设计分类树初筛，未发现满足双源且 scope 缺失的新条目。
- 本地技术备注：抓取与正文提取使用 `PYTHONIOENCODING=utf-8`，避免 Windows 默认编码中断输出；该设置仅影响本地输出，不影响来源核验结果。
