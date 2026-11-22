# 绘画理论与建筑空间设计知识库 Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** 在 E:/ai_project/shejihuihua 搭建数据驱动、机器校验、可离线浏览的《绘画理论与建筑空间设计》静态知识库。

**Architecture:** JSON 数据层经 check.py 校验后由 gen_site.py 渲染为 site/ 静态 HTML+CSS；来源库全局共享，条目按 L1→L2→L3 分层增量补完。

**Tech Stack:** Python 3.11 标准库（json/unittest/html.parser/urllib）、原生 HTML/CSS、内联 SVG、git。

**Spec:** docs/superpowers/specs/2026-11-22-design-drawing-knowledge-design.md；D:/Users/Administrator/Desktop/TASK_design.md；D:/Users/Administrator/Desktop/WORKFLOW.md

## Global Constraints

- 所有文件在当前项目文件夹；每阶段更新 PROGRESS.md、运行 `python tools/check.py`、git commit；不 push。
- 每轮最多处理 40 个条目；L1 未全部完成前不得深写个别条目。
- 不编造数字、日期、人名、引文、出处；单源关键事实标待核实。
- 只引用 sources.json 中 `verified=true` 的来源。
- 不使用图片；SVG 自绘且注明“示意图，非施工图”。
- 尺寸/坡度/消防/无障碍仅一般性说明并附规范提示。
- 条目 id 仅允许 `a-z0-9-`。

## Review Focus

1. 未核验来源被 L2 条目引用 → check.py 必须拒绝；测试放在 Task 4。
2. SVG 脚本/外链/出界元素 → check.py 必须拒绝；测试放在 Task 4。
3. 待核实条目缺少 pending_notes → check.py 必须拒绝；测试放在 Task 4。
4. 生成页面内部链接 404 → check_links.py 必须报告；测试放在 Task 7。
5. 覆盖矩阵与 scope 条目数不一致 → check.py 必须报告；测试放在 Task 4。

---

### Task 1: 治理与仓库初始化

**Files:** Create PROGRESS.md、DECISIONS.md、BLOCKERS.md、README.md、docs/superpowers/specs/...、docs/superpowers/plans/...
**Interfaces:** Produces: 决策记录与阶段状态文件。
- [x] Step 1: 写入治理文件并 git init（本轮已完成）
- [x] Step 2: 提交初始提交：`git add ... && git commit -m "chore: initialize project governance"`

### Task 2: 阶段0 范围

**Files:** Create scope.md、coverage.json、coverage-matrix.md、research/outline_raw.md
**Interfaces:** Consumes: 权威百科分类树/教材目录抓取结果。Produces: 全量条目 id 清单供 Task 4/6 使用。
- [ ] Step 1: 用 Python urllib + User-Agent 抓取至少 3 份权威大纲/分类树页面，保存 research/outline_raw.md（含 URL、抓取日期、章节标题）
- [ ] Step 2: 取并集生成 scope.md：每条含名称、层级（核心/重要/补充）、来源编号
- [ ] Step 3: 生成 coverage.json（id/L1-L3/状态/来源数/待核实数/最后更新）与 coverage-matrix.md（主题×时期×地区）
- [ ] Step 4: 运行 `python tools/check.py --scope-only`，期望 0 errors
- [ ] Step 5: 更新 PROGRESS.md 并提交

### Task 3: 阶段1 来源库

**Files:** Create data/sources.json、research/source_notes.md、tools/linkcheck.py
**Interfaces:** Produces: 来源 id 白名单供条目引用。
- [ ] Step 1: 检索并打开至少 90 条权威页面，逐条核对标题/机构后写 verified
- [ ] Step 2: 运行 `python tools/linkcheck.py` 记录三态结果到 research/source_notes.md
- [ ] Step 3: 检查 verified 数量 ≥ 80，否则继续补来源
- [ ] Step 4: 更新 PROGRESS.md 并提交

### Task 4: 阶段2 校验器

**Files:** Create tools/check.py、tests/test_check.py
**Interfaces:** Consumes: coverage.json、data/sources.json、entries/*.json。Produces: 全量校验命令。
- [ ] Step 1: 写失败测试：未 verified 来源引用、SVG 脚本、pending_notes 缺失、矩阵数量不符
- [ ] Step 2: 运行 `python -m unittest discover -s tests -v` 确认 FAIL
- [ ] Step 3: 实现 check.py（R1/R4/R5/R6/R9/R10/R16 + 项目规则 + scope-only）
- [ ] Step 4: 运行测试确认 PASS，再运行 `python tools/check.py` 确认 0 errors
- [ ] Step 5: 更新 PROGRESS.md 并提交

### Task 5: 阶段3 样板

**Files:** Create entries/sample-theory.json、entries/sample-space.json
**Interfaces:** Consumes: sources.json。Produces: L2 条目结构范例。
- [ ] Step 1: 选 2 个核心条目（透视法、下沉庭院）写 L2 七节结构 + SVG
- [ ] Step 2: 运行 `python tools/check.py`，期望 0 errors
- [ ] Step 3: 更新 coverage.json 并提交

### Task 6: 阶段4 首批条目

**Files:** Create entries/batch-01.json（≤40 条）
**Interfaces:** Consumes: scope.md 顺序。Produces: L1 骨架条目。
- [ ] Step 1: 按核心→重要→补充写入 40 条 L1（定义、时间/位置、概述、相关条目、来源/待核实）
- [ ] Step 2: 运行 check.py，0 errors
- [ ] Step 3: 更新 coverage.json 与 PROGRESS.md，提交

### Task 7: 站点生成与链接核验

**Files:** Create tools/gen_site.py、tools/check_links.py、site/assets/site.css、site/index.html 等
**Interfaces:** Consumes: entries/*.json、coverage.json、sources.json。Produces: site/ 静态站点。
- [ ] Step 1: 实现 gen_site.py：首页/单元页/条目页/索引/来源页/覆盖报告页
- [ ] Step 2: 运行 `python tools/gen_site.py` 生成站点
- [ ] Step 3: 运行 `python tools/check_links.py`，期望 0 broken links
- [ ] Step 4: 提交

### Task 8: 阶段5 报告与全量验收

**Files:** Create REPORT.md
**Interfaces:** Consumes: coverage.json、sources.json、site/。
- [ ] Step 1: 生成 REPORT.md（总条目、各层级数量、验证通过数、待核实数、空白格子清单）
- [ ] Step 2: 运行 `python tools/check.py && python tools/gen_site.py && python tools/check_links.py` 全绿
- [ ] Step 3: 更新 PROGRESS.md（不写 ALL_DONE），提交
