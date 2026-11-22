# 项目进度 PROGRESS.md

- 项目：静态网站《绘画理论与建筑空间设计》
- 启动时间：2026-11-22 14:57 Asia/Hong_Kong
- 工作方式：无人值守，按 TASK_design.md 与 WORKFLOW.md 分阶段推进；决策写入 DECISIONS.md
- 当前轮次：第 1 轮（项目搭建 + 首批条目）

## 阶段状态

| 阶段 | 内容 | 状态 | 产物 |
| --- | --- | --- | --- |
| 0 | 范围 scope / coverage / 覆盖矩阵 | 已完成 | scope.md（219 条）、coverage.json、coverage-matrix.md、research/outline_raw.md（S1–S12） |
| 1 | 来源库 sources.json | 待开始（后台检索中） | data/sources.json、research/source_notes.md |
| 2 | 校验器 tools/check.py | 待开始 | tools/check.py、tests/ |
| 3 | 2 个 L2 样板 | 待开始 | entries/ 样板条目 |
| 4 | 首批 L1 条目（≤40） | 待开始 | entries/*.json |
| 5 | 总览页 / 索引 / 导航 / REPORT | 待开始 | site/、REPORT.md |

## 本轮完成目标

1. 建立可审计的数据驱动静态站骨架（JSON → check.py → gen_site.py → site/）。
2. 完成阶段 0 全量范围清单与覆盖矩阵。
3. 建立来源库并对可访问页面做 verified 核验。
4. 完成 2 个 L2 样板与首批 40 条 L1 骨架。
5. 生成站点首页、索引、导航、来源页、覆盖报告；通过全量校验并提交。

## 下一轮起点

阶段 4：从 scope.md 中第 41 条未处理条目开始，按核心→重要→补充顺序继续 L1 升级。
本轮尚未写入 ALL_DONE；全部阶段完成后才写入。

## 变更日志

- 2026-11-22 14:57 初始化项目目录、git 仓库与治理文件。
