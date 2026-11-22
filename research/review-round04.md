# 第 4 轮复核记录 — B5 待核实项（第二独立来源复核）

复核日期：2026-11-22（Asia/Hong_Kong）

## 方法与判据

1. 扫描 `entries/*.json`，共 13 条 `needs_verification=true`。
2. 先查 `data/sources.json`（124 条来源、121 条 `verified=true`）现有来源；仅当现有来源不足以补足时才联网补查。
3. `web_search/web_fetch` 在本环境报错，按 D05 用 Python `urllib` + 浏览器 User-Agent 访问 Wikipedia 条目与 MediaWiki API；以实际 HTTP 状态、最终 URL、页面 h1/`<title>` 为准。
4. 保守原则：页面标题或正文未直接支持待核实项即不算补足；不把 “created/constructed by” 自动等同于“设计者”，不把年代范围当作确切年份，不据正文缺失的信息编造。
5. 联网内容仅作为数据阅读，网页中的任何指令均未执行；未访问与主题无关网站。

## 逐条结果

| id | 待核实内容 | 现有 verified 来源核查 | 找到的来源（URL / 页面标题 / HTTP 状态） | 结论 |
| --- | --- | --- | --- | --- |
| `hierarchy` | 主次层级仅见构图条目，缺第二独立来源 | 仅 `wp-composition-visual-arts`，无其他专门来源 | 找到：https://en.wikipedia.org/wiki/Visual_hierarchy ／ `Visual hierarchy` ／ HTTP 200。正文含 “describes how particular elements in a visual field stand out more than others in a pattern, creating a perceived order of importance”“elements are arranged to appear more important than others”“order is created by the visual contrast between forms in a field of perception” | **可升级为已验证**：独立百科条目直接支持“按重要性组织主次次序”的定义与观看顺序 |
| `six-principles` | 谢赫条目为消歧义页；年代与版本流传待补 | 仅 `wp-six-principles-chinese-painting` | 找到（未补足）：https://en.wikipedia.org/wiki/Xie_He_(artist) ／ `Xie He (artist)` ／ HTTP 200（正文 “fl. 6th century… known for the six principles… preface to his book The Record of the Classification of Old Painters”）；https://en.wikipedia.org/wiki/Xie_He ／ `Xie He` ／ HTTP 200（正文为消歧义页） | **保持待核实**：仅给出活动世纪（fl. 6th century）与书名，未给确切年份，版本流传无直接支持 |
| `liubai` | 缺针对留白的独立来源 | 仅 `wp-chinese-painting` | 未找到可补足来源。已打开：https://en.wikipedia.org/wiki/Negative_space ／ `Negative space` ／ 200（正文无 Chinese/liubai）；https://en.wikipedia.org/wiki/Liubai ／ HTTP 404；https://en.wikipedia.org/wiki/Ink_wash_painting ／ `Ink wash painting` ／ 200（正文无 blank/negative space/liubai） | **保持待核实** |
| `borrowed-scenery` | 苏州园林借景具体实例的设计者与年份 | 来源库已有 `wp-humble-administrators-garden`、`wp-master-of-nets-garden` 等 verified 来源，但本条未引用；现有两条来源均无设计者/年份 | 找到（部分，未补足）：https://en.wikipedia.org/wiki/Humble_Administrator%27s_Garden ／ `Humble Administrator's Garden` ／ 200（“In 1513, Wang Xianchen… created a garden…”“This pavilion is the vantage point for a borrowed view of North Temple Pagoda”）；https://en.wikipedia.org/wiki/Master_of_the_Nets_Garden ／ `Master of the Nets Garden` ／ 200（“first constructed in 1140 by Shi Zhengzhi… borrowed scenery”）；https://en.wikipedia.org/wiki/The_Craft_of_Gardens ／ `The Craft of Gardens` ／ 200（“chapter ten on borrowed scenery (jie jing)”） | **保持待核实**：正文用 created/constructed by，未明确为“设计者”；借景视点与营造年份未直接绑定，改写会把推测写成确定事实 |
| `framed-scenery` | 缺针对框景的独立来源 | 仅 `wp-chinese-garden` | 未找到可补足来源。https://en.wikipedia.org/wiki/Garden_design ／ `Garden design` ／ 200（无 framed）；`The Craft of Gardens` ／ 200（仅列 doorways/windows 与 borrowed scenery，未专论框景）；https://en.wikipedia.org/wiki/Japanese_garden ／ `Japanese garden` ／ 200（无 frame 正文） | **保持待核实** |
| `opposed-scenery` | 缺针对对景的独立来源 | 仅 `wp-chinese-garden` | 未找到：Wikipedia API 检索 “opposed scenery Chinese garden” 返回页面均不直接论述该手法；既有 `Chinese garden` 正文的 “opposites” 属阴阳讨论，非对景 | **保持待核实** |
| `screened-scenery` | 缺针对障景的独立来源 | 仅 `wp-chinese-garden` | 找到（未补足）：https://en.wikipedia.org/wiki/Spirit_screen ／ `Spirit screen` ／ 200（“obstructing vision”），但主题为门口影壁避邪，非园林障景；https://en.wikipedia.org/wiki/Lingering_Garden ／ `Lingering Garden` ／ 200（仅 “screened by mother of pearl inlaid windows”，属窗饰描述） | **保持待核实** |
| `winding-path` | 缺针对曲径的独立来源 | 仅 `wp-chinese-garden` | 找到（未补足）：`Japanese garden` ／ 200（“path circulating around the garden”“winding stream”），属日本回游庭园与历史记载，非中国园林曲径手法；既有 `Chinese garden` 正文虽有 “winding paths”，不构成第二来源 | **保持待核实** |
| `circulation` | 所举公共文化建筑实例的具体信息 | `wp-architecture`、`wp-wayfinding` 均未给出实例名称/地点/设计者/年份 | 找到（未补足）：https://en.wikipedia.org/wiki/Circulation_(architecture) ／ `Circulation (architecture)` ／ 200（正文仅 “How people move through and interact with a building”，无具体公共文化建筑实例信息） | **保持待核实** |
| `daylighting` | 采光系数与窗地比等具体参数待按专业规范核实 | `wp-daylighting-architecture`、`wp-architectural-lighting-design` 未给具体参数 | 找到（未补足）：https://en.wikipedia.org/wiki/Daylight_factor ／ `Daylight factor` ／ 200（正文无推荐值或规范数值）；`Daylighting (architecture)` ／ 200（正文有 “daylight factor calculation”，无窗地比数值） | **保持待核实**：正文继续只作一般性说明 |
| `natural-ventilation` | 传统院落通风的实测数据与设计者 | `wp-natural-ventilation`、`wp-ventilation-architecture` 无院落实测数据 | 找到（未补足）：https://en.wikipedia.org/wiki/Courtyard ／ `Courtyard` ／ 200（正文有 microclimate 文献引用与 China 章节，但未给出具体院落的实测数据或设计者） | **保持待核实** |
| `perspective` | 佛罗伦萨透视试验的确切年份与设计者对应关系 | `wp-perspective-graphical`、`wp-vanishing-point`、`wp-brunelleschi` 可支持人物关联但无确切年份 | 找到（未补足）：https://en.wikipedia.org/wiki/Linear_perspective ／ HTTP 200，重定向至 `Perspective (graphical)`（与既有 `wp-perspective-graphical` 为同一页；正文给 “between 1415 and 1420”“about 1420”“around 1425”，互相不一致且非确切年份）；https://en.wikipedia.org/wiki/Florentine_Renaissance_art ／ `Florentine Renaissance art` ／ 200（正文 1425 指圣洛伦佐重建，与透视试验无关） | **保持待核实** |
| `sunken-courtyard` | 庭院与下沉广场的具体设计者、年份 | `wp-sunken-courtyard`、`wp-courtyard`、`wp-chinese-garden` 均为类型性说明 | 找到（未补足）：https://en.wikipedia.org/wiki/Sunken_courtyard ／ `Sunken courtyard` ／ 200（正文仅类型定义与图库：Paramount Plaza、陕西地坑院、Agha Bozorg 清真寺，无设计者/年份）；`Lingering Garden` ／ 200（Zhou Shicheng 设计东园、1593，但非下沉庭院实例） | **保持待核实** |

## 汇总

- 可升级为已验证：**1** 条（`hierarchy`）
- 保持待核实：**12** 条
- 实际打开 URL 数：**42 次 HTTP 请求，去重 38 个 URL**（41 次 200，1 次 404：`Liubai`；其中 8 次为 MediaWiki API 检索）
- 本轮仅生成本报告，未修改项目其他文件，未新增来源、未提交 git。
