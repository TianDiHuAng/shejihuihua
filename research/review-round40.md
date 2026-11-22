# 第 40 轮返工补源报告（review-round40）——4 条目各补两条独立权威来源

复核日期：2026-11-23（Asia/Hong_Kong）　｜　复核人：review-r40（lead 委派子任务，无人值守）　｜　性质：**严格只读，唯一产出本文件**

## 〇、执行说明与只读声明

- **已读治理文档**：项目根无 `AUTONOMOUS.md` / `TASK_design.md`；实读桌面同名文件 `D:/Users/Administrator/Desktop/AUTONOMOUS.md`（71 行）与 `D:/Users/Administrator/Desktop/TASK_design.md`（67 行）（**只读**），并与 `E:/ai_project/shejihuihua/DECISIONS.md`（21 行）核对；格式参照 `research/review-round39.md`。
- **硬性规则（TASK_design.md 第 34–42 行）确认**：不编造数字/日期/人名/引文/出处；**关键事实至少两个独立来源互相印证，否则标“待核实”**；引文最多一两句并标明出处；查不到宁可写“待补充/不可得”，不凑数。
- **已加载技能**：`using-superpowers`（本会话为委派子任务，按其 SUBAGENT-STOP 以本任务说明书为准）、`verification-before-completion`（**先实抓证据、后下断言**：全部关键句逐条 `norm(quote) in norm(page)` 回验，见第五节回执）。
- **数据快照（本轮只读核对 `entries/batch-38.json`）**：
  - `time-scenery`（L36–63）、`rock-garden`（L66–93）、`tibetan-architecture`（L607–634）、`xinjiang-architecture`（L637–664）：`sections.实例` 现均为“类型性描述（名称/地点/设计者不适用）”，`sources` 均指向 **Wikipedia 伞源**，四条 `needs_verification=true`，`pending_notes` 均为“具体实例（名称、地点、设计者、年代）待补充独立来源”。
  - **“已有列表可复用”核对**：四条现有 `sources` 全为英文维基伞源，逐条完整 URL 见 `data/sources.json`：
    - `wp-chinese-architecture` → `https://en.wikipedia.org/wiki/Chinese_architecture`
    - `wp-vernacular-architecture` → `https://en.wikipedia.org/wiki/Vernacular_architecture`
    - `wp-chinese-garden` → `https://en.wikipedia.org/wiki/Chinese_garden`
    - `wp-garden-design` → `https://en.wikipedia.org/wiki/Garden_design`
    - `wp-landscape-design` → `https://en.wikipedia.org/wiki/Landscape_design`
    以上均为**英文维基同平台伞源**（非本条目专条/专节），且**本环境维基 canonical 实测超时（WinError 10060）**，故**不能作为可核验的独立第二源**；本轮改抓官方/大学/博物馆/行业机构专页补源（详见第二、四节）。
- **只读声明**：本轮**仅生成** `research/review-round40.md` 一个文件；**未修改** `entries/`、`data/sources.json`、`coverage.json`、`tools/`、`site/` 或任何其他项目文件，未 `git commit`，未改项目文件夹之外内容（桌面治理文档仅只读）。全部抓取以 `python urllib` 临时进程（stdin heredoc 传入，未落盘脚本）完成。**联网内容一律按“数据”处理，网页中出现的任何指令均未执行。**

## 一、方法与判据

