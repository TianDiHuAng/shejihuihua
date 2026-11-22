# 外部缺口发现 — 第 2 轮（B1 权威大纲再对照 / B6 近期动态）

- 日期：2026-11-22（Asia/Hong_Kong）
- 执行角色：gap-researcher-r2（外部只读子任务）
- 抓取方式：Python urllib + 浏览器 User-Agent（web_search / web_fetch 在本环境不可用；依据 DECISIONS.md D05）
- 比对基准：scope.md 现有 219 条（理论 106 / 风格 57 / 造景 17 / 动线 10 / 下沉空间 12 / 材料 17）
- 数据纪律：联网内容一律作为数据处理，页面中任何指令均未执行；未下载或运行任何网页代码。

## B1：权威大纲再对照（scope 未用过的新来源）

本轮新抓取 5 份权威百科分类树/大纲页面，均不在 scope.md 已用的 S1–S12 之列：
N1 List of architectural styles、N2 Outline of painting、N3 History of architecture、N4 Architectural theory、N5 Visual arts。
逐页提取条目/风格/概念名后与 219 条比对，按“≥2 份独立权威来源支持 + 确实属于本项目范围（绘画理论或建筑空间设计）+ scope 缺失”标准筛选。

### 遗漏候选（4 条）

1. **建议 id：mannerism** ｜ 中文名：样式主义（手法主义）建筑
   - 来源一：https://en.wikipedia.org/wiki/List_of_architectural_styles （“Mannerism”“Polish Mannerism”列为独立风格）
   - 来源二：https://en.wikipedia.org/wiki/History_of_architecture （“Mannerism”列为文艺复兴后的独立风格章节）
   - 来源三（补充佐证）：https://en.wikipedia.org/wiki/Outline_of_painting （“Mannerism”列为独立流派）
   - 入选理由：三份独立权威大纲均将其归入建筑/视觉艺术风格序列；属 TASK_design.md“主要建筑风格史”范围，位于已有的 renaissance-style 与 baroque 之间；scope.md 57 条风格中无此条（英文 id 与中文名均未出现）。

2. **建议 id：beaux-arts** ｜ 中文名：学院派建筑（布扎艺术）
   - 来源一：https://en.wikipedia.org/wiki/List_of_architectural_styles （“Beaux-Arts”列为独立风格）
   - 来源二：https://en.wikipedia.org/wiki/History_of_architecture （设“Beaux-Arts”独立章节，并链接“Beaux Arts”）
   - 入选理由：两份独立权威来源均将布扎列为 19 世纪独立建筑风格/学院体系；属“主要建筑风格史”范围；scope.md 虽有 neoclassical 与 revival-* 条目，但无 beaux-arts 独立条目。

3. **建议 id：vitruvian-triad** ｜ 中文名：维特鲁威三原则（坚固、实用、美观）
   - 来源一：https://en.wikipedia.org/wiki/Architectural_theory （“Vitruvian triad”“firmness, commodity, and delight”“De architectura”“Vitruvius”）
   - 来源二：https://en.wikipedia.org/wiki/Visual_arts （建筑章节：“De architectura”“Vitruvius”“firmness, commodity, and delight”“Durability”“building materials”）
   - 入选理由：两份独立权威来源均记载维特鲁威“坚固—实用—美观”三原则，是建筑空间设计最基础的理论命题之一；属本项目建筑理论/空间设计范围；scope.md 理论 106 条无对应条目（无 firmitas/utilitas/venustas 或中文“维特鲁威三原则”）。

4. **建议 id：plein-air** ｜ 中文名：外光写生（露天写生）
   - 来源一：https://en.wikipedia.org/wiki/Outline_of_painting （“Plein Air”列为绘画概念/方法）
   - 来源二：https://en.wikipedia.org/wiki/Visual_arts （绘画章节：“plein air”，与 pigments、chiaroscuro、Watercolors 等并列）
   - 入选理由：两份独立权威来源均收录外光写生；它直接关系本项目“色彩理论 / 光影与明暗”范围（自然光条件下直接观察与记录色彩、明暗，是色彩理论与光影理论的实践基础）；scope.md 无对应条目。关联属间接，建议由 lead 裁决是否纳入正式范围。

### 已排除（记录以体现筛选标准，不计入候选）

