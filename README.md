# 《绘画理论与建筑空间设计》静态知识库

数据驱动的静态网站：结构化 JSON 数据 → `tools/check.py` 机器校验 → `tools/gen_site.py` 确定性渲染 → `site/index.html` 纯静态站点。

## 快速开始

```bash
python tools/check.py          # 全量校验
python tools/gen_site.py       # 生成 site/
python tools/check_links.py    # 站内链接核验
```

浏览器打开 `site/index.html` 即可离线浏览。

## 目录

- `scope.md`：全量范围清单（编辑基准线）
- `coverage.json` / `coverage-matrix.md`：覆盖状态与矩阵
- `data/sources.json`：全局来源库（verified 字段控制可引用性）
- `entries/*.json`：条目数据（L1/L2/L3）
- `tools/`：校验器、生成器、链接检查
- `tests/`：校验器单元测试
- `site/`：生成的静态站点（不要手改）
- `PROGRESS.md` / `DECISIONS.md` / `REPORT.md`：进度、决策与报告

## 硬性规则

1. 不编造数字、日期、人名、引文、出处；查不到写“待核实”。
2. 只引用 `data/sources.json` 中 `verified=true` 的来源。
3. 关键事实双源互证，否则标待核实；争议并列各方理由。
4. 不使用任何图片；所有图示为内联 SVG，并注明“示意图，非施工图”。
5. 尺寸/坡度/消防/无障碍数据仅作一般性说明，附“实际工程须按当地规范和专业设计人员的要求”。
6. 每轮最多处理 40 个条目；L1 未全部完成前不得深写个别条目。