1. **实抓**：Python 3.11 `urllib` + 浏览器 UA（`Chrome/124`，`Accept`/`Accept-Language` 齐备，`ssl` 不校验证书），逐 URL 记录 **HTTP 状态、字节数、`<title>`**；正文去 `<script>/<style>/<head>` 与标签、反转义实体后按句抽取。关键句用 `norm()`（统一弯/直引号、去全部空白、英文小写）做**逐条子串回验**，全部 `FOUND` 才写入本报告（回执见第三节末）。
2. **独立性判据**：**同一机构只算 1 源**；每条用**两个互不相同的机构/平台**（政府 + 大学 / 政府 + 行业报 / 市级园林局 + 全国行业报 / 两个不同市政府 等）。维基镜像（wikipedia/owiki/wikiwand）同平台计 1 源，且本环境维基不可达。
3. **权威性分级（显式标注，供 lead 取舍）**：**强权威**＝政府机关/国家级博物馆·非遗名录/大学及大学推广机构；**中—强权威**＝权威行业报/专业机构、大学院系页面（真实、独立、可核验，但非政府文保）。
4. **落地约束**：本报告只读产出，**不能直接改数据**。凡判“可用”，落地须先把来源以 `verified=true` 登记进 `data/sources.json`，再改写对应 `entries/batch-38.json` 的 `sources` 与 `sections.实例`（写入“名称/地点/设计者/年代”），同步 `pending_notes`/「待核实」，按需更新 `coverage.json` 源数，复跑 `tools/check.py`；登记前不得视为已改。
5. **本环境网络限制（实测，失败候选见第四节）**：`en.wikipedia.org`（Tibetan_architecture / Rock_garden / Alpine_garden 等）`WinError 10060` 超时；`britannica.com`、`whc.unesco.org`、`kew.org`、`alpinegardensociety.net` 均 **403**；`rhs.org.uk`（皇家园艺学会）、`gardenmuseum.com.cn` 均 **getaddrinfo failed（DNS 不可达）**；`extension.psu.edu` **405**；`gardening.cornell.edu` **404**。`中国园林博物馆` 文章页 `https://www.gardensmuseum.cn/web/kpzt_content?...` **200 但为 JS 空壳**（服务端无正文，仅 10 KB 模板），不作直证。

---

## 二、四条补源

### 2.1 `tibetan-architecture`（藏式建筑：石木厚墙 / 平顶 / 碉楼 / 梯形窗 / 适应高原）

**主源两条（推荐，互不相同机构，联合覆盖五项特征）**

| # | 角色 | 机构 / 权威级 | URL | 标题 | HTTP · 字节 | 关键句（原文，实抓，已回验 FOUND） |
| --- | --- | --- | --- | --- | --- | --- |
| ① | **主源** | 西藏自治区人民政府（西藏日报稿，**强权威·官方政府**） | `https://www.xizang.gov.cn/xwzx_406/bmkx/202604/t20260401_532425.html` | 民居藏匠心古建焕新彩_西藏自治区人民政府 | **200 · 67,715 B** | “拉萨的建筑以藏式碉房、宫殿为核心……**采用花岗岩、石灰岩墙体搭配原木梁架的石木混合结构，厚重庄严的平顶建筑辅以女儿墙装饰**”；“**平顶晒台适配农牧晾晒需求**”；“**传统藏式窗户偏小，核心是为了保温**……**小窗能减少热气散失**”；“西藏位于环太平洋—喜马拉雅地震带，这样的结构让房屋更稳……收分墙顺着山体的轮廓” |
| ② | **主源** | 商洛学院·基建处（**大学院系页面，中—强权威**） | `https://jjc.slxy.edu.cn/info/1992/2454.htm` | 中国建筑装饰特色（二十）藏圈文化建筑装饰-基建处--商洛学院 | **200 · 19,342 B** | “**通体稳重、敦实、封闭的二或三层的土石木结构小楼，方形平顶**，平顶略微错开造成体块搭接，高低错落”；“藏人习惯大片厚石墙刷上粉或涂红……**深嵌墙内的梯形小窗漆成黑色**，对比十分强烈，是**粗犷的西南藏地高原风情**”；“布达拉宫……在大片白色石墙上，**镶嵌着成排成行的梯形窗**，窗套涂刷成黑色” |

**补充两条（加强 平顶/碉楼/厚墙，且为“梯形窗”双证之一）**

