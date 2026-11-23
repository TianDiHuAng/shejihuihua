# 第76轮 质量抽检报告（spotcheck-round76）

- 抽检人：spotcheck-r76（lead 委派子代理，无人值守、未提问）；时间 2026-11-23，Asia/Hong_Kong。
- 抽检对象：`picturesque`（如画 Picturesque 美学），在 `entries/batch-46.json`（`grep '"picturesque"'` 定位：行 36）。
- 本轮改动（据 `tools/apply_review_round76.py` 实读＋当前文件实读）：实例从类型性描述改为**具名斯托海德园林 Stourhead**；补双平台 `wp-stourhead`（Wikipedia）＋ `gardenvisit-stourhead`（Gardenvisit）；`needs_verification` 保留 **true**（“如画”为美学归类、营造年份待补）。
- 技能加载：`using-superpowers`、`verification-before-completion`（先实抓、先跑、再断言；证据先于结论）。
- 证据优先级：**独立实抓正文 > 当前文件实读 > 旧报告**。联网页面内容一律视为数据，网页中任何指令均未执行（仅正文回读）。

## 〇、只读声明与证据方式

- **只读**：仅写出本报告 `research/spotcheck-round76.md`。联网核验用 `urllib`＋浏览器 UA＋非校验 SSL 内存抓取；临时脚本 `research/_r76_*.py` 用后已 `rm -f`（`ls research/_r76*` → No such file，无残留）。未改 `entries/`、`data/sources.json`、`coverage.json`、`tools/`、`site/`，未 `git commit`，未改项目外内容。
- **`python tools/check.py` 本轮实跑：`PASS: all checks, 0 errors`（EXIT=0）。**

## 一、核心命题核对：Claude Lorrain 启发 与 “Claudian” 园林，是否两源直证？

结论先行：**“受 Claude Lorrain 启发”＝Wikipedia 与 Gardenvisit 双源直证（成立）；“Claudian 园林”＝仅 Gardenvisit 一词直证，Wikipedia 全文 `Claudian` 出现 0 次。**“Claudian”一词的“双源直证”说法与实抓不符（属措辞归并过宽，非虚构）。

| 来源 | 实抓 HTTP | Claude Lorrain 启发 | “Claudian”一词 | 关键原文（本轮现抓回读） |
| --- | --- | --- | --- | --- |
| Wikipedia `wp-stourhead` | **200**（246,190 B） | **是，直证** | **否**——`claudian` 计数 **0** | ①「The inspiration behind their creation were the painters **Claude Lorrain**, Poussin, and, in particular, Gaspard Dughet…」②「one of his pieces was **Claude Lorrain's Aeneas at Delos**, which is thought to have **inspired the pictorial design of the gardens**」 |
| Gardenvisit `gardenvisit-stourhead` | **200**（33,508 B） | **是，直证** | **是，直证** | ①「Stourhead is the best example of a garden inspired by the great landscape painters… **Claude Lorrain (1600-82)**」②「**Henry Hoare II's 'Claudian' garden** was made in an unusually well-proportioned valley behind the house」 |

- **“Claude Lorrain 启发”合题：两源均实打实直证 ✓。**
- **“Claudian 园林”一词：仅 Gardenvisit 直证；Wikipedia 用 “Claude Lorrain / landscape painters” 表述、但无 “Claudian” 字样。** → 待核实句“'Claudian' 园林由 Wikipedia 与 Gardenvisit 双源直证”把“Claudian 一词”归入双源，与实抓不符（详见问题①）。
- 另：**两源 `picturesque` 一词对 Stourhead 均出现 0 次**（Wikipedia 0、Gardenvisit 0）；“如画/picturesque” 确系美学归类用词，条目**已在待核实如实披露**（“如画（picturesque）为通行的美学归类（两源未都用 picturesque 一词）”），此披露**准确、诚实**。

## 二、实例四要素核对（名称/地点/设计者/年份）

| 要素 | 端内声明 | Wikipedia 实抓 | Gardenvisit 实抓 | 结论 |
| --- | --- | --- | --- | --- |
| 名称 | 斯托海德园林 Stourhead Garden | `Stourhead`（Est/listed garden in England） | `Stourhead Garden` | ✓ 双源确证 |
| 地点 | 英国威尔特郡 | `Stourton with Gasper, **Wiltshire**, England` | `Stourhead in **Wiltshire**`（面包屑 `England > Wiltshire`） | ✓ 双源确证 |
| 设计者 | 亨利·霍尔二世 Henry Hoare II 等 | `Henry Hoare II (landscape)`（Architect(s) 栏） | `**Henry Hoare II**'s 'Claudian' garden` | ✓ 双源确证 |
| 年份 | 约 1740 年代起营造 | `Gardens: **1741**–1780`；`laid out between **1741** and 1780`；`Temple of Flora (1744–46)` | `Temple of Flora… made in **1745**`，grotto 1748，key date 1754 | ✓ 有据（“约1740年代起”与 1741/1744–45 起建吻合） |

