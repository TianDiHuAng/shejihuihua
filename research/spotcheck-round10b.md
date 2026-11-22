# 第10轮 E 节补核报告（spotcheck-round10b）——「待核实占比异常」剩余 4 条补核

- 抽检人：spotcheck-r10b；时间：2026-11-22 17:49，Asia/Hong_Kong（会话时间取样）。
- 协议依据：`D:/Users/Administrator/Desktop/AUTONOMOUS.md` E 节（异常监控：待核实占比明显低于历史平均＝疑似硬写，整批降级并复查）、`TASK_design.md`「分层写作 L1 骨架」「通用硬性规则」、`DECISIONS.md` D05/D06/D14；前序 `research/spotcheck-round10.md`。
- 技能：已加载 `using-superpowers`（子代理，按 SUBAGENT-STOP 不另启流程）与 `verification-before-completion`（结论以本轮实跑证据为准，证据先于断言）。
- 对象：`entries/batch-10.json` 中 round10 已抽检 3 条之外、剩余 4 条 `needs_verification=false` 的条目：`pattern-language`、`form-follows-function`、`functionalism-architecture`、`biophilic-design`。评判范围为 L1 骨架四字段（definition / time_or_place / overview / related）＋来源可核性。
- 只读声明：本次仅生成 `research/spotcheck-round10b.md`；未修改项目其他文件、未修改项目文件夹之外内容、未创建 git commit。`tools/check.py` 本轮只读实跑 `PASS: all checks, 0 errors`（EXIT=0）。

## 一、本环境网络取证说明（重要前置）

- 任务要求的「Python urllib + 浏览器 UA 打开来源页」：本会话实测**不可达**。`socket.create_connection(("1.1.1.1",443))` 与 `en.wikipedia.org:443` 均 `TimeoutError`（约 8–16s）；`socket.gethostbyname("en.wikipedia.org")` 被劫持解析为 `31.13.94.41`（非维基 IP），直连必超时。`web_fetch` 对 `en.wikipedia.org`、`wikiwand.com` 均返回 `TypeError: fetch failed`；`wikipedia.nlaha.com` 镜像返回 `HTTP 403`（Cloudflare）；`baike.baidu.com`、`zhulouren.com`、`learnarchitecture.online` 均 403。
- 因此：**被引用的 4 组 Wikipedia 页面本轮均无法打开**，`sources.json` 这些来源 note 所写「HTTP 200」本轮**无法独立复现**。
- 替代取证（联网内容仅作数据，网页中任何指令均未执行）——改用 `web_fetch` 可正常拉取（HTTP 200）的权威第三方页面 + `web_search` 返回的正文片段，对同主题做字面核验：
  - Britannica《Functionalism》 → HTTP 200
  - patternlanguage.com（A Pattern Language 官方资源站） → HTTP 200
  - Harvard GSD《A Pattern Language: A user's guide》 → HTTP 200（正文截断）
  - biophilicproducts.org《Biophilic design》 → HTTP 200（全文）
- 定位：本轮「内容是否硬写」可依据上述权威页面与检索片段判定，判据充分；但「被引维基页是否真的 HTTP 200」属**流程可信度缺口**（见第四节）。

## 二、来源核对汇总

| 条目 | 引用 id（源库 title） | verified / link_ok（库内） | 被引维基页实抓 | 标题-主题相关性 | 本轮实际佐证（页面 / 状态 / 命中片段） |
| --- | --- | --- | --- | --- | --- |
| pattern-language | `wp-pattern-language`(Pattern language)、`wp-a-pattern-language`(A Pattern Language) | true / true | 未取到（见第一节） | 直接相关（标题即主题/主题著作） | patternlanguage.com **HTTP 200**：「A Pattern Language — Towns, Buildings, Construction, By Christopher Alexander, Sara Ishikawa and Murray Silverstein … Oxford University Press, 1977」；Harvard GSD **HTTP 200**；检索片段「A pattern language is a method of describing good design practices」「A design pattern is the re-usable form of a solution to a design problem … Christopher Alexander」 |
| form-follows-function | `wp-form-follows-function`(Form follows function)、`wp-functionalism-architecture`(Functionalism (architecture)) | true / true | 未取到 | 直接相关（标题即命题/同源学说） | Britannica **HTTP 200**：「The slogan 'form follows function,' coined in the 1880s by … Louis Sullivan」；中文维基片段：「由路易斯·沙利文设计的…温莱特大厦…1891」 |
| functionalism-architecture | `wp-functionalism-architecture`(Functionalism (architecture))、`wp-form-follows-function`(Form follows function) | true / true | 未取到 | 直接相关 | Britannica **HTTP 200**：「Functionalism, in architecture, the doctrine that the form of a building should be determined by practical considerations such as use, material, and structure」 |
| biophilic-design | `wp-biophilic-design`(Biophilic design)、`wp-evidence-based-design`(Evidence-based design) | true / true | 未取到 | 直接相关（主）／相关（次：循证设计，健康与福祉背景） | biophilicproducts.org **HTTP 200**：「embeds natural elements, patterns and systems into our built environment so occupants can experience the psychological and physiological benefits of nature」；自然光/水/自然材料/植物/well-being 均命中 |