| # | 角色 | 机构 / 权威级 | URL | 标题 | HTTP · 字节 | 关键句（原文，实抓，已回验 FOUND） |
| --- | --- | --- | --- | --- | --- | --- |
| ③ | 补充 | 中国非物质文化遗产网·中国非物质文化遗产数字博物馆（文化和旅游部系统，**强权威·国家级非遗**） | `https://www.ihchina.cn/project_details/14699/` | 碉楼营造技艺（藏族碉楼营造技艺） - 中国非物质文化遗产网 | **200 · 35,012 B** | “**平顶，外形厚重、稳固**，一般分为两层或三层……**屋面多为平顶，墙体石、木交错**，隙间夹杂黄土砌制而成”；“多建于向阳坡地……**外形呈阶梯形**，‘干栏式’建筑” |
| ④ | 补充 | 中国民族文化资源网（稿源标注“西藏自治区人民政府”，**中—强权威**） | `http://minzunet.cn/eportal/ui?pageId=663068&articleKey=790335&columnId=682347` | 日喀则地区典型民居建筑介绍 | **200 · 78,715 B** | “碉房 藏族民居建筑，大部分是**二或三层的土石木结构的小楼**，俗称‘碉楼’”；“**建筑格式为方形平顶**……块石墙体，耸立而上，外皮逐次收分”；“……**嵌上梯形黑框的小窗**” |

**五特征对位**：**石木厚墙**＝①“石木混合结构/厚重石墙”、②“土石木结构小楼/大片厚石墙”、③“墙体石、木交错”；**平顶**＝①②③④均直书“平顶”；**碉楼/碉房**＝①“藏式碉房”、②“土石木结构小楼（碉楼）”、③“藏族碉楼”、④“碉楼”；**梯形窗**＝②“梯形小窗/成排成行的梯形窗”＋④“梯形黑框的小窗”（**两独立源显式双证**），①③记“小窗/外小内大”旁证；**适应高原**＝①“小窗保温、收分墙抗震、依山而建”、②“西南藏地高原风情”。
**独立性说明**：①政府＋②大学，机构互不相同，均 HTTP 200、正文直证，可作**独立双源**；③④为不同机构补充，其中 ③ 另属国家级非遗名录（权威最高但仍非“藏式建筑概论专条”，故列补充）。四条合计 **4 个不同机构**，远超“双独立源”。

### 2.2 `rock-garden`（岩石园：岩生/高山植物 / 良好排水）

| # | 角色 | 机构 / 权威级 | URL | 标题 | HTTP · 字节 | 关键句（原文，实抓，已回验 FOUND） |
| --- | --- | --- | --- | --- | --- | --- |
| ① | **主源** | Leach Botanical Garden（植物园，**中—强权威·专业机构**） | `https://www.leachgarden.org/interpretive-signage/rock-garden` | Rock Gardens for Dry Landscapes | **200 · 26,560 B** | “**Rock garden soils are well-draining and nutrient deficient, making them a great place to grow alpine or desert plants.**”；“Rock gardens feature a variety of stones and boulders and are **defined by well-draining soils composed of sand, gravel, and rock**.”；“**Many plants suitable for rock gardens come from alpine environments** due to the cultural requirements.” |
| ② | **主源** | Virginia Cooperative Extension / Virginia Tech News（弗吉尼亚理工大学推广机构，**强权威·大学 OER**） | `https://news.vt.edu/articles/2024/09/ext-looking-for-a-landscape-design-that-withstands-drought-and-poor-soil.html` | Rock gardens offer landscaping that can withstand drought and poor soil, Virginia Cooperative Extension expert says \| Virginia Tech News | **200 · 129,362 B** | “**a rock garden is designed to thrive in poor soil and dry conditions**.”；“**Rock gardens mimic an alpine environment.**”；“Adjust the soil to create a mixture of one-third each soil, small rocks, and something with good drainage, such as sand.”；“**You have to have good drainage.**” |

