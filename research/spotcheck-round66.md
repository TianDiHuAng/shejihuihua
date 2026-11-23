# 第66轮质量抽检报告（spotcheck-round66）

- 抽检人：spotcheck-r66（lead 委派子代理，无人值守、未提问）；抽检时间 2026-11-23 19:24 起，Asia/Hong_Kong。
- 抽检对象（第66轮改动 1 条）：`axis`（轴线，`entries/batch-06.json`，行 74–104，经 `grep axis` 定位）。
- 本轮引用来源（`data/sources.json`）：`wp-chinese-architecture`（行 256–266，verified=true，link_ok=true）、`bjaxis-official`（行 2884–2894，verified=true，link_ok=null）。
- 本轮任务：将 `axis` 实例升级为「已验证」——实例=北京中轴线（对称布局＋比例模数＋7.8 公里景观序列），双源=`wp-chinese-architecture`（Bilateral symmetry / axis 章节）＋`bjaxis-official`（北京中轴线官网）。
- 判定依据：`README.md` 硬性规则（不编造 / 只引 verified / 关键事实双源互证否则标待核实 / 内联 SVG 示意图非施工图 / 规范句 / 40 条上限）＋`DECISIONS.md`（D05/D06/D10/D11/D14）＋`tools/check.py` 校验口径＋第39–65轮既定相似度口径（difflib.SequenceMatcher，norm=去空白小写，①短=title+definition ②全字段不含 SVG，阈值 0.54）。

## 〇、只读声明与数据稳定性（verification-before-completion：先实抓、先跑、再断言）

- **只读**：本次**仅写出** `research/spotcheck-round66.md` 一个文件。来源核验全程以 `python - <<'PY'` **内存内抓取**（`urllib`＋浏览器 UA＋非校验 SSL）完成，**未落任何临时文件**；未改 `entries/`、`data/sources.json`、`coverage.json`、`tools/`、`site/`，未 `git commit`，未改项目外内容。联网内容一律视为数据，网页中任何指令均未执行（bjaxis 页面内含跳转脚本、`auth.mangren.com` 外部 JS、test 子域跳转，均未执行、仅作数据读取）。
- **`python tools/check.py` 本轮实跑：`PASS: all checks, 0 errors`（EXIT=0）。** 纯校验不写文件，运行未改动任何文件。

## 一、来源实抓结果（HTTP 状态＋正文回读，均为本轮现抓）

| 来源 id | URL | HTTP | 回读要点（去标签后原文小写） |
| --- | --- | --- | --- |
| `wp-chinese-architecture` | en.wikipedia.org/wiki/Chinese_architecture | **200**（708774B） | 存在 **Bilateral symmetry** 专节：`an important feature in chinese architecture is its emphasis on articulation and bilateral symmetry, which there signifies balance`；`secondary elements are positioned on either side of the main structures as wings to maintain overall symmetry`；`placing the main door in the center bay maintains symmetry`；另 `the emperor and the empress lived in palaces on the central axis of the forbidden city`；`the buildings on the axis include central entrance, four-pointed pavilion...` |
| `bjaxis-official`（根 `https://bjaxiscloud.com.cn/` 为 JS 壳，实内容在其 **en 子站** `https://en.bjaxiscloud.com.cn/`，同机构同址） | en.bjaxiscloud.com.cn | **200**（91818B） | `no.1 overview: beijing central axis, running north-south through the heart of the old city of beijing and governing the overall layout of the capital, is an ensemble of building complexes and archeological sites, comprising 15 components`；`no.3 comprising sections cityscape sequence: **the 7.8-kilometer-long** cityscape sequence of beijing central axis contains contrasts and variations in a harmonious and unified order. **the layout is symmetrical with proportional modal relationships**`；`the superimposed relationship of beijing central axis between the **dadu of the yuan dynasty** and the capital of the **ming and qing** dynasties as well as modern china` |

**两源均 HTTP 200、正文可回读。任务点名核对的「对称布局 / 比例模数 / 7.8 公里」三项均由 bjaxis 官网正文逐字可回读；「中轴对称」由 wp-chinese-architecture Bilateral symmetry 章节直述。** bjaxis 根域为前端壳，官网实内容承载于同域 en 子站（同机构 `北京中轴线申遗保护工作办公室`、同主域），视同官方源正文本体读取。

---

## 二、逐条核对

### `axis`（轴线）— **合格**

