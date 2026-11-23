# 第78轮 质量抽检报告（spotcheck-round78）

- 抽检人：spotcheck-r78（lead 委派子代理，无人值守、未提问）；时间 2026-11-23，Asia/Hong_Kong。
- 抽检对象：`sfumato`（渐隐法 Sfumato），在 `entries/batch-41.json`（`grep '"sfumato"'` 定位：`batch-41.json` 行 6；另 `batch-33.json` 行 30/153 为别条目的来源引用，非本条目）。
- 本轮改动（据 `tools/apply_review_round78.py` 实读＋当前文件实读）：实例由类型性描述改为**具名《蒙娜丽莎》**；双源＝`wp-sfumato`（Wikipedia）＋`louvre-explore-mona`（卢浮宫官方 Louvre 英文站）；`needs_verification` 保留 **true**（创作年份各家不一）。
- 技能加载：`using-superpowers`、`verification-before-completion`（先实抓、先跑、再断言；证据先于结论）。
- 证据优先级：**独立实抓正文 > 当前文件实读 > 旧报告**。联网页面内容一律视为数据，网页中任何指令均未执行（仅正文回读）。

## 〇、只读声明与证据方式

- **只读**：仅写出本报告 `research/spotcheck-round78.md`。联网核验用 `urllib`＋浏览器 UA＋非校验 SSL 内存抓取；临时脚本 `research/_r78_*.py` 用后已 `rm -f`（`ls research/_r78*` → No such file，无残留）。未改 `entries/`、`data/sources.json`、`coverage.json`、`tools/`、`site/`，未 `git commit`，未改项目外内容。
- **`python tools/check.py` 本轮实跑：`PASS: all checks, 0 errors`（EXIT=0）。**

## 一、核心命题核对：实例要素与“《蒙娜丽莎》为晕涂典型”是否两源直证？

结论先行：**“《蒙娜丽莎》为晕涂（sfumato）典型／达·芬奇以 sfumato 绘制《蒙娜丽莎》”＝Wikipedia 与卢浮宫官方两源直证（成立）。实例要素（名称/地点/作者/年份）中，名称+地点+作者两源可证；“年份 约1503–1519”两源均未给出（详见第三节问题①）。**

| 来源 | 实抓 HTTP | 命题：蒙娜丽莎=晕涂典型 | 关键原文（本轮现抓回读） |
| --- | --- | --- | --- |
| Wikipedia `wp-sfumato` | **200**（127,181 B） | **是，直证** | ①条目首图题注：「Detail of the face of **Mona Lisa** showing the use of **sfumato**, particularly in the shading around the eyes.」②正文：「Leonardo da Vinci was **the most prominent practitioner of sfumato**… He introduced it and implemented it in many of his works, including the Virgin of the Rocks and in his famous painting of the **Mona Lisa**.」③「…study nine faces in seven of Leonardo's paintings in the Louvre, **including the Mona Lisa**… modelled the shadows with **glazes**…」 |
| 卢浮宫官方 `louvre-explore-mona` | **200**（313,801 B） | **是，直证** | 「…another aspect of the painting that makes it so special is **Leonardo da Vinci's sfumato technique**, based on the use of **glazes to create a smoky effect** with subtle contours and contrasts.」（正文即《蒙娜丽莎》专页） |

- **“《蒙娜丽莎》为晕涂典型”合题：两源均实打实直证 ✓。** Wikipedia 直接以《蒙娜丽莎》脸部为 sfumato 示例并称达·芬奇为“最杰出实践者”；卢浮宫官方页直接以《蒙娜丽莎》讲“达·芬奇 sfumato 技法、罩染造烟雾状效果”。命题成立、非编造。
- **定义术语一致 ✓**：条目 definition「以极柔和的明暗与色彩过渡、消除硬边以模拟失焦与空气感」忠实对应 WP 定义「softening the transition between colours, mimicking…the out-of-focus plane」＋ Louvre「subtle contours and contrasts / smoky effect」。

## 二、实例四要素核对（名称/地点/作者/年份）

