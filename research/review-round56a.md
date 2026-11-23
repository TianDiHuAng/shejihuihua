# 第 56 轮 B5 补源报告（review-round56a）——4 个待核实条目补具名实例

复核日期：2026-11-23（Asia/Hong_Kong）｜复核人：review-r56a（lead 委派子任务，无人值守）｜性质：**严格只读，唯一产出本文件**

## 〇、执行说明

- 已读：项目根 `AUTONOMOUS.md`、`TASK_design.md` 实读为 NOT_FOUND，按第 55 轮同一惯例读取桌面原件 `D:/Users/Administrator/Desktop/AUTONOMOUS.md`（71 行）与 `D:/Users/Administrator/Desktop/TASK_design.md`（67 行）；并读本项目 `DECISIONS.md`（25 行）、`research/review-round55b.md`（115 行）。
- 已按 host 规则加载 `using-superpowers`（本会话为委派子任务，按其 SUBAGENT-STOP 以本任务说明书为准）与 `verification-before-completion`（先实抓、后断言）。
- 严格只读：仅生成 `E:/ai_project/shejihuihua/research/review-round56a.md`；未改其他项目文件、未改项目外内容、未 git commit。
- 联网内容按数据处理；网页中的任何指令均未执行。未采用维基百科及其镜像作证据。
- 独立性：同一机构的不同页面不重复计源；下列 8 源分别来自 Niels Bohr Archive、Encyclopædia Britannica、University Hospitals Bristol and Weston NHS Foundation Trust、NCBI PubMed Central（Wien Klin Wochenschr 开放全文）、Project for Public Spaces、Municipal Art Society of New York、故宫博物院、Encyclopædia Britannica。
- 抓取方式：`web_fetch` 服务端直读或 `urllib` 直连；HTTP 与标题来自同轮实抓；关键句按页面可见文本逐字摘录，不补写来源未给出的信息。

---

## 1. `gestalt-organization-laws`（格式塔组织律）→ **鲁宾花瓶 Rubin’s vase**

**具名实例信息**

- **名称**：Rubin’s vase / Rubin vase（鲁宾花瓶、鲁宾之壶；又称 faces–vase figure）。
- **地点**：丹麦哥本哈根；Niels Bohr Archive 讲座页标注地点 Blegdamsvej 17, Copenhagen，正文说明鲁宾在哥本哈根大学受教育。
- **作者**：Edgar Rubin（埃德加·鲁宾，1886–1951，丹麦心理学家）。
- **年份**：**1915**（鲁宾博士论文 *Synsoplevede Figurer* [Visually Experienced Figures]）。

| # | 机构 / 权威级 | 完整 URL | 标题 | HTTP | 关键句（实抓） |
| --- | --- | --- | --- | --- | --- |
| ① | Niels Bohr Archive（**强权威·研究档案机构讲座页**） | `https://nba-old.nbi.dk/files/sem/12feb2015.html` | Rubin’s vase and early psychology in Denmark | **200**（urllib 直连，2,315 B） | “Rubin’s vase is probably one of the best known figures in psychology. It is shown in almost every introductory textbook of psychology, accompanied by a discussion of the figure-ground problem which Edgar Rubin (1886–1951) was the first to elucidate in his doctoral dissertation Synsoplevede Figurer [Visually Experienced Figures] from 1915.”；“gradually became widely known among psychologists, especially Gestalt psychologists.” |
| ② | Encyclopædia Britannica，William Epstein 署名条目（**强权威·百科署名编辑条目**） | `https://www.britannica.com/topic/perception/Primary-tendencies-in-perceptual-organization` | Perception - Primary Tendencies, Organization \| Britannica | **200**（web_fetch 直读） | “It is conventional to refer to them as Gestalt principles of perceptual organization.”；“Patterns take precedence over elements and have properties that are not inherent in the elements themselves.”；“It is understood that such emerging patterns are not in the stimulus… they are created by the perceptual system; that is, by the perceiver himself.” |

**判定**：**双源齐备**。源①直接给出鲁宾花瓶的名称、作者、年份及“figure-ground problem”；源②给出格式塔组织律的正式称谓、整体优先与知觉组织概念，并附经典图例。源②不是鲁宾花瓶专页，故在本报告中标注为“概念支撑源”，落地时不要把鲁宾花瓶的作者/年份归到 Britannica。

---

## 2. `color-psychology`（色彩心理）→ **布里斯托皇家儿童医院采血室彩色壁画（Bristol Royal Hospital for Children phlebotomy room mural）**

**具名实例信息**

