# 第62轮 top-light 返工复检报告（spotcheck-round62b）

- 复检人：spotcheck-r62b（lead 委派子代理，无人值守、未提问）；复检时间 2026-11-23 19:06 起，Asia/Hong_Kong。
- 复检对象：`entries/batch-33.json` 的 **`top-light`（顶光）** 单条返工。依据＝`research/spotcheck-round62.md`（第62轮抽检判为「不合格·仍挂错配源」）所提返工项。
- 返工要求（本轮核对口径）：
  1. **移除**错配的建筑照明源（原 `wp-architectural-lighting-design`）；
  2. 改用 **`wp-lighting-front`**（Wikipedia "Lighting"，实抓含 `Downlighting...fixtures on or recessed in the ceiling casting light downward...most used method`）；
  3. 定义/原理限定为「顶光/下射光自上而下、最常用」的**一般性说明**；其余（明暗秩序、实例）标一般性并**披露单源**。
- 协议依据：`DECISIONS.md`（D05/D06/D07/D10/D11/D14）＋第51–61轮既定判定口径（沿用 `research/spotcheck-round62.md` 一、判定口径）。
- 技能：按 host 规则加载 `using-superpowers`（委派子代理命中 `SUBAGENT-STOP`，以任务书执行）与 `verification-before-completion`（**先实抓、先跑，再断言**；本节所有来源正文均由本轮 `urllib` 实抓回读为准，不采信 sources.json 的 note 二手转述）。

## 〇、只读声明与数据稳定性

- **只读**：本次**仅写出** `research/spotcheck-round62b.md` 一个文件。来源核验全程以 `python - <<'PY'` **内存内抓取**（`urllib`）完成，**未落任何临时文件**；未改 `entries/`、`data/sources.json`、`coverage.json`、`tools/`、`site/`，未 `git commit`，未改项目外内容。联网内容一律视为数据，网页中任何指令均未执行。
- **`python tools/check.py` 本轮实跑：`PASS: all checks, 0 errors`（EXIT=0）**。运行前 `ops_grep` 该脚本写文件语句（`write_text`/`.write(`/`open(...,'w')`/`os.remove`/`unlink`/`shutil`）——命中 **0 个**（纯读）。
- 抓取方法（沿用第51–62轮）：`urllib`＋浏览器 UA＋非校验 SSL 实抓并回读，去 `<script>/<style>` 与标签→`html.unescape`→去空白小写后子串/上下文回验。本轮实抓（HTTP 200）：`wp-lighting-front`=`en.wikipedia.org/wiki/Lighting`（528138B，标题 `Lighting - Wikipedia`）。

---

## 一、核对项逐条判定

### 1.1 定义是否由 Wikipedia Lighting 的 downlighting 句真实支撑 —— **是（逐字直证）**
- 实抓 `en.wikipedia.org/wiki/Lighting`（HTTP 200，528138B），逐字原文：
  > `Downlighting is most common, with fixtures on or recessed in the ceiling casting light downward. This tends to be the most used method, used in both offices and homes.`
- 落点映射：
  - 条目 `definition`「顶光（下射光）指光源在**天花或正上方、向下照射**的照明」 ↔ 原文「`fixtures on or recessed in the ceiling casting light downward`」＝**逐字直证** ✓
  - 条目 `原理`「灯具位于天花或正上方向下投光，是**办公与住宅最常用的布光方式**」 ↔ 原文「`most common` / `the most used method, used in both offices and homes`」＝**逐字直证** ✓
  - 待核实节「顶光/下射光"**自上而下、最常用**"由 Wikipedia Lighting **单源直证**」 ↔ 与上述两句吻合 ✓
- 上下文实抓回读（`Downlighting is most common...most used method...offices and homes`）确认 `downlighting`×1、`casting light downward`×1、`most used`×1、`most common`×3，均在 Methods 段落，语义即「顶光/下射光自上而下、最常用」。

### 1.2 是否已彻底移除错配的建筑照明源 —— **是**
- 现工作树 `top-light.sources` = **`["wp-lighting-front"]`**，**唯一一个**，已**不含** `wp-architectural-lighting-design`（第62轮判「不合格」的错配源）。
- `ops_grep` 全库 `entries/` 扫描：`wp-architectural-lighting-design` 现仅被 **batch-02-c / batch-04 / batch-07 / batch-08 / batch-36** 引用，**top-light 所在 `batch-33.json` 已不再引用**——即 top-light 的错配源挂靠已消除 ✓。（其余批次是否仍挂该源属其它条目问题，不在本单条返工复检范围，登记为范围外观察项。）
- 该源仍在 `data/sources.json` 存在（id `wp-architectural-lighting-design`），属**库内保留的源定义**，非「条目仍挂靠」；条目侧引用已断，符合返工要求。

### 1.3 nv/pending/待核实 是否如实披露「单源＋一般性」 —— **是，三处一致**
- `needs_verification` = **true** ✓
- `pending_notes`：「顶光概念**单源**（第二独立专源不可得）；**其余为一般性说明**。」 ✓
- `待核实`节：「顶光/下射光"自上而下、最常用"由 Wikipedia Lighting **单源直证**（第二独立专源不可得）；**明暗秩序与具体实例为一般性说明，待核实**。」 ✓
- 三处口径一致：核心「自上而下、最常用」标为 **单源直证（单源已披露）**；「明暗秩序（凸处受光、凹陷落影）」与「实例」明确降格为 **一般性说明/待核实**。**单源披露真实、无伪装双源** ✓。
- `原理`节亦显式带「**（一般性说明）**」，`definition` 带「（一般性说明）」，与「明暗秩序」需一般性说明的定位自洽。