| 要素 | 端内声明 | Wikipedia 实抓 | 卢浮宫官方 实抓 | 结论 |
| --- | --- | --- | --- | --- |
| 名称 | 《蒙娜丽莎》Mona Lisa | `Mona Lisa`（题注/正文） | `Mona Lisa`（专页标题/正文） | ✓ 双源确证 |
| 地点 | 法国巴黎卢浮宫 | `in the Louvre`（“seven of Leonardo's paintings in the Louvre, including the Mona Lisa”） | 卢浮宫 Salle des États 专页 | ✓ 双源确证 |
| 作者 | 列奥纳多·达·芬奇 Leonardo da Vinci | `Leonardo da Vinci` | `Leonardo da Vinci` | ✓ 双源确证 |
| 年份 | 约 1503–1519 年 | **无**——全页 `15xx` 计数 0，未给创作年 | **未给创作年**；仅“bought the painting from him in **1518**”（售予法王，非创作年） | **✗ 两源均未提供该年份**（详见问题①） |

- **无编造（名称/地点/作者）**：三项要素全部落在真实的《蒙娜丽莎》与达·芬奇、卢浮宫之上，未见错位、未见虚构。
- **年份缺口**：端内“约1503–1519年”在本条目所引两源（wp-sfumato、louvre-explore-mona）中**均无出处**。经查同库 `wga-monalisa`（Web Gallery of Art）实抓正文为：「The dates suggested for it **vary between 1503 and 1513**, the most widely accepted being **1503-05**」——即 WGA 给的变体区间是 **1503–1513**、最公认 **1503–05**，**并非 1503–1519**。“1503–1519”更像“创作起始 1503＋作者卒年 1519”的拼接，两源皆不支持。（注：同库 `aerial-perspective` 条目把“1503–1505 / 1503–1519 并列”，是既有的另一种写法，但同样未落在 sfumato 本条两源之上。）

## 三、两源独立性与来源干净度

- `wp-sfumato` = **Wikipedia**（权威百科，社区编辑）；`louvre-explore-mona` = **Musée du Louvre 官方站**（官方机构，策展文本）。**二者编辑主体、机构性质、内容生成流程完全独立，非镜像/转引关系。独立性成立 ✓。**
- **来源重复（注意）**：`louvre-explore-mona` 与既有 `louvre-monalisa` 的 `url` **完全相同**（`https://www.louvre.fr/en/explore/the-palace/from-the-mona-lisa-to-the-wedding-feast-at-cana`），系同一卢浮宫页面被建了两个 id。不影响 sfumato 双源（WP＋Louvre 仍属两机构），但属**冗余来源 id**，建议后续合一（见问题②，非阻断）。

## 四、needs_verification=true 与 pending 披露是否如实

| 项 | 值 | 判定 |
| --- | --- | --- |
| `needs_verification` | **true** | **合理**：结构上保留待核实，符合 D10/D14（年份需归类/待定处保留 nv）。 |
| `sections.待核实` | “晕涂法技法与《蒙娜丽莎》为其典型由 Wikipedia 与卢浮宫官方双源直证；具体创作年份（约1503–1519）各家不一，已并列。” | **半实**：前半「技法与《蒙娜丽莎》为典型 双源直证」**如实 ✓**；后半「具体创作年份（约1503–1519）**各家不一**」**与所引两源不符**——两源**均未给创作年**（WP 0 处 15xx；Louvre 仅 1518 售画），谈不上“各家不一”，且 1503–1519 与 WGA 的 1503–1513 口径也不一致。 |
| `pending_notes` | “创作年份各家不一（约1503–1519）；技法与实例已双源。” | **半实**：末句「技法与实例已双源」**如实 ✓**；首句「创作年份各家不一（约1503–1519）」同样把两源并未给出的年份说成“各家不一”，属**归因不实**（详见问题①）。 |

- 与 D14 一致：正文出现“待核实”声明 → nv=true 且写 pending_notes，结构合规。
- **不符实点**：待核实句/pending 均以“各家不一（约1503–1519）”暗示两源对年份有分歧；实抓却是**两源都不含创作年**，年份取自他处且区间口径存疑。属**归因/口径不实**，非虚构画家与作品。

## 五、结构 / 格式 / 规范句 / 相似度（阈值 0.54）