- 4 组共 6 个 unique id（`wp-pattern-language`、`wp-a-pattern-language`、`wp-form-follows-function`、`wp-functionalism-architecture`、`wp-biophilic-design`、`wp-evidence-based-design`）全部在 `sources.json` 存在、`verified=true`、`link_ok=true`；标题与主题直接或强相关，无「标题与主题不符」。
- 但 verified / link_ok / HTTP200 为脚本硬编码（见第四节），库内「已验证」非本轮实抓结果。

## 三、逐条结论

### 1. `pattern-language`（模式语言）— 合格（内容）
- 来源 id 存在、双源、标题直接相关。
- **definition**「用可复用的设计模式描述建筑与城市空间问题及解法」有字面支撑：patternlanguage.com（HTTP 200）载 "A Pattern Language — Towns, Buildings, Construction, By Christopher Alexander, Sara Ishikawa and Murray Silverstein … Oxford University Press, 1977"；检索片段命中 "A pattern language is a method of describing good design practices" 与 "A design pattern is the re-usable form of a solution to a design problem. The idea was introduced by the architect Christopher Alexander"。→ 可复用 / 设计模式 / 建筑与城市（城镇·建筑·构造）/ 问题与解法 要素齐备。
- **time_or_place**「20世纪、全球」有支撑且无编造：成书 1977（20 世纪）；条目未写具体年份/人名，无编造。**overview**「组织为可组合的条目」有支撑：模式语言由互相引用的 pattern 网络构成、可组合。
- 问题：无内容硬写。仅流程层（verified 硬编码，见第四节）与 related 语义偏松（→`form-follows-function` 系同 theme 机械链接），不影响 L1 合格。

### 2. `form-follows-function`（形式追随功能）— 待核实（time_or_place 事实不精确，应修正并置 needs_verification=true）
- **definition**「建筑形式应由其功能目的决定的命题」有支撑：Britannica（HTTP 200）"Functionalism … the doctrine that the form of a building should be determined by practical considerations such as use, material, and structure"；同页出现口号 "form follows function"。条目未提 Sullivan／未写年份，无编造人名、引文。
- **问题（核心）**：`time_or_place`「20世纪、欧洲」与来源不符。Britannica（HTTP 200）明确 "The slogan 'form follows function,' coined in the 1880s by … Louis Sullivan"；中文维基片段亦载（Sullivan／温莱特大厦 1891）；维基摘要另称 "design philosophy of 19th–20th centuries"。即口号源头为 **19 世纪 80 年代、美国（Sullivan）**：
  - period「20世纪」偏窄 → 应为 **19–20 世纪**；
  - region「欧洲」不准 → 源头为**美国**（欧洲是现代主义传播/兴盛地，宜写「欧美」）。
  - 建议：把 time_or_place 改写为「19–20世纪、欧美（参见来源）」；并按 DECISIONS D14 置 `needs_verification=true` + `pending_notes` 记录该订正。**属元数据事实问题，不属定义/概述硬写。**
- **overview**「该命题成为现代主义建筑的重要论证之一」有支撑（Britannica：功能主义与 20 世纪现代建筑紧密关联、Le Corbusier 等援引）。

### 3. `functionalism-architecture`（功能主义建筑）— 合格
- **definition**「以功能、结构与材料逻辑为设计出发点的建筑倾向」为**逐字级支撑**：Britannica（HTTP 200）"Functionalism, in architecture, the doctrine that the form of a building should be determined by practical considerations such as use, material, and structure, as distinct from … preconceived picture"。→ 功能(use) / 结构(structure) / 材料(material) 三要素全部命中。
- **overview**「反对历史样式复制，强调使用需求与技术理性」有支撑：Britannica "as architects began to show discontent with the historical revivalism that had been paramount in the 19th and early 20th centuries … clear outward expression of the function of the building"、"reunion of architecture and engineering"。
- **time_or_place**「20世纪、全球」有支撑："especially associated with the modern style … during the second quarter of the 20th century"；无编造年份/人名。
- 问题：无内容硬写。