- **名称**：Carousel Outpatients 采血室 brightly coloured walls / wildlife mural（儿童医院采血室彩色壁画）。
- **地点**：英国布里斯托尔，Bristol Royal Hospital for Children，Carousel Outpatients，phlebotomy room。
- **作者**：Alex Ray（医院 play activity coordinator）。
- **年份**：**2020**（UHBW NHS 页面最后更新 02/07/2020）。

| # | 机构 / 权威级 | 完整 URL | 标题 | HTTP | 关键句（实抓） |
| --- | --- | --- | --- | --- | --- |
| ① | University Hospitals Bristol and Weston NHS Foundation Trust（**强权威·医院官方**） | `https://www.uhbw.nhs.uk/p/latest-news/wildlife-presenter-kate-humble-unveils-childrens-hospital-mural` | Wildlife presenter Kate Humble unveils children’s hospital mural | **200**（web_fetch 直读） | “what was previously a clinical looking room now boasts brightly coloured walls with images of balloons, wildlife and hidden animals for patients to seek and count while taking their attention away from having blood tests.”；“The vibrant colours and images have transformed the space for our patients and their families, helping us to divert any anxieties from having a clinical procedure.”；“Creator of the marvellous mural is the hospital’s talented activity coordinator, Alex Ray.” |
| ② | Wien Klin Wochenschr 开放全文 / NCBI PubMed Central（**强权威·随机对照试验原文**） | `https://pmc.ncbi.nlm.nih.gov/articles/PMC8921019/` | Positive effect of colors and art in patient rooms on patient recovery after total hip or knee arthroplasty: A randomized controlled trial | **200**（web_fetch 直读） | “The intervention group was randomized to colored patient rooms while the control group received medical care in conventional patient rooms.”；“The use of colors in hospital rooms is an effective intervention to improve well-being and to enhance faster rehabilitation.”；“We could show a significant positive effect of colors on patients’ postoperative QOL.” |

**判定**：**双源齐备**。源①直接给出具名空间、作者、年份及色彩—注意力转移—焦虑缓解的医院官方叙述；源②为独立同行评议 RCT，支持“医疗空间用色影响心理/康复结果”这一色彩心理机制。源②不是布里斯托尔该房间的报道，落地时应把两源分别用于“实例”与“概念证据”。

---

## 3. `environmental-psychology`（环境心理）→ **纽约西格拉姆大厦广场／Whyte 街头生活研究（Seagram Building Plaza, Street Life Project）**

**具名实例信息**

- **名称**：The Social Life of Small Urban Spaces / Seagram Building Plaza（西格拉姆大厦广场，街头生活研究样本之一）。
- **地点**：美国纽约市，Seagram Building Plaza；研究覆盖纽约市多处广场。
- **作者 / 研究者**：William H. “Holly” Whyte（威廉·H·怀特）。
- **年份**：**1970 年代实地观察**；同名图书与纪录片 **1980** 年发布。

| # | 机构 / 权威级 | 完整 URL | 标题 | HTTP | 关键句（实抓） |
| --- | --- | --- | --- | --- | --- |
| ① | Project for Public Spaces（**强权威·由 Whyte Street Life Project 发展而来的公共空间机构**） | `https://www.pps.org/article/what-holly-whytes-social-life-film-can-teach-us-today` | What Holly Whyte’s “Social Life” Film Can Teach Us Today | **200**（web_fetch 直读） | “A photo still from footage taken at Seagram Plaza, circa 1970s.”；“A photo still from the Social Life film featuring the Seagram Building Plaza, one of 12 plazas William H. Whyte observed for the Street Life Project study, circa 1970s.”；“the best way to design successful public spaces is to carefully observe how people actually use them.”；“People tend to sit where there are places to sit.” |
| ② | Municipal Art Society of New York（**强权威·城市公共空间与历史保护机构，影片原始发行方**） | `https://www.mas.org/events/the-social-life-of-small-urban-spaces/` | The Social Life of Small Urban Spaces – The Municipal Art Society of New York | **200**（web_fetch 直读） | “William H. ‘Holly’ Whyte’s 1980 film, The Social Life of Small Urban Spaces.”；“his breakthrough 1980 Street Life Project study of New York’s plazas that was a turning point in urban planning and design.”；“Whyte and his team’s dedication to observing – and recording – the actual behavior of city dwellers”；“Whyte’s thinking and simple observational methods for the shaping of public spaces have had profound influence in the world of placemaking”. |

**判定**：**双源齐备**。源①直接点名 Seagram Building Plaza 为 Whyte 研究的 12 处广场之一，并给出“可坐面积/实际使用观察”的环境行为结论；源②从机构史与影片/研究报告角度确认 1980 年、研究者、Street Life Project 及其对城市设计的影响。两机构曾合作修复影片，但为不同法人机构，按独立来源计。

