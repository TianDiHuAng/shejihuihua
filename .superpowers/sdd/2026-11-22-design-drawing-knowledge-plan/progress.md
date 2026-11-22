# SDD ledger — plan: docs/superpowers/plans/2026-11-22-design-drawing-knowledge-plan.md

Pre-flight: no shared interfaces（各任务通过文件接口衔接，无并发共享状态）

Task 1: complete (54dfb48) — 治理文件与 git init
Task 2: complete (18de9ed) — scope 219 条 / coverage / 矩阵 / S1–S12
Task 3: complete (189d7e6) — sources.json 118 条（115 verified）
Task 4: complete (d6d0dfe) — check.py + 7 tests RED→GREEN
Task 5: complete (524bda6) — 2 个 L2 样板
Task 6: complete (524bda6) — 38 条 L1，合计 40 条/轮
Task 7: complete (60da1f0) — gen_site.py / check_links.py / site/
Task 8: complete (60da1f0) — REPORT.md / PROGRESS.md

## Final review

Final review: dispatched `final-reviewer` subagent (read-only, full diff 54dfb48..60da1f0). Verdict: With fixes.
Findings: 2 Critical + 6 Important + 6 Minor。Critical/Important 全部在单轮修复中处理，每个均有失败测试先行。

- Final: fixed 元数据漂移 — test_metadata_drift_rejected RED→GREEN，suite 14/14
- Final: fixed L2 七节缺节 — test_l2_seven_sections_required RED→GREEN，suite 14/14
- Final: fixed 覆盖矩阵未校验 — test_matrix_mismatch_rejected RED→GREEN，suite 14/14
- Final: fixed SVG 越界/事件属性 — test_svg_out_of_bounds_rejected、test_svg_event_handler_rejected RED→GREEN，suite 14/14
- Final: fixed 来源链接三态缺失 — test_classify_status RED→GREEN，suite 14/14
- Final: fixed 待核实标志脱节 — test_pending_text_without_flag_rejected RED→GREEN，suite 14/14
- Final: fixed 首页层级口径与批次顺序 — 数据/生成器修改，check.py 0 errors，check_links.py 0 broken links

## Rulings I made

- Ruling: 在当前目录内联执行、不建 git worktree — 用户明确要求所有文件放当前项目文件夹且无人值守 — 代价是隔离性弱，靠分阶段 commit 与 PROGRESS 追踪。
- Ruling: web_search/web_fetch 不可用时改用 Python urllib + 浏览器 UA 抓取 — 实际 HTTP 200 可核验 — 代价是部分反爬站点需保守标 verified=false。
- Ruling: 在线百科 year 用 null 并写访问说明 — 不编造年份 — 代价是来源页年份列显示“动态/未标注”。
- Ruling: 来源 verified 与 link_ok 分离 — 前者核对标题/机构，后者是当前可达性 — 代价是两列需分别解释。
- Ruling: 审查 Minor 中根 index.html、锚点检查留待后续 — 本轮发布根定为 site/，Review Focus 关注文件 404 — 代价是从项目根打开需进入 site/。

## Deferred minors

- Minor (deferred): 项目根缺 index.html 入口；以 site/index.html 为发布根。
- Minor (deferred): check_links.py 未校验 #锚点目标是否存在。
- Minor (deferred): 阶段3 与阶段4 合并为一次提交（524bda6），后续保持独立提交。
- Minor (resolved in fix pass): 报告硬编码数字、覆盖页未分组、相关条目显示 slug 已修。