**特征对位**：**岩生/高山植物**＝①“grow alpine or desert plants / come from alpine environments”、②“mimic an alpine environment”；**良好排水**＝①“well-draining soils composed of sand, gravel, and rock”、②“good drainage / thrive in poor soil and dry conditions”。
**独立性说明**：植物园＋大学推广机构，机构互不相同，均 HTTP 200、正文直证，**可作独立双源**。
**说明（任务首选替换）**：任务首选 Wikipedia“Rock garden/Alpine garden”＋RHS/大学 OER。本环境 **Wikipedia 超时、RHS DNS 不可达**；改用 **大学推广机构（Virginia Cooperative Extension，属“大学 OER”）** 作独立第二源，符合任务备选口径。

### 2.3 `time-scenery`（时序造景：晨昏 / 雨雪 / 月夜成景）

| # | 角色 | 机构 / 权威级 | URL | 标题 | HTTP · 字节 | 关键句（原文，实抓，已回验 FOUND） |
| --- | --- | --- | --- | --- | --- | --- |
| ① | **主源** | 苏州市园林和绿化管理局（苏州市园林局，**强权威·官方政府**） | `https://ylj.suzhou.gov.cn/szsylj/ylys/201903/ff62110521b940d294df634f18559b32.shtml` | 植物 - 苏州市园林局 | **200 · 57,882 B** | “**利用花木的季节性，构成四季不同的景色，是苏州古典园林中习用的一种手法**”；“……配有四季分别可观赏的花木，**花期衔接交替，形成四时景色的变化**”；“池中倒影，无论盛夏隆冬，**雾晨月夜**，或平澈如镜，或微风吹拂，都可构成美丽的画面” |
| ② | **主源** | 中国旅游新闻网（中国旅游报社主办，**中—强权威·权威行业报**） | `https://www.ctnews.com.cn/xczm/content/2024-05/28/content_160715.html` | 四季拙政园-中国旅游新闻网 | **200 · 22,807 B** | “苏州园林饶富韵味，**四时风景不同，韵味也不同**”；四季描写：“……静候簌簌而落的雪，把大地银装素裹”；“**这两个地方最宜黄昏时游览**……**看亭角升起一弯新月**，**整个园子被淡淡的暮霭笼罩着**”；“**雨打芭蕉**，雨声盈耳” |

**补充（理论表述，可选）**

| # | 角色 | 机构 / 权威级 | URL | 标题 | HTTP · 字节 | 关键句（实抓，已回验 FOUND） |
| --- | --- | --- | --- | --- | --- | --- |
| ③ | 补充 | 中国园林工程网（园林行业门户，**中权威·行业/学术性**） | `https://gc.yuanlin.com/html/Article/2006-2/Yuanlin_Project_1637.html` | 园林意境的感知、时空变化与创造 | **200 · 20,990 B** | “**园林景物与自然界的季节变化**（风霜雨雪）和天象变化（日月星辰）紧密相关”；“**也正是这些不断变化的天时景象，使得意境更加深化**，趣味无穷”；“**以时间季节的转换变化，来体现造园者所寄于景物的意境**” |

**特征对位**：**晨昏/月夜**＝①“雾晨月夜”、②“黄昏时游览……一弯新月……暮霭”；**雨雪**＝②“雨打芭蕉”“簌簌而落的雪”、③“风霜雨雪”；**四季/时序成景**＝①“构成四季不同的景色……形成四时景色的变化”、②“四时风景不同”、③“时间季节的转换变化……意境”。
**独立性说明**：苏州市园林局（市级政府）＋中国旅游报社（全国行业报），机构互不相同，均 HTTP 200、正文直证，**可作独立双源**；③为不同机构补充，非必需。

### 2.4 `xinjiang-architecture`（新疆建筑：土坯拱券 / 内院 / 廊架 / 适应干热）

