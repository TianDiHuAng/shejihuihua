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

## 第 10 轮：来源实抓网络中断，回滚未核验来源（已处置）

- 现象：本轮拟新增的 12 份 Wikipedia 来源在生成脚本中按计划写入 verified=true，但 add_sources_round10.py 缺少实抓核验步骤；随后网络完全中断（en.wikipedia.org:443 / britannica.com 超时或 403，DNS 异常）。
- 处置：按「verified=true 必须实抓核对」硬性规则，已 `git checkout` 回滚 scope.md、coverage.json、coverage-matrix.md、data/sources.json、tools/gen_scope.py，并删除 entries/batch-10.json 与两个生成脚本。本轮改为：体检（F）+ 用现有已核验来源升级核心 L1→L2，不新增来源。
- 教训：新增来源脚本必须先 urllib 实抓并校验 title/H1 才能置 verified=true；不得硬编码 verified= 或 needs_verification 标志。
- 遗留：B1 的 7 条候选待网络恢复后实抓核验再纳入。
- 不影响已提交知识库、校验与站点生成。
- 第 10 轮推送：`git push origin master:main` 失败（`Failed to connect to github.com:443 after ~21s`）；本地提交 `5d464ee` 已完成，远端仍停留 `5d19478`，下轮补推。
- 第 11 轮推送：`git push` 报 `Recv failure: Connection was reset`；本地 `4e14d54` 已提交，远端仍 `9e6bafe`，下轮补推。另：本轮 12 份来源经 owiki.org 镜像+web_search 核验，canonical en.wikipedia.org 直连待网络恢复后复核。
- 第 12 轮推送：`git push` 报 `Empty reply from server`；本地 `49ef620` 已提交，远端仍 `9e6bafe`（本地 ahead 3），下轮补推。
- 第 13 轮推送：`git push` 报 `Recv failure: Connection was reset`；本地 `8fc50a1` 已提交，远端仍 `9e6bafe`（本地 ahead 5），下轮补推。
- 第 16 轮推送：`git push` 报 `Recv failure: Connection was reset`；本地 `4675af5` 已提交，远端仍 `fba0fd6`（本地 ahead 1），下轮补推。
- 第 19 轮推送：`git push` 报 `Recv failure: Connection was reset`；本地 `0bc3fcf` 已提交，远端仍 `8e5034b`（本地 ahead 1），下轮补推。
- 第 23 轮推送：`git push` 报 `Recv failure: Connection was reset`；本地 `f29973f` 已提交，远端仍 `8cf52f3`（本地 ahead 1），下轮补推。
- 第 24 轮推送：`git push` 报 `Empty reply from server`；本地 `2854579` 已提交，远端仍 `8cf52f3`（本地 ahead 3），下轮补推。
- 第 26 轮推送：`send-pack: unexpected disconnect` / `Failed to connect github.com:443`；本地 `be5c132` 已提交，远端仍 `0c280b3`（本地 ahead 1），下轮补推。
- 第 27 轮推送：`git push` 报 `Recv failure: Connection was reset`；本地 `6efda06` 已提交，远端仍 `0c280b3`（本地 ahead 3），下轮补推。
- 第 29 轮推送：`git push` 报 `Recv failure: Connection was reset`；本地 `d2d8e34` 已提交，远端仍 `00b04a1`（本地 ahead 1），下轮补推。
- 第 37 轮推送：`git push` 报 `Empty reply`/`Failed to connect`；本地 round37 提交已入库，远端仍 `b8597ee`（本地 ahead 1），下轮补推。
- 第 40 轮推送：`git push` 报 `Failed to connect github.com:443`；本地 round40 提交已入库，下轮补推。
- 第 41 轮推送若失败已记录；本地提交已入库，下轮补推。
- 第 42 轮推送：`git push` 报 `Recv failure: Connection was reset`；本地提交已入库，下轮补推。
- 第 43 轮推送：网络抖动；本地提交已入库，下轮补推。
- 第 45 轮（饱和）推送：`git push` 多次网络不可达（Empty reply / Failed to connect）。本地提交 `f7e06e7` 已入库；SATURATED=true 已达成，代码与站点均在本地完成，待网络恢复后 `git push origin master:main` 补推。
- 第 49 轮推送：网络不可达（Recv reset / connect failed）；本地提交已入库，下轮补推。
- 第 51 轮推送：网络不可达（Empty reply / connect failed）；本地提交已入库，下轮补推。
- 第 53 轮推送：网络不可达；本地提交已入库，下轮补推。
- 第 54 轮推送：网络重置；本地提交已入库，下轮补推。
- 第 55 轮推送：网络重置；本地提交已入库，下轮补推。
- 第 57 轮推送：网络重置；本地提交已入库（含 SVG 校验器加固），下轮补推。
- 第 63 轮推送：网络不可达；本地提交已入库，下轮补推。
- 第 65 轮推送：网络重置；本地提交已入库，下轮补推。
- 第 66/67 轮推送：网络不可达；本地提交已入库，下轮补推。
- 第 69 轮推送：网络重置；本地提交已入库，下轮补推。
- 第 70 轮推送：网络不可达；本地提交已入库。
- 第 72 轮推送：网络重置；本地提交已入库。
- 第 72/73 轮推送：网络反复不可达；本地提交已入库，待网络恢复补推。
- 第 73/74 轮推送：网络反复不可达；本地提交已入库，待网络恢复补推。
- 第 77 轮推送：网络重置；本地提交已入库。
- 第 77/78 轮推送：网络反复不可达；本地提交已入库。
- 第 78/79 轮推送：网络反复中断；本地提交已入库。
- 第 84 轮推送：网络重置；本地提交已入库。
- 第 87 轮推送：网络中断；本地提交已入库。
- 第 88 轮推送：网络中断；本地提交已入库。
- 第 89 轮推送：网络中断；本地提交已入库。
- 第 91 轮推送：网络中断；本地提交已入库。
- 第 91/92 轮推送：网络中断；本地提交已入库。
- 第 96 轮推送：网络中断；本地提交已入库。
- 第 100 轮推送：网络中断；本地提交已入库。
