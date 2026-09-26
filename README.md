# 📄 Resume Claude Stylist (专业求职简历排版优化器 · 央国企与私企双模版)

> 借鉴 **Claude 前端设计语言与排版美学** 的专业求职简历排版、润色与自动化导出 Antigravity 技能。提供针对 **央国企体制内求职** 与 **私营/商业互联网科技企业** 的双模版架构。

[![Antigravity Skill](https://img.shields.io/badge/Antigravity-Skill-orange.svg)](https://github.com/ARTISTA666/resume-claude-stylist)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)
[![Format: PDF / DOCX / HTML](https://img.shields.io/badge/Formats-PDF%20%7C%20DOCX%20%7C%20HTML-success.svg)]()

---

## 🌟 核心特性与设计哲学

1. **Claude 前端刊物级字体美学 (Editorial Typography)**：
   - **标题体系**：严选 `Source Serif 4` / `Noto Serif SC` / `Songti SC` 典雅宋体衬线，配合字距微调（`letter-spacing: 0.05em`），在保留沉稳庄重审美的同时，大幅增添学术底蕴与书卷气质。
   - **正文字体**：采用现代 Humanist 无衬线体系（`Inter` / `PingFang SC`），数字与日期使用等宽对齐属性（`tabular-nums`），整齐利落。
2. **色调调和（Claude 陶土暖红 × 国企稳健朱砂）**：
   - 提取 Claude 标志性陶土红（`#B24C2C` / `#A33B1F`），呼应中国传统朱砂色与故宫红，内敛庄重且具有视觉聚焦效果。
   - 采用深炭灰色（`#1F1D1A` / `#38342F`）替代生硬纯黑，阅读体验极其温润。
3. **针对性双模版预设 (Dual-Mode Architecture)**：
   - **🏛️ 央国企版 (SOE Mode)**：突出强化政治面貌（中共党员/共青团员）、籍贯、民族、稳定性、全流程闭环及服从组织调配作风。
   - **🚀 私企/互联网版 (Private Tech Mode)**：强化 GitHub 开源主页、个人站点、Owner 闭环交付能力、高并发/JUC/JVM 底层调优、AI 工程化与量化指标（时延削减 60%、内存防 OOM、算力降载 40%）。
4. **高信息密度与精炼工程表述**：
   - 剔除虚浮套话，采用 `【业务背景/职责】+【架构/技术方案】+【量化成效】` 经典表达公式。
   - 技术关键词科学加粗，契合 ATS 与面试官 15 秒快速扫读习惯。
5. **严苛的 A4 一页纸满幅控制 (Strict Single-Page A4)**：
   - 精密计算垂直节奏与行间距，确保内容**整版匀称铺满整张 A4 纸**，无底部突兀空白，且**绝对不溢出第 2 页**。
6. **多端多格式全流程交付**：
   - **PDF 终稿**：通过 Chrome Headless 编译，矢量文字与超清证件照，即刻打印。
   - **Word 版**：通过 `python-docx` 生成，继承同款字体、色调与间距，便于后续根据不同岗位微调。
   - **HTML 模板**：单文件自包含（证件照 Base64 内联），浏览器内随时预览，按 `Cmd + P` 可直接导出。

---

## 📂 技能目录结构

```text
resume-claude-stylist/
├── SKILL.md                          # Antigravity 技能主定义文件
├── README.md                         # 项目与技能说明
├── LICENSE                           # MIT 开源协议
├── scripts/
│   ├── render_pdf.py                 # Headless Chrome PDF 编译与单页严格校验脚本
│   └── generate_docx.py              # Word (.docx) 导出器（匹配 Claude 风格排版）
├── templates/
│   ├── claude_resume_template.html   # 可复用 HTML 模板
│   ├── resume_schema.json            # 结构化数据 Schema 校验规范
│   ├── sample_resume_data.json       # 央国企版样例数据
│   └── sample_resume_private.json    # 私企/互联网版样例数据
└── references/
    ├── claude_design_system.md       # Claude 前端设计规范与设计令牌 (Design Tokens)
    ├── sooe_resume_guidelines.md     # 央国企与体制内求职规范指南
    └── private_enterprise_guidelines.md # 私企与互联网科技公司求职规范指南
```

---

## 🚀 快速使用指南

### 1. 作为 Antigravity 技能调用

将本目录克隆或放置在 Antigravity 技能路径下：
- **全局路径**：`~/.gemini/config/skills/resume-claude-stylist`
- **项目路径**：`<project_root>/.agents/skills/resume-claude-stylist`

在与 Antigravity 对话中直接提示：
> “帮我制作一份面向私企的 Java 后端简历，使用 Claude 前端风格，突出高并发与 AI 工程化经验，严格保持一页 A4 铺满。”

### 2. 本地命令行独立运行

#### 从数据生成 Word (.docx)
```bash
python3 scripts/generate_docx.py \
  --data templates/sample_resume_private.json \
  --avatar path/to/avatar.png \
  --output output/resume_private.docx
```

#### 从 HTML 编译单页 PDF
```bash
python3 scripts/render_pdf.py \
  --html templates/claude_resume_template.html \
  --output output/resume.pdf
```
脚本将自动调用系统 Chrome 并使用 `pdfinfo` 校验是否严格为 1 页。

---

## 📄 License

[MIT License](./LICENSE) © 2026 ARTISTA666
