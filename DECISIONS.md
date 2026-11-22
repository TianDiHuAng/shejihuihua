# 决策记录 DECISIONS.md

> 无人值守模式下所有自主选择均记录于此。用户任务文档 TASK_design.md / WORKFLOW.md 为最高约束。

| 编号 | 决策 | 理由 | 影响 / 代价 |
| --- | --- | --- | --- |
| D01 | 采用 JSON 数据层 → check.py 校验 → gen_site.py 渲染 → site/ 纯静态 HTML+CSS 的架构 | WORKFLOW.md 明确要求数据呈现分离、机器校验强制诚实 | 新增数据需重跑生成器，不能直接手改 HTML |
| D02 | 目录结构：data/（来源）、entries/（条目）、tools/（脚本）、tests/（测试）、site/（产物）、research/（检索笔记）、docs/（设计/计划） | 单一职责、便于增量写入与校验 | 目录层级固定，后续扩展按此结构 |
| D03 | 工作区为空，无样板页可参照；自建 CSS 变量主题（浅/深双模式、纸张墨色基调） | TASK_design.md 允许无样板时自行设计并记录 | 若后续提供样板页需按样板调整变量 |
| D04 | 条目按 L1 骨架全量建库，每轮最多处理 40 条；L2 先做 2 个样板，核心条目优先 | TASK_design.md 硬性规则，避免先深写个别条目导致不平衡 | 单轮内容深度有限，需多轮持续补完 |
| D05 | Web 检索工具端点异常时改用 Python urllib + 浏览器 User-Agent 抓取权威页面；无法核验的来源标 verified=false | web_search / web_fetch 在本环境返回错误，Python 直连 Wikipedia 返回 200 | 来源核验以实际 HTTP 响应与页面标题为准，不虚构 verified |
| D06 | 在线百科条目的 year 字段允许 null，note 写明“动态页面，访问于 YYYY-MM-DD” | 不编造页面未标明的年份 | check.py 需对 null 年份做例外规则 |
| D07 | 所有图示为内联 SVG，禁用外部图片；SVG 元素限制在 viewBox 内，深浅色变量可读 | TASK_design.md 专用规则 | 图示表达力受限于手绘示意图，但保证离线与一致性 |
| D08 | 在当前目录内联执行，不创建 git worktree；按阶段 commit，不 push | 用户明确要求所有文件放在当前项目文件夹；push 非本任务要求 | 无法隔离未提交改动，需靠 commit 与 PROGRESS 追踪 |
| D09 | 尺寸/坡度/消防/无障碍等数据仅一般性说明，统一附加“实际工程须按当地规范和专业设计人员的要求” | TASK_design.md 专用规则 | 条目页固定脚注模板 |
| D10 | 争议观点并列写持有方与理由，不替读者下结论；关键事实双源或标待核实 | TASK_design.md 通用硬性规则 | 单源内容进入待核实，降低“已验证”条目数量但更诚实 |
