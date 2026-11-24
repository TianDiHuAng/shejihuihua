# 第 114 轮 B4 — 跨页/跨数据一致性核验（AUTONOMOUS.md 缺口发现七法）

- 执行时间：2026-11-24（host 采样 2026-11-24T15:08:05+08:00）。
- 方式：只读 Python 脚本交叉解析 JSON / Markdown / HTML；**未修改任何既有文件、未 git commit**。本文件为唯一输出。
- 旁证校验器（只读执行）：`python tools/check.py` → `PASS: all checks, 0 errors`；`python tools/check_links.py` → `PASS: 0 broken links`（仅站内链接）。

## 一、核对项与实测结论

### 1）coverage.json vs scope.md

| 比对字段 | 实测 |
| --- | --- |
| id 集合 | 258 vs 258，双向差集为空 |
| title / 名称 | 逐条比对 258 条，0 处不一致 |
| tier / period / region | 逐条比对 258 条，0 处不一致 |
| theme（按 scope.md 章节归属） | 逐条比对 258 条，0 处不一致 |
| 主题声明数 | 理论 128 / 风格 66 / 造景 19 / 动线 13 / 下沉空间 13 / 材料 19，与 scope 实际行、coverage 统计三者全等，合计 258 |
| 层级声明数 | 核心 50 / 重要 153 / 补充 55，scope 实际与 coverage 三者全等 |

**结论：未发现不一致。**

### 2）coverage.json vs entries/*.json

覆盖 31 个 batch 文件、258 条已写条目。

| 比对字段 | 实测 |
| --- | --- |
| id 集合 | coverage 258 = entries 258，无重复 id、无孤儿条目 |
| level / tier / theme / period / region / title | 逐条 258 比对，0 处不一致 |
| source_count vs `len(entry.sources)` | 0 处不一致 |
| needs_verification_count vs `entry.needs_verification`（精确 0/1，非仅 bool） | 0 处不一致；两处统计均为 138 |
| last_updated | coverage 258 条全为 `2026-11-24`，与顶层 `updated=2026-11-24` 一致；entries 文件中 `last_updated` 字段数为 **0**，无逐条对照物，属"不可核对"而非不一致 |

说明：`tools/check.py::validate_coverage` 已覆盖 title/tier/period/region/level/source_count，但 `needs_verification_count` 只比 bool；本轮独立按精确数值复核，仍为 0 差异。

**结论：未发现不一致。**

### 3）data/sources.json（485 条）

| 检查 | 实测 |
| --- | --- |
| 重复 id | 0 组 |
| 精确重复 URL（去首尾空白、大小写归一） | **3 组**（详见发现 1–3） |
| 忽略查询参数后的重复 URL | 5 组；其中 2 组为不同查询参数指向不同资源（`jfdaily-jingan?id=1010081` vs `jfdaily-xiangshanbang?id=1027626`；`dpm-luoshenfu?id=69037…` vs `dpm-xiaoxiang?id=fmfs…`），**判为非重复**，不计入发现 |
| verified=true 且 link_ok=false | **1 条**（详见发现 4） |
| verified=true 且 link_ok="blocked" | 0 条 |
| verified 统计 | 485/485 全部 verified=true；link_ok=false 1 条、blocked 0 条、true 若干、null 若干 |

### 4）site/*.html 生成物 vs 数据

