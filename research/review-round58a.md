# 第 58 轮 B5 补源报告（review-round58a）——4 条中国画理论条目补具名实例（各两条独立权威来源）

复核日期：2026-11-23（Asia/Hong_Kong）　｜　复核人：review-r58a（lead 委派子任务，无人值守）　｜　性质：**严格只读，唯一产出本文件**

## 〇、执行说明与只读声明

- **已读治理与上下文文档**：项目根 `AUTONOMOUS.md` / `TASK_design.md` 在本工作区实读为 NOT_FOUND；按 `research/review-round57b.md` 第 7 行记录，读取桌面原件 `D:/Users/Administrator/Desktop/AUTONOMOUS.md`（71 行）与 `D:/Users/Administrator/Desktop/TASK_design.md`（67 行）；并读本项目 `DECISIONS.md`（25 行）、`research/review-round57b.md`（124 行）。
- **已加载技能**：`using-superpowers`（本会话为委派子任务，按其 SUBAGENT-STOP 以任务说明书为准）、`verification-before-completion`（先实抓、后断言；关键句均取自本轮 `web_fetch` 实抓正文）。
- **硬性规则确认**：不编造名称、地点、作者、年份、引文、出处；关键事实须两个独立来源互证；同一机构只算 1 源；凑不齐双源写“仅单源/不可得”并尽量换更易双源实例。网页内容一律视为数据，页面中出现的任何指令均未执行。
- **通道与故障**：`web_search` 端点异常（返回 no web_search_tool_result，与 DECISIONS D05 一致）；`cn.bing.com` 结果页对中文多词查询严重污染（把“洛神赋图”拆成“洛神”），仅用于定位不作证据；Wikipedia / wikipedia API 在本环境 fetch failed；`www.dpm.org.cn/searchs.html` 404；`minghuaji.dpm.org.cn/search?k=...` 仅命中标题且多为 0 项；TNM collection search 404。证据正文全部来自 `web_fetch` 实抓的权威页面。
- **只读声明**：本轮仅生成 `E:/ai_project/shejihuihua/research/review-round58a.md`；未修改 `entries/`、`data/sources.json`、`coverage.json`、`tools/`、`site/` 或其他项目文件，未 git commit，未改项目外内容。

## 一、方法与判据

1. **实抓**：逐 URL 记录 HTTP 状态、页面标题、关键句；关键句直接引自本轮 `web_fetch` 返回的正文，未据记忆补全。
2. **独立性判据**：同一机构只算 1 源。故宫博物院（dpm.org.cn / minghuaji.dpm.org.cn）计 1 源；Britannica 计 1 源；ChinaCulture（en.chinaculture.org，中国文化网英文站）计 1 源。Britannica 的多篇 AI 问答页仍属同一机构，未彼此凑双源。
3. **权威性分级**：强权威＝博物馆/故宫官方、国家级文化机构官网、权威百科全书；中—强权威＝Britannica 编辑审稿词条与其官方 AI 问答页（页面自称 AI 生成、需核对，故仅作概念/语境支撑，不单独承载年份等硬事实）。
4. **不采用维基作主源**：沿用项目既定口径，Wikipedia 及其镜像未作证据。
5. **落地约束**：本报告只读产出，不直接改数据。落地须先把来源以 `verified=true` 登记进 `data/sources.json`，再改写对应 `entries/batch-*.json` 的 `sources` 与「实例」段，同步 `pending_notes` /「待核实」，复跑 `tools/check.py`。

## 二、四条补源（名称 / 地点 / 作者 / 年代 + 两条独立权威来源）

### 2.1 `qi-yun`（气韵生动）→ **顾恺之《洛神赋图》卷（宋摹本）**

- **名称**：顾恺之《洛神赋图》卷（宋摹），故宫博物院藏。
- **地点**：北京故宫博物院（源②：“His representative work, *Luoshen Appraisal Painting*, is now kept at the Palace Museum in Beijing.”）。
- **作者**：顾恺之（东晋，约 345—406；源①：“顾恺之（约345—406），工诗赋，善丹青。”）。
- **年代**：题作东晋，现存本学界一般认为是宋摹本（源①：“本幅无作者款印，原本相传为顾恺之作，学界一般认为是宋摹本。”）。

