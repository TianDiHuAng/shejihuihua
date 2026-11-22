# BACKLOG.md — 待办队列

> 按 AUTONOMOUS.md 第三节 B/C 生成。优先级：复核/修复 > 核心 > 重要 > 补充；被引用次数多、所在维度稀疏者优先。

## 第 3 轮缺口发现摘要

- B1：4 条 scope 候选（沿用上轮已核验的 N1–N5 双源依据）
- B2：空格 0，稀疏格 9
- B3：悬空引用 0
- B4：读者 80 问中 34 问暂无法从已写条目直接找到答案
- B5：待核实 8 条（上轮 3 条 + 新增单源条目 5 条）
- B6：3 条近期动态待评估
- B7：核心未写 2 条；核心已写 L1 待升级若干

## 第 3 轮队列（23 任务，≤40）

| 序号 | 任务 | 优先级 | 依据 |
| --- | --- | --- | --- |
| 1–5 | 纳入 5 份新核验来源 N1–N5 并置 verified=true / link_ok=true | 最高 | B1，HTTP 200 已核对 |
| 6–9 | 新增 4 个 scope 条目（mannerism、beaux-arts、vitruvian-triad、plein-air） | 核心 | B1，双源支持 |
| 10–13 | 复核 4 条待核实（原 3 条 + 新条目中的保守项） | 最高 | B5 |
| 14–16 | 评估 3 条 B6 近期动态并记录处置 | 重要 | B6 |
| 17–18 | 核心 L1 收尾：sunken-accessibility、chinese-architecture-style | 核心 | B7 |
| 19–23 | 5 个核心条目升级 L2（six-principles、borrowed-scenery、circulation、daylighting、natural-ventilation） | 核心 | B7，质量优先，不强行凑 40 |

执行顺序：每完成一批运行 check.py 并 commit；抽检 10%（至少 3 个）另起子任务。

## 下一轮队列（第 34 轮，按优先级）

1. 继续批量写未写条目（约 85 条：风格史组/造景组/下沉空间/材料组），直接 L2、写前去模板化+相似度预检。
2. 维持 25% 抽检；按第33轮建议复核其余明暗术语条目来源。
3. 复核 135 条待核实；补录 wp-rembrandt-lighting 的 link_ok。
4. 收敛剩余 5 稀疏格。

## 已完成

