# BACKLOG.md — 待办队列

> 按 AUTONOMOUS.md 第三节 B/C 生成。优先级：复核/修复 > 核心 > 重要 > 补充；被引用次数多、所在维度稀疏者优先。

## 第 3 轮缺口发现摘要

- B1：4 条 scope 候选（沿用上轮已核验的 N1–N5 双源依据）
- B2：空格 0，稀疏格 9
- B3：悬空引用 0
- B4：读者 80 问中 34 问暂无法从已写条目直接找到答案
- B5：待核实 8 条（上轮 3 条 + 新增单源条目 5 条）
- B6：3 条近期动态待评估
- B7：核心未写 2 条；核心已写 L1 待升级若干

## 第 3 轮队列（23 任务，≤40）

| 序号 | 任务 | 优先级 | 依据 |
| --- | --- | --- | --- |
| 1–5 | 纳入 5 份新核验来源 N1–N5 并置 verified=true / link_ok=true | 最高 | B1，HTTP 200 已核对 |
| 6–9 | 新增 4 个 scope 条目（mannerism、beaux-arts、vitruvian-triad、plein-air） | 核心 | B1，双源支持 |
| 10–13 | 复核 4 条待核实（原 3 条 + 新条目中的保守项） | 最高 | B5 |
| 14–16 | 评估 3 条 B6 近期动态并记录处置 | 重要 | B6 |
| 17–18 | 核心 L1 收尾：sunken-accessibility、chinese-architecture-style | 核心 | B7 |
| 19–23 | 5 个核心条目升级 L2（six-principles、borrowed-scenery、circulation、daylighting、natural-ventilation） | 核心 | B7，质量优先，不强行凑 40 |

执行顺序：每完成一批运行 check.py 并 commit；抽检 10%（至少 3 个）另起子任务。

## 下一轮队列（第 80 轮，按优先级）

1. 剩余待核实稳定在 179 诚实边界；继续逐条尝试（每轮1-2条），实例须"作品—技法"关联有源。
2. B1/B6；补推积压。

## 已完成/历史（维护模式说明保留）

每轮仅做：体检（F）、复核待核实、更新过期数据、跟进近期动态（B6）。若缺口发现再现新缺口，立即退出饱和回到正常循环。不得写 ALL_DONE。

## 已完成