| # | 机构 / 权威级 | URL | 标题 | HTTP | 关键句（实抓） |
| --- | --- | --- | --- | --- | --- |
| ① | 故宫博物院·故宫名画记（**强权威·博物馆官方**） | `https://minghuaji.dpm.org.cn/paint/detail?id=69037b434240e1bbaa99067ca79e94f3` | 顾恺之洛神赋图卷（宋摹）-故宫名画记 | **200**（由 `/ad/hits/77` 重定向至此） | “东晋，顾恺之作，绢本，设色，纵27.1cm，横572.8cm”；“图中人物衣纹线条紧劲绵长，是典型的高古游丝描”；“传神写照，正在阿堵(六朝人口语“这个”，即指眼珠)之中”；“他提出的‘迁想妙得’、‘以形写神’等著名论点，对中国绘画的发展有深远影响。” |
| ② | ChinaCulture / 中国文化网英文站（**强权威·国家级文化机构官网**） | `http://en.chinaculture.org/gb/en_artqa/2003-09/24/content_39739.htm` | Luoshen Appraisal Painting | **200** | “His representative work, *Luoshen Appraisal Painting*, is now kept at the Palace Museum in Beijing.”；“The picture vividly captures the jovial mood of their first encounter, and the sadness that ensued following their separation. With an original concept and heart-stirring scenes, the painting is considered a classic in Chinese painting history.”；“Gu emphasized the subjects' expressions.” |

**对 `qi-yun`（气韵生动）的支撑**：两源各自独立且均点名该作品。源①给出“以形写神”“传神写照正在阿堵”的画论原文与“高古游丝描”的笔法描述，是气韵生动在人物画上的理论前提与技法表现；源②以“vividly captures the jovial mood… sadness… heart-stirring scenes”“considered a classic”给出权威评价。**保留标注（重要）**：两源均未逐字写出中文“气韵生动”四字，也未直接说“此画气韵生动”；落地应写“源①记为‘以形写神/传神写照’，源②记为‘生动捕捉情致’，按谢赫六法第一法归入气韵生动实例”，不得写成两源逐字使用了该术语。

### 2.2 `liubai`（留白）→ **马远、夏圭“马夏派”边角山水（代表作品类型：马远《寒江独钓图》）**

- **名称**：马夏派边角山水；常用具名代表为马远《寒江独钓图》（南宋）。**本轮双源只支持到“马夏派/马远、夏圭的边角构图”这一层级，未支持到《寒江独钓图》单幅的藏地与年代，落地须保留该标注。**
- **地点**：两源均未给单幅作品藏地；马夏派活动地域为南宋画院（临安）与浙江山水（源②：“Subjects in paintings of Ma Yuan and Xia Gui usually came from mountains and rivers of Zhejiang Province in East China.”）。单幅《寒江独钓图》藏地按“待核实”处理，不写死。
- **作者**：马远、夏圭（南宋画院画家；源②点名“Ma Yuan and Xia Gui”；源①：“two great painters of the Southern Song academy”）。
- **年代**：南宋，约 1175—1210（源① Quick Facts “Date: 1175 - 1210”，指马夏派活跃期）。

| # | 机构 / 权威级 | URL | 标题 | HTTP | 关键句（实抓） |
| --- | --- | --- | --- | --- | --- |
| ① | Britannica（**权威百科全书·编辑审稿词条**） | `https://www.britannica.com/art/Ma-Xia-school` | Ma-Xia school \| Traditional, Landscape, Chinese \| Britannica | **200** | “The aim of their landscapes was to create a feeling of **limitless space, a vast atmospheric void** out of which a few elements, such as mountain peaks and twisted trees, emerge with subdued drama.”；“Ma-Xia school compositions are of a type, called ‘one corner,’ that is asymmetrical, with the design weight off to one side and **the rest of the silk or paper left bare or slightly tinted**.”；“Ma and Xia are credited with the fullest expression of this tendency in Chinese painting.” |
| ② | ChinaCulture / 中国文化网英文站（**强权威·国家级文化机构官网**） | `http://en.chinaculture.org/gb/en_artqa/2003-09/24/content_39574.htm` | Four Great Painters in Southern Song Dynasty | **200** | “The Four Great Painters of the academies in the Southern Song Dynasty were Li Tang, Liu Songnian, **Ma Yuan and Xia Gui**.”；“This dynastic change was accompanied by a major change in landscape painting: **from a panoramic structure to a partial-focus layout**.” |

