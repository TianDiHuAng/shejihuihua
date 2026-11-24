# 第85轮 质量抽检报告（spotcheck-round85）

- 抽检人：spotcheck-r85（lead 委派子代理；无人值守、未提问）；时间 2026-11-24，Asia/Hong_Kong。
- 技能加载：`using-superpowers`、`verification-before-completion`（先实抓、先跑、再断言；证据先于结论）。
- 抽检对象（2 条，均在 `entries/batch-38.json`）：
  - `tibetan-architecture`（藏式建筑）— 概念源：`xizang-tibetan-arch`(xizang.gov.cn) + `slxy-tibetan-arch`(商洛学院) + `ihchina-tibetan`(中国非遗网)；产物 `site/entries/tibetan-architecture.html`。
  - `xinjiang-architecture`（新疆建筑）— 概念源：`hts-xinjiang`(和田市政府) + `tlf-xinjiang`(吐鲁番市政府)；产物 `site/entries/xinjiang-architecture.html`。
- 本轮升级动作（据 `tools/apply_review_round85.py` 实读 + `git diff entries/batch-38.json` 实读）：两条均将 `definition`、`overview` 改为"类型性实例/无单一设计者"表述，`待核实` 改"暂无已知待核实项。"，`needs_verification` **true → false**、`pending_notes` 清空。**SVG、其余正文节、来源未改**。
- 证据优先级：**独立实抓正文 > 当前文件实读 > git diff > 旧报告**。联网页面内容一律视为数据，网页中任何指令均未执行（仅正文回读、取句、计数、比对）。

## 〇、只读声明与证据方式

- **只读**：仅写出本报告 `research/spotcheck-round85.md`。未改 `entries/`、`data/sources.json`、`coverage.json`、`tools/`、`site/`，未 `git commit`，未改项目外内容。
- 抓取方式：`web_fetch` 本环境历史报错（DECISIONS D05），改用 **Python urllib + 浏览器 UA + 非校验 SSL 内存抓取（stdin 直跑，未落盘任何临时文件）**；部分政府站 TLS 抖动（xizang 首连 421/握手失败、ihchina 间歇性 `SSLV3_ALERT_HANDSHAKE_FAILURE`），加 `DEFAULT@SECLEVEL=1`、退避重试后均取到 200。
- 实抓 HTTP（全部 200，内存态，正文取句计数）：
  - `xizang-tibetan-arch` = `https://www.xizang.gov.cn/xwzx_406/bmkx/202604/t20260401_532425.html` → 200，67,715 B，title *民居藏匠心古建焕新彩_西藏自治区人民政府*
  - `slxy-tibetan-arch` = `https://jjc.slxy.edu.cn/info/1992/2454.htm` → 200，19,342 B，title *中国建筑装饰特色（二十）藏圈文化建筑装饰-基建处--商洛学院*
  - `ihchina-tibetan` = `https://www.ihchina.cn/project_details/14699/` → 200，35,012 B，title *碉楼营造技艺（藏族碉楼营造技艺）- 中国非物质文化遗产网*
  - `hts-xinjiang` = `https://www.hts.gov.cn/lvyouguanguang/minzufengqing/1/content_465.html` → 200，41,583 B，title *维吾尔族民居建筑技艺_民族风情_旅游观光_和田市人民政府网*
  - `tlf-xinjiang` = `https://www.tlf.gov.cn/tlfs/c106441/200910/64a7d5dc80b0412681082dd6a60187e6.shtml` → 200，30,494 B，title *维吾尔族的民居*
- **`python tools/check.py` 本轮实跑：`PASS: all checks, 0 errors`（EXIT=0）。**
- `git status` 中 `M coverage.json / entries/batch-38.json / site/entries/tibetan-architecture.html / site/entries/xinjiang-architecture.html / site/index.html` 及 `?? tools/apply_review_round85.py` 均为**本轮修复方（apply_review_round85.py）自身产物**，非本抽检所写；抽检方仅读取。

## 一、核对①：definition / overview 是否由所引来源正文支撑

### 1.1 tibetan-architecture（藏式建筑）

