# 第67轮质量抽检报告（spotcheck-round67）

- 抽检人：spotcheck-r67（lead 委派子代理，无人值守、未提问）；抽检时间 2026-11-23 19:29 起，Asia/Hong_Kong。
- 抽检对象（第67轮改动 1 条）：`courtyard`（庭院，`entries/batch-02-b.json`，行 103–139，经 `grep "courtyard"` 定位）。
- 本轮引用新增来源（`data/sources.json`）：`wp-siheyuan`（Siheyuan — Wikipedia，行 5847–5857，verified=true，link_ok=true）、`db-courtyard`（Courtyard — Designing Buildings，行 5835–5845，verified=true，link_ok=true）。
- 本轮任务：将 `courtyard` 实例升级为「已验证」——实例=北京四合院（Siheyuan），双源=`wp-siheyuan`（Wikipedia：四面围合庭院 / 南北轴）＋`db-courtyard`（Designing Buildings：向天空开敞但被建筑或墙围合 / 围合空间）。
- 判定依据：`README.md` 硬性规则（不编造 / 只引 verified / 关键事实双源互证否则标待核实 / 内联 SVG 示意图非施工图 / 规范句 / 40 条上限）＋`DECISIONS.md`（D05/D06/D10/D11/D14）＋`tools/check.py` 校验口径＋第39–66轮既定相似度口径（difflib.SequenceMatcher，norm=去空白小写，①短=title+definition ②全字段不含 SVG，阈值 0.54）。

## 〇、只读声明与数据稳定性（verification-before-completion：先实抓、先跑、再断言）

