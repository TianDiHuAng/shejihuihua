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

## 下一轮队列（第 22 轮，按优先级）

1. 继续升级剩余 13 条核心 L1→L2：east-west-perspective-compare/east-west-space-compare/transition-space/spatial-organization/interior-exterior-transition/winding-path/evacuation-route/level-change/damp-proofing/safety-guarding/sustainable-architecture/vitruvian-triad/sunken-accessibility。
2. 维持 25% 抽检；补抽 liubai/yijing/human-scale 闭环第21轮。
3. 复核 90 条待核实（顾如珍/glare数值/green-architecture 常州案例/赵堂子胡同时期）。
4. 收尾 6 条补充 L1；处理 B4 的 6 个未答读者问题。

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