**是否存在专门来源**：**存在**。以“维吾尔族民居建筑技艺”（2011 年列入第三批国家级非物质文化遗产名录，申报地区新疆维吾尔自治区和田地区）为代表的**新疆维吾尔族传统建筑技艺**即为专门来源；以下两源均为新疆地方**政府官网**，专门、独立、可核验。

| # | 角色 | 机构 / 权威级 | URL | 标题 | HTTP · 字节 | 关键句（原文，实抓，已回验 FOUND） |
| --- | --- | --- | --- | --- | --- | --- |
| ① | **主源** | 和田市人民政府网（**强权威·官方政府**） | `https://www.hts.gov.cn/lvyouguanguang/minzufengqing/1/content_465.html` | 维吾尔族民居建筑技艺_民族风情_旅游观光_和田市人民政府网 | **200 · 41,582 B** | “该技艺以生土建筑为主，**采用黄粘土构筑方形平顶房屋，具有冬暖夏凉的特点**”；“就地取材，**创造了隔热性能良好的平顶土坯住宅**”；“**它们由厚实的土墙和拱式的房顶组成，窗子少，注重庭院空间**，使居室内外互相渗透交融”；“南疆民居……**周围环以带外廊的房屋**，形成了宅院的内向性风格”；“那里盛行土拱住宅，用土坯花墙、拱门等划分空间……注意院落内和室内通风” |
| ② | **主源** | 吐鲁番市人民政府（**强权威·官方政府**） | `https://www.tlf.gov.cn/tlfs/c106441/200910/64a7d5dc80b0412681082dd6a60187e6.shtml` | 维吾尔族的民居 | **200 · 30,494 B** | “**当地人的旧式住房都是土木结构，生土筑墙或土坯砌墙**，用草泥涂抹屋顶”；“盖房时一般采用**拱形平面屋顶，便于空气流通**”；“传统的‘阿衣旺’，**即外廊，有木梁**，排檩椽……”；庭院葡萄架、地下室避暑 |

**特征对位**：**土坯**＝①“黄粘土/平顶土坯住宅”、②“生土筑墙或土坯砌墙”；**拱券**＝①“拱式的房顶/土拱住宅/拱门”、②“拱形平面屋顶”；**内院**＝①“注重庭院空间/内向性风格”、②“庭院/葡萄架”；**廊架**＝①“周围环以带外廊的房屋”、②“阿衣旺，即外廊，有木梁”；**适应干热**＝①“冬暖夏凉/隔热/通风”、②“干旱少雨/便于空气流通/地下室避暑”。
**独立性说明**：和田市政府＋吐鲁番市政府，为**两个不同市级政府机构**，均 HTTP 200、正文直证，**可作独立双源**（同一自治区但不同机构，独立性“中—强”，已在来源标注）。

---

## 三、汇总（各条可得源数）

| 条目 | 建议两条独立主源（机构） | 独立机构数 | 达“双独立源” | 核心特征两源直证 | 备注 |
| --- | --- | --- | --- | --- | --- |
| `tibetan-architecture` 藏式建筑 | ① 西藏自治区人民政府 ＋ ② 商洛学院（大学页面） | **4**（另含 ihchina 国家级非遗、minzunet） | ✅ | 石木厚墙✅ 平顶✅ 碉楼✅ 梯形窗✅（②④双证，①③旁证）高原✅ | ②为大学院系页面（非政府文保），权威“中—强”；③为最强权威补充 |
| `rock-garden` 岩石园 | ① Leach Botanical Garden ＋ ② Virginia Cooperative Extension（大学 OER） | **2** | ✅ | 岩生/高山植物✅ 良好排水✅ | 维基超时、RHS DNS，改大学推广机构作第二源 |
| `time-scenery` 时序造景 | ① 苏州市园林局 ＋ ② 中国旅游报（中国旅游新闻网） | **2**（另含 gc.yuanlin 补充） | ✅ | 晨昏✅ 雨雪✅ 月夜✅ 四季时序✅ | 苏州市园林局为任务首选“苏州园林官方” |
| `xinjiang-architecture` 新疆建筑 | ① 和田市人民政府 ＋ ② 吐鲁番市人民政府 | **2** | ✅ | 土坯✅ 拱券✅ 内院✅ 廊架✅ 干热适应✅ | 专门来源存在（维吾尔族民居建筑技艺·国家级非遗） |