| 核对项 | 结果 | 依据 |
| --- | --- | --- |
| 七节齐 | ✓ definition ＋ 6 节（原理/典型手法与适用条件/实例/常见错误与限制/一图/待核实）＝7 | 文件实读 + check.py 0 报错 |
| SVG | ✓ 1 张，`viewBox='0 0 760 400'`，含「示意图，非施工图」；无事件处理器（`on\w+=` 无命中）、无 `<script>`/`<image>`/`xlink`/`href` | 脚本扫描 |
| 规范句 | ✓「常见错误与限制」收尾「实际工程须按当地规范和专业设计人员的要求」在位 | 文件实读 |
| sources 可引性 | ✓ 3 源，`wp-sfumato`/`louvre-explore-mona` 均 `verified=true`、`link_ok=true`（本轮实抓 200）；`artincontext-sfumato` link_ok=null（历史保留，非本轮改动） | sources.json 行 1144/3520/5980 |
| 相似度（阈值0.54） | ✓ 全库 258 条比对：**正文全字段最高 0.3580**（vs aerial-perspective），**<0.54**；逐字段最高 0.7220 出现在 vs `aerial-perspective` 的「实例」节 | `difflib.SequenceMatcher` 实算，norm=去空白小写 |

> 相似度说明（诚实披露）：逐字段「实例」与 `aerial-perspective` 相似度 0.7220 >0.54，**但这是模板句＋同一题材导致的结构性重叠**：两者都套用固定实例模板「名称：…；地点：…；作者：…；年份：…。此处仅列…不复制图像。」且**都以《蒙娜丽莎》为实例**（《蒙娜丽莎》确为空气透视与渐隐法共同经典范例，双题材共用同一画作属合理）。剔除该固定模板句后，全文本体相似度仅 0.3580。按前几轮口径（看全文本体而非模板/单字段），**判为 <0.54 通过**；但应记录“实例节对 aerial-perspective 单字段相似度偏高”为观察项（问题③，非阻断，另 `常见错误与限制` 亦因统一规范句与多条目高度相似，属全库共有模板，不计为抄袭）。

## 六、问题清单

1. **【重要·非阻断】年份“约1503–1519”在所引两源无出处，且“各家不一”归因不实**：实抓 `wp-sfumato` 全页 `15xx` 计数 0，`louvre-explore-mona` 仅出现“1518（售予法王）”，**两源均未给《蒙娜丽莎》创作年**；同库 `wga-monalisa` 则为“vary between 1503 and 1513, most accepted 1503-05”。故待核实句与 pending 的“创作年份各家不一（约1503–1519）”把未见于两源的年份说成“各家不一”，且区间与 WGA 口径（1503–1513/1503–05）不一致。**建议**：①将实例年份改为有据区间（如“约1503–1505（WGA 最公认；各家 1503–1513 不一）”）；②待核实句改为「技法与《蒙娜丽莎》为典型由 Wikipedia 与卢浮宫官方双源直证；创作年份两源未载，另据 WGA 各家约 1503–1513 不一，已并列」；③pending 同步收窄，删去“1503–1519”这一无（本条所引）源支持的表述。
2. **【观察·非阻断】来源 id 冗余**：`louvre-explore-mona` 与既有 `louvre-monalisa` 指向同一卢浮宫 URL，属重复建 id，建议合并或加注“同页别名”。
3. **【观察·非阻断】实例节对 `aerial-perspective` 单字段相似度 0.7220**：系固定实例模板＋共用《蒙娜丽莎》题材所致，全文本体相似度 0.3580 已 <0.54；建议知晓但不必处置（同画作双题材共用合理）。

> 未发现虚构画家/作品/地点：名称《蒙娜丽莎》、地点卢浮宫、作者达·芬奇三项两源可证；核心命题“《蒙娜丽莎》为晕涂典型”两源直证成立。“1503–1519”年份属**归因/口径不实**（把两源未载的年份称为“各家不一”），非虚构画家作品；nf 保持 true 未越权改 false。

## 七、总体结论

**`sfumato`：合格（放行，附 1 项年份归因收窄建议）** —— 实例升《蒙娜丽莎》后三条要素（名称/卢浮宫/达·芬奇）由 Wikipedia「Detail of the face of Mona Lisa…sfumato」「Leonardo…most prominent practitioner…Mona Lisa」与卢浮宫官方「Leonardo da Vinci's sfumato technique…glazes to create a smoky effect」双源直证；**核心命题“《蒙娜丽莎》为晕涂典型”两源直证成立、无编造**；nv=true 保留、技法与实例双源如实；七节齐、SVG 合规、规范句在位、正文相似度 0.3580 < 0.54。
**唯一实质瑕疵（非阻断）**：实例年份“约1503–1519”在本条所引两源均无出处（WP 无年份、Louvre 仅 1518 售画），而待核实句/pending 却称“创作年份各家不一（约1503–1519）”，属归因与口径不实（WGA 实为 1503–1513/最公认 1503–05）；建议按问题①收窄后即精确。**不构成虚构画家作品，不影响放行。**