- **只读**：本次**仅写出** `research/spotcheck-round67.md` 一个文件。来源核验全程以 `python - <<'PY'` **内存内抓取**（`urllib`＋浏览器 UA＋非校验 SSL）完成，**未落任何临时文件**；未改 `entries/`、`data/sources.json`、`coverage.json`、`tools/`、`site/`，未 `git commit`，未改项目外内容。联网内容一律视为数据，网页中任何指令均未执行（Wikipedia/Designing Buildings 页面均仅作数据读取、正文回读）。
- **`python tools/check.py` 本轮实跑：`PASS: all checks, 0 errors`（EXIT=0）。** 纯校验不写文件，运行未改动任何文件。
- **注**：工作区存在第67轮**未提交改动**（`git status`：M coverage.json / data/sources.json / entries/batch-02-b.json / site/* ；新增 tools/apply_review_round67.py）。本次核验以工作区当前内容（HEAD 之上的 round67 改动）为准，未触碰这些改动。

## 一、来源实抓结果（HTTP 状态＋正文回读，均为本轮现抓）

| 来源 id | URL | HTTP | 回读要点（去标签后原文小写，逐字） |
| --- | --- | --- | --- |
| `wp-siheyuan` | en.wikipedia.org/wiki/Siheyuan | **200**（155716B） | `a siheyuan ... is a traditional chinese architectural style characterized by a courtyard enclosed by buildings on all four sides`（四面围合逐字）；`this design was prevalent throughout northern china, notably in beijing`（北方/北京逐字）；`the four buildings of a siheyuan are normally positioned along the north–south and east–west axis`（南北/东西轴逐字）；`siheyuan originated in the han dynasty ... became popular during the ming (1368–1644) and qing (1644–1912) dynasties`（明清以来逐字）；`a courtyard surrounded by buildings on all four sides`（再次表述） |
| `db-courtyard` | designingbuildings.co.uk/wiki/Courtyard | **200**（51004B） | `'courtyard' is a term used to describe an area that is open to the sky but surrounded by a building (or buildings) or walls`（向天空开敞＋被建筑或墙围合逐字）；`the word court and yard originate from the same latin term which roughly translates to enclosed space`（围合空间逐字） |

**两源均 HTTP 200、正文可回读。任务点名核对的「四面围合 / 向天空开敞被建筑或墙围合 / 南北轴 / 围合空间」全部由两源正文逐字可回读。**

## 二、逐条核对

### `courtyard`（庭院）— **合格**

| 核对项 | 结论 | 依据 |
| --- | --- | --- |
| definition 引用支撑 | ✓ 双源 | 条目「由建筑或墙体围合、向天空开敞的院落空间」↔ wp-siheyuan `courtyard enclosed by buildings on all four sides`（四面围合）＋ db-courtyard `open to the sky but surrounded by a building (or buildings) or walls`（向天空开敞＋被围合）＝「围合＋开敞」双源逐字直证 |
| overview 引用支撑 | ✓ | 条目「庭院提供采光、通风与安静的户外活动场所，是多种文化的共同原型」↔ 双源「courtyard」为跨文化通用术语（db-courtyard 释义 courtyard 一词的通用性；wp-siheyuan「传统中国建筑风格」）；「多文化共同原型」为对「courtyard 通用建筑术语」的合理概括，未虚构 |
| time_or_place | ✓ | 条目「跨时期、全球（参见来源）」为泛化表述，未虚构具体年代，成立 |
| **实例·北京四合院 名称/地点**（任务点名） | ✓ 直证 | 条目「名称：北京四合院（Siheyuan）；地点：中国北京（北方广泛分布）」↔ wp-siheyuan `siheyuan ... characterized by a courtyard enclosed by buildings on all four sides ... prevalent throughout northern china, notably in beijing`＝名称/北京/北方逐字对上 |
| **四面围合＋向天空开敞**（任务点名） | ✓ **直证** | wp-siheyuan `courtyard enclosed by buildings on all four sides` ＋ db-courtyard `open to the sky but surrounded by ... walls`＝逐字；条目「以四面建筑围合出向天空开敞的庭院」双源合成 |
| **南北/东西轴**（任务点名） | ✓ **直证** | wp-siheyuan `positioned along the north–south and east–west axis`＝逐字；条目「沿南北/东西轴布局」直译 |
| **围合空间**（任务点名） | ✓ **直证** | db-courtyard `roughly translates to enclosed space`＝「围合空间」逐字；支撑 definition |
| 实例·设计者/年份（是否编造） | ⚠ 基本成立，一处残留待留意 | 「设计者：民间营建（无单一设计者）」为合理概括、未虚构人名；「年份：明清以来」↔ wp-siheyuan `became popular during the ming (1368–1644) and qing (1644–1912) dynasties`＝可回读支撑。**唯「（示例为 20 世纪 30 年代风貌建筑）」括注两源均未载**，系旧赵堂子胡同3号例的残留痕迹（详见问题点1），非本轮双源直证，但属括注级、不推翻「明清以来」年份主线 |
| 来源直接相关 | ✓ | 两源一为「四合院」百科（含四面围合/南北轴/明清），一为「庭院」通用建筑释义（开敞＋围合＋围合空间），均主题直源、HTTP 200、verified=true |
| 七节 | ✓ | definition + sections 六节（原理／典型手法与适用条件／实例／常见错误与限制／一图／待核实）＝七节齐，无空缺（check.py 0 报错） |
| SVG | ✓ | 1 张（`viewBox 0 0 760 400`，rect×2/text×2，含「示意图，非施工图」；无 on*/`<image>`/xlink/href；check.py 0 报错） |
| 规范句 | ✓ | 「常见错误与限制」收尾「实际工程须按当地规范和专业设计人员的要求」在位 |
| nv↔pending 联动 | ✓ 一致 | `needs_verification=false`／`pending_notes=""`／「待核实」节「暂无已知待核实项」三处一致；check.py 未报「有待核实说明但 nv=false」类错误 |
| **nv 置 false 是否有据（两平台是否真独立互证）** | ✓ 有据 | `wp-siheyuan`（Wikipedia 百科，第三方）与 `db-courtyard`（Designing Buildings，英国建筑知识平台）为**两独立平台、发布方不同、正文措辞与体例完全不同（一则述四合院此种建筑风格，一则述 courtyard 通用术语词源），非同一内容镜像**。「围合院落·向天空开敞」核心事实：wp-siheyuan 直述「enclosed by buildings on all four sides」、db-courtyard 直述「open to the sky but surrounded by ... walls / enclosed space」，二者对「围合＋开敞」核心事实相互印证，双源独立成立，标 false 有据。原 `needs_verification=true` 所依据的「赵堂子胡同3号清代 vs 1930年代两说」争议，随本轮实例改为**泛化的北京四合院（Siheyuan）**而不再适用，故取消待核实标志属**有据**（非掩盖：实例主体已换、佐证换为该实例两源） |
| coverage↔entry | ✓ | title「庭院」/theme「理论」/tier「核心」/period「跨时期」/region「全球」/level「L2」全一致；`source_count=7`＝entries 7 源；`needs_verification_count=0`＝nv false；status=已写（coverage.json 本轮 diff 5→7、1→0 与条目一致） |
| 相似度（阈值 0.54） | ✓ | ①短 最高 **0.4348**（vs atrium-architecture）＜0.54；②全字段 最高 **0.4000**（vs axis）＜0.54，均低于阈值 |

