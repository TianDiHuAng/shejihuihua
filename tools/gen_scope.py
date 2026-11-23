"""确定性生成 scope.md、coverage.json、coverage-matrix.md。
数据来源：research/outline_raw.md 中 S1–S12 权威百科分类树取并集，并补入任务文档指定条目。
"""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
TODAY = "2026-11-22"

# 格式: id|名称|主题|层级|时期|地区|来源编号
# 主题限定为任务规定的六类: 理论/风格/造景/动线/下沉空间/材料
DATA = """
perspective|透视法|理论|核心|文艺复兴至19世纪|欧洲|S1,S5
linear-perspective|线性透视|理论|核心|文艺复兴至19世纪|欧洲|S5
one-point-perspective|一点透视|理论|重要|文艺复兴至19世纪|欧洲|S5
two-point-perspective|两点透视|理论|重要|文艺复兴至19世纪|欧洲|S5
three-point-perspective|三点透视|理论|重要|20世纪|欧洲|S5
curvilinear-perspective|曲线透视|理论|补充|20世纪|全球|S5
aerial-perspective|空气透视|理论|重要|跨时期|全球|S5
foreshortening|缩短法|理论|重要|文艺复兴至19世纪|欧洲|S5
vanishing-point|灭点|理论|重要|文艺复兴至19世纪|欧洲|S5
horizon-line|视平线|理论|重要|文艺复兴至19世纪|欧洲|S5
scattered-perspective|散点透视|理论|核心|古代|中国|S4
composition|构图法则|理论|核心|跨时期|全球|S6
rule-of-thirds|三分法|理论|重要|跨时期|全球|S6
rule-of-odds|奇数法则|理论|补充|跨时期|全球|S6
rule-of-space|空间法则|理论|补充|跨时期|全球|S6
simplification|简化|理论|重要|跨时期|全球|S6
geometry-symmetry|几何与对称|理论|重要|跨时期|全球|S6
visual-movement|视觉动势|理论|重要|跨时期|全球|S6
leading-lines|引导线|理论|重要|跨时期|全球|S6
figure-ground|图底关系|理论|重要|20世纪|全球|S6
negative-space|负空间|理论|重要|20世纪|全球|S6,S4
visual-center|视觉中心|理论|重要|跨时期|全球|S6
balance|均衡|理论|核心|跨时期|全球|S6
contrast-principle|对比|理论|重要|跨时期|全球|S6
rhythm-repetition|节奏与重复|理论|重要|跨时期|全球|S6
hierarchy|主次层级|理论|重要|跨时期|全球|S6
proportion|比例|理论|核心|跨时期|全球|S6
golden-ratio|黄金分割|理论|补充|跨时期|欧洲|S6
diagonal-composition|对角线构图|理论|补充|跨时期|全球|S6
s-curve-composition|S形构图|理论|补充|跨时期|全球|S6
triangular-composition|三角形构图|理论|补充|跨时期|全球|S6
framing-composition|框架式构图|理论|补充|跨时期|全球|S6,S3
color-theory|色彩理论|理论|核心|跨时期|全球|S7
hue|色相|理论|重要|跨时期|全球|S7
value|明度|理论|核心|跨时期|全球|S6,S7
saturation|纯度|理论|重要|跨时期|全球|S7
primary-colors|三原色|理论|重要|跨时期|全球|S7
complementary-colors|互补色|理论|重要|跨时期|全球|S7
color-contrast|色彩对比|理论|重要|跨时期|全球|S7
warm-cool|冷暖色|理论|重要|跨时期|全球|S7
color-harmony|色彩和谐|理论|重要|跨时期|全球|S7
color-scheme|配色方案|理论|重要|跨时期|全球|S7
color-symbolism|色彩象征|理论|补充|跨时期|全球|S7
tints-shades|色调与明暗层次|理论|补充|跨时期|全球|S7
split-primary|分离原色调色|理论|补充|跨时期|全球|S7
chiaroscuro|明暗法|理论|核心|文艺复兴至19世纪|欧洲|S5
light-shadow-modeling|光影塑形|理论|重要|文艺复兴至19世纪|欧洲|S5
five-tones|明暗五调子|理论|重要|文艺复兴至19世纪|欧洲|S5
highlight|高光|理论|补充|跨时期|全球|S5
reflected-light|反光|理论|补充|跨时期|全球|S5
cast-shadow|投影|理论|重要|跨时期|全球|S5
core-shadow|明暗交界线|理论|补充|文艺复兴至19世纪|全球|S5
front-light|正面光|理论|补充|跨时期|全球|S9
side-light|侧面光|理论|重要|跨时期|全球|S9
back-light|逆光|理论|重要|跨时期|全球|S9
top-light|顶光|理论|补充|跨时期|全球|S9
six-principles|中国画六法|理论|核心|古代|中国|S4
qi-yun|气韵生动|理论|核心|古代|中国|S4
bone-method|骨法用笔|理论|重要|古代|中国|S4
likeness-form|应物象形|理论|重要|古代|中国|S4
color-according-type|随类赋彩|理论|重要|古代|中国|S4
composition-placement|经营位置|理论|重要|古代|中国|S4
transmission-copy|传移模写|理论|补充|古代|中国|S4
liubai|留白|理论|核心|古代|中国|S4,S3
ink-wash|水墨|理论|重要|古代|中国|S4
cunfa|皴法|理论|重要|古代|中国|S4
gongbi|工笔|理论|重要|古代|中国|S4
xieyi|写意|理论|重要|古代|中国|S4
yijing|意境|理论|核心|古代|中国|S4,S3
xu-shi|虚实|理论|重要|古代|中国|S4,S3
landscape-painting|山水画|理论|重要|古代|中国|S4
east-west-perspective-compare|散点与焦点透视比较|理论|核心|跨时期|全球|S4,S5
east-west-space-compare|留白与负空间比较|理论|核心|跨时期|全球|S3,S4,S6
east-west-color-compare|中西色彩观比较|理论|重要|跨时期|全球|S4,S7
space-definition|建筑空间定义|理论|核心|跨时期|全球|S1
place-spirit|场所精神|理论|重要|20世纪|欧洲|S1
spatial-perception|空间感知|理论|重要|跨时期|全球|S1
human-scale|人体尺度|理论|核心|跨时期|全球|S1
monumental-scale|纪念性尺度|理论|重要|跨时期|全球|S1
intimate-scale|亲切尺度|理论|重要|跨时期|全球|S1
spatial-sequence|空间序列|理论|核心|跨时期|全球|S1
axis|轴线|理论|重要|跨时期|全球|S11
symmetry-layout|对称布局|理论|重要|古代|中国|S11
enclosure|围合|理论|重要|跨时期|全球|S11
openness|开敞|理论|重要|跨时期|全球|S1
boundary|边界|理论|重要|跨时期|全球|S1
node-path|节点与路径|理论|重要|跨时期|全球|S1
transition-space|过渡空间|理论|核心|跨时期|全球|S1
gray-space|灰空间|理论|重要|20世纪|东亚|S1,S11
vestibule|门厅|理论|重要|跨时期|全球|S1
corridor-space|廊道空间|理论|重要|跨时期|全球|S1,S8
functional-zoning|功能分区|理论|重要|跨时期|全球|S1
spatial-organization|空间组织方式|理论|核心|跨时期|全球|S1
interior-exterior-transition|室内外过渡|理论|核心|跨时期|全球|S1,S11,S12
eaves-space|檐下空间|理论|重要|古代|中国|S11
raised-floor|架空层|理论|补充|20世纪|全球|S1
courtyard|庭院|理论|核心|跨时期|全球|S3,S11
opening-interface|门窗洞口|理论|重要|跨时期|全球|S11
interface-permeability|界面渗透|理论|重要|20世纪|全球|S1
view-corridor|视线通廊|理论|重要|跨时期|全球|S3
visual-comfort|视觉舒适度|理论|重要|20世纪|全球|S9
thermal-comfort|热舒适度|理论|重要|20世纪|全球|S10
acoustic-environment|声环境|理论|补充|20世纪|全球|S1
universal-design|通用设计|理论|重要|20世纪|全球|S1
accessibility-design|无障碍设计|理论|重要|20世纪|全球|S1
sustainable-design|可持续设计|理论|重要|20世纪|全球|S1
borrowed-scenery|借景|造景|核心|古代|中国|S3
framed-scenery|框景|造景|核心|古代|中国|S3
opposed-scenery|对景|造景|核心|古代|中国|S3
screened-scenery|障景|造景|核心|古代|中国|S3
winding-path|曲径|造景|核心|古代|中国|S3
tour-route|游线|造景|核心|古代|中国|S3
leaked-scenery|漏景|造景|重要|古代|中国|S3
added-scenery|添景|造景|重要|古代|中国|S3
side-scenery|夹景|造景|重要|古代|中国|S3
suppressed-scenery|抑景|造景|重要|古代|中国|S3
rockery|叠石|造景|重要|古代|中国|S3
water-management|理水|造景|重要|古代|中国|S3
planting-design|植物配置|造景|重要|跨时期|全球|S12
garden-architecture|园林建筑|造景|重要|古代|中国|S3
seasonal-scenery|四季造景|造景|重要|古代|中国|S3
time-scenery|时序造景|造景|补充|古代|中国|S3
rock-garden|岩石园|造景|补充|跨时期|全球|S12
circulation|动线设计|动线|核心|跨时期|全球|S8
pedestrian-flow|人行流线|动线|核心|跨时期|全球|S8
vehicle-flow|车行流线|动线|重要|20世纪|全球|S8
people-vehicle-separation|人车分流|动线|重要|20世纪|全球|S8
visitor-route|参观动线|动线|重要|跨时期|全球|S8
service-route|服务动线|动线|重要|跨时期|全球|S8
evacuation-route|疏散动线|动线|核心|20世纪|全球|S8
loop-route|回游式动线|动线|重要|古代|中国|S3,S8
serial-route|串联式动线|动线|重要|跨时期|全球|S8
radial-route|放射式动线|动线|补充|跨时期|全球|S8
sunken-courtyard|下沉庭院|下沉空间|核心|跨时期|全球|S1,S3
sunken-plaza|下沉广场|下沉空间|核心|20世纪|全球|S1
sunken-garden|下沉花园|下沉空间|重要|跨时期|全球|S3,S12
semi-sunken-space|半下沉空间|下沉空间|重要|20世纪|全球|S1
earth-sheltered|覆土建筑|下沉空间|补充|20世纪|全球|S1
light-well|天井|下沉空间|重要|古代|中国|S11
sunken-atrium|地下中庭|下沉空间|重要|20世纪|全球|S1
level-change|高差处理|下沉空间|核心|跨时期|全球|S1
drainage|排水|下沉空间|核心|跨时期|全球|S1
damp-proofing|防潮|下沉空间|核心|20世纪|全球|S1
safety-guarding|安全防护|下沉空间|核心|20世纪|全球|S1
sunken-accessibility|下沉空间无障碍|下沉空间|核心|20世纪|全球|S1
daylighting|自然采光|材料|核心|跨时期|全球|S9
side-window-daylight|侧窗采光|材料|重要|跨时期|全球|S9
skylight|天窗采光|材料|重要|跨时期|全球|S9
daylight-factor|采光系数|材料|补充|20世纪|全球|S9
glare|眩光|材料|重要|20世纪|全球|S9
natural-ventilation|自然通风|材料|核心|跨时期|全球|S10
wind-driven-ventilation|风压通风|材料|重要|跨时期|全球|S10
stack-ventilation|热压通风|材料|重要|跨时期|全球|S10
atrium-ventilation|中庭通风|材料|补充|20世纪|全球|S10
mixed-mode-ventilation|混合通风|材料|重要|20世纪|全球|S10
demand-controlled-ventilation|需求控制通风|材料|补充|20世纪|全球|S10
material-texture|材料质感|材料|核心|跨时期|全球|S1,S11
material-color|材料色彩|材料|重要|跨时期|全球|S7,S11
material-durability|材料耐久|材料|重要|跨时期|全球|S1
vernacular-material|乡土材料|材料|重要|跨时期|全球|S11
transparent-material|透明与半透明材料|材料|重要|20世纪|全球|S1
structural-material|结构材料|材料|重要|跨时期|全球|S1
ancient-greek|古希腊建筑|风格|重要|古代|欧洲|S1,S2
ancient-roman|古罗马建筑|风格|重要|古代|欧洲|S1,S2
byzantine|拜占庭建筑|风格|重要|中世纪|欧洲|S1,S2
romanesque|罗马风建筑|风格|重要|中世纪|欧洲|S1,S2
gothic|哥特建筑|风格|核心|中世纪|欧洲|S1,S2
renaissance-style|文艺复兴建筑|风格|核心|文艺复兴至19世纪|欧洲|S1,S2
baroque|巴洛克建筑|风格|重要|文艺复兴至19世纪|欧洲|S1,S2
rococo|洛可可建筑|风格|重要|文艺复兴至19世纪|欧洲|S1,S2
neoclassical|新古典主义建筑|风格|重要|文艺复兴至19世纪|欧洲|S1,S2
romanticism-style|浪漫主义建筑|风格|补充|文艺复兴至19世纪|欧洲|S1,S2
eclecticism|折衷主义建筑|风格|补充|文艺复兴至19世纪|全球|S1,S2
revival-gothic|哥特复兴|风格|补充|文艺复兴至19世纪|欧洲|S1,S2
revival-renaissance|文艺复兴复兴|风格|补充|文艺复兴至19世纪|欧洲|S1,S2
arts-crafts|工艺美术运动|风格|重要|文艺复兴至19世纪|欧洲|S1,S2
art-nouveau|新艺术运动|风格|重要|20世纪|欧洲|S1,S2
art-deco|装饰艺术|风格|重要|20世纪|全球|S1,S2
modernism|现代主义建筑|风格|核心|20世纪|全球|S1,S2
international-style|国际风格|风格|重要|20世纪|全球|S1,S2
bauhaus|包豪斯|风格|核心|20世纪|欧洲|S1,S2
de-stijl|风格派|风格|补充|20世纪|欧洲|S1,S2
constructivism|构成主义|风格|重要|20世纪|欧洲|S1,S2
futurism-style|未来主义建筑|风格|补充|20世纪|欧洲|S1,S2
expressionism-style|表现主义建筑|风格|补充|20世纪|欧洲|S1,S2
brutalism|粗野主义|风格|重要|20世纪|全球|S1,S2
structuralism|结构主义建筑|风格|补充|20世纪|欧洲|S1,S2
organic-architecture|有机建筑|风格|重要|20世纪|全球|S1,S2
high-tech|高技派|风格|重要|20世纪|全球|S1,S2
postmodernism|后现代主义建筑|风格|核心|20世纪|全球|S1,S2
deconstructivism|解构主义|风格|重要|20世纪|全球|S1,S2
minimalism-architecture|极简主义建筑|风格|重要|20世纪|全球|S1,S2
critical-regionalism|批判地域主义|风格|重要|20世纪|全球|S1,S2
parametric-architecture|参数化建筑|风格|重要|当代|全球|S1,S2
green-architecture|绿色建筑|风格|核心|当代|全球|S1
sustainable-architecture|可持续建筑|风格|核心|当代|全球|S1
vernacular-architecture|乡土建筑|风格|重要|跨时期|全球|S1,S11
chinese-architecture-style|中国传统建筑|风格|核心|古代|中国|S1,S11
japanese-architecture|日本建筑|风格|重要|跨时期|东亚|S1
korean-architecture|韩国建筑|风格|补充|跨时期|东亚|S1
islamic-architecture|伊斯兰建筑|风格|重要|中世纪|伊斯兰/南亚|S1
indian-architecture|印度建筑|风格|重要|古代|伊斯兰/南亚|S1
southeast-asian-architecture|东南亚建筑|风格|补充|跨时期|东亚|S1
african-architecture|非洲建筑|风格|补充|跨时期|全球|S1
latin-american-colonial|拉美殖民建筑|风格|补充|文艺复兴至19世纪|美洲|S1
brazilian-modernism|巴西现代主义|风格|补充|20世纪|美洲|S1
mexican-modernism|墨西哥现代主义|风格|补充|20世纪|美洲|S1
huizhou-style|徽派建筑|风格|重要|古代|中国|S11
shanxi-style|晋派建筑|风格|补充|古代|中国|S11
lingnan-style|岭南建筑|风格|补充|古代|中国|S11
hokkien-style|闽南建筑|风格|补充|古代|中国|S11
hakka-style|客家建筑|风格|补充|古代|中国|S11
gan-style|赣派建筑|风格|补充|古代|中国|S11
yaodong|窑洞|风格|补充|古代|中国|S11
tibetan-architecture|藏式建筑|风格|补充|古代|中国|S11
xinjiang-architecture|新疆建筑|风格|补充|古代|中国|S11
imperial-architecture|宫殿建筑|风格|重要|古代|中国|S11
religious-architecture|宗教建筑|风格|重要|跨时期|全球|S11
urban-planning-style|城市规划|风格|补充|跨时期|全球|S11
mannerism|样式主义（手法主义）建筑|风格|重要|文艺复兴至19世纪|欧洲|N1,N3,N2
beaux-arts|学院派建筑（布扎艺术）|风格|重要|文艺复兴至19世纪|全球|N1,N3
vitruvian-triad|维特鲁威三原则|理论|核心|古代|欧洲|N4,N5
plein-air|外光写生|理论|重要|文艺复兴至19世纪|欧洲|N2,N5
gestalt-organization-laws|格式塔组织律|理论|重要|20世纪|全球|wp-visual-perception,wp-gestalt-psychology
color-psychology|色彩心理学|理论|重要|20世纪|全球|wp-interior-design,wp-color-psychology
environmental-psychology|环境心理学|理论|重要|20世纪|全球|wp-landscape-architecture,wp-environmental-psychology
hardscape-softscape|硬质景观与软质景观|造景|重要|跨时期|全球|wp-landscape-architecture,wp-landscape-design
wayfinding|导视与寻路|动线|重要|跨时期|全球|wp-graphic-design,wp-wayfinding
lighting-design|照明设计|材料|重要|跨时期|全球|wp-interior-design,wp-lighting-design
place-attachment|场所依恋|理论|重要|当代|全球|wp-environmental-psychology,wp-place-attachment
placemaking|场所营造|理论|重要|当代|全球|wp-placemaking,wp-urban-design
space-syntax|空间句法|理论|重要|20世纪|全球|wp-space-syntax,wp-urban-morphology
pattern-language|模式语言|理论|重要|20世纪|全球|wp-pattern-language,wp-a-pattern-language
form-follows-function|形式追随功能|理论|重要|跨时期|全球|wp-form-follows-function,wp-functionalism-architecture
functionalism-architecture|功能主义建筑|风格|重要|20世纪|全球|wp-functionalism-architecture,wp-form-follows-function
biophilic-design|亲生命性设计|理论|重要|当代|全球|wp-biophilic-design,wp-evidence-based-design
defensible-space-theory|防御性空间理论|理论|重要|20世纪|全球|wp-defensible-space-theory,wp-cpted
rembrandt|伦勃朗光|理论|补充|文艺复兴至19世纪|欧洲|wp-rembrandt-lighting,rijksmuseum-rembrandt
tenebrism|暗绘风格（暗色调主义）|风格|补充|文艺复兴至19世纪|欧洲|wp-tenebrism,dailyart-tenebrism
plaza|广场（城市广场）|造景|重要|跨时期|全球|wp-town-square,pps-successful-place
atrium-architecture|中庭|材料|重要|跨时期|全球|wp-atrium-architecture,designingbuildings-atrium
exit-sign|疏散标识（安全出口标识）|动线|补充|20世纪|全球|wp-exit-sign,ecfr-1910-37
mexican-baroque|墨西哥巴洛克（新西班牙巴洛克）|风格|补充|文艺复兴至19世纪|美洲|wp-new-spanish-baroque,designingbuildings-baroque
metabolism|新陈代谢派（Metabolism）|理论|重要|20世纪|东亚|wp-metabolism-architecture,designingbuildings-metabolism
proxemics|近距学（Proxemics）|理论|重要|20世纪|全球|wp-proxemics,designingbuildings-proxemics
sfumato|渐隐法（Sfumato）|理论|重要|文艺复兴至19世纪|欧洲|wp-sfumato,artincontext-sfumato
trompe-loeil|错视画（Trompe-l'œil）|理论|重要|文艺复兴至19世纪|欧洲|wp-trompe-loeil,artincontext-trompe
hatching|排线法（Hatching）|理论|重要|文艺复兴至19世纪|欧洲|wp-hatching,artincontext-hatching
stippling|点描法（Stippling）|理论|补充|文艺复兴至19世纪|欧洲|wp-stippling,artincontext-stippling
imperial-axial-route|宫廷中轴仪礼动线|动线|重要|古代|中国|wp-forbidden-city,designingbuildings-forbidden-city
picturesque|如画（Picturesque 美学）|理论|重要|跨时期|欧洲|wp-picturesque,tate-picturesque
mughal-architecture|莫卧儿建筑|风格|重要|文艺复兴至19世纪|伊斯兰/南亚|wp-mughal-architecture,designingbuildings-taj-mahal
early-islamic-architecture|早期伊斯兰建筑|风格|重要|中世纪|伊斯兰/南亚|wp-umayyad-architecture,artincontext-islamic-art
academic-art-theory|学院派理论与素描教学|理论|重要|文艺复兴至19世纪|全球|wp-academic-art,artincontext-academic
classical-order|古典柱式|理论|重要|古代|欧洲|wp-classical-order,designingbuildings-classical
"""