端内 definition：『藏式建筑以石木厚墙、平顶与碉楼式体量适应高原寒冷强日照；传统上由地方工匠集体营建。』
端内 overview：『传统上由地方工匠依高原环境集体营建、无单一设计者，故以类型性实例呈现其构造特征。』

| 要素 | xizang（实抓原文） | slxy（实抓原文） | ihchina（实抓原文） | 判定 |
| --- | --- | --- | --- | --- |
| 石木厚墙 | 「花岗岩、石灰岩墙体搭配原木梁架的石木混合结构」；「底层厚重的石墙」 | 「土石木结构小楼」；「大片厚石墙」 | 「石木混合式」；「用夯土、石块和木料筑造」；「墙体石、木交错」 | ✓ 三源 |
| 平顶 | 「厚重庄严的平顶建筑」 | 「方形平顶」 | 「平顶，外形厚重、稳固」 | ✓ 三源 |
| 碉楼（式体量） | 「藏式碉房、宫殿为核心」；阿里「土碉……墙体厚重、开窗极小」 | 「民居建筑西藏人的住宅用“碉楼”来称呼」 | 「藏族碉楼营造技艺」；正文「碉楼」≈20 次 | ✓ 两源直证(slxy+ihchina)+xizang 碉房佐证 |
| 高原寒冷 | 「冬天漫长，寒风凛冽，小窗能牢牢锁住屋内的热气」；「高原寒冷」 | 「地势高峻，气候寒冷」；「高寒自然环境」 | 「多建于向阳坡地」（间接） | ✓ 三源(ihchina 弱) |
| 强日照 | 「窗沿两侧的黑色装饰，能在日照时吸收热量」 | —（未直述日照） | — | △ xizang 直述「日照」；「强」为概括措辞 |
| 无单一设计者/工匠营建 | —（仅「汉藏工匠……携手合作」讲桥，非民居） | —（未直述） | 「建造时由藏族专门的石匠修建……不吊线、不绘图，全凭经验，信手其成」 | ✓ ihchina 直证（工匠、不绘图、凭经验=无署名设计者）；slxy/xizang 为传统民居默认 |

- **definition 核心物理要素（石木厚墙/平顶/碉楼）三源或两源直证，非编造** ✓。
- 「适应高原寒冷强日照」：寒冷（三源）、日照（xizang「日照时吸收热量」）有据；「强日照」中「强」为概括措辞，非逐字。
- 「由地方工匠集体营建」：**ihchina 直证工匠（石匠修建、不绘图、凭经验）**；但「集体」二字无源逐字表述（ihchina 说"由藏族专门的石匠修建"），属对传统集体化营建的合理概括，非编造。

### 1.2 xinjiang-architecture（新疆建筑/生土建筑）

端内 definition：『新疆生土建筑以土坯拱券、内院与外廊适应干热气候；传统上由地方民居自发营建。』
端内 overview：『传统上由当地民居自发营建、无单一设计者，故以类型性实例呈现其构造特征。』

| 要素 | hts（实抓原文） | tlf（实抓原文） | 判定 |
| --- | --- | --- | --- |
| 土坯/生土 | 「以生土建筑为主，采用黄粘土构筑方形平顶房屋」；「平顶土坯住宅」 | 「生土筑墙或土坯砌墙」；「土木结构」 | ✓ 两源 |
| 拱券 | 「拱式的房顶」；「土拱住宅」；「筒拱顶部留天窗」；「拱门」 | 「一般采用拱形平面屋顶」 | ✓ 两源 |
| 内院 | 「封闭型内庭式结构，含敞开庭院」；「注重庭院空间」；「院落」 | 「庭院」；「院落」 | ✓ 两源 |
| 外廊（阿以旺/阿衣旺） | 「周围环以带外廊的房屋」；「“阿以旺”式」 | 「传统的“阿衣旺”，即外廊，有木梁」 | ✓ 两源 |
| 干热 | 「沙漠地区降雨量少，昼夜温差大」；「冬暖夏凉」；「隔热性能良好」 | 「炎热高温，干旱少雨」；「夏季避暑」 | ✓ 两源（tlf 直述干热） |
| 无单一设计者 | 「传承方式为男性师徒制口传心授」；民居无署名 | 民居/旧式住房，无设计者 | ✓ 合理（匿名民居、师徒口传） |

