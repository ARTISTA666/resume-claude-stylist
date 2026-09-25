---
name: resume-claude-stylist
description: >-
  Optimizes, restyles, and reformats resumes (especially for Central SOEs / State-Owned Enterprises and technical roles)
  using Claude's frontend design language. Enforces editorial serif typography, warm terracotta accents,
  high information density, punchy phrasing, strict 1-page A4 canvas budget, and multi-format export (PDF, DOCX, HTML).
---

# Resume Claude Stylist Skill

A specialized skill for Antigravity to optimize, restyle, and reformat resumes into publication-grade documents inspired by Claude's frontend design language and typography, tailored particularly for Chinese State-Owned Enterprises (央国企) and modern technology positions.

## Core Capabilities

1. **Claude Frontend Aesthetic**: Incorporates editorial serif headings (`Source Serif 4`, `Noto Serif SC`, `Songti SC`), clean humanist sans-serif body typography (`Inter`, `PingFang SC`), subtle warm terracotta / cinnabar accents (`#B24C2C` / `#A33B1F`), soft warm micro-cards (`#FAF8F5`), and capsule tag badges (`#F4F1EA`).
2. **State-Owned Enterprise (央国企) Rigor**: Retains and highlights mandatory institutional background fields (political affiliation: 共青团员/中共党员, hometown/籍贯, graduation timeline, demographic essentials) with serious, dignified, and professional aesthetics.
3. **High Information Density & Punchy Phrasing**: Restructures verbose bullet points into crisp, high-impact statements following the `【Action / Role】+【Architecture / Technology】+【Quantified Outcome】` formula with visual ATS keyword bolding.
4. **Strict 1-Page A4 Budgeting**: Precision layout calculation that fills the A4 canvas evenly and comfortably without bottom voids and guarantees zero page spillover.
5. **Multi-Format Export**: Generates pixel-perfect vector PDF (via Headless Chrome), editable Word document (via `python-docx` with matching typography and palettes), and self-contained portable HTML with base64 embedded photos.

---

## Workflow Procedures

### Step 1: Input Analysis & Asset Extraction
1. Inspect the source resume (`.docx`, `.pdf`, `.md`, or `.txt`).
2. **Rule**: Never overwrite original resume files. Always save outputs with a new suffix (e.g., `_Claude风格`).
3. Extract embedded candidate ID photo (if in `.docx`, extract `word/media/image1.png`) and convert to base64 for self-contained HTML embedding.
4. Verify core applicant demographics required by Central SOEs:
   - 姓名 (Name) & 求职意向 (Target Role)
   - 政治面貌 (中共党员 / 共青团员 / 群众)
   - 出生年月 (Birth Date) & 籍贯 (Hometown) & 民族 (Ethnicity)
   - 现居城市 (Current City) & 联系电话 (Phone) & 电子邮箱 (Email)

### Step 2: Content Optimization & Density Enhancement
1. **自我评价 (Self-Evaluation)**: Summarize into 3 structured pillars:
   - 工程底色与系统闭环 (Engineering practice & full lifecycle closure)
   - 核心技术与架构集成 (Core tech stack depth & middleware integration)
   - 作风稳健与组织纪律 (Reliability, teamwork, discipline & willingness to adapt)
2. **专业技能 (Technical Skills)**: Categorize into 4 clear technical domains (e.g., Java 后端, 存储与中间件, AI 应用工程, 运维与全栈) with warm terracotta bold labels.
3. **实习与项目经历 (Experience & Projects)**:
   - Extract tech stack as inline micro-capsule tags (`tech-pill`).
   - Bullet points must be concise and actionable: highlight architectural strategies (**乐观锁版本号**, **RabbitMQ 异步解耦与死信队列**, **分片批处理**, **混合检索与 RRF 重排**, **自适应抽帧降载**).
   - Add clear outcome indicators (`【项目成效】` / `• 结果：`).

### Step 3: Claude Typography & Styling Application
- **Font Stack**:
  - Headings: `"Source Serif 4", "Noto Serif SC", "Songti SC", "Source Han Serif SC", STSong, Georgia, serif`
  - Body: `"Inter", -apple-system, BlinkMacSystemFont, "PingFang SC", "Hiragino Sans GB", "Microsoft YaHei", sans-serif`
  - Numbers / Tabular: `font-variant-numeric: tabular-nums`
- **Color Codes**:
  - Terracotta Accent: `#B24C2C` / `#A33B1F`
  - Primary Charcoal: `#1F1D1A`
  - Secondary Text: `#55504A`
  - Subtle Border: `#EAE5DC`
  - Card Fill: `#FAF8F5`
  - Tag Fill: `#F4F1EA`

### Step 4: Strict 1-Page A4 Budgeting & Compilation
Use the helper script to compile and verify single-page geometry:
```bash
python3 scripts/render_pdf.py --html <path_to_html> --output <path_to_pdf>
```
Verification checks:
- Run `pdfinfo <pdf_path> | grep Pages:` and ensure output is exactly `Pages: 1`.
- If `Pages: 2`, adjust font size by `0.1pt` or reduce section margins by `0.5px` until it fits on exactly 1 page.
- Run `pdftoppm -png -r 150 <pdf_path> <preview_prefix>` to visually verify balance and margin proportions.

### Step 5: Matching Word (.docx) Generation
Run the Word exporter script to generate an editable Word document with matching fonts, colors, and layout:
```bash
python3 scripts/generate_docx.py --data <path_to_data_or_json> --output <path_to_docx>
```

---

## Detailed References

- [Claude Design System Guide](./references/claude_design_system.md)
- [State-Owned Enterprise (央国企) Resume Guidelines](./references/sooe_resume_guidelines.md)
- [HTML Resume Template](./templates/claude_resume_template.html)
- [Resume Data Schema](./templates/resume_schema.json)
