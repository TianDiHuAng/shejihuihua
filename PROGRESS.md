# 项目进度 PROGRESS.md

- 项目：静态网站《绘画理论与建筑空间设计》
- 启动时间：2026-11-22 14:57 Asia/Hong_Kong
- 工作方式：无人值守，按 TASK_design.md 与 WORKFLOW.md 分阶段推进；决策写入 DECISIONS.md
- 当前轮次：第 1 轮（项目搭建 + 首批条目）

## 阶段状态

| 阶段 | 内容 | 状态 | 产物 |
| --- | --- | --- | --- |
| 0 | 范围 scope / coverage / 覆盖矩阵 | 已完成 | scope.md（219 条）、coverage.json、coverage-matrix.md、research/outline_raw.md（S1–S12） |
| 1 | 来源库 sources.json | 已完成 | data/sources.json（118 条，115 verified，link_ok 三态）、research/source_notes.md |
| 2 | 校验器 tools/check.py | 已完成 | tools/check.py、tests/test_check.py（7/7 通过） |
| 3 | 2 个 L2 样板 | 已完成 | entries/l2-samples.json（透视法、下沉庭院，含自绘 SVG） |
| 4 | 首批条目（合计 40） | 本轮已完成 | entries/batch-01.json（38 条 L1）+ 2 条 L2；coverage.json 已同步 |
| 5 | 总览页 / 索引 / 导航 / REPORT | 已完成 | site/（首页、40 条目页、索引、来源、覆盖报告）、REPORT.md |

## 本轮完成目标

1. 建立可审计的数据驱动静态站骨架（JSON → check.py → gen_site.py → site/）。
2. 完成阶段 0 全量范围清单与覆盖矩阵。
3. 建立来源库并对可访问页面做 verified 核验。
4. 完成 2 个 L2 样板与首批 40 条 L1 骨架。
5. 生成站点首页、索引、导航、来源页、覆盖报告；通过全量校验并提交。

## 下一轮起点

阶段 4：从首个未写核心条目 `chiaroscuro` 开始，按核心→重要→补充顺序继续 L1 升级。
本轮尚未写入 ALL_DONE；全部阶段完成后才写入。

## 变更日志

- 2026-11-22 14:57 初始化项目目录、git 仓库与治理文件。
- 2026-11-22 15:0x 阶段0：生成 scope.md（219 条）、coverage.json、覆盖矩阵；抓取 S1–S12 权威分类树。
- 2026-11-22 15:1x 阶段1：来源库 118 条（115 verified），逐条 HTTP 核验标题与机构。
- 2026-11-22 15:2x 阶段2：check.py 完成，7 个单元测试 RED→GREEN 全通过。
- 2026-11-22 15:3x 阶段3–5：2 个 L2 样板、38 条 L1、站点生成、链接核验、报告完成。
- 2026-11-22 15:4x 全量审查后修复：元数据漂移、L2 七节、覆盖矩阵校验、SVG 越界/事件属性、link_ok 三态、待核实联动、层级口径、批次优先级；14/14 测试通过。

## 审查与修复记录

最终审查发现 2 项 Critical、6 项 Important，均已用 RED→GREEN 测试修复：
- 元数据一致性：条目与 scope/coverage 的 theme/tier/period/region 对齐，check.py 增加字段比对。
- L2 七节：sections 统一为七节键，生成器按七节输出，校验器强制约束。
- 覆盖矩阵：check.py 解析矩阵格子并与 scope 数量比对。
- SVG 安全：补齐 r/width/height/points/d 越界与全部 on* 事件属性拦截；生成器复用 validate_svg。
- 来源链接：新增 tools/linkcheck.py 三态（true/blocked/false/null），来源页展示链接状态。
- 待核实：内联“待核实”声明与 needs_verification 标志联动。
- 口径与顺序：首页区分“已写层级/范围目标层级”，批次按核心→重要→补充排序。
最终验证：14/14 unittest、check.py 0 errors、gen_site.py 成功、check_links.py 0 broken links。