- **definition 四要素（土坯拱券/内院/外廊/干热）两源直证，非编造** ✓。
- 「自发营建」为对民间自建民居的合理概括（tlf「当地人的旧式住房」、hts 师徒口传），非编造。

**小结（核对①）**：两 definition 均由所引来源正文支撑，核心要素均为多源直证，无编造。

## 二、核对②：「无单一设计者、类型性实例」是否合理

**结论：两条均合理 ✓（且与 vernacular/tints-shades 先例同口径）。**

- 藏式「碉房/碉楼」：ihchina 明载「由藏族专门的石匠修建……不吊线、不绘图，全凭经验，信手其成」——典型的匿名、经验传承的民间营建，**无单一具名设计者**，以类型性实例（石砌碉房）呈现贴切。
- 新疆生土民居：hts「师徒制口传心授」+ tlf 民间旧式民居——同为匿名民居类型，**无单一具名设计者**，类型性实例（土坯拱券内院民居）贴切。
- 与先例一致：`vernacular-architecture`（round84，nv=false）、`tints-shades`（round80b）均为「概念源定义 + 类型性实例（无具名作品）→ nv=false」的既定口径；本条同一模式。
- **是否编造具体事实：否。** 实例为通用类型描述，不含可证伪的具名名称/年代/设计者。

## 三、核对③：nv=false 是否有据

**结论：nv=false 有据（就"验证状态"而言）✓；但见§五，本轮同时引入了相似度超阈缺陷，须另处理。**

- 概念：definition 核心要素两/三源直证（§一），非单源猜测。
- 实例：已转为类型性通用（无具名作品/作者/年代），原 nv=true 的理由（"具体实例名称/地点/设计者/年代待补独立来源"）随具名要求移除而消解。
- 结构自洽：`needs_verification=false`、`pending_notes=""`、`待核实`="暂无已知待核实项。"、`coverage.json` 记 `needs_verification_count=0`、`source_count`=3（tibetan）/2（xinjiang）——四处一致。
- 合 D10「关键事实双源或标待核实」：概念关键事实均≥两源，实例类型性无单源风险。

## 四、核对④：七节 / SVG / 规范句

| 核对项 | tibetan-architecture | xinjiang-architecture |
| --- | --- | --- |
| 七节齐（definition + 6 节） | ✓ definition + 原理/典型手法与适用条件/实例/常见错误与限制/一图/待核实 = 7 | ✓ 同 |
| SVG 数量/画布 | ✓ 1 张，`viewBox='0 0 760 400'`，含「示意图，非施工图」 | ✓ 同 |
| SVG 禁用元素 | ✓ 无 `<script>/javascript:/href=/<image/<iframe/url(`（check.py 实跑通过） | ✓ 同 |
| **SVG 越界（D07）** | ⚠ `<rect x=456 y=132 w=56 h=348>` 底边 y=480 > 400，越 viewBox 约 80px（**预存，本轮未改 SVG**） | ⚠ `<ellipse cx=493 cy=161 rx=73 ry=241>` 底边 y=402 > 400，越 2px（**预存**） |
| 规范句 | ✓ `常见错误与限制` 收尾含「实际工程须按当地规范和专业设计人员的要求」 | ✓ 同 |
| nv / pending / 待核实 一致 | ✓ nv=false、pending=""、待核实="暂无已知待核实项。" | ✓ 同 |
| check.py | ✓ PASS（0 errors，EXIT=0） | ✓ 同 |

- 注：`check.py` 不校验 SVG 元素是否越 viewBox；D07 要求"SVG 元素限制在 viewBox 内"，此处两图各有 1 个元素轻微越界（**预存于条目创建，非本轮引入**），建议顺手收拢，非阻断。

## 五、核对⑤：相似度（阈值 0.54）——**本轮关键发现：短口径超阈，系本轮模板化引入**