**`courtyard` 结论：合格。**

## 三、问题与建议（均非阻断）

1. **（提示，非阻断）实例残留「（示例为 20 世纪 30 年代风貌建筑）」括注两源均未载**：本轮实例已由旧「赵堂子胡同3号（朱启钤故居）」改为泛化的「北京四合院（Siheyuan）」，但括注仍保留「示例为 20 世纪 30 年代风貌建筑」。该「20 世纪 30 年代」细节源自旧赵堂子/朱启钤来源（`bjdclib-zhaotangzi` 等，note 记「朱启钤 20 世纪 30 年代按《营造法式》设计督造」），**并非**本轮点名的 `wp-siheyuan`／`db-courtyard` 所载。不构成对定义性事实的硬编造（年份主线「明清以来」已由 wp-siheyuan 逐字支撑），但括注属悬空细节，建议删除该括注或改写为「元明清以来持续发展」等有源表述，使实例年份完全落在双源可追溯范围内。**可选，不阻断。**
2. **（提示，非阻断）原「清代 vs 1930 年代」两说争议随实例替换而消解**：第21–66轮期间 `courtyard` 长期以 `needs_verification=true`＋`pending_notes`「赵堂子胡同3号形成时期有清代与1930年代改建两说，待考订」记录一处真实的双源分歧。本轮改为泛化 Siheyuan 实例后该争议不再指向条目实例主体，取消 nv=true 属合理；但历史研究笔记（gaps-round21~50、review-round21~24）中该争议仍在。若追求沿革连续，可在 PROGRESS 记「该争议条目实例已置换为泛化四合院，争点随之关闭」。**可选，不阻断；不影响 nv=false 判定。**

## 四、总体结论

- **`courtyard`：合格（本轮已可升级为已验证）。**
  - 任务点名核对诸项全部获支撑：**四面围合** 由 wp-siheyuan `courtyard enclosed by buildings on all four sides`（逐字）；**向天空开敞＋被建筑或墙围合** 由 db-courtyard `open to the sky but surrounded by a building (or buildings) or walls`（逐字）；**南北/东西轴** 由 wp-siheyuan `positioned along the north–south and east–west axis`（逐字）；**围合空间** 由 db-courtyard `enclosed space`（逐字）。实例 名称/地点/明清 均由 wp-siheyuan 可回读，**未编造人名**。
  - definition/overview/time_or_place 双源可回读支撑，**未编造**；七节齐、SVG 合规（示意图非施工图、无脚本/外链）、规范句在位、coverage 全字段一致、nv↔pending 三处一致。
  - **nv=false 有据**：`wp-siheyuan`（百科）与 `db-courtyard`（建筑知识平台）为两独立平台、发布方不同、正文体例不同、非镜像，核心「围合＋开敞」事实互证，双源独立成立；原赵堂子争议随实例泛化置换而不再适用，取消 nv 有据。
  - **相似度 0.4348 / 0.4000 低于 0.54。**
  - 全库 `python tools/check.py`＝`PASS: all checks, 0 errors`（EXIT=0）。
