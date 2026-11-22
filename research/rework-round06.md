# 第 6 轮抽检返工记录

抽检报告：`research/spotcheck-round06.md`（合格 2、不合格 1、待核实 0；3/6 = 50%）。

按 AUTONOMOUS.md E 节触发整批返工：

| 条目 | 问题 | 返工措施 |
| --- | --- | --- |
| `stack-ventilation` | 与 `natural-ventilation` 相似度 0.648，正文/来源/SVG 三重重复；pending_notes 与正文声明不一致 | 重写 overview 与七节，突出“浮力驱动、与风压区别”；改用左右对比 SVG（左风压、右热压）；实例改为竖井式公共建筑；统一 pending_notes 为实测数据缺口；related 指向已写的 natural-ventilation |
| `color-harmony` | 面积比例等经验性表述缺直接来源；related 指向未写页面 | pending_notes 补充经验表述缺口；related 改为已写的 color-theory |
| `axis` | related 指向未写页面 | related 改为已写的 symmetry-layout |

来源真伪、事实编造、七节结构、SVG 图注与规范提示均未发现问题；返工后 `tools/check.py` 0 errors、0 broken links。下一轮抽检维持 25%。