- 第 1 轮：项目搭建 + 40 条首批条目
- 第 2 轮：复核 3 条 + 新增 38 条核心 L1；抽检 4/4 合格
- 第 3 轮：纳入 6 份来源、新增 4 条 scope、新增 6 条 L1、升级 5 条 L2；抽检 2 不合格，整批返工完成
- 第 4 轮：复核 13 条待核实（1 条可升级）、新增 4 份来源、新写 5 条 L2、升级 2 条 L1→L2；抽检 1 不合格，整批返工完成
- 第 5 轮：体检；新增 7 份来源、新写 5 条 L2、升级 1 条；复核 23 条待核实；抽检 1 不合格，整批返工完成
- 第 6 轮：B1 找到 7 条候选；新写 6 条 L2（累计 100）；复核 24 条待核实；抽检 1 不合格，整批返工完成
- 第 7 轮：纳入 9 份新来源、7 个新 scope 条目与 7 条 L1（累计 107）；复核 24 条（0 可升级）；抽检 3/3 合格
- 第 8 轮：新增 6 条从业者问题 L2（累计 113）；复核 30 条（2 条概念层面升级）；B6 发现 2 条新动态；抽检 1 合格 / 2 待核实（已定向修正），无整批返工
- 第 9 轮：新写 6 条 L2（累计 119）；复核 34 条（3 条概念层面升级）；B1 找到 7 条候选；抽检 1 不合格，整批返工完成
- 第 10 轮：体检（0 死链/0 重复/0 孤儿）；网络中断，回滚未核验来源；用现有来源升级 6 条核心 L1→L2；复核 31 条（0 可升级）；抽检 3/3+4/4+3/3 合格，无返工
- 第 11 轮：镜像+web_search 核验 12 份来源、新增 7 个 scope 条目与 7 条 L1（累计 126）；复核 37 条（0 可升级）；抽检 3/3 合格，无返工
- 第 12 轮：7 个核心理论 L1→L2（核心已全部 L2）；bauhaus 补独立双源并升级；light-well 收窄待核实；抽检 3/3 合格，无返工
- 第 13 轮：6 个重要理论 L1→L2；chinese-architecture-style（紫禁城）、daylighting（金贝尔美术馆）补独立双源并升级实例；daylight-factor 收窄；抽检 3/3 合格
- 第 14 轮：6 条透视 L1→L2（返工去模板化，相似度<0.54）；复核 54 条，six-principles/circulation/water-management/borrowed-scenery 补官方双源升级、liubai 补源；抽检返工后复检通过（L2 63）
- 第 15 轮：6 条跨主题重要 L1→L2；复核 57 条，six-principles/borrowed-scenery/perspective/sunken-courtyard 收窄；修复 2 对既有相似度过高条目；抽检 3/3 合格（L2 69）
- 第 16 轮：6 条跨主题重要 L1→L2；six-principles 升级（异说并列）、perspective/sunken-courtyard 收窄；修 lighting-design 取源；抽检 2/3 合格+1 已修（L2 75）
- 第 17 轮：7 条升级（placemaking/space-syntax/pattern-language/biophilic-design/defensible-space-theory/functionalism-architecture/sunken-plaza）；sunken-plaza 待核实澄清；复核 69 条（3 项收窄因 URL 不精确延后）
- 第 18 轮：6 条升级（simplification/hierarchy/color-contrast/framed-scenery/pedestrian-flow/material-texture）；framed-scenery、natural-ventilation 实例补双源，opposed/leaked 补专门来源；material-texture 待核实扩写（L2 88）
- 第 19 轮：7 条升级（geometry-symmetry/visual-movement/leading-lines/rhythm-repetition/place-attachment/tour-route/drainage）；tour-route 升级验证、drainage/glare 实例补双源（L2 95）
- 第 20 轮：体检（0 死链/0 重复/0 孤儿）；6 条升级（visual-center/contrast-principle/form-follows-function/curvilinear-perspective/courtyard/green-architecture），重要条目全部 L2；courtyard 三源、sunken-plaza 补 1999 第二源
- 第 21 轮：6 条核心 L1→L2（气韵/留白/意境/空间定义/人体尺度/空间序列）；space-definition（巴塞罗那德国馆）、human-scale（帕伊米奥疗养院）补双源升级；返工修 qi-yun 年份、spatial-sequence 换古根海姆来源（核心 L1 余 13）
- 第 22 轮：6 条核心 L1→L2（过渡空间/空间组织/室内外过渡/曲径/疏散动线/高差处理）；level-change（劳力士学习中心）、winding-path（拙政园）补双源升级（核心 L1 余 7）
- 第 23 轮：7 条核心 L1→L2 收尾（东西透视/东西空间/防潮/安全防护/可持续/维特鲁威三原则/下沉无障碍）；**核心与重要条目全部 L2**；The Edge、Peavey Plaza 补双源；返工 3 条（东/西与无障碍引证）；仅余 6 条补充 L1
- 第 24 轮：6 条补充 L1→L2（空间法则/黄金比/对角/S形/三角/框架构图）——**全库 126 条全部 L2（L1=0）**；spatial-organization（萨伏伊别墅）双源升级、green-architecture 评价数据补多源；返工构图类改为单源如实标注
- 第 25 轮（体检轮）：体检 0 死链/0 重复/0 孤儿；B4 补齐 5 条新条目（伦勃朗光/暗绘/广场/中庭/疏散标识），读者未答问题 6→1；修 pedestrian-flow 死链、screened-scenery 单源披露；记录模板/伞源系统性问题
- 第 26 轮：5 条新增 L1→L2（伦勃朗光/暗绘/广场/中庭/疏散标识），**全库 131 条全部 L2**；pending_notes 去模板化（63 同句→各异）；12 条伞源条目改单源如实标注；green-architecture（常州高新智汇中心）升级、drainage 收窄
- 第 27 轮：补齐 vestibule（门厅）L2，**读者 80 问全部可答（未答 0）**；9 条单源条目补真实第二来源（Getty/LibreTexts/ArchDaily/同济等）、sunken-plaza 补同济第二源；vestibule 返工为单源如实标注
- 第 28 轮：leading-lines/axis 补第二源；gothic/modernism/color-theory 去骨架化具名实例（巴黎圣母院/包豪斯德绍/蒙塞尔色彩体系），color-theory 升级为已验证；10 条单源中 9 条已补源（余 gothic 待完整 URL）
- 第 29 轮：gothic 补第二源并升级；postmodernism（意大利广场）、bauhaus（德绍校舍）去骨架化；新增 baroque（圣彼得大教堂，双官方源）L2；抽检 3/3 合格
- 第 30 轮（体检轮）：体检 0 死链/0 重复/0 孤儿；新增 2 条稀疏格条目（墨西哥巴洛克/新陈代谢派），稀疏格 9→7；抽检 3/3 合格
- 第 31 轮：新增学院派理论、古典柱式 2 条（稀疏格 7→5）；bauhaus 与 modernism 实例去重（相似度降至 <0.54）；抽检 2 合格/1 已修
- 第 32 轮：写 12 条未写条目（中国画技法组骨法/应物象形/随类赋彩/传移模写/水墨/皴法/工笔/写意/虚实/山水 + 对称布局/开敞），均 L2；去模板化后相似度 <0.54；抽检 3/3 合格
- 第 33 轮：写 12 条未写条目（光影塑形/五调子/投影/高光/反光/交界线/正侧逆顶光 + 配色方案/色彩象征）均 L2；四向光与五调子去同质化；five-tones 补待核实披露