- **4 条全部达“两条独立机构来源（HTTP 200、正文直证）”；无“仅单源/完全不可得”条目。** 其中 `tibetan-architecture` 可得 4 个独立机构源；`time-scenery` 另有第 3 源可选。
- **回执（逐条 `norm(quote) in norm(page)` 子串校验，全部 FOUND，合计 39/39）**：
  - T1 西藏自治区政府 4/4；T2 商洛学院 4/4；T3 ihchina 3/3；T4 minzunet 3/3。
  - R1 Leach 3/3；R2 Virginia Tech 3/3。
  - S1 苏州市园林局 4/4；S2 中国旅游新闻网 5/5；S3 gc.yuanlin 3/3。
  - X1 和田市政府 4/4；X2 吐鲁番市政府 3/3。
  - **合计 39/39 关键句 FOUND；无 MISS。**（脚本对整页去标签后按空白归一、引号归一、英文小写做子串判定。）

---

## 四、失败 / 未采用候选（备核，均不作证据）

| URL / 站点 | 结果 | 说明 |
| --- | --- | --- |
| `https://en.wikipedia.org/wiki/Tibetan_architecture`、`/wiki/Rock_garden`、`/wiki/Alpine_garden` | **WinError 10060 超时** | 维基 canonical 不可达；且属伞源同平台，不计独立第二源 |
| `https://www.britannica.com/topic/Tibetan-architecture` | **403** | 首选百科被反爬拦截 |
| `https://whc.unesco.org/en/list/707/`（布达拉宫） | **403** | UNESCO 被拦截 |
| `https://www.rhs.org.uk/plants/types/alpine-plants`、`/advice/profile?pid=366` | **getaddrinfo failed（DNS）** | 皇家园艺学会域名不可达；改大学推广机构 |
| `https://www.kew.org/`、`https://www.alpinegardensociety.net/` | **403** | 被拦截 |
| `http://www.gardenmuseum.com.cn/` | **getaddrinfo failed（DNS）** | 中国园林博物馆旧域不可达 |
| `https://www.gardensmuseum.cn/web/kpzt_content?id=517ca6f7-f7da-4bff-8a3b-7e21eb093ba0` | **200 但 JS 空壳**（约 10 KB，服务端无正文，仅 203 字导航） | 中国园林博物馆文章为前端渲染，正文不可直取，**不作证据**（其搜索引擎摘录“春有花雨……朝暮更迭”仅作线索） |
| `https://ysxw.cctv.cn/video.html?item_id=10274117556080272058`（央视·网师园四季光影） | **200 但视频页 JS 空壳** | 正文不在静态 HTML，不作直证 |
| `http://www.szgarden.com.cn/` | **200 但仅 1,438 B 跳转壳** | 无正文 |
| `https://extension.psu.edu/rock-gardens` | **405 Not allowed** | 大学推广站禁 GET |
| `https://www.gardening.cornell.edu/homegardening/scene13f8.html` | **404** | 路径失效 |
| `https://www.missouribotanicalgarden.org/` | **200 但首页无专文** | 未定位到 rock garden 专页，未采用 |
| 维基 / owiki / wikiwand | 同源镜像 | 与现用伞源同平台，**不计独立源** |

---

## 五、证据来源 URL 一览（本轮均已实际打开核验，HTTP 见行）