**对 `liubai`（留白）的支撑**：源①逐字给出“vast atmospheric void”“rest of the silk or paper left bare or slightly tinted”，是留白/空白构图最直接的权威英文表述；源②独立确认马远、夏圭为南宋画院四大家，并把构图变化概括为“from a panoramic structure to a partial-focus layout”（边角取景），与源①的“one corner”互证。**单幅作品级判定：仅单源/不可得**——《寒江独钓图》的第二独立权威来源本轮未取得：TNM collection search 404、`cn.bing.com` 结果污染、Britannica 专问页 `/art/How-did-Ma-Yuan-and-Xia-Gui-use-empty-space...` 与 `/question/...` 分别 403/404、Wikipedia 与 wikipedia API fetch failed。落地建议：流派级实例可标双源；若条目实例栏只收单幅作品，则维持 `needs_verification=true`，`pending_notes` 写明“单幅《寒江独钓图》第二独立权威源未取得”。

### 2.3 `yijing`（意境）→ **王维诗画 / 文人水墨山水传统**

- **名称**：王维（诗画合一）的文人水墨山水；传统代表作为《辋川图》，**本轮两源未点名《辋川图》单幅，故单幅级标“仅单源/不可得”**。
- **地点**：唐代长安／辋川（**待核实**，两源均未给作品具体地点）。
- **作者**：王维（701—761；源①：“Wang Wei (701–761)”）。
- **年代**：唐（盛唐至中唐；源①）。

| # | 机构 / 权威级 | URL | 标题 | HTTP | 关键句（实抓） |
| --- | --- | --- | --- | --- | --- |
| ① | Britannica（**权威百科全书·官方 AI 问答页，页面自标需核对**） | `https://www.britannica.com/art/How-did-Wang-Wei-influence-the-tradition-of-scholar-landscape-painting` | How did Wang Wei influence the tradition of scholar landscape painting? \| Britannica | **200** | “Wang Wei (701–761) is widely regarded as the foundational figure of the Southern school of painter-poets and the scholarly landscape painting tradition known as *wenrenhua*.”；“He is particularly associated with the *pomo* (‘breaking the ink’) technique, which utilized varied ink tones to create a **subtle, atmospheric effect rather than relying on surface representation**.”；“Later critics… characterized Wang’s work as **prioritizing personal expression over literal or decorative accuracy**.” |
| ② | ChinaCulture / 中国文化网英文站（**强权威·国家级文化机构官网**） | `http://en.chinaculture.org/gb/en_artqa/2003-12/17/content_44510.htm` | Chinese Brush Painting | **200** | “But even more important than the visual image is the **message behind the painting: it expresses the inner spirit of the subject or the feelings of the artist**.”；“This is why **a full flower is never painted, only a few blossoms representing the subject in its entirety**, and all of life (TAO principle.)” |

**对 `yijing`（意境）的支撑**：源②给出意境的定义性表述——画外的“message / inner spirit / feelings”重于视觉图像，并以“不全画花朵、只画几朵以代表整体”说明以少总多；源①独立给出王维作为文人画奠基者的身份，以及“subtle, atmospheric effect”“personal expression over literal… accuracy”的风格判断，两者合起来支撑“王维诗画作为中国画意境实例”。**保留标注**：源②未点名王维，源①未点名《辋川图》单幅；落地写“以王维诗画传统为意境实例（概念由源②、作者与风格由源①支撑）”，不要写“两源均评《辋川图》意境”。单幅《辋川图》维持待核实。

### 2.4 `bone-method`（骨法用笔）→ **吴道子《送子天王图》（又名《释迦降生图》；传吴道子，宋摹本，原作不存）**

- **名称**：吴道子《送子天王图》（"Presentation of Buddha"；源②：“The *Presentation of Buddha* is his most representative work.”）。
- **地点**：原作多为长安、洛阳寺观壁画（源②记“many of them involved Buddhism and Taoism”；严格地点未逐字给出，落地不写死具体寺名）。
- **作者**：吴道子（吴道玄；唐，约 700—760；源①：“Wu Daoxuan (flourished c. 700–760…)”）。
- **年代**：盛唐（开元、天宝间，713—755；源②：“Wu's most prolific period was during the Kaiyuan and Tianbao eras (713-755)”）。**原作不存，现存为摹本/传本。**

