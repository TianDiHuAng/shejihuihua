# BLOCKERS.md

记录连续 3 次失败且需跳过的问题。当前为空。

## 环境说明（非阻塞）

- 2026-11-22：web_search 工具返回搜索端点配置错误；web_fetch 返回 fetch failed。改用 Python urllib + 浏览器 User-Agent 抓取权威站点，Wikipedia 页面返回 HTTP 200，来源核验流程继续。详见 DECISIONS.md D05。
