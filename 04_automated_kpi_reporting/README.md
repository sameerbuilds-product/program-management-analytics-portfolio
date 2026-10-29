# 04 — Automated KPI Reporting

## Business question
How can a recurring KPI update be generated consistently from a CSV without manually rebuilding the report every day?

## Dataset
`data/daily_kpis_synthetic.csv` contains fictional daily operational metrics.

## How to run
From the repository root:

```bash
python 04_automated_kpi_reporting/generate_report.py
```

The script creates `04_automated_kpi_reporting/output/daily_kpi_report.md`.

## Production extensions
- Schedule the script with cron, Task Scheduler, or an orchestration tool.
- Add data validation and alert thresholds.
- Write results to a database or BI tool.
- Add logging, retries, and ownership documentation.
- Use real data only where authorized.