| 页面 / 项 | 实测 |
| --- | --- |
| 首页卡片 | 范围条目 258、已写 258、L1 0、L2 258、已核验来源 485、待核实 138 —— 与 coverage/entries/sources 实测全等 |
| 首页主题标签 | 理论 128 / 风格 66 / 造景 19 / 动线 13 / 下沉空间 13 / 材料 19 —— 与 coverage 全等 |
| 首页目标层级说明 | L1 0 / L2 258 / L3 0 —— 与 coverage 全等 |
| coverage.html 表体 | 6 主题 × 6 时期格子（含"合计"列）逐格核对 coverage，0 处不一致；未写条目 0、格子 0 —— 与实测全等 |
| indexes.html | 6 个主题分节计数、节内条目 id 集合（全域 258 个、无重复）、状态列 —— 与 coverage/entries 全等 |
| timeline.html | 6 个时期分组，共 258 个链接、258 个唯一 id；无"待写"项；每条 period 归属与 coverage 一致；标题与 coverage 一致（HTML 转义解码后） |
| site/entries/*.html | 258 个页面，id 集合与 entries 全等；`<h1>` 与条目 title 解码后全等 |

**结论：未发现不一致。**（`trompe-loeil` 页面 h1 为 `错视画（Trompe-l&#x27;œil）`，系 `html.escape` 对 `'` 的正常转义，解码后与源数据一致，非不一致。）

### 5）REPORT.md 最新一轮（第 113 轮）统计数字

| REPORT 数字 | 报告值 | 实测值 | 结论 |
| --- | --- | --- | --- |
| 范围总条目 | 258 | 258 | 一致 |
| 已写条目 | 258 | 258 | 一致 |
| L1 / L2 / L3 | 0 / 258 / 0 | 0 / 258 / 0 | 一致 |
| 验证通过数（来源） | 485 | 485（verified=true） | 一致 |
| 待核实 | 138 | 138（entries 标志计数与 coverage 计数皆 138） | 一致 |
| 来源总数 | 485 | 485 | 一致 |
| 复核条目 | 258 | 258 | 一致 |
| 19/19 | 19/19 | 指测试套件 19 项（见 METRICS.json 历轮 `19/19 tests`），非条目数 | 一致，非条目口径 |
| 0 broken links | 0 | `check_links.py` 实测 0（仅站内 href/src） | 一致，非外链口径（见"口径说明"） |

**结论：未发现不一致。**

## 二、发现清单：共 **4 处不一致**

### 发现 1 — 重复 URL（组 A）：卢浮宫页面登记两次且元数据分叉

- id / 位置：`louvre-monalisa`（data/sources.json:3628）、`louvre-explore-mona`（data/sources.json:5440）
- 字段 / 各处取值：
  - `url`（相同）：`https://www.louvre.fr/en/explore/the-palace/from-the-mona-lisa-to-the-wedding-feast-at-cana`
  - `title`：`From the Mona Lisa to the Wedding Feast at Cana — Musée du Louvre` / `From the Mona Lisa to the Wedding Feast at Cana — Louvre`
  - `link_ok`：`null` / `true`
  - `note`：前者指向"空气透视"，后者指向"晕涂法(sfumato)"
- 受影响条目：`aerial-perspective`（nv=true）引用前者；`sfumato`（nv=true）引用后者。
- 建议修法：合并为单一 source id（保留 `louvre-explore-mona` 的 `link_ok=true` 与较完整 note），把 `aerial-perspective` 的引用改指合并 id，并在合并 note 中并列记录两条论点；或若坚持双 id，则统一 title 并在 URL 上补可区分的锚点/深链，同时对齐 `link_ok`。

### 发现 2 — 重复 URL（组 B）：TU Delft 同一页面两种标题

- id / 位置：`tudelft-figure-ground`（data/sources.json:4108）、`tudelft-hierarchy`（data/sources.json:4156）
- 字段 / 各处取值：
  - `url`（相同）：`https://ocw.tudelft.nl/course-readings/ways-distinguish-elements-complex-situation/`
  - `title`：`Figure-ground — TU Delft OCW` / `Ways to distinguish elements — TU Delft OCW`
  - `note`：前者记"白=公共空间、黑=建成/私人空间，诺利图"，后者记"信息层级：下一站/换乘站"
  - `link_ok`：均为 `null`
- 受影响条目：`figure-ground`（nv=false）、`hierarchy`（nv=false）分别引用。
- 建议修法：以页面实际 h1 统一两个 id 的 title（建议 `Ways to distinguish elements — TU Delft OCW`）；若两者确为同一页面的不同论点，改为共用同一 source id、在 note 中区分论点，避免"同 URL 两个标题"在来源页与条目页同时呈现。

### 发现 3 — 重复 URL（组 C）：梵高博物馆来源近乎完全重复

- id / 位置：`vangogh-colours`（data/sources.json:4828）、`vgm-colours`（data/sources.json:5404）
- 字段 / 各处取值：
  - `url`（相同）：`https://www.vangoghmuseum.nl/en/art-and-stories/stories/vincents-colours`
  - `title` / `author` / `type` / `year`：完全相同（`Vincent's colours — Van Gogh Museum` / `Van Gogh Museum` / `官方机构` / `null`）
  - `link_ok`：`null` / `true`（同一 URL 链接状态不一致）
  - `note`：措辞略异，均记互补色
- 受影响条目：`split-primary`（nv=true）引用前者；`complementary-colors`（nv=true）、`color-contrast`（nv=false）引用后者。
- 建议修法：合并为一个 id（建议保留 `vgm-colours`，其 `link_ok=true`），把 `split-primary` 的引用改为合并 id，并核对 `split-primary` 在合并后是否仍满足双源/待核实披露规则。

### 发现 4 — 来源记录自相矛盾：verified=true 但 link_ok=false

- id / 位置：`artincontext-academic`（data/sources.json:2548）
- 字段 / 各处取值：
  - `verified`：`true`
  - `link_ok`：`false`（`tools/linkcheck.py` 三态定义中 `false` = 死链）
  - `url`：`https://artincontext.org/academic-art/`
  - `note`：`访问于 2026-11-22，经 owiki 镜像/独立站点实抓核对标题与正文，canonical 直连待复；…；2026-11-23 复核为 HTTP 404，canonical 待复`
  - `tools/check.py` 视角：`verified=true` 仅校验 URL 合法与 note 非空，未交叉校验 `link_ok`，故仍 PASS；`research/healthcheck-round113.md` 亦把该条列为"过期数据：link_ok=false 共 1 条"而非死链。
- 受影响条目：`academic-art-theory`（batch-31.json，nv=true，已按单源披露）。
- 建议修法：二选一——(a) 将 `verified` 置为 `false`（或引入 `verified_snapshot` / `archived` 状态字段区分"快照核验"与"现链可达"），并确认引用条目维持待核实披露；(b) 若核验依据为镜像/存档，则补 `url2` 或存档链接、说明核验载体，并把 `link_ok` 按真实可达状态修正，消除"已核验 + 死链"并存。

## 三、口径说明（已排除的疑似不一致，不计入上表）

1. **REPORT 的 "19/19"**：指测试套件 19 项通过（METRICS.json 多轮 `19/19 tests`），与已写条目 258 无关，非数字不一致。
2. **REPORT 的 "0 broken links"**：`tools/check_links.py` 只检查生成页内部 `href/src` 是否存在，实测 PASS；外部来源 URL 的 `link_ok=false` 由 `tools/linkcheck.py` 单独三态管理，两者口径不同。发现 4 属于来源记录内部矛盾，不与"0 broken links"冲突。
3. **`coverage.last_updated`**：entries 数据模型中不存在该字段（31 文件 0 处），无法逐条核对；coverage 内部 258 条与顶层 `updated` 均为 `2026-11-24`，无内部矛盾。
4. **忽略查询参数后的 2 组同路径 URL**：`jfdaily-*.do?id=1010081` / `?id=1027626` 与故宫名画记 `?id=69037…` / `?id=fmfs…` 指向不同文章/藏品，判为非重复。

## 四、结论

- 五个核对项中，**第 1、2、4、5 项未发现不一致**；第 3 项（data/sources.json）发现 **4 处不一致**：3 组精确重复 URL + 1 条 `verified=true` 与 `link_ok=false` 矛盾的来源记录。
- 站点的首页、索引、覆盖报告、时间线与 258 条条目页在条目数、层级统计、待核实数、时期分组上均与 coverage.json / entries 完全一致；时间线 258 条无遗漏、无重复、无错误分组。
- REPORT.md 第 113 轮的全部可测统计数字与实测吻合。
- 已知校验器盲区：`tools/check.py` 不检查重复 URL，也不交叉校验 `verified` 与 `link_ok`；本轮 4 处发现均落在该盲区，建议后续在校验器中补两条规则（URL 唯一性、`verified && link_ok is False` 矛盾）。