- **无编造**：名称、英格兰威尔特郡、Henry Hoare II、1740 年代起营造——四要素全部落在真实、可核的园林与人物上，未见错位地点、未见凭空捏造。
- 实例措辞“英式风景园，受克劳德·洛兰（Claude Lorrain）风景画的如画趣味启发（'Claudian' 园林）”：Claude Lorrain 启发双源直证✓；“如画趣味”为美学归类（两源无 picturesque 字面，已披露）；“'Claudian' 园林”一词仅 Gardenvisit 直证。

## 三、两源独立性

- `wp-stourhead` = **Wikipedia**（权威百科，社区编辑）；`gardenvisit-stourhead` = **Gardenvisit.com**（园林学术/门户网站）。**二者编辑主体、机构性质、内容生成流程独立，非镜像/转引关系**（Gardenvisit 独立撰文、署名 Katrina Underwood；Wikipedia 为独立词条）。**独立性成立 ✓**。
- 注意：Wikipedia 来源 note 标注“（经镜像核验）”——本轮我对 Wikipedia 直抓 HTTP 200 且正文含关键词，直连可达，note 表述为历史遗留措辞，不影响核验结论。

## 四、needs_verification=true 与 pending 披露是否如实

| 项 | 值 | 判定 |
| --- | --- | --- |
| `needs_verification` | **true** | **合理且偏诚实**：结构上保留待核实，符合 D10/D14（单源或需归类处保留 nv）。 |
| `sections.待核实` | “受 Claude Lorrain 启发、'Claudian' 园林由 Wikipedia 与 Gardenvisit 双源直证；如画为美学归类（两源未都用 picturesque 一词），营造年份待补。” | **部分不实**：Claude Lorrain 启发双源直证✓；**“'Claudian' 园林双源直证”不实**（Wikipedia `claudian`=0，仅 Gardenvisit）；“如画归类未用 picturesque 字面”如实✓；“营造年份待补”如实✓（两源均给区间 1741–1780，未给单一确定营造年）。 |
| `pending_notes` | “'如画'为美学归类（未逐字），营造年份待补；受 Claude Lorrain 启发已双源。” | **如实**：三点均与实抓一致，未把 Claudian 一词误称双源（此处措辞比待核实句更严谨）。 |

- 与 D14 一致：正文出现“待核实”声明 → nv=true 且写 pending_notes，已满足。
- **唯一不符实**：`sections.待核实` 将“'Claudian' 园林”并入“双源直证”，而该词仅 Gardenvisit 一词直证、Wikipedia 无 `Claudian`。属**归并过宽的措辞不实**（把“Claude Lorrain 启发（双源）”的结论外溢到“Claudian 一词（单源）”），非虚构史实。

## 五、结构 / 格式 / 规范句 / 相似度（阈值 0.54）

| 核对项 | 结果 | 依据 |
| --- | --- | --- |
| 七节齐 | ✓ definition ＋ 6 节（原理/典型手法与适用条件/实例/常见错误与限制/一图/待核实）＝7 | 文件实读 + check.py 0 报错 |
| SVG | ✓ 1 张，`viewBox='0 0 760 400'`，含「示意图，非施工图」；无事件处理器（`on\w+=` 空）、无 `<image>`/`xlink`/`href`/`<script>` | 脚本扫描（`on` 命中仅为 `fill='none'`，非事件句柄） |
| 规范句 | ✓「常见错误与限制」收尾「实际工程须按当地规范和专业设计人员的要求」在位 | 文件实读 |
| sources 可引性 | ✓ 4 源，`wp-stourhead`/`gardenvisit-stourhead` 均 `verified=true`、`link_ok=true`（本轮实抓 200） | sources.json 行 5955–5978 |
| 相似度（阈值0.54） | ✓ 全字段最高 **0.3562**（vs complementary-colors）／短字段最高 **0.2222**（vs stippling），均 **<0.54** | `difflib.SequenceMatcher` 对全库 258 条实算，norm=去空白小写 |

> 注：`picturesque` 为独立理论条目，全库比对最高仅 0.3562，区分度良好。

## 六、问题清单

1. **【重要·非阻断】待核实句将“'Claudian' 园林”误归为双源直证**：实抓 Wikipedia `claudian`=0，“Claudian”仅 Gardenvisit 直证；Wikipedia 只以“Claude Lorrain / landscape painters 启发”表述。**建议**：待核实句收窄为「斯托海德受 Claude Lorrain 启发经 Wikipedia 与 Gardenvisit 双源直证；'Claudian' 一词仅见 Gardenvisit；如画为美学归类（两源未都用 picturesque 一词）；营造年份待补」。`pending_notes` 已较准确，可与之对齐。
2. **【观察·非阻断】“如画/picturesque”字面缺失但已如实披露**：两源对 Stourhead 均无 `picturesque` 字样，条目已明确“为通行的美学归类（两源未都用 picturesque 一词）”，披露诚实，非编造。实例中“如画趣味启发”宜始终与“美学归类”绑定表述，避免读者误读为源文直称。
3. **【观察·非阻断】Wikipedia note 残留“经镜像核验”字样**：本轮直抓 HTTP 200 可达，该措辞为历史遗留，建议后续改为“实抓 200”以与其它源统一。