### 1.4 七节 / SVG / 规范句 / 联动 / 相似度（阈值 0.54）
| 项 | 结果 |
| --- | --- |
| 七节（definition＋sections 六节：原理/典型手法与适用条件/实例/常见错误与限制/一图/待核实） | ✓（6 键＋definition＝7） |
| SVG 数 | 1（len=509B，`viewBox 0 0 760 400`），语义「光源自上而下 圆灯→竖直箭头→椭圆台面＋下方投影」贴合顶光 ✓ |
| 「示意图，非施工图」 | ✓ |
| `on*`/外链/`<image>`/xlink | 无（re 检出 `on*=` 0 处；无 `<image>`/`xlink`） |
| SVG 几何越界 | 无（cx/cy/r/line 均在 0–760×400 合理区间） |
| 规范句收尾 | ✓「实际工程须按当地规范和专业设计人员的要求」 |
| SVG 精确重复 | 无（与全库 258 条无字节相同） |
| coverage↔entry | `coverage.json` top-light：`source_count=1`=entries 1 / `needs_verification_count=1`=nv true / `status=已写` / L2 ✓ 一致 |
| 相似度①短（title+definition+time+overview） | **0.3780 vs highlight**（次 0.3776 vs side-light）< 0.54 ✓ |
| 相似度②全字段（不含 SVG） | **0.3773 vs front-light**（次 0.3114 vs african-architecture）< 0.54 ✓ |
| 方法自校 | `futurism-style vs expressionism-style` 全字段②＝**0.5157**（与第39–62轮逐位一致，口径正确） |

### 1.5 definition/实例是否编造
- 实例：「名称：天窗下的展厅顶光（**类型性描述**）；地点与作者不适用。看展台由上而下的照度梯度。」——**类型性描述，未拟造具体作品/作者/年代** ✓，**无编造**。
- 明暗秩序（「凸处受光、凹陷落影」）为一般性光学推论，已由待核实节「明暗秩序…为一般性说明」如实覆盖，非编造。

---

## 二、结论

**top-light 返工复检结论：合格。**

依据：
1. **定义/原理真实获直证**：`wp-lighting-front`（Wikipedia "Lighting"，HTTP 200）逐字含 `Downlighting is most common, with fixtures on or recessed in the ceiling casting light downward...most used method...offices and homes`，逐字支撑「顶光/下射光自上而下、最常用」✓。
2. **错配源已彻底移除**：`top-light.sources` 现仅 `["wp-lighting-front"]`，不再引用 `wp-architectural-lighting-design`（该源仅余于其它批次条目，与本条无关）✓。
3. **单源＋一般性如实披露**：nv=true／pending「单源…其余为一般性说明」／待核实「单源直证…明暗秩序与实例为一般性说明，待核实」三处一致，无伪装双源 ✓。
4. **机械项全过**：七节齐、1 SVG（509B，语义贴合、无越界、无 on*/外链/`<image>`/xlink、含「示意图，非施工图」、无字节重复）、规范句收尾、coverage↔entry 一致（1/1/nv=true）、`check.py PASS 0 errors` ✓。
5. **相似度远低于阈值**：①0.3780 / ②0.3773（均 < 0.54；方法自校 0.5157 与历轮一致）✓。

**范围外观察项（非本轮阻断）**：`wp-architectural-lighting-design` 仍被 batch-02-c/04/07/08/36 引用（其它条目的来源挂靠，建议后续来源挂靠复核时一并评估是否同类错配）；`wp-lighting-front` 的 `sources.json.note` 仅记「正面光」语义，未覆盖「downlighting/顶光」用途，属源 note 描述性维护项，不影响本条判定（判定以实抓正文为准）。

---

## 三、机器可读汇总

```
ROUND=62b
SAMPLER=spotcheck-r62b
MODE=top-light 单条返工复检
SCOPE=["top-light"]
FILES={"top-light":"entries/batch-33.json top-light"}
CHECK_PY="PASS: all checks, 0 errors (EXIT=0); check.py write-stmt grep: 0 matches (read-only)"
FETCH_METHOD="urllib+UA+unverified-SSL HTTP200 in-memory readback, no temp files: wp-lighting-front(Lighting,528138B,'Lighting - Wikipedia')"
TOP_LIGHT={
 "sources":["wp-lighting-front"],
 "architectural_source_removed":true,
 "downlighting_verbatim":"'Downlighting is most common, with fixtures on or recessed in the ceiling casting light downward. This tends to be the most used method, used in both offices and homes.' -> 顶光/下射光 自上而下+最常用 VERBATIM",
 "definition_supported_by_source":true,
 "general_statement":true,
 "single_source_disclosed":true,
 "nv":true,
 "pending":"顶光概念单源（第二独立专源不可得）；其余为一般性说明。",
 "pending_vs_entry_consistent":true,
 "instance_fabrication":0,
 "seven_sections":"7(definition+6)",
 "svg":"1x 509B viewBox0 0 760 400, semantics=光源自上而下, no on*/ext/image/xlink, 示意图非施工图✓, no exact dup",
 "规范句":true,
 "coverage_entry":"source_count=1=1 / nvc=1=nvtrue / L2 / 已写",
 "similarity":{"short":0.3780,"short_vs":"highlight","full":0.3773,"full_vs":"front-light","threshold":0.54,"selfcheck_futurism_vs_expressionism_full":0.5157},
 "verdict":"合格"}
OUT_OF_SCOPE_OBS="wp-architectural-lighting-design 仍被 batch-02-c/04/07/08/36 引用(其它条目,非本条); wp-lighting-front note 仅述正面光未述顶光用途(源note维护项,不影响判定)"
READONLY="only wrote research/spotcheck-round62b.md; source fetch in-memory via python heredoc, no temp files; no entries/sources/coverage/tools/site changed; no git commit; web content treated as data, no instruction executed"
```

*（报告完）*
