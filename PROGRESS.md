# 项目进度 PROGRESS.md

- 项目：静态网站《绘画理论与建筑空间设计》
- 启动时间：2026-11-22 14:57 Asia/Hong_Kong
- 工作方式：无人值守，按 TASK_design.md 与 WORKFLOW.md 分阶段推进；决策写入 DECISIONS.md
- 当前轮次：第 40 轮已完成（自动模式，含体检）；下一轮：第 41 轮

## 阶段状态

| 阶段 | 内容 | 状态 | 产物 |
| --- | --- | --- | --- |
| 0 | 范围 scope / coverage / 覆盖矩阵 | 已完成 | scope.md（219 条）、coverage.json、coverage-matrix.md、research/outline_raw.md（S1–S12） |
| 1 | 来源库 sources.json | 已完成 | data/sources.json（118 条，115 verified，link_ok 三态）、research/source_notes.md |
| 2 | 校验器 tools/check.py | 已完成 | tools/check.py、tests/test_check.py（7/7 通过） |
| 3 | 2 个 L2 样板 | 已完成 | entries/l2-samples.json（透视法、下沉庭院，含自绘 SVG） |
| 4 | 条目累计 247 | 第 40 轮已完成 | 范围 247；已写 247（全部 L2）；来源 293；待核实 215；稀疏格 5 |
| 5 | 总览页 / 索引 / 导航 / REPORT | 已完成 | site/（首页、40 条目页、索引、来源、覆盖报告）、REPORT.md |

## 本轮完成目标

1. 建立可审计的数据驱动静态站骨架（JSON → check.py → gen_site.py → site/）。
2. 完成阶段 0 全量范围清单与覆盖矩阵。
3. 建立来源库并对可访问页面做 verified 核验。
4. 完成 2 个 L2 样板与首批 40 条 L1 骨架。
5. 生成站点首页、索引、导航、来源页、覆盖报告；通过全量校验并提交。

## 下一轮起点

阶段 4：按 BACKLOG 第 41 轮队列执行：补抽、复核 215 条待核实（补具名实例）、再评估 B1/B6 与零缺口、收敛稀疏格。
本轮尚未写入 ALL_DONE；AUTONOMOUS.md 规定项目没有“做完”，只有饱和（SATURATION.json）。

## 变更日志

