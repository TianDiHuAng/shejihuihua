# 第2轮质量闸抽检报告 — spotcheck-round02

抽检人：spotcheck-r2（子任务）
抽检日期：2026-11-22（Asia/Hong_Kong）
抽检对象：本轮新增 38 条中随机指定的 4 条 — `chiaroscuro`、`six-principles`、`borrowed-scenery`、`modernism`
数据位置：`entries/batch-02-a.json`、`entries/batch-02-b.json`、`entries/batch-02-d.json`；来源库 `data/sources.json`

## 核验方法
1. 逐条读取条目 definition / time_or_place / overview / sources / needs_verification / pending_notes。
2. 在 `data/sources.json` 中确认每个 source id 存在且 `verified=true`。
3. 因 web_search / web_fetch 在本环境报错，改用 Python urllib + 浏览器 User-Agent 直连来源页面，HTTP 状态与 H1 标题如下（全部 200，标题与来源库登记一致）：

| source id | 来源库标题 | HTTP | 页面 H1 |
| --- | --- | --- | --- |
| wp-chiaroscuro | Chiaroscuro | 200 | Chiaroscuro |
| wp-tenebrism | Tenebrism | 200 | Tenebrism |
| wp-six-principles-chinese-painting | Six principles of Chinese painting | 200 | Six principles of Chinese painting |
| wp-xie-he | Xie He | 200 | Xie He |
| wp-borrowed-scenery | Borrowed scenery | 200 | Borrowed scenery |
| wp-chinese-garden | Chinese garden | 200 | Chinese garden |
| wp-modern-architecture | Modern architecture | 200 | Modern architecture |
| wp-le-corbusier | Le Corbusier | 200 | Le Corbusier |

4. 打开页面首段正文，核对条目事实是否有支撑，是否编造年份/人名/引文；核对与来源文本的重合与套话情况。

## 逐条结论

- **chiaroscuro — 合格**。依据：`wp-chiaroscuro`（页面标题 Chiaroscuro，HTTP 200，verified=true）、`wp-tenebrism`（页面标题 Tenebrism，HTTP 200，verified=true）。definition「以强烈明暗对比塑造体积和戏剧性效果」对应 Chiaroscuro 页首段「the use of strong contrasts between light and dark」；overview「光线作为组织画面焦点…其后出现更极端的暗绘倾向」对应 Chiaroscuro 页「focus strongly on the subject of a painting is called tenebrism」及 Tenebrism 页「especially pronounced chiaroscuro」。两来源均与主题直接相关。needs_verification=false、pending_notes 为空，正文无「待核实」声明，一致。无编造年份、人名、引文，无大段重合。问题：无（time_or_place「文艺复兴至19世纪欧洲」为宽泛时期标签、来源页有对应历史叙述，未写具体年份，可接受）。

- **six-principles — 合格**。依据：`wp-six-principles-chinese-painting`（页面标题 Six principles of Chinese painting，HTTP 200，verified=true）、`wp-xie-he`（页面标题 Xie He，HTTP 200，verified=true）。definition「六条准则，传统上归于谢赫」对应来源页「were established by Xie He」；overview「气韵、用笔、象形、赋彩、位置与传移」与来源页六法条目（spirit resonance / bone method / correspondence to the object / suitability to colour / division and planning / transmission by copying）逐项对应。time_or_place「古代中国」对应来源「written circa 550」（未编造具体年份，作宽泛表述）。两来源均与主题直接相关。needs_verification=false、pending_notes 为空，正文无「待核实」声明，一致。无编造年份、人名、引文，无大段重合。问题：无。

- **borrowed-scenery — 合格（附轻微提示）**。依据：`wp-borrowed-scenery`（页面标题 Borrowed scenery，HTTP 200，verified=true）、`wp-chinese-garden`（页面标题 Chinese garden，HTTP 200，verified=true）。definition「把园外景物纳入园内视线」对应来源页「incorporating background landscape into the composition of a garden」；overview「远景、山形」对应来源页「a view on a distant mountain」。两来源均与主题直接相关。needs_verification=false、pending_notes 为空，正文无「待核实」声明，一致。无编造年份、人名、引文，无大段重合。**轻微提示（不影响合格判定）**：overview 举例「塔影」在所引 Borrowed scenery 页正文中未出现（页面有「distant mountain」及日本庭园中城堡远景的图注，但无 pagoda/tower 表述），属未被该来源直接支撑的示例，但为通用描述、未指向具体对象或年份，不构成编造事实；time_or_place「古代中国」而来源强调其为东亚（中/日）造景传统且见于 17 世纪《园冶》，表述略偏窄，但仍属宽泛定性。

- **modernism — 合格**。依据：`wp-modern-architecture`（页面标题 Modern architecture，HTTP 200，verified=true）、`wp-le-corbusier`（页面标题 Le Corbusier，HTTP 200，verified=true）。definition「以功能、结构与简洁形式为核心」对应来源页「principle of functionalism」「embrace of minimalism」「new and innovative technologies of construction」；time_or_place「20世纪、全球」对应「prominent in the 20th century」；overview「反对历史样式复制，强调新材料、新结构」对应「desire to break away from historical architectural styles」「new technologies」。两来源均与主题直接相关（Le Corbusier 为该页正文引用的代表人物）。needs_verification=false、pending_notes 为空，正文无「待核实」声明，一致。无编造年份、人名、引文，无大段重合。问题：无（「空间自由」为现代主义通行概括，未在首段逐字出现，属合理概述）。

## 总体结论
- 抽检 4 条：**合格 4 条，不合格 0 条，待核实 0 条**。
- 4 条的 8 个来源引用 id 全部存在、verified 均为 true，来源页 HTTP 200 且标题与登记一致，来源主题与条目直接相关；未发现编造年份、人名、引文；未发现与来源文本大段重合；needs_verification / pending_notes 与正文声明一致。
- 仅 borrowed-scenery 有一处轻微提示（「塔影」示例未被所引页面直接支撑），属通用描述，不构成不合格。
- **是否建议整批返工：不建议**。本批抽检未触发 AUTONOMOUS.md 第 E 节「不合格则整批返工」条件，待核实占比与硬写迹象未见异常。