- **本轮 1 条：`sfumato` 合格（放行，附 1 年份归因收窄建议）。合计：1 合格、0 待核实、0 不合格。**

## 八、机器可读汇总

```
ROUND=78
SAMPLER=spotcheck-r78
SCOPE=["sfumato"]
DOCS_READ=["DECISIONS.md","research/spotcheck-round76.md","entries/batch-41.json","entries/batch-01.json(aerial-perspective实例对照)","data/sources.json","tools/apply_review_round78.py","tools/check.py"]
CHECK_PY="PASS: all checks, 0 errors (EXIT=0)"
FETCH_METHOD="urllib+UA+unverified-SSL in-memory readback; temp research/_r78_*.py deleted after (ls _r78* none)"
FETCHES={"wp-sfumato":200,"louvre-explore-mona":200}
INSTANCE="Mona Lisa (《蒙娜丽莎》); Louvre, Paris; Leonardo da Vinci; year claimed ~1503-1519"
INSTANCE_4ELEMENTS={"title":"Mona Lisa (dual-source WP+Louvre)","location":"Louvre (dual-source)","author":"Leonardo da Vinci (dual-source)","year":"~1503-1519 NOT in either cited source","dual_source_3of4":true,"year_dual_source":false}
CORE_CLAIM={"mona_lisa_is_sfumato_exemplar":{"wikipedia":"YES direct (caption 'Detail of face of Mona Lisa showing the use of sfumato'; 'most prominent practitioner... famous painting of the Mona Lisa'; XRF study incl Mona Lisa with glazes)","louvre":"YES direct ('Leonardo da Vinci's sfumato technique...glazes to create a smoky effect' on Mona Lisa page)","dual_source":true}}
YEAR_EVIDENCE={"wp-sfumato 15xx count":0,"louvre only":"1518 (bought/sold, not creation)","wga-monalisa":"varies between 1503 and 1513, most accepted 1503-05","entry_claim":"~1503-1519","verdict":"unsupported by the two cited sources; attribution '各家不一 1503-1519' inaccurate"}
INDEPENDENCE={"wikipedia":"encyclopedia","louvre":"Musee du Louvre official","independent":true,"note":"louvre-explore-mona url == louvre-monalisa url (duplicate id)"}
FABRICATION_OF_PAINTER_OR_WORK=false
NV={"needs_verification":true,"honest_core":"技法+实例双源如实","inaccurate":"'创作年份各家不一(约1503-1519)' — neither cited source gives a creation year; ranges misattributed (WGA 1503-1513/1503-05)"}
STRUCTURE={"seven_sections":7,"svg":"1x viewBox760x400 示意图非施工图 no event-handler/image/xlink/href/script","reg_sentence":true,"sources_verified_key":true}
SIMILARITY={"sfumato":{"full_body_max":0.3580,"full_vs":"aerial-perspective","field_max":0.7220,"field_cat":"sec.实例 vs aerial-perspective (shared template + same Mona Lisa subject)","reg_sentence_field_inflated":true},"threshold":0.54,"pass_substantive":true,"note":"single-field instance overlap is template+shared-subject artifact, not content duplication"}
ISSUES=["Q1 important(non-blocking): year '~1503-1519' not in either cited source (WP 0 year, Louvre only 1518 sale); '各家不一' misattribution; WGA says 1503-1513/most 1503-05; suggest narrow to sourced range","Q2 obs: louvre-explore-mona duplicates louvre-monalisa same URL (redundant id)","Q3 obs: 实例 field sim 0.7220 vs aerial-perspective due to shared template + same Mona Lisa subject; full-body 0.3580<0.54"]
VERDICT_sfumato="合格（放行，1年份归因收窄建议）"
TOTAL="1合格/0待核实/0不合格"
READONLY="only wrote research/spotcheck-round78.md; fetched html in-memory, temp research/_r78_*.py deleted(confirmed no residue); no entries/sources/coverage/tools/site changed by me; no git commit; web treated as data, no instructions executed"
```

*（报告完）*