THEMES = ["理论", "风格", "造景", "动线", "下沉空间", "材料"]
PERIODS = ["古代", "中世纪", "文艺复兴至19世纪", "20世纪", "当代", "跨时期"]
REGIONS = ["欧洲", "中国", "东亚", "伊斯兰/南亚", "美洲", "全球"]


def parse():
    rows = []
    seen = set()
    for line in DATA.strip().splitlines():
        parts = line.strip().split("|")
        if len(parts) != 7:
            raise ValueError(f"bad row: {line}")
        eid, title, theme, tier, period, region, sources = parts
        if not all(c.isascii() and (c.islower() or c.isdigit() or c == "-") for c in eid):
            raise ValueError(f"bad id: {eid}")
        if eid in seen:
            raise ValueError(f"duplicate id: {eid}")
        seen.add(eid)
        if theme not in THEMES or tier not in ("核心", "重要", "补充"):
            raise ValueError(f"bad theme/tier: {line}")
        if period not in PERIODS or region not in REGIONS:
            raise ValueError(f"bad period/region: {line}")
        rows.append({
            "id": eid, "title": title, "theme": theme, "tier": tier,
            "period": period, "region": region,
            "sources": [s for s in sources.split(",") if s],
        })
    return rows


def main():
    rows = parse()
    counts = {t: sum(1 for r in rows if r["theme"] == t) for t in THEMES}
    tiers = {t: sum(1 for r in rows if r["tier"] == t) for t in ("核心", "重要", "补充")}

    scope = [
        "# scope.md — 《绘画理论与建筑空间设计》入选清单",
        "",
        "来源说明：S1–S12 为 research/outline_raw.md 中实际抓取成功的权威百科分类树（Wikipedia），",
        "取并集后补入任务文档 TASK_design.md 指定条目。N1–N5 为第 3 轮新增的权威大纲页面（见 research/gaps-external-round02.md）。",
        "第 7 轮候选直接以 data/sources.json 的来源 id 标注（详见 research/gaps-external-round06.md）。",
        "每条标注层级与来源编号。",
        "",
        f"总计 {len(rows)} 条：理论 {counts['理论']}、风格 {counts['风格']}、造景 {counts['造景']}、",
        f"动线 {counts['动线']}、下沉空间 {counts['下沉空间']}、材料 {counts['材料']}。",
        f"层级分布：核心 {tiers['核心']}、重要 {tiers['重要']}、补充 {tiers['补充']}。",
        "",
    ]
    for theme in THEMES:
        scope += [f"## {theme}（{counts[theme]} 条）", "", "| id | 名称 | 层级 | 时期 | 地区 | 来源 |", "| --- | --- | --- | --- | --- | --- |"]
        for r in rows:
            if r["theme"] == theme:
                scope.append(f"| {r['id']} | {r['title']} | {r['tier']} | {r['period']} | {r['region']} | {','.join(r['sources'])} |")
        scope.append("")
    (ROOT / "scope.md").write_text("\n".join(scope), encoding="utf-8")

    cov_path = ROOT / "coverage.json"
    existing = {}
    if cov_path.exists():
        old = json.loads(cov_path.read_text(encoding="utf-8"))
        existing = {e["id"]: e for e in old.get("entries", [])}

    def coverage_row(r):
        row = {
            "id": r["id"], "title": r["title"], "theme": r["theme"],
            "tier": r["tier"], "period": r["period"], "region": r["region"],
            "level": "L1", "status": "未开始", "source_count": len(r["sources"]),
            "needs_verification_count": 0, "last_updated": TODAY,
        }
        if r["id"] in existing:
            for key in ("level", "status", "source_count", "needs_verification_count", "last_updated"):
                row[key] = existing[r["id"]].get(key, row[key])
        return row

    coverage = {
        "updated": TODAY,
        "total": len(rows),
        "entries": [coverage_row(r) for r in rows],
    }
    cov_path.write_text(json.dumps(coverage, ensure_ascii=False, indent=2), encoding="utf-8")

    matrix = [
        "# 覆盖矩阵 — 主题 × 时期 × 地区",
        "",
        f"生成日期：{TODAY}。单元格格式：条目数（核心/重要/补充）。空白格为 0。",
        "",
    ]
    for region in REGIONS:
        matrix += [f"## 地区：{region}", "", "| 主题 | " + " | ".join(PERIODS) + " |", "| --- | " + " | ".join(["---"] * len(PERIODS)) + " |"]
        for theme in THEMES:
            cells = []
            for period in PERIODS:
                subset = [r for r in rows if r["theme"] == theme and r["period"] == period and r["region"] == region]
                if not subset:
                    cells.append("—")
                else:
                    core = sum(1 for r in subset if r["tier"] == "核心")
                    imp = sum(1 for r in subset if r["tier"] == "重要")
                    sup = sum(1 for r in subset if r["tier"] == "补充")
                    cells.append(f"{len(subset)}（{core}/{imp}/{sup}）")
            matrix.append(f"| {theme} | " + " | ".join(cells) + " |")
        matrix.append("")
    (ROOT / "coverage-matrix.md").write_text("\n".join(matrix), encoding="utf-8")
    print(f"scope entries={len(rows)} themes={counts} tiers={tiers}")


if __name__ == "__main__":
    main()