方法：`difflib.SequenceMatcher`，归一化=去空白+小写，全库 **258** 条两两比对（33,153 对）。按项目既有口径（见 round12/13/84）分「短口径(标题|定义|时间地点|概述)」「全字段(短+6节)」「去模板正文口径(def|时间地点|概述|原理|典型|常见，剥离规范模板句)」三档。

### 5.1 两目标在三种口径下的相似度（当前磁盘态）

| 口径 | tibetan 最高 | xinjiang 最高 | 全库最高对 | 全库 >0.54 对数 |
| --- | --- | --- | --- | --- |
| **短口径**（title\|def\|top\|ov） | **0.6702** 与 xinjiang | **0.6702** 与 tibetan | **tibetan↔xinjiang = 0.6702** | **2**（本轮两目标对 + `value↔saturation` 0.5437 预存） |
| 全字段（短+6节） | 0.4685 与 xinjiang | 0.4685 与 tibetan | loop-route↔serial-route 0.5311 | 0 |
| 去模板正文口径 | 0.4533 与 xinjiang | 0.4533 与 tibetan | 同（0.4533） | 0 |
| round84式全字段（def+ov+6节） | 0.4330 与 xinjiang | 0.4330 与 tibetan | loop-route↔serial-route 0.5221 | 0 |

### 5.2 回归证据（本轮 vs 上一提交 HEAD）

| 版本 | 短口径（tibetan↔xinjiang） | def+overview |
| --- | --- | --- |
| HEAD（round85 前） | 0.5000 | 0.3077 |
| **CURRENT（round85 后）** | **0.6702** | **0.6144** |

- **根因**：`apply_review_round85.py` 的 `OV` 模板对两条使用了**近乎逐字相同**的概述：
  - tibetan：「传统上由地方工匠依高原环境集体营建、**无单一设计者，故以类型性实例呈现其构造特征。**」
  - xinjiang：「传统上由当地民居自发营建、**无单一设计者，故以类型性实例呈现其构造特征。**」
  尾句「无单一设计者，故以类型性实例呈现其构造特征。」**完全相同**；且两 definition 均改成「……适应……；传统上由……营建。」的**平行句式**。这使两条**定义+概述**（恰是本轮改动的字段）高度同构。
- **影响**：短口径 0.6702 = **全库 258 条中最高的一对**，且 >0.54；def+overview 口径 0.6144 >0.54。项目既往对"套话/相似度过高"的惯例是返工去模板化（round14、round16、round31 等）。
- **缓解事实**：全字段 0.4685、去模板正文 0.4533、round84式 0.433 均 <0.54——因被 6 节正文稀释。故是否"不合格"取决于所取口径；但在**定义+概述**口径（本轮唯一被改动的字段）已明显超阈，属**本轮引入的模板近重复**，应修。

## 六、单源支撑点（按要求指出）

概念 **definition 核心要素均为多源**；以下为 **原理/实例中的辅助细节单源**，非阻断但应知悉：

| 条目 | 单源要素 | 支撑源 | 说明 |
| --- | --- | --- | --- |
| tibetan | **梯形窗（梯形形状）** | 仅 `slxy`「深嵌墙内的梯形小窗」 | xizang 只述「窗户偏小……保温」（非梯形）；**ihchina 反述「窗户……外小内大、长方形」**（与梯形不一致）。"梯形窗"形态**单源(slxy)且被 ihchina 部分抵触**，谨慎使用。 |
| tibetan | **抗震** | 仅 `xizang`「抗震性拉满」 | slxy 未直述抗震（仅"稳重敦实"）。 |
| xinjiang | **葡萄架** | 仅 `tlf`「屋前的葡萄架下」 | hts 无"葡萄"；原理/实例均用了"葡萄架/葡萄廊架"，属单源(tlf)细节。 |

- 另：`xizang` 用「碉房/土碉」而非「碉楼」二字；「碉楼」由 slxy+ihchina 双源直证，definition 的"碉楼式体量"成立。

## 七、抽检结论（逐条）