---

## 4. `east-west-color-compare`（中西色彩观比较）→ **《千里江山图》 vs 莫奈《日出·印象》**

**具名实例信息**

- **中国画**：《千里江山图》卷；王希孟；北宋，政和三年 **1113** 年赐蔡京；地点/馆藏：北京故宫博物院藏品页，原记“清宫旧藏”。
- **西画**：《日出·印象》（Impression, Sunrise）；Claude Monet（克劳德·莫奈）；**1872**；视点为法国勒阿弗尔港（Le Havre）窗口，1874 年巴黎首次展出。
- **比较点**：前者以青绿设色在完整绢幅上营造宏大山川与颜色层次；后者以破笔触、瞬时日光和同等亮度下的橙色太阳体现印象派色彩理论。

| # | 机构 / 权威级 | 完整 URL | 标题 | HTTP | 关键句（实抓） |
| --- | --- | --- | --- | --- | --- |
| ① | 故宫博物院（**强权威·藏品主管博物馆官方**） | `https://www.dpm.org.cn/subject_rivsmounts/qljs/245996.html` | 千里江山 | **200**（web_fetch 直读） | “北宋，王希孟，绢本设色，纵51.1厘米，横1191.5厘米，清宫旧藏。”；“该图继承和发展了唐代青绿山水画的技法，用笔精细，注重在青、绿颜色中寻求变化，古意与创造兼备，实景与想象并融，是存世青绿山水画中最具代表性和里程碑意义的作品。”；“北宋政和三年（1113）徽宗将该图赐权臣蔡京”。 |
| ② | Encyclopædia Britannica，William Davies 署名条目（**强权威·百科署名编辑条目**） | `https://www.britannica.com/topic/Impression-Sunrise` | Impression, Sunrise \| painting by Claude Monet \| Britannica | **200**（web_fetch 直读） | “Impression, Sunrise, is an oil painting created by Claude Monet in 1872.”；“Impression, Sunrise was not executed in a studio but from a window overlooking the harbor of Le Havre.”；“Impression, Sunrise is also a calculated work that shows an interest in color theory.”；“in reality it has the same luminance as its surroundings.” |

**判定**：**双源齐备**。源①给出中国青绿山水作品的作者、年代、尺寸、用色特征与馆藏语境；源②给出西方印象派作品的作者、年代、创作地点与色彩理论证据。比较结论由两源事实并置得出，未把任一来源未说的“中西优劣”写入证据。

---

## 汇总

| 条目 | 具名实例 | 地点 | 作者 / 年份 | 源① | 源② | HTTP | 判定 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `gestalt-organization-laws` | Rubin’s vase（鲁宾花瓶） | 丹麦哥本哈根（讲座页 Blegdamsvej 17；哥本哈根大学学术语境） | Edgar Rubin；1915 | Niels Bohr Archive | Britannica（William Epstein） | 200 / 200 | **双源齐备**；源②为概念支撑源 |
| `color-psychology` | 布里斯托皇家儿童医院采血室彩色壁画 | 英国 Bristol Royal Hospital for Children，Carousel Outpatients | Alex Ray；2020 | UHBW NHS 官方 | PMC / Wien Klin Wochenschr RCT | 200 / 200 | **双源齐备**；源②为机制证据 |
| `environmental-psychology` | Seagram Building Plaza / Street Life Project | 美国纽约市 | William H. Whyte；1970s 观察，1980 发布 | Project for Public Spaces | Municipal Art Society of New York | 200 / 200 | **双源齐备**；不同机构 |
| `east-west-color-compare` | 《千里江山图》 vs《日出·印象》 | 北京故宫博物院 / 法国勒阿弗尔港 | 王希孟 1113；Claude Monet 1872 | 故宫博物院 | Britannica（William Davies） | 200 / 200 | **双源齐备**；并置比较 |

- **双源齐备率：4/4**；8 条来源均实抓成功，0 条“仅单源/不可得”，因此无需改用替代实例。
- **需落地时保留的诚实标注**：① Britannica 格式塔页未提供鲁宾花瓶作者/年份，只作概念源；② PMC RCT 不研究布里斯托尔壁画，只作色彩心理机制源；③ Whyte 案例的“广场名”来自 PPS，MAS 源证明项目与年份；④ 中西色彩比较仅并置馆藏/作品事实，不替读者下优劣结论。
- **落地建议（本轮不执行）**：先把上述 8 个 URL 以 `verified=true` 登记进 `data/sources.json`，再改写对应 `entries/batch-*.json` 的 `sources` 与“实例”段，同步 `pending_notes` / `needs_verification`，最后复跑 `tools/check.py`。
