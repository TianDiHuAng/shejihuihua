# 设计文档：绘画理论与建筑空间设计知识库

日期：2026-11-22
状态：无人值守模式已授权执行（见 TASK_design.md）

## 意图与原因

构建一个可离线浏览、可机器校验、可持续增量的静态知识网站，覆盖绘画理论与建筑空间设计两大领域。核心价值不是“先做出漂亮页面”，而是让每条知识都可追溯来源、诚实标注待核实内容，并能在多轮中按统一结构补完。

## 目标 / 非目标 / 反目标

- 目标：全量范围清单、来源库、校验器、生成器、首批条目、可浏览站点、覆盖报告。
- 非目标：图片素材、服务端、用户系统、评论、在线协作。
- 反目标：为了页面丰满而编造数字、年份、人名、引文或来源；把单源说法写成定论。

## 约束

- 所有文件在当前项目文件夹；首页 `site/index.html`（生成物）与项目根 `index.html` 入口保持一致（根入口为重定向或生成副本，见实现）。
- 每轮最多 40 条目；L1 未全量完成前不得深写个别条目。
- 只引用 `verified=true` 来源；关键事实双源或待核实。
- 无图片；SVG 自绘，深浅色变量可读，注明“示意图，非施工图”。
- 尺寸/坡度/消防/无障碍数据仅一般性说明并附规范提示。
- 每阶段结束更新 PROGRESS、运行 `tools/check.py`、git commit。

## 方案对比

1. **手工编写 HTML 页面**：上手快，但来源、链接、重复、覆盖无法机器校验，增量写作会迅速失控。放弃。
2. **CMS / 静态站点框架（Hugo/Hexo）**：有现成模板，但引入构建依赖与主题约束，且校验规则难以内嵌到内容模型。放弃。
3. **JSON 数据 + 自定义 check.py + 自定义 gen_site.py（选定）**：数据、校验、渲染三层解耦；校验规则可精确落实双源、待核实、SVG 白名单、链接一致性；生成物纯静态可离线。代价是要自己维护脚本，但完全契合 WORKFLOW.md。

## 架构

```
scope.md / coverage.json        # 编辑基准线
        ↓
entries/*.json + data/sources.json
        ↓  tools/check.py（R1–R16 + 项目专用规则）
        ↓  tools/gen_site.py
site/*.html + site/assets/site.css
        ↓  tools/check_links.py
      REPORT.md / PROGRESS.md
```

## 数据契约

- 条目文件 `entries/<unit-id>.json`：`unit_id`、`title`、`entries: [...]`
- 条目字段：`id`（a-z0-9-）、`title`、`level`（L1/L2/L3）、`tier`（核心/重要/补充）、`theme`（理论/风格/造景/动线/下沉空间/材料）、`period`、`region`、`definition`、`time_or_place`、`overview`、`related`、`sections`（L2 起：原理/手法/实例/常见错误/限制）、`svg`（字符串数组）、`sources`、`needs_verification`、`pending_notes`。
- 来源字段：`id`、`title`、`author`、`type`、`year`（可 null）、`url`、`url2`、`verified`、`note`。
- 覆盖矩阵维度：主题 × 时期 × 地区；每格记录条目 id 与层级。

## 页面类型

1. 首页：统计卡片 + 入口导航 + 覆盖概览。
2. 单元页：按主题分组的条目列表。
3. 条目页：L1 骨架结构；L2 追加七节固定结构、SVG、来源与待核实。
4. 索引页：全站条目按主题/时期/地区索引。
5. 来源页：全部来源与 verified 状态、链接核验三态。
6. 覆盖报告页：矩阵与空白格子清单。

## 校验规则摘要

- R1 必填字段；R4 来源 id 必须存在且 verified；R5 重复检测；R6 SVG 白名单与 viewBox/出界检查；R9 全局 id 唯一；R10 needs_verification 与 pending_notes 联动；R16 id 仅 a-z0-9-。
- 项目专用：L2 条目必须含 1–2 张 SVG 与“示意图，非施工图”；尺寸/坡度/消防/无障碍段落必须含规范提示；关键事实双源或待核实。
- 生成器与检查器共享同一 SVG 清洗函数，避免两套逻辑漂移。
