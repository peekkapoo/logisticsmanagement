# Data Pipeline Skill Bundle

This bundle provides a complete, modular, and reproducible workflow for data collection, cleaning, aggregation, and export within Google Antigravity. It is designed to handle structured data prep for academic, business, finance, logistics, and forecasting domains.

## Bundle Architecture
- **Rules:** `rules/data-ethics.md` (Always-on constraints for reproducibility and legal compliance).
- **Workflows:** `workflows/pipeline.md` (Provides the `/pipeline` slash command to orchestrate the process).
- **Shared Scripts:** `shared/scripts/` (Utilities and validation scripts used across skills).
- **Skills:**
  - `data-collection`: Extract data from APIs, static/dynamic web pages, and local files.
  - `data-cleaning`: Standardize formats, handle missing values, and deduplicate.
  - `data-aggregation`: Group, pivot, and synthesize metrics.
  - `data-export`: Write output to formatted files (Excel multi-sheet, CSV, JSON).

## Installation
Skills must be installed in one of the following locations so Antigravity can detect them:
- **Workspace scope:** `.agents/skills/<name>/` (relative to your workspace root)
- **Global scope:** `~/.gemini/antigravity/skills/<name>/`

**IMPORTANT:** After copying the skills, rules, and workflows to their respective directories, you MUST restart the Antigravity session so they are detected.
