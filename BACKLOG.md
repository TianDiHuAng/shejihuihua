# BACKLOG.md — 待办队列

> 按 AUTONOMOUS.md 第三节 B/C 生成。优先级：复核/修复 > 核心 > 重要 > 补充；被引用次数多、所在维度稀疏者优先。

## 第 2 轮缺口发现摘要

- B2 覆盖矩阵：空格 0，稀疏格（≤1 条）9 个
- B3 悬空引用：0
- B5 待核实清单：3 条（`hierarchy`、`perspective`、`sunken-courtyard`）
- B7 深度缺口：核心未写 40 条；核心已写 L1 待升级 8 条；重要未写若干
- B1/B6：外部子任务检索中，结果写入 `research/gaps-external-round02.md`

## 本轮队列（≤40 任务）

| 序号 | id / 类型 | 优先级 | 依据 |
| --- | --- | --- | --- |
| 1 | 复核 3 条待核实（合并任务） | 最高 | B5：来源不足，需重新核对 |
| 2–39 | 38 条核心未写条目的 L1 写作 | 核心 | B7：`chiaroscuro` 起至 `sustainable-architecture` |
| 40 | 剩余核心 `chinese-architecture-style` | 核心 | B7：下一轮起点 |

执行顺序：每 10 个任务运行一次 `tools/check.py` 并 git commit；本轮新增 scope 条目 0（仅消化现有 scope）。

## 已完成

- 第 1 轮：项目搭建 + 40 条首批条目（详见 PROGRESS.md）