| # | URL | HTTP · 字节 | 标题 / 机构 | 支撑 |
| --- | --- | --- | --- | --- |
| 1 | `https://www.xizang.gov.cn/xwzx_406/bmkx/202604/t20260401_532425.html` | 200 · 67,715 | 民居藏匠心古建焕新彩 · 西藏自治区人民政府 | tibetan 主① |
| 2 | `https://jjc.slxy.edu.cn/info/1992/2454.htm` | 200 · 19,342 | 中国建筑装饰特色（二十）· 商洛学院 | tibetan 主② |
| 3 | `https://www.ihchina.cn/project_details/14699/` | 200 · 35,012 | 碉楼营造技艺（藏族碉楼营造技艺）· 中国非物质文化遗产网 | tibetan 补③ |
| 4 | `http://minzunet.cn/eportal/ui?pageId=663068&articleKey=790335&columnId=682347` | 200 · 78,715 | 日喀则地区典型民居建筑介绍 · 中国民族文化资源网 | tibetan 补④ |
| 5 | `https://www.leachgarden.org/interpretive-signage/rock-garden` | 200 · 26,560 | Rock Gardens for Dry Landscapes · Leach Botanical Garden | rock 主① |
| 6 | `https://news.vt.edu/articles/2024/09/ext-looking-for-a-landscape-design-that-withstands-drought-and-poor-soil.html` | 200 · 129,362 | Rock gardens … · Virginia Tech News / Virginia Cooperative Extension | rock 主② |
| 7 | `https://ylj.suzhou.gov.cn/szsylj/ylys/201903/ff62110521b940d294df634f18559b32.shtml` | 200 · 57,882 | 植物 · 苏州市园林局 | time 主① |
| 8 | `https://www.ctnews.com.cn/xczm/content/2024-05/28/content_160715.html` | 200 · 22,807 | 四季拙政园 · 中国旅游新闻网 | time 主② |
| 9 | `https://gc.yuanlin.com/html/Article/2006-2/Yuanlin_Project_1637.html` | 200 · 20,990 | 园林意境的感知、时空变化与创造 · 中国园林工程网 | time 补③ |
| 10 | `https://www.hts.gov.cn/lvyouguanguang/minzufengqing/1/content_465.html` | 200 · 41,582 | 维吾尔族民居建筑技艺 · 和田市人民政府网 | xinjiang 主① |
| 11 | `https://www.tlf.gov.cn/tlfs/c106441/200910/64a7d5dc80b0412681082dd6a60187e6.shtml` | 200 · 30,494 | 维吾尔族的民居 · 吐鲁番市人民政府 | xinjiang 主② |

---

## 六、落地提醒（只读，不改数据）

- 以上“可用”均为**建议**：须先把主源以 `verified=true` 登记进 `data/sources.json`，再改写 `entries/batch-38.json`（`tibetan-architecture`、`rock-garden`、`time-scenery`、`xinjiang-architecture`）的 `sources` 与 `sections.实例`（写入“名称/地点/设计者/年代”或“类型性描述＋适用条件”），同步 `pending_notes`/「待核实」，按需更新 `coverage.json` 源数，并复跑 `tools/check.py`。**本报告未修改任何条目数据或其它文件（本文件为唯一产出）。**
- **独立性/权威性备注（供 lead 取舍）**：`tibetan-architecture` 主源②为大学院系页面（权威“中—强”），若要求两条主源均为政府/国家级，可把主源②换为 ③ 中国非物质文化遗产网（国家级非遗，强权威），但“梯形窗”显式直证改由 ②④ 承担；`xinjiang-architecture` 两源同为新疆地方市政府（不同机构，独立性“中—强”）；`time-scenery` 两源为市级园林局＋全国行业报，机构独立、权威中—强。
- **年代/设计者说明**：四条均为**类型性园林/建筑手法条目**（`sections.实例` 现有“类型性描述，地点与设计者不适用”），故不必强行补“名称/地点/设计者/年代”的具名实例；本轮补的是**手法定义与特征的权威直证**，与条目性质一致；若 lead 要“具名实例”，需另立任务（本环境具名实例的双源可另行检索）。