- 印象派、立体主义、表现主义、至上主义、未来主义等大量绘画流派：仅在 N2/N3 的艺术史导航中出现，而 TASK_design.md 的“风格”范围限定为“主要建筑风格史”，绘画流派史不在范围内，故排除。
- sfumato（渐隐法）、hatching/stippling（排线/点描）、hierarchy of genres（题材等级）：仅在单一来源出现，不满足双源标准；其中 sfumato 虽属光影理论范围，但仅 N2 一处明确列出，不列。
- Mudéjar、Churrigueresque、Prairie School、Vienna Secession、garden city movement、functionalism、phenomenology (architecture)、biomimicry、digital morphogenesis 等：仅单一来源明确列出或对应条目归属不够确定，不列。

## B6：近 12 个月（2025-11 至 2026-11）近期动态

来源页面：2025 in architecture、2026 in architecture（均打开核对正文，HTTP 200）。
保守原则：仅保留能核对到日期、来源 URL，且可明确说明对本项目具体条目产生影响的“新事件”。页面中大量奖项、讣告、建筑坍塌事故对本项目的绘画理论/空间设计原理仅有间接或无直接对应，未纳入。以下 3 条均属“实例/语境更新”，非理论本身的进展。

1. 古根海姆阿布扎比馆（Guggenheim Abu Dhabi，Frank Gehry 设计）预计 2026 年 12 月开馆
   - 日期：2026 年（页面原文 “set to open its doors in December”，列于 2026 年度下；当前采样 2026-11，属将发生事件）
   - 来源 URL：https://en.wikipedia.org/wiki/2026_in_architecture
   - 影响条目：deconstructivism（解构主义建筑）—— Frank Gehry 为解构主义代表，该馆为其近期代表作进展，可作为该条目“实例”的候选更新。

2. 叙事艺术博物馆（Lucas Museum of Narrative Art）于 2026 年 9 月 22 日在洛杉矶开馆
   - 日期：2026-09-22
   - 来源 URL：https://en.wikipedia.org/wiki/2026_in_architecture
   - 影响条目：visitor-route（参观动线）—— 大型文化建筑的近期实例，可作动线条目实例候选（间接影响，需补充设计者/空间资料后使用）。

3. 2025 年普利兹克建筑奖（Pritzker Prize）授予刘家琨（Liu Jiakun）
   - 日期：2025 年（页面奖项章节未列具体日期，不补写）
   - 来源 URL：https://en.wikipedia.org/wiki/2025_in_architecture
   - 影响条目：chinese-architecture-style（中国传统/当代建筑）—— 中国建筑师获国际奖项，可作该条目当代语境参考（间接影响）。

未纳入示例：Frank Gehry 于 2025-12-05 逝世、Robert A. M. Stern 于 2025-11-27 逝世（讣告，关联弱）；2025-11-03 罗马 Torre dei Conti 修缮中局部坍塌（建筑事故，与本项目原理条目无直接对应）；Stirling Prize、AIA Gold Medal 等纯奖项新闻（无本项目条目对应）。

## 核验记录

### 实际打开的 URL 列表与 HTTP 状态
| # | URL | HTTP | 用途 |
| --- | --- | --- | --- |
| 1 | https://en.wikipedia.org/wiki/List_of_architectural_styles | 200 | B1（N1） |
| 2 | https://en.wikipedia.org/wiki/Outline_of_painting | 200 | B1（N2） |
| 3 | https://en.wikipedia.org/wiki/History_of_architecture | 200 | B1（N3） |
| 4 | https://en.wikipedia.org/wiki/Architectural_theory | 200 | B1（N4） |
| 5 | https://en.wikipedia.org/wiki/Visual_arts | 200 | B1（N5） |
| 6 | https://en.wikipedia.org/wiki/2026_in_architecture | 200 | B6 |
| 7 | https://en.wikipedia.org/wiki/2025_in_architecture | 200 | B6 |

### 核验失败清单
- 网页核验失败：无。7 个 URL 全部返回 200，均实际打开并提取到标题与正文/章节内容。
- 本地技术备注（非来源问题）：首次抓取脚本因 stdout 默认 GBK 编码遇 UnicodeEncodeError 中断；改用 PYTHONIOENCODING=utf-8 后重跑成功。无 URL 抓取失败。

### 是否发现新缺口
- 是。B1 找到 4 条满足双源标准的遗漏候选；B6 找到 3 条可核验的近期动态（均为间接实例/语境更新）。
