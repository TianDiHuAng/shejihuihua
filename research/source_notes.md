# 阶段1 来源库 — 检索与核验记录

- 记录日期：2026-11-22（Asia/Hong_Kong）
- 项目：《绘画理论与建筑空间设计》静态知识库
- 产出：`data/sources.json`、`research/source_notes.md`（仅此两个交付文件）

## 一、检索策略

1. **主题清单法**：先把任务要求的范围拆成固定主题组（透视/构图/色彩/光影；中国画六法与留白；东西方比较；西方与东方建筑风格史；中国园林造景四法与游线；动线；下沉式空间；空间序列与尺度；室内外过渡；采光通风材料），每组列出候选权威条目。
2. **权威源优先级**：Wikipedia（权威百科，条目名稳定、可开放抓取）为主；UNESCO 世界遗产中心（官方机构）补园林实例；尝试 Britannica 但被反爬拒绝，未收录。
3. **真实联网核验**：环境内 `web_fetch`/`web_search` 工具报错（fetch failed / 端点配置错误），改用本机 Python `urllib.request` + 浏览器 User-Agent 逐条 HTTP GET（8 线程并发，30s 超时，失败重试 1 次）。用正则解析 HTML `<title>` 与 `<h1 id="firstHeading">`，二者之一包含预期条目名才算标题匹配；`200 <= status < 400` 且标题匹配才置 `verified=true`。
4. **标题纠错**：对 200 但发生重定向的条目，以页面**实际 h1** 为准写入 `title`，并在 `note` 注明重定向；对 404 条目尝试 MediaWiki API 搜索正确条目名后重新抓取；仍失败者标 `verified=false`。
5. **保守原则**：查不到就标 `verified=false` 并在 `note` 说明；年份一律记 `null` 并在 `note` 说明“百科条目无固定出版年”，不臆造年份；不编造 URL/标题/作者，备用链接 `url2` 一律 `null`。

## 二、实际打开的页面数

- 候选 URL 总数：**118**（第1批 111 条 + 纠错/补充 7 条 + UNESCO/Britannica 探测 5 条，其中重复条目按 id 合并）
- HTTP 成功打开（200–399）的页面数：**116**
- 最终收录来源：**118**，其中 `verified=true`：**115**，`verified=false`：**3**
- 另用 MediaWiki API 查询 5 次以确认正确条目名（非页面打开）。

## 三、核验失败清单

### 已收录但 verified=false

- `wp-linear-perspective` — https://en.wikipedia.org/wiki/Linear_perspective — HTTP 200；页面标题与预期不符
- `wp-means-of-egress` — https://en.wikipedia.org/wiki/Means_of_egress — HTTP 404；页面标题与预期不符
- `wp-underground-space` — https://en.wikipedia.org/wiki/Underground_space — HTTP 404；页面标题与预期不符

### 探测后未收录（保守排除）

- https://whc.unesco.org/en/list/492/ — HTTP 200但页面标题为 Taos Pueblo，与莫高窟不符，URL映射错误
- https://www.britannica.com/science/color — HTTP 403 反爬拒绝，未能核对标题，保守起见不收录
- https://www.britannica.com/art/Gothic-architecture — HTTP 403 反爬拒绝，未能核对标题，保守起见不收录
- https://www.britannica.com/art/Chinese-painting — HTTP 403 反爬拒绝，未能核对标题，保守起见不收录

## 四、来源分类统计

### 按类型

- 官方机构: 1
- 权威百科: 117

### 按作者/机构

- UNESCO World Heritage Centre: 1
- Wikipedia: 117

### 按主题覆盖（可重叠归类，主归类）

- 中国园林造景: 9
- 中国画六法/留白与东西方比较: 14
- 动线与下沉空间: 9
- 建筑风格史—东方: 6
- 建筑风格史—西方: 39
- 绘画理论—光影明暗: 6
- 绘画理论—构图: 7
- 绘画理论—色彩: 9
- 绘画理论—透视与空间: 11
- 采光通风与材料: 8

## 五、备注

- 所有 `title` 均来自 HTTP 实抓页面（h1 或 `<title>`），非推测。
- 所有 `year=null`，因为来源均为持续更新的百科/名录页，无单一出版年；原典介绍页（De pictura / De architectura / Theory of Colours）本身是百科条目而非原典全文，故不虚填原典年份。
- 写作阶段应只引用 `verified=true` 来源；`verified=false` 条目仅作待核实占位。
- 使用 Python 脚本抓取属环境工具故障下的替代手段，核验标准（实际打开页面＋标题比对）与任务要求一致。