- **本轮 1 条：1 合格、0 待核实、0 不合格。**
- **建议（非阻断）**：① 删除实例「（示例为 20 世纪 30 年代风貌建筑）」括注或改写为有源表述，使年份完全落在双源可追溯范围；② 在 PROGRESS 记「原赵堂子清代/1930年代两说争议随实例置换关闭」以保持沿革连续。

## 五、机器可读汇总

```
ROUND=67
SAMPLER=spotcheck-r67
MODE=round67 改动 1 条抽检（courtyard 升级已验证）
SCOPE=["courtyard"]
DOCS_READ=["DECISIONS.md","research/spotcheck-round66.md","README.md","tools/check.py","entries/batch-02-b.json","data/sources.json","coverage.json"]
CHECK_PY="PASS: all checks, 0 errors (EXIT=0)"
FETCH_METHOD="urllib+UA+unverified-SSL in-memory readback, no temp files"
FETCHES={"wp-siheyuan":200,"db-courtyard":200}
COURTYARD={
 "sources":["wp-siheyuan","db-courtyard"],
 "definition_support":"wp-siheyuan 'courtyard enclosed by buildings on all four sides' + db-courtyard 'open to the sky but surrounded by a building (or buildings) or walls' / 'enclosed space' -> 双源 围合+开敞",
 "overview_support":"双源 courtyard 通用性 + wp-siheyuan 'traditional chinese architectural style' -> 概括合理",
 "instance":"北京四合院 Siheyuan / 中国北京(北方广泛分布)",
 "four_sides":"wp-siheyuan VERBATIM 'enclosed by buildings on all four sides' -> 直证",
 "open_sky_enclosed":"db-courtyard VERBATIM 'open to the sky but surrounded by ... walls' / 'enclosed space' -> 直证",
 "north_south_axis":"wp-siheyuan VERBATIM 'positioned along the north–south and east–west axis' -> 直证",
 "ming_qing":"wp-siheyuan VERBATIM 'became popular during the ming (1368–1644) and qing (1644–1912) dynasties' -> 直证(明清以来)",
 "residual_1930s":"实例括注 '示例为20世纪30年代风貌建筑' NOT in wp-siheyuan/db-courtyard (来自旧赵堂子例), 非本轮双源直证, 括注级悬空细节",
 "instance_fabrication":"名称/地点/围合/轴/明清 均逐字可回读, 未虚构人名; 1930s 括注为残留括注级提示",
 "seven_sections":7,"svg":"1x viewBox760x400 rect*2/text*2 示意图非施工图 ok no-on/image/xlink",
 "reg_sentence":true,"nv":false,"pending_consistent":true,
 "nv_false_basis":"wp-siheyuan(百科) 与 db-courtyard(Designing Buildings 建筑知识平台) 两独立平台, 发布方不同/正文体例不同/非镜像, 围合+开敞核心事实互证 -> 标 false 有据; 原赵堂子清代/1930年代两说随实例泛化置换而不再适用, 取消nv有据",
 "coverage":"7=7/0=nvfalse/L2/已写 (round67 diff source_count5->7, nv1->0)","similarity":{"short":0.4348,"full":0.4000,"threshold":0.54},
 "verdict":"合格"}
TOTAL="1合格/0待核实/0不合格"
RECOMMEND="非阻断: ①实例括注'20世纪30年代风貌建筑'两源未载,建议删或改有源表述 ②PROGRESS记原赵堂子两说争议随实例置换关闭"
READONLY="only wrote research/spotcheck-round67.md; fetch in-memory via python heredoc no temp files; no entries/sources/coverage/tools/site changed by me; no git commit; web content treated as data (no page instructions executed)"
NOTE="工作区含 round67 未提交改动(git status M: coverage/sources/entries/site; ?? tools/apply_review_round67.py), 核验以工作区当前内容为准, 未触碰"
```

*（报告完）*