- 第 1 轮：项目搭建 + 40 条首批条目
- 第 2 轮：复核 3 条 + 新增 38 条核心 L1；抽检 4/4 合格
- 第 3 轮：纳入 6 份来源、新增 4 条 scope、新增 6 条 L1、升级 5 条 L2；抽检 2 不合格，整批返工完成
- 第 4 轮：复核 13 条待核实（1 条可升级）、新增 4 份来源、新写 5 条 L2、升级 2 条 L1→L2；抽检 1 不合格，整批返工完成
- 第 5 轮：体检；新增 7 份来源、新写 5 条 L2、升级 1 条；复核 23 条待核实；抽检 1 不合格，整批返工完成
- 第 6 轮：B1 找到 7 条候选；新写 6 条 L2（累计 100）；复核 24 条待核实；抽检 1 不合格，整批返工完成
- 第 7 轮：纳入 9 份新来源、7 个新 scope 条目与 7 条 L1（累计 107）；复核 24 条（0 可升级）；抽检 3/3 合格
- 第 8 轮：新增 6 条从业者问题 L2（累计 113）；复核 30 条（2 条概念层面升级）；B6 发现 2 条新动态；抽检 1 合格 / 2 待核实（已定向修正），无整批返工
- 第 9 轮：新写 6 条 L2（累计 119）；复核 34 条（3 条概念层面升级）；B1 找到 7 条候选；抽检 1 不合格，整批返工完成
- 第 10 轮：体检（0 死链/0 重复/0 孤儿）；网络中断，回滚未核验来源；用现有来源升级 6 条核心 L1→L2；复核 31 条（0 可升级）；抽检 3/3+4/4+3/3 合格，无返工
- 第 11 轮：镜像+web_search 核验 12 份来源、新增 7 个 scope 条目与 7 条 L1（累计 126）；复核 37 条（0 可升级）；抽检 3/3 合格，无返工
- 第 12 轮：7 个核心理论 L1→L2（核心已全部 L2）；bauhaus 补独立双源并升级；light-well 收窄待核实；抽检 3/3 合格，无返工
- 第 13 轮：6 个重要理论 L1→L2；chinese-architecture-style（紫禁城）、daylighting（金贝尔美术馆）补独立双源并升级实例；daylight-factor 收窄；抽检 3/3 合格
- 第 14 轮：6 条透视 L1→L2（返工去模板化，相似度<0.54）；复核 54 条，six-principles/circulation/water-management/borrowed-scenery 补官方双源升级、liubai 补源；抽检返工后复检通过（L2 63）
- 第 15 轮：6 条跨主题重要 L1→L2；复核 57 条，six-principles/borrowed-scenery/perspective/sunken-courtyard 收窄；修复 2 对既有相似度过高条目；抽检 3/3 合格（L2 69）
- 第 16 轮：6 条跨主题重要 L1→L2；six-principles 升级（异说并列）、perspective/sunken-courtyard 收窄；修 lighting-design 取源；抽检 2/3 合格+1 已修（L2 75）
- 第 17 轮：7 条升级（placemaking/space-syntax/pattern-language/biophilic-design/defensible-space-theory/functionalism-architecture/sunken-plaza）；sunken-plaza 待核实澄清；复核 69 条（3 项收窄因 URL 不精确延后）
- 第 18 轮：6 条升级（simplification/hierarchy/color-contrast/framed-scenery/pedestrian-flow/material-texture）；framed-scenery、natural-ventilation 实例补双源，opposed/leaked 补专门来源；material-texture 待核实扩写（L2 88）
- 第 19 轮：7 条升级（geometry-symmetry/visual-movement/leading-lines/rhythm-repetition/place-attachment/tour-route/drainage）；tour-route 升级验证、drainage/glare 实例补双源（L2 95）
- 第 20 轮：体检（0 死链/0 重复/0 孤儿）；6 条升级（visual-center/contrast-principle/form-follows-function/curvilinear-perspective/courtyard/green-architecture），重要条目全部 L2；courtyard 三源、sunken-plaza 补 1999 第二源
- 第 21 轮：6 条核心 L1→L2（气韵/留白/意境/空间定义/人体尺度/空间序列）；space-definition（巴塞罗那德国馆）、human-scale（帕伊米奥疗养院）补双源升级；返工修 qi-yun 年份、spatial-sequence 换古根海姆来源（核心 L1 余 13）
- 第 22 轮：6 条核心 L1→L2（过渡空间/空间组织/室内外过渡/曲径/疏散动线/高差处理）；level-change（劳力士学习中心）、winding-path（拙政园）补双源升级（核心 L1 余 7）
- 第 23 轮：7 条核心 L1→L2 收尾（东西透视/东西空间/防潮/安全防护/可持续/维特鲁威三原则/下沉无障碍）；**核心与重要条目全部 L2**；The Edge、Peavey Plaza 补双源；返工 3 条（东/西与无障碍引证）；仅余 6 条补充 L1
- 第 24 轮：6 条补充 L1→L2（空间法则/黄金比/对角/S形/三角/框架构图）——**全库 126 条全部 L2（L1=0）**；spatial-organization（萨伏伊别墅）双源升级、green-architecture 评价数据补多源；返工构图类改为单源如实标注
- 第 25 轮（体检轮）：体检 0 死链/0 重复/0 孤儿；B4 补齐 5 条新条目（伦勃朗光/暗绘/广场/中庭/疏散标识），读者未答问题 6→1；修 pedestrian-flow 死链、screened-scenery 单源披露；记录模板/伞源系统性问题
- 第 26 轮：5 条新增 L1→L2（伦勃朗光/暗绘/广场/中庭/疏散标识），**全库 131 条全部 L2**；pending_notes 去模板化（63 同句→各异）；12 条伞源条目改单源如实标注；green-architecture（常州高新智汇中心）升级、drainage 收窄
- 第 27 轮：补齐 vestibule（门厅）L2，**读者 80 问全部可答（未答 0）**；9 条单源条目补真实第二来源（Getty/LibreTexts/ArchDaily/同济等）、sunken-plaza 补同济第二源；vestibule 返工为单源如实标注
- 第 28 轮：leading-lines/axis 补第二源；gothic/modernism/color-theory 去骨架化具名实例（巴黎圣母院/包豪斯德绍/蒙塞尔色彩体系），color-theory 升级为已验证；10 条单源中 9 条已补源（余 gothic 待完整 URL）
- 第 29 轮：gothic 补第二源并升级；postmodernism（意大利广场）、bauhaus（德绍校舍）去骨架化；新增 baroque（圣彼得大教堂，双官方源）L2；抽检 3/3 合格
- 第 30 轮（体检轮）：体检 0 死链/0 重复/0 孤儿；新增 2 条稀疏格条目（墨西哥巴洛克/新陈代谢派），稀疏格 9→7；抽检 3/3 合格
- 第 31 轮：新增学院派理论、古典柱式 2 条（稀疏格 7→5）；bauhaus 与 modernism 实例去重（相似度降至 <0.54）；抽检 2 合格/1 已修
- 第 32 轮：写 12 条未写条目（中国画技法组骨法/应物象形/随类赋彩/传移模写/水墨/皴法/工笔/写意/虚实/山水 + 对称布局/开敞），均 L2；去模板化后相似度 <0.54；抽检 3/3 合格
- 第 33 轮：写 12 条未写条目（光影塑形/五调子/投影/高光/反光/交界线/正侧逆顶光 + 配色方案/色彩象征）均 L2；四向光与五调子去同质化；five-tones 补待核实披露
- 第 34 轮：写 12 条风格史条目（古罗马/罗曼/洛可可/新古典/新艺术/装饰艺术/国际风格/有机/风格派/哥特复兴/文艺复兴复兴/折衷）均 L2；art-deco 伞源缺口披露、SVG 加标题去同图；抽检 2 合格/1 已修
- 第 35 轮：写 12 条条目（添景/夹景/抑景/叠石/植物配置/园林建筑/四季造景/下沉花园/半下沉/地下中庭/材料色彩/结构材料）均 L2；下沉组与材料色据抽检改为一般性工程说明并披露来源局限（sunken-garden 时期改跨时期）
- 第 36 轮：写 12 条（车行/人车分流/参观/回游/串联/放射动线 + 侧窗/天窗/风压/中庭通风 + 视觉舒适/无障碍）均 L2；visitor-route/accessibility 披露来源局限、风压与无障碍图重绘、SVG 逐条差异化
- 第 37 轮：写 24 条（空间组/风格史/地域风格等）全部 L2；**重要条目全部写完**，仅余 25 条补充；arts-crafts/monumental-scale/rule-of-odds 换真源、arts-crafts 时期改 19 世纪、24 条 SVG 逐条重绘
- 第 38 轮：写剩余 25 条补充条目，**全库 246 条范围全部写完、全部 L2（未写 0）**；acoustic/romanticism/korean 补真双源、25 条 SVG 逐条重绘；抽检 1 合格/2 待核实/1 不合格→整批返工修正
- 第 39 轮（体检轮）：体检 0 死链/0 重复/0 孤儿；为 6 个风格条目补具名实例双源（杜伦大教堂/阿玛琳堡/先贤祠/红屋/塔塞爾公館/克莱斯勒大厦）升级；raised-floor 改为一般性工程说明并披露、african/latin 伞源披露
- 第 40 轮：B1 发现并纳入 proxemics（近距学，双源）；batch-38 的 tibetan/rock-garden/time-scenery/xinjiang 补真实来源重写（藏/岩生/时序/生土）；全库 247 条全 L2；抽检 2 待核实/1 不合格→返工修正
- 第 41 轮：B1 发现并纳入 sfumato（渐隐法）、trompe-l'œil（错视画）2 条（全库 249 条全 L2）；batch-38 shanxi/lingnan/urban 换源去伞源、SVG 去同图；B6 无新动态
- 第 42 轮：B1 发现并纳入 hatching（排线法）、stippling（点描法）2 条（全库 251 条全 L2）；proxemics 补单源披露；sfumato/trompe 抽检合格
- 第 43 轮：B1 从严判定 0 新缺口、B6 无动态；hatching/stippling 去模板（相似度 0.567→<0.45）；**零缺口第 1/3 轮**；体检 0 死链/0 重复/0 孤儿
- 第 44 轮：B1 从严 0 新缺口、B6 无动态（**零缺口 2/3**）；batch-38 全 25 条 SVG 重绘为结构唯一（0 近重复）、修 3 处来源标题、time-scenery 原理与四季造景区分
- 第 45 轮（体检+饱和终判）：B1 从严 0 新缺口、B6 无动态（**零缺口 3/3**）；核心+重要 197 条全 L2、全库 251 条全 L2、未写 0；体检 0 死链/0 重复/0 孤儿；**SATURATION.json 置 SATURATED=true**
- 第 46 轮（退出饱和后扩充第 1 轮）：新增 4 条填 4 稀疏格（宫廷中轴动线/如画/莫卧儿/早期伊斯兰）；6 条补具名实例双源升级（万神殿/流水别墅/蓬皮杜/西格拉姆/施罗德住宅/新国家美术馆）；全库 255 条全 L2，来源 320
- 第 47 轮：新增 3 条填满剩余稀疏格（地坑院/萨珊/奥斯曼）→**覆盖矩阵稀疏格归零（0）**；4 条补具名实例（得特宫/巴黎歌剧院/最后的晚餐/哀悼基督）；全库 258 条全 L2，来源 333，待核实 216
- 第 48 轮：B1 0 新缺口、B6 无动态（新循环零缺口 1/3）；5 条补具名实例（古根海姆纽约/阿利耶夫中心/毕尔巴鄂/马赛公寓/卡纳莱托圣马可广场）；258 条全 L2，来源 343
- 第 49 轮：B1/B6 无新缺口（零缺口 2/3）；6 条补具名实例（雅典学院/蒙娜丽莎/斗兽场/朗香/圆厅别墅/龙安寺）；brutalism 去冗余伞源、atrium 恢复单源披露；258 条全 L2，来源 355
- 第 50 轮（体检+终判）：B1/B6 无新缺口（新循环零缺口 3/3）；核心+重要 203 全 L2、258 全 L2、未写 0、稀疏格 0；体检 0 死链/0 重复/0 孤儿；**SATURATED=true**
- 第 51 轮：8 条补具名实例（马萨乔圣三位一体/清明上河图/夸廖三点透视/蒙娜丽莎/维特鲁威人/大碗岛/阿尔诺菲尼肖像/夜巡）；scattered 据抽检恢复待核实并披露概念单源；258 条全 L2，来源 371
- 第 52 轮：色彩理论 8 条补具名实例（牛顿色环/马蒂斯舞蹈/蒙德里安/自由引导人民/莫奈睡莲/梵高夜间咖啡馆/透纳无畏号）；其中 5 条双源、3 条单源如实保留待核实；color-symbolism 三元映射单源披露；258 条全 L2，来源 383
- 第 53 轮：构图/视觉原理 8 条补具名实例（诺利地图/神奈川冲浪里/伦敦地铁图/马蒂斯红色和谐/雅典学院/故宫等）；symmetry-layout 单源披露回退；258 条全 L2，来源 398
- 第 54 轮：8 条风格类补具名实例（佛罗伦萨穹顶/佛光寺/岩石圆顶/布里哈迪斯瓦拉神庙/法隆寺/凡尔赛/塔特林塔/萨伏伊别墅）；constructivism 无源“红色几何”改写；258 条全 L2，来源 414
- 第 55 轮：8 条补具名实例（布查特下沉花园/卢浮宫金字塔地下大厅/莫斯高覆土博物馆/伦敦下沉住宅/狮子林假山/邱园花境/桂离宫/卢浮宫参观流线）；earth-sheltered 无源热工表述改写并恢复待核实 + 修 SVG 出界；258 条全 L2，来源 430
- 第 56 轮：8 条补具名实例（鲁宾花瓶/儿童医院壁画/怀特广场/千里江山图Vs日出印象/华盛顿纪念碑/待庵茶室/夜巡/梵高夜间咖啡座）；intimate-scale 无源概述改写；258 条全 L2，来源 446
- 第 57 轮：6 条补具名实例（史基浦导视/金贝尔美术馆/NMNH无障碍/贝丁顿零碳/曼尼托巴水电/柏林爱乐）；pedestrian/corridor 单源保留待核实；**质量闸系统升级**：check.py 增 SVG rx/ry 与 rect 宽高越界校验（新增5测试），修复 19 条目 30 处越界；258 条全 L2，来源 458
- 第 58 轮：8 条中国画理论/技法补具名实例（洛神赋图/马夏派/王维/吴道子/潇湘图/芙蓉锦鸡图/泼墨仙人图/枯木怪石图）；gongbi/xieyi 升级、xieyi SVG 去重；258 条全 L2，来源 474
- 第 59 轮：4 条六法组补具名实例（应物象形/随类赋彩/传移模写/经营位置，复用库内已验证故宫/ChinaCulture/Columbia 源）；抽检后移除随类赋彩不相关源、去 disclose、likeness/color SVG 各自换图；258 条全 L2，来源 474
- 第 60 轮：chiaroscuro（Tate+NG《以马忤斯的晚餐》1601）、cast-shadow（NG《气泵中的鸟实验》1768 单烛光投影）补具名实例并升级；抽检 2/2 合格；258 条全 L2，来源 477，待核实 189
- 第 61 轮：back-light（Contre-jour+ExpertPhotography）、side-light（StudioBinder+Wikipedia 伦勃朗光）换真源重写并重绘专属 SVG；light-shadow-modeling 专属图；**系统修复**：解散 4 组共 15 条共用相同 SVG 的存量缺陷→全库 SVG 重复组 0；258 条全 L2，来源 482
- 第 62 轮：front-light/top-light 移除建筑照明错配源（改 Wikipedia Lighting 直证并如实单源/一般性披露）；five-tones 标明教学通用术语；top-light 返工后复检合格；258 条全 L2，来源 483
- 第 63 轮：plein-air（Tate+Wiki 双源）补具名实例；确认 wp-architectural-lighting-design 对采光/眩光类条目合法（非错配）；academic-art-theory 第二源 404 死链→回退待核实并披露、标记死链；258 条全 L2，来源 485
- 第 64 轮：修正 3 个曾被误标 false 的 wiki 源 link_ok=true（canonical 复探 200）；确认 artincontext-academic 404（academic 保留单源披露）；sasanian/religious 具名实例缺第二独立平台源，据实保留待核实；258 条全 L2，来源 485
- 第 65 轮：form-follows-function（沙利文 1896/Wainwright 大楼 1891，WP+DesigningBuildings 双源）补具名实例升级；wp-plaza link_ok 复探修正；258 条全 L2，来源 486
- 第 66 轮：axis（轴线）补北京中轴线实例并升级（wp-chinese-architecture + bjaxis-official 双独立平台，对称/比例模数/7.8km 逐字直证）；258 条全 L2，来源 486，待核实 186
- 第 67 轮：courtyard（庭院）补北京四合院实例并升级（wp-siheyuan + db-courtyard 双独立平台，四面围合/向天开敞逐字直证）；删无源 1930 年代括注；258 条全 L2，来源 488，待核实 185
- 第 68 轮：spatial-sequence（空间序列）补古根海姆螺旋坡道实例并升级（NYC LPC 报告 PDF + 古根海姆访客指南 PDF 双官方）；258 条全 L2，来源 488，待核实 184
- 第 69 轮：interior-exterior-transition（室内外过渡）用敞廊 Loggia 实例并升级（wp-loggia + db-loggia 双独立平台）；258 条全 L2，来源 489，待核实 183
- 第 70 轮：space-syntax（Hillier/Hanson《The Social Logic of Space》1984）与 pattern-language（Alexander《建筑模式语言》1977 253模式）补具名著作实例并升级（各双独立平台）；258 条全 L2，来源 491，待核实 181
- 第 71 轮：biophilic-design（Wilson《Biophilia》1984 亲生命设计）补具名实例并升级（wp + Designing Buildings 双平台）；258 条全 L2，来源 492，待核实 180
- 第 72 轮：placemaking 首升被抽检判不合格（“于纽约创立”错位引用+PPS 1975 单源），返工删错位、1975 标待核实、回退 nv；返工复检合格；258 条全 L2，来源 493，待核实 179
- 第 73 轮：探测 engawa/gray-space/transition-space/metabolism 第二平台源，均单平台不可得；按协议不强升、据实保留待核实（无数据变更）；258 条全 L2，来源 493，待核实 180
- 第 74 轮：审计 77 条 pending（多平台但有具体 nv 理由，不盲升）；trompe-loeil 实例改为具名 Pozzo《圣依纳爵的荣耀》(1685–1694)，补 WGA 佐证、保留技法单源待核实；258 条全 L2，来源 494，待核实 180
- 第 75 轮：color-contrast 升级（《夜间咖啡馆》wp-night-cafe+Van Gogh Museum 双平台）；complementary-colors 收窄措辞（红绿对比双源、“互补”为色论桥接）保留待核实；258 条全 L2，来源 496，待核实 179
- 第 76 轮：picturesque 实例改具名斯托海德园林（受 Claude Lorrain 启发 Wikipedia+Gardenvisit 双源），保留待核实（“如画”为归类、“Claudian”仅单源），收窄披露；258 条全 L2，来源 498，待核实 179
- 第 77 轮：B1 无新缺口（12 份未用分类树）、B6 无动态；dead-link 复核 3 条均确认 404 维持 false；体检 0 死链/0 重复/0 孤儿、来源完整性 0 问题；258 条全 L2，待核实 179
- 第 78 轮：sfumato 实例改具名《蒙娜丽莎》（卢浮宫官方+Wikipedia 双源），年份由无源 1503–1519 修正为有据 1503–1505（1503–1513 不一），保留待核实；258 条全 L2，来源 499，待核实 179
- 第 79 轮：hatching 实例由《忧郁 I》(排线关联无源)改为《圣维罗妮卡》(wp-hatching 逐文明证交叉排线)，保留待核实(年代)；258 条全 L2，来源 499，待核实 179