- 2026-11-22 14:57 初始化项目目录、git 仓库与治理文件。
- 2026-11-22 15:0x 阶段0：生成 scope.md（219 条）、coverage.json、覆盖矩阵；抓取 S1–S12 权威分类树。
- 2026-11-22 15:1x 阶段1：来源库 118 条（115 verified），逐条 HTTP 核验标题与机构。
- 2026-11-22 15:2x 阶段2：check.py 完成，7 个单元测试 RED→GREEN 全通过。
- 2026-11-22 15:3x 阶段3–5：2 个 L2 样板、38 条 L1、站点生成、链接核验、报告完成。
- 2026-11-22 15:4x 全量审查后修复：元数据漂移、L2 七节、覆盖矩阵校验、SVG 越界/事件属性、link_ok 三态、待核实联动、层级口径、批次优先级；14/14 测试通过。
- 2026-11-22 15:5x 第 2 轮自动模式：缺口发现 6 种方法；复核 3 条待核实；新增 38 条核心 L1（累计 78）；抽检 4/4 合格；发现 B1 4 条 + B6 3 条新缺口；check.py 0 errors、0 broken links。
- 2026-11-22 15:6x 第 3 轮自动模式：七种缺口发现；纳入 6 份来源、4 个新 scope 条目；新增 6 条 L1、升级 5 条 L2（累计 84）；复核 4 条待核实、评估 3 条动态；抽检发现 2 不合格，按协议整批返工 3 条；check.py 0 errors。
- 2026-11-22 15:7x 第 4 轮自动模式：七种缺口发现；复核 13 条待核实（hierarchy 升级为已验证）；新增 4 份来源、新写 5 条 L2、2 条 L1→L2（累计 89，L2 14）；25% 抽检发现 1 不合格，整批返工 3 条；check.py 0 errors、0 broken links。
- 2026-11-22 15:8x 第 5 轮自动模式：每 5 轮体检（0 死链/0 孤儿/0 重复/0 矛盾）；复核 23 条待核实（5 条可升级）；新增 7 份来源、新写 5 条 L2、升级 1 条（累计 94，L2 20）；25% 抽检 1 不合格，整批返工完成；check.py 0 errors。
- 2026-11-22 16:0x 第 6 轮自动模式：B1 找到 7 条双源候选；新写 6 条读者问题对应 L2（累计 100，L2 26）；复核 24 条待核实；25% 抽检发现 stack-ventilation 套话重复，整批返工 3 条；check.py 0 errors、0 broken links。
- 2026-11-22 16:1x 第 7 轮自动模式：纳入 9 份新来源、7 个新 scope 条目与 7 条 L1（累计 107，范围 230）；复核 24 条待核实（0 可升级）；25% 抽检 3/3 合格，无返工；check.py 0 errors。
- 2026-11-22 16:2x 第 8 轮自动模式：缺口发现 B2/B4/B5/B6/B7；新写 6 条从业者问题 L2（累计 113，L2 32）；复核 30 条（2 条概念层面升级）；B6 发现 2 条新动态；抽检 1 合格 / 2 待核实，已定向修正，无整批返工；check.py 0 errors。
- 2026-11-22 16:3x 第 9 轮自动模式：缺口发现 B1/B2/B4/B5/B7；新写 6 条 L2（累计 119，L2 38）；复核 34 条待核实（3 条概念层面升级）；B1 找到 7 条候选；抽检 1 不合格，整批返工 3 条；check.py 0 errors。

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
- 2026-11-22 17:5x 第 10 轮自动模式：体检（0 死链/0 重复/0 孤儿）；网络中断，按硬性规则回滚 12 份未核验来源，改为用现有已核验来源升级 6 条核心 L1→L2（累计 119，L1 75、L2 44）；复核 31 条（0 可升级）；三轮抽检 3/3、4/4、3/3 全合格，无返工；check.py 0 errors。
- 2026-11-22 18:3x 第 11 轮自动模式：经 Wikipedia 镜像 owiki.org + web_search 核验 12 份来源（canonical 直连待复），新增 7 个 scope 条目与 7 条 L1（累计 126，范围 237，来源 163）；复核 37 条（0 可升级）；25% 抽检 3/3 合格，无返工；check.py 0 errors。
- 2026-11-22 18:5x 第 12 轮自动模式：用现有来源把 7 个核心理论 L1→L2（核心 L1 清零，累计 126，L2 51）；复核 44 条，bauhaus 补独立双源升级、light-well 收窄；抽检 3/3 合格，无返工；check.py 0 errors。
- 2026-11-22 19:1x 第 13 轮自动模式：6 个重要理论 L1→L2（累计 126，L1 69、L2 57）；复核 49 条，chinese-architecture-style（紫禁城 1406–1420）、daylighting（金贝尔美术馆 1972）补双源升级，daylight-factor 收窄；抽检 3/3 合格；check.py 0 errors。
- 2026-11-22 19:2x 第 14 轮自动模式：6 条透视 L1→L2（抽检发现相似度/时段问题→整批返工去模板化，复检全 <0.54）；复核 54 条，4 条补官方双源升级、liubai 补源（累计 126，L2 63，来源 178）；check.py 0 errors。
- 2026-11-22 19:3x 第 15 轮自动模式：6 条跨主题重要 L1→L2（saturation/primary-colors/warm-cool/hardscape-softscape/wayfinding/mannerism）；复核 57 条并收窄 4 条（六法版本、借景距离、透视约1413、静安寺下沉广场）；修复 2 对相似度超标条目；抽检 3/3 合格（累计 126，L2 69，来源 185）。
- 2026-11-22 19:4x 第 16 轮自动模式：6 条跨主题重要 L1→L2（beaux-arts/plein-air/gestalt-organization-laws/color-psychology/environmental-psychology/lighting-design）；复核 63 条，six-principles 升级、perspective/sunken-courtyard 收窄；修 lighting-design 取源；抽检 2/3 合格+1 修复（累计 126，L2 75，来源 186）。
- 2026-11-22 19:5x 第 17 轮自动模式：7 条升级（placemaking/space-syntax/pattern-language/biophilic-design/defensible-space-theory/functionalism-architecture + sunken-plaza L2）；复核 69 条，sunken-plaza 待核实澄清，3 项收窄因 URL 不精确延后；抽检 2/3 合格+1 澄清（累计 126，L2 82）。
- 2026-11-22 20:0x 第 18 轮自动模式：6 条升级（simplification/hierarchy/color-contrast/framed-scenery/pedestrian-flow/material-texture）；framed-scenery、natural-ventilation 实例补双源（颐和园画中游/恭王府+翠郊院），opposed/leaked 补中国园林博物馆来源；material-texture 待核实扩写；抽检 2/3 合格+1 已修（累计 126，L2 88，来源 192）。
- 2026-11-22 20:1x 第 19 轮自动模式：7 条升级（几何对称/视觉动势/引导线/节奏重复/场所依恋/游线/排水）；tour-route 用拙政园双源升级、drainage/glare 实例补双源，drainage 补专业来源并修 period；抽检 2/3 合格+1 已修（累计 126，L2 95，来源 198）。
- 2026-11-22 20:2x 第 20 轮自动模式：体检（0 死链/0 重复/0 孤儿）；6 条升级（视觉中心/对比/形式追随功能/曲线透视/庭院/绿色建筑），重要条目全部 L2；courtyard 三源、sunken-plaza 补 1999 第二源；抽检 3/3 合格（累计 126，L2 101，来源 202，核心 L1 余 19）。
- 2026-11-22 20:3x 第 21 轮自动模式：6 条核心 L1→L2（气韵/留白/意境/空间定义/人体尺度/空间序列）；space-definition（巴塞罗那馆）、human-scale（帕伊米奥）补双源升级；抽检 1 不合格（spatial-sequence）→返工换源、qi-yun 年份改约550；check.py 0 errors（累计 126，L2 107，来源 206）。
- 2026-11-22 20:4x 第 22 轮自动模式：6 条核心 L1→L2（过渡空间/空间组织/室内外过渡/曲径/疏散动线/高差处理）；level-change（劳力士学习中心）、winding-path（拙政园）补双源升级；抽检 3/3 合格（累计 126，L2 113，来源 212，核心 L1 余 7）。
- 2026-11-22 21:0x 第 23 轮自动模式：7 条核心 L1→L2 收尾，**核心与重要条目全部 L2**；sustainable-architecture（The Edge）、sunken-accessibility（Peavey Plaza）补双源；抽检 2 不合格→返工（东西透视/无障碍/安全防护换源重述）；check.py 0 errors（累计 126，L2 120，来源 218，仅余 6 条补充 L1）。
- 2026-11-22 21:1x 第 24 轮自动模式：6 条补充 L1→L2 收尾，**全库 126 条全部 L2（L1=0）**；spatial-organization（萨伏伊别墅）双源、green-architecture 评价多源；构图类改单源如实标注；check.py 0 errors（来源 222，待核实 104）。
- 2026-11-22 22:1x 第 25 轮自动模式（体检）：体检 0 死链/0 重复/0 孤儿；B4 补齐 5 条新条目（伦勃朗光/暗绘/广场/中庭/疏散标识），读者未答问题 6→1；修 pedestrian-flow 死链与 screened-scenery 单源披露；抽检 2 合格/1 已修（累计 131，来源 229，待核实 105）。
- 2026-11-22 22:2x 第 26 轮自动模式：5 条新增 L1→L2（伦勃朗光/暗绘/广场/中庭/疏散标识），全库 131 条全部 L2；pending_notes 去模板化（63 同句→各异）；12 条伞源条目改单源如实标注；green-architecture 升级、drainage 收窄；抽检 1 合格/2 已修（来源 231，待核实 108）。
- 2026-11-22 22:4x 第 27 轮自动模式：补齐 vestibule（门厅）L2，读者 80 问全部可答；9 条单源条目补真实第二来源（Getty/LibreTexts/ArchDaily/同济等）、sunken-plaza 补同济第二源；vestibule 返工为单源如实标注；抽检 2 合格/1 已修（累计 132，来源 239，待核实 109）。
- 2026-11-22 23:0x 第 28 轮自动模式：leading-lines/axis 补第二源；gothic（巴黎圣母院）、modernism（包豪斯德绍）、color-theory（蒙塞尔色彩体系）去骨架化具名实例，color-theory 升级；抽检 2 合格/1 定向（gothic 第二源待完整 URL）；check.py 0 errors（累计 132，来源 245，待核实 108）。
- 2026-11-22 23:1x 第 29 轮自动模式：gothic 补 LibreTexts 第二源并升级；postmodernism（意大利广场）、bauhaus（德绍校舍）去骨架化；新增 baroque（圣彼得大教堂，双官方源）；抽检 3/3 合格（累计 133，来源 250，待核实 107）。
- 2026-11-22 23:3x 第 30 轮自动模式（体检）：体检 0 死链/0 重复/0 孤儿；新增墨西哥巴洛克、新陈代谢派 2 条（稀疏格 9→7）；抽检 3/3 合格（累计 135，来源 254，待核实 107）。
- 2026-11-22 23:5x 第 31 轮自动模式：新增学院派理论、古典柱式 2 条（稀疏格 7→5）；bauhaus 实例去重（与 modernism 相似度降至 <0.54）；抽检 2 合格/1 已修（累计 137，来源 258，待核实 111）。
- 2026-11-22 23:5x 第 32 轮自动模式：写 12 条未写条目（中国画技法组+对称布局/开敞）全部 L2，去模板化相似度 <0.54；抽检 3/3 合格；check.py 0 errors（累计 149，未写 97，来源 258）。
- 2026-11-23 00:0x 第 33 轮自动模式：写 12 条未写条目（光影/照明组+配色/象征）全部 L2（累计 161，未写 85）；四向光与五调子去同质化；抽检 2 合格/1 已修；check.py 0 errors。
- 2026-11-23 00:1x 第 34 轮自动模式：写 12 条风格史条目全部 L2（累计 173，未写 73）；art-deco 伞源缺口披露、SVG 加标题去同图；抽检 2 合格/1 已修；check.py 0 errors。
- 2026-11-23 00:2x 第 35 轮自动模式：写 12 条（造景/下沉/材料）全部 L2（累计 185，未写 61）；下沉组与材料色按抽检改为一般性工程说明并披露来源局限；抽检 1 合格/1 待核实/1 不合格→整批返工修正；check.py 0 errors。
- 2026-11-23 00:3x 第 36 轮自动模式：写 12 条（动线/采光通风/视觉舒适/无障碍）全部 L2（累计 197，未写 49）；visitor-route/accessibility 披露来源局限、风压与无障碍图重绘、SVG 逐条差异化；抽检 2 合格/1 待核实→已修；check.py 0 errors。
- 2026-11-23 00:4x 第 37 轮自动模式：写 24 条（空间组/风格史/地域风格）全部 L2——重要条目全部写完，未写仅剩 25 条补充；arts-crafts/monumental-scale/rule-of-odds 换真源、arts-crafts 时期改 19 世纪、24 条 SVG 逐条重绘；抽检 2 合格/1 待核实/1 不合格→整批返工修正（累计 221，来源 264）。
- 2026-11-23 00:5x 第 38 轮自动模式：写剩余 25 条补充条目，**246/246 全部写完且全部 L2（未写 0）**；acoustic/romanticism/korean 补双源（DesigningBuildings/LibreTexts/HenryFord/Korea.net/Springer）、25 条 SVG 逐条重绘；抽检 1 合格/2 待核实/1 不合格→返工修正（来源 270，待核实 220）。
- 2026-11-23 01:2x 第 39 轮自动模式（体检）：体检 0 死链/0 重复/0 孤儿；6 个风格条目补具名实例双源升级（待核实 220→214）；raised-floor 改一般性说明、african/latin 伞源披露；抽检 2 待核实/1 不合格→返工修正（来源 282）。
- 2026-11-23 01:3x 第 40 轮自动模式（体检）：B1 发现并纳入 proxemics（近距学）；batch-38 tibetan/rock-garden/time-scenery/xinjiang 补真源重写；体检 0 死链/0 重复/0 孤儿；抽检 2 待核实/1 不合格→返工修正（247 条全 L2，来源 293）。