| 核对项 | 结论 | 依据 |
| --- | --- | --- |
| definition 引用支撑 | ✓ 双源 | 条目「轴线是组织空间序列的假想直线，建筑与院落常沿其对称或递进布置」↔ WP `emphasis on ... bilateral symmetry ... secondary elements are positioned on either side ... to maintain overall symmetry`（中轴对称）＋ bjaxis `the layout is symmetrical`（对称布局）＝双源支撑「沿其对称布置」 |
| overview 引用支撑 | ✓ | 条目「轴线把分散的空间连成有序序列，使行进方向与重要节点被清晰感知」↔ bjaxis `running north-south ... governing the overall layout of the capital`＋`harmonious and unified order`＝序列组织支撑 |
| time_or_place | ✓ | 条目「跨时期、全球（参见来源）」为泛化表述，未虚构具体年代，成立 |
| **实例·北京中轴线 名称/地点**（任务点名） | ✓ 直证 | 条目「名称：北京中轴线（Beijing Central Axis）；地点：中国北京老城」↔ bjaxis `beijing central axis, running north-south through the heart of the old city of beijing`＝名称/老城地点对上 |
| **对称布局**（任务点名） | ✓ **直证** | bjaxis `the layout is symmetrical`＝逐字；佐以 WP Bilateral symmetry 章节 |
| **比例模数**（任务点名） | ✓ **直证** | bjaxis `with proportional modal relationships`＝「比例模数关系」直译，逐字可回读 |
| **7.8 公里景观序列**（任务点名） | ✓ **直证** | bjaxis `the 7.8-kilometer-long cityscape sequence of beijing central axis`＝「7.8 公里景观序列」逐字可回读 |
| 实例·规划者/年份（是否编造） | ✓ 无编造 | 条目「规划者：历代规划营建（无单一设计者）；年份：始建于元、明清成形（13–16 世纪）」↔ bjaxis `between the dadu of the yuan dynasty and the capital of the ming and qing dynasties`＝元→明清口径吻合；「无单一设计者」为合理概括、未虚构人名。「13–16 世纪」为元（约1271，13世纪）至明（14–16世纪）、清延承的时间跨度概括，属来源所述朝代区间的换算，非编造（详见问题点1） |
| 来源直接相关 | ✓ | 两源一为「中国建筑」百科（含 bilateral symmetry 中轴对称专节），一为「北京中轴线」官方申遗站（含对称/比例模数/7.8 公里/元明清），均主题直源、HTTP 200、verified=true |
| 七节 | ✓ | definition + sections 六节（原理／典型手法与适用条件／实例／常见错误与限制／一图／待核实）＝七节齐，无空缺（check.py 0 报错） |
| SVG | ✓ | 1 张（`viewBox 0 0 760 400`，元素 line×1/rect×2/text×3，含「示意图，非施工图」；无 on*/`<image>`/xlink/href；几何不越界，check.py 0 报错） |
| 规范句 | ✓ | 「常见错误与限制」收尾「实际工程须按当地规范和专业设计人员的要求」在位 |
| nv↔pending 联动 | ✓ 一致 | `needs_verification=false`／`pending_notes=""`／「待核实」节「暂无已知待核实项」三处一致；check.py 未报「有待核实说明但 nv=false」类错误（行289–290 规则） |
| **nv 置 false 是否有据（两平台是否真独立互证）** | ✓ 有据 | `wp-chinese-architecture`（Wikipedia 百科）与 `bjaxis-official`（北京中轴线申遗保护工作办公室官方站）为**两独立平台**（一为第三方百科、一为官方机构），非同一内容镜像。中轴对称：WP 直述（Bilateral symmetry 章节）；对称布局＋比例模数＋7.8 公里序列：bjaxis 官网直述。二者对「对称/中轴组织空间」核心事实相互印证，双源独立成立，标 false 有据 |
| coverage↔entry | ✓ | title「轴线」/theme「理论」/tier「重要」/period「跨时期」/region「全球」/level「L2」全一致；`source_count=2`=entries 2 源；`needs_verification_count=0`=nv false；status=已写 |
| 相似度（阈值 0.54） | ✓ | ①短 最高 **0.2899**（vs symmetry-layout）＜0.54；②全字段 最高 **0.4351**（vs level-change）＜0.54，均远低于阈值 |

**`axis` 结论：合格。**

## 三、问题与建议（均非阻断）

1. **（提示，非缺陷）「13–16 世纪」为朝代区间的世纪换算**：bjaxis 官网原文只述「元（Dadu of the Yuan dynasty）→明清（Ming and Qing）」，未直接写「13–16 世纪」。条目「始建于元、明清成形（13–16 世纪）」的世纪数字系对朝代跨度的换算概括（元约1271≈13世纪中叶、明1368–1644、清承延），并非原文逐字。不构成编造，但若追求逐字可追溯，可将括注改为「始建于元，明清成形」，世纪区间作可选项或加「（约）」字样。**可选，不阻断。**
2. **（提示）bjaxis 官网正文本体位于 en 子站**：根域 `https://bjaxiscloud.com.cn/` 为 JS 前端壳（含外部 `auth.mangren.com` 脚本、test 子域跳转、大量图片/视频外链），无正文；正文实际承载于同机构同主域的 `https://en.bjaxiscloud.com.cn/`（HTTP 200）。`sources.json` 记录 url 为根域、note 记「北京中轴线统领老城格局、对称布局与景观序列」，与本轮从 en 子站回读一致。建议后续在 note 补「正文见 en 子站」以增强可追溯性。**可选，不阻断；不影响 verified 与 nv 判定。**