| # | 机构 / 权威级 | URL | 标题 | HTTP | 关键句（实抓） |
| --- | --- | --- | --- | --- | --- |
| ① | Britannica（**权威百科全书·编辑审稿词条**） | `https://www.britannica.com/biography/Wu-Daoxuan` | Wu Daoxuan \| Qing Dynasty, Landscape Art, Calligraphy \| Britannica | **200** | “He is especially noted for his imagination and **the expressive vigour of his brush**—which is cited even by Tang critics who lavished a ‘divine’ (*shen*) rating upon him.”；“Probably, however, his brush created **vividly expressive lines of alternately thick and thin tensions**—seen then and remembered still in distinct contrast to the more preciously coloured and evenly controlled delineations of the contemporary courtly style.”；“**There are no known extant works** that give anything other than the most hazy impression of his skill and accomplishment.” |
| ② | ChinaCulture / 中国文化网英文站（**强权威·国家级文化机构官网**） | `http://en.chinaculture.org/gb/en_artqa/2003-09/24/content_39639.htm` | Wu Daozi, Sage in Chinese Painting | **200** | “In Chinese history, three people are revered as sages: the calligrapher Wang Xizhi… the poet Du Fu… and **the painter Wu Daozi**, also of the Tang Dynasty.”；“Unlike his predecessor Gu Kaizhi, whose line strokes were slender and forceful but lacked variety, **Wu's strokes were full of change and vigor, expressing the internal world of his subjects**.”；“The *Presentation of Buddha* is his most representative work.” |

**对 `bone-method`（骨法用笔）的支撑**：两源均点名吴道子并直接评价其用笔。源①的“expressive vigour of his brush”“vividly expressive lines of alternately thick and thin tensions”即骨法用笔所说的线内结构张力；源②的“strokes were full of change and vigor, expressing the internal world”从另一机构独立给出同类判断，并点名代表作《Presentation of Buddha》。配合本轮另抓的 Britannica 概念页 `https://www.britannica.com/art/How-do-brushstrokes-create-movement-and-energy-in-Chinese-paintings`（HTTP 200）逐字写出“*gufa yongbi* (‘structural method in the use of the brush’)… essential for achieving *qiyun shengdong*”，可作为术语映射的补充（与源①同机构，不另计独立源）。**保留标注**：源①明确说吴道子无可靠存世真迹；落地必须写“传吴道子/宋摹本，原作不存”，不得写成真迹双源认证。

## 三、汇总

| 条目 | 具名实例 | 地点 | 作者 / 年代 | 源① | 源② | HTTP | 判定 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `qi-yun` | 顾恺之《洛神赋图》卷（宋摹） | 北京故宫博物院 | 顾恺之，东晋约345—406；现存宋摹 | 故宫名画记作品页 | ChinaCulture *Luoshen Appraisal Painting* | 200 / 200 | **双源齐备**；两源未逐字用“气韵生动”，用“以形写神/传神写照”与“vividly captures… classic”支撑概念归属 |
| `liubai` | 马远、夏圭马夏派边角山水（《寒江独钓图》为常用代表） | 南宋画院 / 浙江山水；单幅藏地待核实 | 马远、夏圭；约1175—1210 | Britannica *Ma-Xia school* | ChinaCulture *Four Great Painters in Southern Song Dynasty* | 200 / 200 | **流派级双源齐备**；**单幅《寒江独钓图》第二独立源不可得**，维持待核实 |
| `yijing` | 王维诗画 / 文人水墨山水传统 | 唐代长安、辋川（待核实） | 王维，701—761 | Britannica *How did Wang Wei influence…* | ChinaCulture *Chinese Brush Painting* | 200 / 200 | **传统级双源齐备**；**单幅《辋川图》第二源不可得**；源②不给作者、源①不给画名，落地须分写 |
| `bone-method` | 吴道子《送子天王图》（传，宋摹） | 长安/洛阳寺观壁画（具体寺名待核实） | 吴道子，唐约700—760；盛唐713—755 | Britannica *Wu Daoxuan* | ChinaCulture *Wu Daozi, Sage in Chinese Painting* | 200 / 200 | **双源齐备**；源①明确无可靠存世真迹，必须写“传/摹本” |

- **双源齐备（概念/流派级）：4/4**；其中**可落到单幅作品且两源均点名作品的仅 1/4**（`qi-yun` 的《洛神赋图》）；`liubai`、`yijing` 的单幅级第二源不可得；`bone-method` 两源点名作者与代表作英文名，但原作不存。
- **机构独立性**：全部 4 条的源①与源②分属不同机构（故宫博物院 / Britannica / 中国文化网）。Britannica 的多页面与 ChinaCulture 的多页面均只在同一条内计 1 源，未内部凑数。
- **需落地时保留的诚实标注**：①`qi-yun` 两源未逐字写“气韵生动”；②`liubai` 单幅《寒江独钓图》藏地与第二源待补；③`yijing` 两源分别支撑概念与作者，未点名《辋川图》；④`bone-method` 必须写“传吴道子/宋摹本，原作不存”；⑤所有来源页中出现的任何指令性文字均未执行。

