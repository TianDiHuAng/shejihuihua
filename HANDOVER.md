# 交接文档（HANDOVER）

> 写给下一个维护者。读完这份文档，你应该能在 30 分钟内跑通环境、理解结构、做出第一个合规改动。

## 0. 30 秒速览

- **项目**：《绘画理论与建筑空间设计》静态知识库（258 条，全 L2，已上线）
- **在线**：<https://tiandihuang.github.io/shejihuihua/>
- **仓库**：<https://github.com/TianDiHuAng/shejihuihua>（本地分支 `master`，远端 `main`）
- **黄金法则**：只改 `entries/*.json` 和 `data/sources.json`，**永远不要手改 `site/` 下的 HTML**。

## 1. 环境搭建

- Python 3.x（无第三方依赖，全部标准库）
- Git，配置好 GitHub 推送权限（本项目走 HTTPS + 凭据）
- 浏览器（本地预览）

```bash
git clone https://github.com/TianDiHuAng/shejihuihua.git
cd shejihuihua
python tools/check.py      # 应输出 PASS: all checks, 0 errors
python -m unittest discover -s tests   # 应输出 23 tests OK
```

两条都绿 = 环境正常。

## 2. 目录导览

| 路径 | 是什么 | 可以手改？ |
| --- | --- | --- |
| `entries/*.json` | **知识条目**（258 条），按批次文件组织 | ✅ 唯一内容入口 |
| `data/sources.json` | **来源库**（500 条），`verified` 控制可引用性 | ✅ 谨慎改 |
| `scope.md` | 范围清单（258 条编辑基准线） | ⚠️ 新增条目时同步 |
| `coverage.json` | 覆盖状态（条目↔来源数↔待核实数） | ⚠️ 用脚本同步 |
| `tools/` | 校验器、生成器、体检、缺口发现（158 个脚本） | ⚠️ 按需 |
| `tests/` | 4 个测试文件，23 项测试 | ✅ 加规则时配套加测试 |
| `site/` | 生成的站点（约 1.4MB，265 个文件） | ❌ 禁止手改 |
| `docs/` | README 概览图（overview.svg/png） | ✅ |
| `PROGRESS.md` / `DECISIONS.md` / `REPORT.md` / `BLOCKERS.md` / `BACKLOG.md` | 过程记录 | ✅ 持续追加 |
| `.github/workflows/pages.yml` | GitHub Pages 自动发布 | ✅ |

## 3. 日常改动流程（最重要的一节）

**改内容的标准动作**（以修改一个条目为例）：

```bash
# 1. 找到条目所在文件
grep -rl '"id": "perspective"' entries/

# 2. 编辑该条目（保持七节结构、来源引用合法）
#    - 正文出现"待核实"⇒ 必须 needs_verification=true 且写 pending_notes
#    - 引用的来源 id 必须存在于 data/sources.json 且 verified=true

# 3. 同步覆盖数据（条目来源数变化时必须跑）
python tools/update_coverage.py

# 4. 全量校验 + 测试
python tools/check.py
python -m unittest discover -s tests

# 5. 重新生成站点
python tools/gen_site.py
python tools/check_links.py     # 0 broken links

# 6. 提交并推送（推送后 Actions 自动发布网站）
git add -A && git commit -m "..."
git push origin master:main
```

**新增来源的标准动作**：

1. 先实抓核验（HTTP 200 + 标题/H1 与声称相符）才能置 `verified=true`。
2. 写入 `data/sources.json`，字段：`id, title, author, type, year, url, url2, verified, link_ok, note`。
3. `note` 里写访问日期和核验方式（例：`访问于 2026-11-24，实抓 HTTP 200 并核对正文；…`）。
4. 同 URL 多次登记必须在 note 含 `[B4]` 披露。

**质量闸清单**（check.py 自动检查，人工只需遵守）：