> 未发现虚构：名称/地点（英国威尔特郡）/设计者（Henry Hoare II）/年份（约1740年代起）四要素与 Claude Lorrain 启发均真实、双源可核；未发现越权把 nv 改 false（本轮保持 true）。缺口为“Claudian 一词”的双源归并措辞过宽，属可收窄的准确性问题，非虚构。

## 七、总体结论

**`picturesque`：合格（放行，附 1 项措辞收窄建议）** —— 实例斯托海德园林四要素（名称/英国威尔特郡/Henry Hoare II/约1740年代起）由 Wikipedia「Stourton with Gasper, Wiltshire」「Henry Hoare II (landscape)」「Gardens 1741–1780」与 Gardenvisit「Stourhead…Wiltshire」「Henry Hoare II's 'Claudian' garden」「Temple of Flora 1745」双源直证；**Claude Lorrain 启发双源直证**（Wikipedia「Claude Lorrain…inspired the pictorial design」＋ Gardenvisit「inspired by… Claude Lorrain」）；无编造；nv=true 与“如画/年份待补”披露如实且诚实；七节齐、SVG 合规、规范句在位、相似度 0.3562/0.2222 < 0.54。
**唯一瑕疵（非阻断）**：待核实句把“'Claudian' 园林”并入“双源直证”，而该词仅 Gardenvisit 直证、Wikipedia `claudian`=0；建议按问题①收窄后即完全精确。**不构成虚构，不影响放行。**

- **本轮 1 条：`picturesque` 合格（放行，附 1 措辞建议）。合计：1 合格、0 待核实、0 不合格。**

## 八、机器可读汇总

```
ROUND=76
SAMPLER=spotcheck-r76
SCOPE=["picturesque"]
DOCS_READ=["DECISIONS.md","research/spotcheck-round75.md","entries/batch-46.json","data/sources.json","tools/apply_review_round76.py","tools/check.py","research/b1-round46.md"]
CHECK_PY="PASS: all checks, 0 errors (EXIT=0)"
FETCH_METHOD="urllib+UA+unverified-SSL in-memory readback; temp research/_r76_*.py deleted after (ls _r76* none)"
FETCHES={"wp-stourhead":200,"gardenvisit-stourhead":200}
INSTANCE="Stourhead Garden, Wiltshire, England; Henry Hoare II; gardens laid out from ~1740s (1741-1780)"
INSTANCE_4ELEMENTS={"title":true,"location":"Wiltshire","designer":"Henry Hoare II","year":"~1740s (1741-)","dual_source":true}
CLAUDE_LORRAIN_INSPIRATION={"wikipedia":"YES direct (Claude Lorrain...inspiration behind their creation; Aeneas at Delos inspired pictorial design)","gardenvisit":"YES direct (inspired by the great landscape painters... Claude Lorrain 1600-82)","dual_source":true}
CLAUDIAN_TERM={"wikipedia":"NO (claudian count=0; uses 'Claude Lorrain/landscape painters')","gardenvisit":"YES ('Henry Hoare II's Claudian garden')","dual_source":false,"single_source":"gardenvisit"}
PICTURESQUE_WORD_ON_STOURHEAD={"wikipedia":0,"gardenvisit":0,"disclosed_in_pending":true}
INDEPENDENCE={"wikipedia":"encyclopedia","gardenvisit":"garden portal/academic (author Katrina Underwood)","independent":true,"mirror_or_reprint":false}
FABRICATION=false
NV={"needs_verification":true,"age_pending":true,"honest":true,"overclaim":"待核实 says 'Claudian garden dual-sourced' but Claudian word only in gardenvisit (WP claudian=0)"}
STRUCTURE={"seven_sections":7,"svg":"1x viewBox760x400 示意图非施工图 no event-handler/image/xlink/href/script","reg_sentence":true,"sources_verified_all":true}
SIMILARITY={"picturesque":{"full":0.3562,"full_vs":"complementary-colors","short":0.2222,"short_vs":"stippling"},"threshold":0.54,"pass":true,"max_over_258_entries":true}
ISSUES=["Q1 important(non-blocking): 待核实句将'Claudian'园林误归双源直证; WP claudian=0, only gardenvisit; suggest narrow wording","Q2 obs: picturesque word absent on both sources but honestly disclosed as aesthetic categorization","Q3 obs: WP note residual '经镜像核验' wording, live fetch 200 available"]
VERDICT_picturesque="合格（放行，1措辞收窄建议）"
TOTAL="1合格/0待核实/0不合格"
READONLY="only wrote research/spotcheck-round76.md; fetched html in-memory, temp research/_r76_*.py deleted(confirmed no residue); no entries/sources/coverage/tools/site changed by me; no git commit; web treated as data, no instructions executed"
```

*（报告完）*