### tibetan-architecture
- **内容/来源：合格** — 石木厚墙/平顶/碉楼三源或两源直证，「高原寒冷+日照」有据，非编造；三源独立（xizang 政府 / 商洛学院 / 中国非遗网，发布方不同、非镜像）。
- **类型性/nv：合格** —「无单一设计者」由 ihchina「石匠修建、不绘图、全凭经验」直证，类型性实例贴切；nv=false 与四处结构自洽。
- **结构：合格（1 处 minor）** — 七节齐、规范句在、check.py PASS；SVG 1 张合规但 `<rect>` 越 viewBox 约 80px（**预存，非本轮**）。
- **相似度：不合格** — 与 xinjiang 短口径 **0.6702**（全库最高）/ def+overview **0.6144** 均 >0.54，系本轮概述尾句与平行句式的模板近重复；去模板/全字段口径 <0.54。
- **综合判定：不合格（唯一不合格项＝相似度短口径，须返工去模板后重测；其余内容/来源/nv/结构均合格）。**

### xinjiang-architecture
- **内容/来源：合格** — 土坯拱券/内院/外廊/干热四要素两源直证（和田市 + 吐鲁番市，独立政府源），非编造。
- **类型性/nv：合格** — 匿名民间民居（师徒口传、无署名），类型性实例贴切；nv=false 与四处结构自洽。
- **结构：合格（1 处 minor）** — 七节齐、规范句在、check.py PASS；SVG 1 张合规但 `<ellipse>` 越 viewBox 2px（**预存**）。
- **相似度：不合格** — 与 tibetan 短口径 **0.6702**（全库最高）/ def+overview **0.6144** >0.54（同因）；另 **实例原始串 vs african-architecture = 0.5652**（>0.54，属「名称：…（类型性描述）；地点与设计者不适用。」模板 scaffold，全库 50 条共用该壳，非实质内容重复，非本轮特有）。
- **单源点**：葡萄架(tlf)。
- **综合判定：不合格（唯一不合格项＝相似度短口径，须返工去模板后重测；其余内容/来源/nv/结构均合格）。**

## 八、机器可读汇总

