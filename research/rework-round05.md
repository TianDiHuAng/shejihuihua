# 第 5 轮抽检返工记录

抽检报告：`research/spotcheck-round05.md`（合格 2、不合格 1、待核实 0；抽检 3/6 = 50%）。

按 AUTONOMOUS.md E 节触发整批返工：

| 条目 | 问题 | 返工措施 |
| --- | --- | --- |
| `huizhou-style` | 原来源为宽泛的 Chinese architecture / Vernacular architecture，正文未出现 Huizhou、粉墙黛瓦等核心事实 | 新增并核验 `wp-hui-style-architecture`（Hui Style architecture，HTTP 200）、`wp-hongcun`、`wp-xidi`；来源整组替换；按专条重写定义、概述与实例；`needs_verification=false`，待核实节改为“暂无已知待核实项” |
| `leaked-scenery` | 来源正文支持机制但无“漏景/漏窗”字面术语 | pending_notes 补充术语缺口说明，维持待核实 |
| `deconstructivism`/`brutalism`/`byzantine`/`ancient-greek` | 第 5 轮复核找到第二独立来源 | 补入 4 条直接来源并按来源原文更新实例，升级为已验证 |

其余条目复核无同类问题。返工后 `tools/check.py` 仍为 0 errors；`huizhou-style` 已确认引用专条且定义含“粉墙黛瓦”。下一轮抽检比例维持 25%。
