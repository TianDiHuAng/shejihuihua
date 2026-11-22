# 第 3 轮抽检返工记录

抽检报告：`research/spotcheck-round03.md`（合格 1、待核实 1、不合格 2）。

按 AUTONOMOUS.md E 节“不合格则整批返工”，对本轮新增/升级条目整批评审并修正 3 条：

| 条目 | 问题 | 返工措施 |
| --- | --- | --- |
| `mannerism` | 原两来源页面正文未直接命中样式主义；“至19世纪”无据 | 新增并核对 `wp-mannerism` 直接条目；来源改为 `wp-mannerism` + `wp-list-architectural-styles`；时间改为“文艺复兴晚期欧洲” |
| `daylighting` | `wp-daylighting` 为消歧义页，`wp-architecture` 未命中采光术语 | 新增 `wp-daylighting-architecture` 与 `wp-architectural-lighting-design` 两条直接来源；来源整组替换；设待核实，说明参数需按规范核对 |
| `six-principles` | `wp-xie-he` 为消歧义页，年代与版本无支撑 | 移除该引用，保留单源并维持 `needs_verification=true`；pending_notes 写明待补专门研究来源 |

其余 8 条本轮条目复核未发现同类问题。返工后 `tools/check.py` 仍为 0 errors。
下一轮抽检比例按协议提高至 25%。