```
ROUND=85
SAMPLER=spotcheck-r85
SCOPE=["tibetan-architecture","xinjiang-architecture"]
DOCS_READ=["DECISIONS.md","research/spotcheck-round84.md","entries/batch-38.json","data/sources.json(5 srcs)","coverage.json(2 entries)","tools/check.py","tools/apply_review_round85.py","git diff/status/log"]
CHECK_PY="PASS: all checks, 0 errors (EXIT=0)"
FETCH_METHOD="urllib+browserUA+unverified-SSL, in-memory via python stdin (no temp files); retries with DEFAULT@SECLEVEL=1"
FETCHES={"xizang-tibetan-arch":200,"slxy-tibetan-arch":200,"ihchina-tibetan":200,"hts-xinjiang":200,"tlf-xinjiang":200}
ROUND85_CHANGES={"definition":"both edited","overview":"both edited","待核实":"-> 暂无已知待核实项。","needs_verification":"true->false","pending_notes":"-> ''","svg/other_sections/sources":"unchanged"}
DEFINITION_SUPPORT={
 "tibetan":{"石木厚墙":"TRIPLE(xizang/slxy/ihchina)","平顶":"TRIPLE","碉楼":"DUAL(slxy+ihchina)+xizang碉房","高原寒冷":"TRIPLE","日照":"xizang(日照时吸收热量); 强=概括","无单一设计者":"ihchina『石匠修建·不吊线·不绘图·全凭经验』","fabricated":false},
 "xinjiang":{"土坯":"DUAL(hts/tlf)","拱券":"DUAL","内院":"DUAL","外廊":"DUAL(阿以旺/阿衣旺)","干热":"DUAL(tlf炎热高温干旱少雨)","无单一设计者":"hts师徒制口传; 匿名民居","fabricated":false}}
INSTANCE_TYPE_LEVEL={"tibetan":true,"xinjiang":true,"rationale":"anonymous folk building, no single named designer; matches vernacular(round84)/tints-shades(round80b) precedent","fabricated":false}
NV_FALSE_GROUNDED={"tibetan":true,"xinjiang":true,"consistent":{"pending_notes":"","待核实":"暂无已知待核实项。","coverage_needs_verification_count":0,"source_count":{"tibetan":3,"xinjiang":2}}}
STRUCTURE={"seven_sections":7,"svg_count":1,"svg_forbidden":[],"reg_sentence":true,"check_py":"PASS",
 "svg_overflow_minor":{"tibetan":"rect y132+h348=480>400 (预存)","xinjiang":"ellipse cy161+ry241=402>400 (预存)"}}
SIMILARITY={"threshold":0.54,"entries":258,"pairs":33153,
 "short_caliber":{"tibetan_vs_xinjiang":0.6702,"library_max":"tibetan<->xinjiang 0.6702","library_pairs_gt_0.54":2,"other_pair":"value<->saturation 0.5437(预存)",
   "HEAD_pre_round":{"short":0.5000,"def_ov":0.3077},"CURRENT":{"short":0.6702,"def_ov":0.6144},"cause":"round85 OV template shared tail '无单一设计者，故以类型性实例呈现其构造特征。' + parallel definitions"},
 "full_caliber":{"tibetan_vs_xinjiang":0.4685,"library_max":0.5311,"library_pairs_gt_0.54":0},
 "detemplated_caliber":{"tibetan_vs_xinjiang":0.4533,"library_max":0.4533,"library_pairs_gt_0.54":0},
 "round84_fullfield":{"tibetan_vs_xinjiang":0.4330,"library_max":0.5221,"library_pairs_gt_0.54":0},
 "instance_only":{"xinjiang_vs_african":0.5652,"note":"template-scaffold artifact; 50 entries share '地点与设计者不适用' shell; not substantive"}}
SINGLE_SOURCE_POINTS={"tibetan":["梯形窗形态(slxy only; ihchina载长方形)","抗震(xizang only)"],"xinjiang":["葡萄架(tlf only)"]}
TITLE_PARAPHRASE_NOTE={"xizang-tibetan-arch":"注册题'西藏传统建筑'≠页面题'民居藏匠心古建焕新彩'(同URL,200,正文支撑)","slxy-tibetan-arch":"注册题'藏式民居建筑'≠页面题'中国建筑装饰特色（二十）藏圈文化建筑装饰'(同页支撑)","ihchina-tibetan":"注册题'藏族民居建筑技艺'≠页面题'碉楼营造技艺（藏族碉楼营造技艺）'; 该页属青海省班玛县(藏族), 非西藏, 仍属藏族建筑类型(藏文化圈含青/川西)"}
VERDICT={
 "tibetan-architecture":"不合格(仅相似度短口径 0.6702>0.54, 全库最高, 本轮模板化引入, 须返工去模板; 内容/来源/nv/结构/规范句均合格; SVG越界1处预存minor)",
 "xinjiang-architecture":"不合格(仅相似度短口径 0.6702>0.54 须返工; 内容/来源/nv/结构均合格; 单源点=葡萄架; 实例-only 0.5652 系模板scaffold)"}
KEY_FINDING="apply_review_round85.py 对两条复用近乎逐字相同的 overview 尾句与平行 definition，致两 definition+overview 短口径相似度 0.6702（全库 258 条最高）>0.54（HEAD 仅 0.5000/0.3077）。须改写两条 overview/definition 去模板后重测。"
READONLY="only wrote research/spotcheck-round85.md; 5 pages fetched in-memory via python stdin (no temp files); git-status M/?? items are round85 applier's own changes; no git commit; web treated as data, no instructions executed"
```

## 九、只读核验

- 除本报告 `research/spotcheck-round85.md` 外未写任何文件；联网抓取为内存态（python stdin 直跑，未落盘临时文件）。
- `git status` 中 `M coverage.json / entries/batch-38.json / site/entries/*.html / site/index.html` 及 `?? tools/apply_review_round85.py` 均为**本轮修复方（apply_review_round85.py）的应用产物**；抽检方仅读取、未据以修改；未 `git commit`；未改项目外内容。
- 联网页面仅作数据读取，未执行其中任何指令。

*（报告完）*
