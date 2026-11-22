# BLOCKERS.md

记录连续 3 次失败且需跳过的问题。当前为空。

## 第 2 轮：GitHub 推送网络不可达（已跳过）

- 连续 3 次 `git push origin master:main` 失败：
  1. `Empty reply from server`
  2. `Failed to connect to github.com:443 after 21049 ms`
  3. `Failed to connect to github.com:443 after 21096 ms`
- 本地提交已完成（`2aa585c`），远端仍停留在 `c61ffe8`。按 AUTONOMOUS.md 第六节记录后跳过，不死磕；下一轮网络恢复时补推。
- 本问题不影响本地知识库、校验与站点生成。
- 第 3 轮网络恢复：已成功执行 `git push origin master:main`（`c61ffe8..b03d382`），远端与本地同步；该阻塞解除。

## 第 4 轮：GitHub 推送再次不可达（已跳过）

- 连续 3 次 `git push origin master:main` 失败，均为 `Failed to connect to github.com:443 after ~21s`。
- 本地提交 `1d741b3` 已完成，远端仍停留在 `7672951`；按 AUTONOMOUS.md 第六节记录后跳过，下一轮网络恢复时补推。
- 本问题不影响本地知识库、校验与站点生成。

- 2026-11-22：web_search 工具返回搜索端点配置错误；web_fetch 返回 fetch failed。改用 Python urllib + 浏览器 User-Agent 抓取权威站点，Wikipedia 页面返回 HTTP 200，来源核验流程继续。详见 DECISIONS.md D05。

## 第 8 轮：GitHub 推送不可达（已跳过）

- 连续 3 次 `git push origin master:main` 失败：`Recv failure: Connection was reset`；两次 `Failed to connect to github.com:443 after ~21s`。
- 本地提交 `8bb83b9` 已完成，远端仍停留在 `09a899b`；按 AUTONOMOUS.md 第六节记录后跳过，下一轮网络恢复时补推。
- 本问题不影响本地知识库、校验与站点生成。