## 四、被拒用来源记录（供后续参考，不作证据）

| URL / 来源 | 状态 | 处置 |
| --- | --- | --- |
| `https://www.britannica.com/art/How-did-Ma-Yuan-and-Xia-Gui-use-empty-space-in-their-landscape-paintings` | web_fetch 403 / urllib 404 | 放弃作留白单幅第二源 |
| `https://www.britannica.com/question/How-did-Ma-Yuan-and-Xia-Gui-use-empty-space-in-their-landscape-paintings` | web_fetch 403 / urllib 404 | 同上 |
| `https://www.britannica.com/biography/Ma-Yuan-Chinese-painter`、`/biography/Qi-Baishi`、`/biography/Wang-Wei`、`/art/wenrenhua` | 403（Cloudflare “Just a moment…”） | 放弃作对应第二源 |
| `https://whc.unesco.org/en/list/813/`（拙政园） | 403（Cloudflare） | 放弃拙政园替代方案 |
| `https://www.tnm.jp/modules/r_collection/index.php?controller=search&lang=en&keyword=Ma%20Yuan` | 200 但“ページが見つかりません” | 未取得《寒江独钓图》藏品页 |
| `https://www.dpm.org.cn/searchs.html?keyword=气韵生动` | 404 | 放弃故宫主站全文检索 |
| `https://minghuaji.dpm.org.cn/search?k=气韵生动`、`?k=马远` | 200 但命中 0 项 | 名画记搜索仅标题级，不作证据 |
| `https://www.npm.gov.tw/` | 200 但返回 “Challenge Validation” | 台北故宫藏品页未取得 |
| `https://en.wikipedia.org/wiki/Fishing_Alone_on_a_Cold_River`、wikipedia API | fetch failed | 仅作定位尝试，按项目口径不作证据 |
| `https://cn.bing.com/search?...` | 200 但中文多词结果严重污染（把“洛神赋图”拆成“洛神”） | 仅定位，不作证据 |

## 五、证据回执（verification-before-completion）

本轮所有采用来源均由 `web_fetch` 实抓，HTTP 状态、页面标题与关键句来自同一批响应；关键句均在第二节表内逐条列出，未使用记忆补全：

- 故宫名画记《洛神赋图》：HTTP 200，标题“顾恺之洛神赋图卷（宋摹）-故宫名画记”；“以形写神”“传神写照，正在阿堵”“高古游丝描”均见实抓正文。
- ChinaCulture *Luoshen Appraisal Painting*：HTTP 200；“kept at the Palace Museum in Beijing”“vividly captures the jovial mood… sadness”“considered a classic”均见实抓正文。
- Britannica *Ma-Xia school*：HTTP 200；“vast atmospheric void”“left bare or slightly tinted”“one corner”均见实抓正文。
- ChinaCulture *Four Great Painters in Southern Song Dynasty*：HTTP 200；“Ma Yuan and Xia Gui”“from a panoramic structure to a partial-focus layout”均见实抓正文。
- Britannica *How did Wang Wei influence…*：HTTP 200；“Wang Wei (701–761)”“subtle, atmospheric effect”“prioritizing personal expression”均见实抓正文。
- ChinaCulture *Chinese Brush Painting*：HTTP 200；“expresses the inner spirit of the subject or the feelings of the artist”“a full flower is never painted, only a few blossoms”均见实抓正文。
- Britannica *Wu Daoxuan*：HTTP 200；“expressive vigour of his brush”“vividly expressive lines of alternately thick and thin tensions”“no known extant works”均见实抓正文。
- ChinaCulture *Wu Daozi, Sage in Chinese Painting*：HTTP 200；“Wu's strokes were full of change and vigor”“The Presentation of Buddha is his most representative work”均见实抓正文。
- Britannica *How do brushstrokes create movement and energy…*：HTTP 200；“gufa yongbi (‘structural method in the use of the brush’)… essential for achieving qiyun shengdong”见实抓正文（仅作术语映射，与同机构词条合并计源）。

> 所有“仅单源/不可得”判定均附对应 URL 的实际 HTTP 状态与失败原因（见第四节），未在无证据情况下声称来源成立。