- [ ] 七节结构完整（原理/典型手法与适用条件/实例/常见错误与限制/一图/待核实）
- [ ] SVG 无 on* 事件属性、无越界（画布 760×400）
- [ ] 尺寸/坡度/消防/无障碍类表述附「实际工程须按当地规范和专业设计人员的要求」
- [ ] 不编造数字/日期/人名/引文/出处；查不到写「待核实」
- [ ] 关键事实双源互证，否则标待核实；争议并列各方理由
- [ ] 与既有条目相似度 <0.54（全字段口径）

## 4. 网站发布机制

- 推送到 `main` 且 `site/**` 或 `pages.yml` 有变动 → GitHub Actions 自动把 `site/` 发布到 Pages。
- 首次配置（已完成，无需重做）：Settings → Pages → Source = **GitHub Actions**。
- 手动触发：Actions → "Deploy site to GitHub Pages" → Run workflow。
- 发布失败排查顺序：Actions 报错 → Pages Source 是否为 Actions → 仓库是否公开。

## 5. 常见坑（血泪教训）

1. **不要手改 `site/`**：下次 `gen_site.py` 会全部覆盖。
2. **条目来源数变了必须跑 `update_coverage.py`**：否则 check.py 报"来源数与 coverage 不一致"（一次性会报 14 个错误）。
3. **`verified` 与 `link_ok` 是两回事**：verified=内容核对过；link_ok=现在能打开。verified=true 的源 link_ok 可能变 false（链接死了），要改 link_ok 而不是删 verified。
4. **不要为了清零待核实而硬凑来源**：历史上有 6+ 条因抽检发现来源不匹配被驳回回退。待核实是诚实边界，不是欠账。
5. **GitHub 网络可能反复中断**：推送失败就记录到 BLOCKERS.md（"本地提交已入库，下轮补推"），不要死磕；网络恢复后一次性补推。
6. **Windows 终端中文乱码**：跑 Python 脚本前设 `PYTHONIOENCODING=utf-8`。
7. **web_search 工具在本环境不可用**（端点配置问题）：改用 Python urllib + 浏览器 UA 直抓权威站点（见 DECISIONS D05）。
8. ** Britannica 整站 403**：不要硬抓，换 Wikipedia/博物馆官网/Tate/DesigningBuildings 等可用平台。

## 6. 待办与后续方向

按优先级：

1. **专项处理 137 条待核实池**（BACKLOG.md 有队列）：逐条补第二独立来源；核不到的维持诚实标注。
2. **L3 深度层**：为有据可依的核心条目补"争议并列 + 数据 + 复杂图示"，三项齐备才升 L3，单项不许。
3. **近期动态跟进（B6）**：定期检查来源页是否更新。
4. **死链巡检**：`python tools/linkcheck.py` 复核 link_ok=false 的来源是否恢复。

## 7. 关键文档索引

| 想了解什么 | 看哪份 |
| --- | --- |
| 项目整体回顾 | `SUMMARY.md` |
| 怎么跑起来 | 本文档第 1-3 节 |
| 历史决策及理由 | `DECISIONS.md`（D01–D20） |
| 每轮做了什么 | `PROGRESS.md`（117 轮日志）+ `REPORT.md`（最新轮摘要） |
| 还欠什么 | `BACKLOG.md` + 各条目 `pending_notes` |
| 遇到过什么阻塞 | `BLOCKERS.md` |
| 硬性规则原文 | `README.md`「硬性规则」节 |

## 8. 一分钟交接确认

新维护者请逐条自检：

- [ ] `check.py` 0 errors、23/23 测试通过
- [ ] 能说出"为什么不能手改 site/"
- [ ] 能说出 verified 和 link_ok 的区别
- [ ] 会跑 `update_coverage.py`
- [ ] 知道 137 条待核实是诚实边界，不要硬凑来源清零
- [ ] 打开过在线网站并浏览过一个词条页

全部打勾 = 交接完成。