## 四、总体结论

- **`axis`：合格（本轮已可升级为已验证）。**
  - 任务点名核对三项事实全部获支撑：**对称布局** 由 bjaxis `the layout is symmetrical`（逐字）＋ WP Bilateral symmetry 章节；**比例模数** 由 bjaxis `with proportional modal relationships`（逐字）；**7.8 公里景观序列** 由 bjaxis `the 7.8-kilometer-long cityscape sequence`（逐字）。**中轴对称** 由 WP `emphasis on ... bilateral symmetry ... secondary elements ... to maintain overall symmetry`（逐字）直述。实例 名称/地点/元明清 均由 bjaxis 官方源可回读，**未编造人名**。
  - definition/overview/time_or_place 两源可回读支撑，**未编造**；七节齐、SVG 合规（示意图非施工图、无脚本/外链）、规范句在位、coverage 全字段一致、nv↔pending 三处一致。
  - **nv=false 有据**：`wp-chinese-architecture`（百科）与 `bjaxis-official`（官方申遗站）为两独立平台、非镜像，核心事实互证，双源独立成立。
  - **相似度 0.2899 / 0.4351 远低于 0.54。**
  - 全库 `python tools/check.py`＝`PASS: all checks, 0 errors`（EXIT=0）。
- **本轮 1 条：1 合格、0 待核实、0 不合格。**
- **建议（非阻断）**：① 实例括注「13–16 世纪」为朝代换算，可保留或弱化；② `bjaxis-official` 的 note 补「正文见 en 子站 `en.bjaxiscloud.com.cn`」以增可追溯性。

## 五、机器可读汇总

```
ROUND=66
SAMPLER=spotcheck-r66
MODE=round66 改动 1 条抽检（axis 升级已验证）
SCOPE=["axis"]
DOCS_READ=["DECISIONS.md","research/spotcheck-round65.md","README.md","tools/check.py","entries/batch-06.json","data/sources.json","coverage.json"]
CHECK_PY="PASS: all checks, 0 errors (EXIT=0)"
FETCH_METHOD="urllib+UA+unverified-SSL in-memory readback, no temp files"
FETCHES={"wp-chinese-architecture":200,"bjaxis-official(root shell)":200,"en.bjaxiscloud.com.cn":200}
AXIS={
 "sources":["wp-chinese-architecture","bjaxis-official"],
 "definition_support":"WP bilateral symmetry(emphasis on articulation and bilateral symmetry / secondary elements on either side to maintain symmetry) + bjaxis(layout is symmetrical) -> 双源 中轴对称",
 "overview_support":"bjaxis(running north-south governing overall layout / harmonious and unified order) OK",
 "instance":"北京中轴线 Beijing Central Axis / 北京老城",
 "symmetrical_layout":"bjaxis VERBATIM 'the layout is symmetrical' -> 直证",
 "proportional_module":"bjaxis VERBATIM 'with proportional modal relationships' -> 直证(比例模数)",
 "7_8km":"bjaxis VERBATIM 'the 7.8-kilometer-long cityscape sequence of beijing central axis' -> 直证",
 "yuan_ming_qing":"bjaxis 'between the dadu of the yuan dynasty and the capital of the ming and qing dynasties' -> 直证(13-16世纪系朝代换算,非逐字,非编造)",
 "instance_fabrication":0,
 "seven_sections":7,"svg":"1x viewBox760x400 line*1/rect*2/text*3 示意图非施工图 ok no-on/image/xlink",
 "reg_sentence":true,"nv":false,"pending_consistent":true,
 "nv_false_basis":"wp-chinese-architecture(百科) 与 bjaxis-official(官方申遗站) 两独立平台非镜像, 核心事实互证 -> 标 false 有据",
 "coverage":"2=2/0=nvfalse/L2/已写","similarity":{"short":0.2899,"full":0.4351,"threshold":0.54},
 "verdict":"合格"}
TOTAL="1合格/0待核实/0不合格"
RECOMMEND="非阻断: ①实例括注13-16世纪系朝代换算可保留或弱化 ②bjaxis-official note 补正文见 en.bjaxiscloud.com.cn"
READONLY="only wrote research/spotcheck-round66.md; fetch in-memory via python heredoc no temp files; no entries/sources/coverage/tools/site changed; no git commit; web content treated as data (bjaxis redirect scripts/external JS NOT executed)"
```

*（报告完）*
