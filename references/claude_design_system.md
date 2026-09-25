# Claude Frontend Design System Reference

This document outlines the core principles and design tokens borrowed from Anthropic's Claude interface, adapted for editorial resumes and high-density technical documents.

## 1. Typography Hierarchy

| Role | Font Families | Size | Weight | Tracking / Leading | Notes |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Primary Headings & Name** | `"Source Serif 4"`, `"Noto Serif SC"`, `"Songti SC"`, `Georgia`, serif | `20pt ~ 23pt` (Name) / `10.5pt` (H2) | `700` | `letter-spacing: 0.04em ~ 0.06em` | Dignified editorial serif with warm brackets and literary presence |
| **Section Micro-Subtitles** | `"Inter"`, `-apple-system`, sans-serif | `6.8pt ~ 7pt` | `600` | `letter-spacing: 0.12em; text-transform: uppercase;` | Light stone gray, provides visual breathing room |
| **Body Text** | `"Inter"`, `"PingFang SC"`, `"Hiragino Sans GB"`, sans-serif | `8.5pt ~ 8.7pt` | `400` / `500` | `line-height: 1.35 ~ 1.4` | Humanist geometric sans-serif for crystal-clear readability |
| **Numeric & Dates** | `"Inter"`, system-ui | `8.3pt ~ 8.6pt` | `400` | `font-variant-numeric: tabular-nums;` | Monospaced figures ensure clean vertical alignment |

## 2. Color Palette & Semantics

| Token | Hex | Role | State Enterprise (央国企) Context |
| :--- | :--- | :--- | :--- |
| **Terracotta Accent** | `#B24C2C` / `#A33B1F` | Section indicators, target role badge, category labels | Harmonizes Claude's terracotta warmth with traditional Chinese cinnabar red (沉稳、大气、内敛) |
| **Primary Charcoal** | `#1F1D1A` | Headings, applicant name, key technical metrics | Replaces harsh jet black (`#000000`) with soft deep charcoal |
| **Body Charcoal** | `#2D2A26` / `#38342F` | Paragraphs, bullet points | High contrast yet easy on interviewer eyes |
| **Secondary Gray** | `#55504A` / `#6E685E` | Subtitles, company roles | Subtle hierarchy contrast |
| **Muted Stone** | `#7A746B` / `#9E9689` | Dates, English section tags | Tabular alignment anchor |
| **Pill Background** | `#F4F1EA` | Tech stack capsule tags | Border: `1px solid #E5E0D6` |
| **Card Background** | `#FAF8F5` | Self-evaluation background | Border-left: `2.8px solid #D6CEBF` |
| **Hairline Dividers**| `#EAE5DC` / `#E6E1D6` | 1px horizontal section rules | Subtle gradient fadeout to right |

## 3. Micro-Components

- **Vertical Section Pill**: `width: 3.2px; height: 12.5px; background: #B24C2C; border-radius: 2px;`
- **Tech Stack Badges**: Inline rounded pills (`padding: 0 4px; font-size: 7.25pt; border-radius: 2.5px;`)
- **Bullet Glyphs**: Custom colored square markers (`▪` in `#B24C2C`) and result indicators (`•` in `#A33B1F`).