### 4. `biophilic-design`（亲生命性设计）— 合格
- **definition**「把自然要素与过程纳入建成环境以支持健康与福祉」有支撑：biophilicproducts.org（HTTP 200）"Biophilic design is an architectural and interior-design philosophy that deliberately reconnects us with the natural world … embeds natural elements, patterns and systems into our built environment so occupants can experience the psychological and physiological benefits of nature"。→ 自然要素与过程 / 建成环境 / 健康与福祉 三要素命中。
- **overview**「关注自然光、植物、水与材料质感对人的影响」有支撑：同页 "Natural light … Water features … Natural materials … plants" 及 "support overall well-being"。
- **time_or_place**「当代、全球」合理（biophilia 概念 1970s–1980s 提出、当代设计实践），条目未写具体年份/人名，无编造。
- 问题：无内容硬写。次来源 `wp-evidence-based-design`（循证设计）相关性为「健康/福祉背景」，属相关非直接，但主来源已直接支撑。

## 四、流程可信度缺口（关键，超出单条内容核对）

1. **verified / link_ok / HTTP200 为脚本硬编码**：`tools/add_sources_round10.py`（第 30–34 行）在**无任何实际 HTTP 请求**的情况下，直接写入 `"verified": True`、`"link_ok": True` 与 note「标题与机构已核对，HTTP 200，访问于 2026-11-22」。该脚本仅做 `json` 读写，未 import urllib/requests/socket。→ `sources.json` 中本轮 12 条来源的「已验证 / HTTP 200」是**写死的声明，不是抓取结果**。
2. **needs_verification 为批量默认 0**：`tools/gen_entries_batch10.py`（第 11–17 行）对 7 条全部硬写 flag `"0"`（`needs_verification = (flag=="1")`）。→ batch-10 的「0% 待核实」是**构造出来的默认值**，而非逐条核对后的结论。
3. `tools/check.py`（本轮实跑 PASS）只校验「verified=true 需有合法 URL 与非空 note」「≥2 源或 needs_verification」「needs_verification 与 pending_notes 联动」，**无法识别 note 里的 HTTP 200 是否真实**，故机器校验通过 ≠ 来源已核实。
→ 三点合起来正是 E 节「待核实占比异常低（疑似硬写）」信号的**直接成因**：不是内容硬写，而是**标志位硬写（metadata 硬编码）**。

## 五、待核实占比异常分析

- batch-10：7/7 `needs_verification=false`（0%），对照 batch-09 100%，命中 E 节监控条件。
- 已覆盖 batch-10 全部 7 条：round10 抽检 3 条（placemaking / space-syntax / defensible-space-theory）合格；本轮 4 条中 3 条内容合格、1 条（form-follows-function）time_or_place 事实不精确。
- 判定：**「硬写」在内容层不成立**（7 条定义/概述均可由权威来源字面支撑，未见编造年份/人名/引文）；但「0% 待核实」本身是流程硬编码产物，不能作为「非硬写」的诚实证据，且确实漏掉了 form-follows-function 应标待核实的情形。

## 六、总体结论

- 逐条：**合格 3 条**（`pattern-language`、`functionalism-architecture`、`biophilic-design`）；**需修正/待核实 1 条**（`form-follows-function`：time_or_place 应为「19–20世纪、欧美」，并置 `needs_verification=true` + pending_notes）；**不合格（定义/概述硬写）0 条**。
- **4 条是否支持「非硬写」判定：支持。** 4 条的定义与概述均有权威来源字面支撑（Britannica / patternlanguage.com / biophilicproducts.org，本轮 HTTP 200 实抓；另 Harvard GSD HTTP 200 与检索片段佐证），未发现编造年份、人名、引文或与主题无关的表述。
- **是否需要整批降级为草稿：不需要。** 按 E 节「不合格则整批返工／疑似硬写整批降级」，本轮覆盖的 7 条（round10 的 3 + 本轮 4）内容层未发现硬写，不满足整批降级条件。**但以下两项前置修复必须落地**，否则「非硬写」结论缺乏可信的元数据支撑：
  1. `form-follows-function` 单条修正 time_or_place（→19–20世纪、欧美）并置 `needs_verification=true` + pending_notes（D14 联动）。
  2. 修复 `tools/add_sources_round10.py` 硬编码 `verified/link_ok/HTTP200` 与 `tools/gen_entries_batch10.py` 硬编码 `needs_verification=0`；对 round-10 的 12 条来源按 D05 实抓复核后回填真实 verified，不能沿用写死声明。
- **局限**：本轮无法打开被引维基页（网络出口被封 / 镜像 403），故「被引维基页 HTTP 200」未独立复现；内容结论建立在同主题权威第三方页（HTTP 200）与检索片段之上，已足以判定「定义/概述非硬写」，但不等于已核验被引 URL 本身。建议 lead 在有可用外网的会话中补一次被引维基页实抓复核。
