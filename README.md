# Program Management & Business Analytics Portfolio

A portfolio of **demonstration projects using synthetic data** to showcase program management, operational analytics, SQL, KPI reporting, process improvement, and experimentation.

> **Important:** All datasets and results in this repository are synthetic and illustrative. They do not represent actual company performance, confidential data, or real work delivered for Blinkit or any employer.

## Projects

| Project | Business problem | Tools | Key outputs |
|---|---|---|---|
| 01. Quick Commerce Operations Analytics | Find delivery delays, cancellation drivers, and store-level bottlenecks | Python, pandas, SQL | KPI summary, delay analysis, SQL queries |
| 02. Customer Churn & Retention Analysis | Identify customer segments with elevated churn | Python, pandas, SQL | Churn drivers, segment comparison, retention actions |
| 03. Campaign ROI & Experiment Analysis | Compare campaign efficiency and test performance | Python, pandas, SQL | ROI, CAC, conversion, A/B test interpretation |
| 04. Automated KPI Reporting | Turn raw operational data into a repeatable reporting workflow | Python, CSV, Markdown | Reproducible report generated from input data |
| 05. Program Execution Tracker | Improve ownership, milestone tracking, and escalation | Google Sheets/Excel-ready CSV | Workstream tracker, risk log, governance cadence |

## Repository structure

```text
program-management-analytics-portfolio/
├── README.md
├── 01_quick_commerce_operations/
│   ├── README.md
│   ├── data/orders_synthetic.csv
│   ├── sql/operations_analysis.sql
│   └── analyze_operations.py
├── 02_churn_retention/
│   ├── README.md
│   ├── data/customers_synthetic.csv
│   └── sql/churn_analysis.sql
├── 03_campaign_roi_experimentation/
│   ├── README.md
│   ├── data/campaigns_synthetic.csv
│   └── sql/campaign_roi.sql
├── 04_automated_kpi_reporting/
│   ├── README.md
│   ├── data/daily_kpis_synthetic.csv
│   └── generate_report.py
├── 05_program_execution_tracker/
│   ├── README.md
│   ├── data/workstream_tracker_template.csv
│   └── data/risk_log_template.csv
└── requirements.txt
```

## How to use this portfolio

1. Start with Project 01 and read its problem statement.
2. Inspect the synthetic dataset and run the Python analysis.
3. Review the SQL queries and explain what each query answers.
4. Read the findings and recommended actions.
5. Replace template values only when you have real, permitted evidence.
6. Add screenshots of outputs after running the projects locally.

## Skills demonstrated

- SQL aggregation, joins, CTEs, and window functions
- KPI design and operational performance analysis
- Root-cause analysis and bottleneck identification
- Churn, ROI, conversion, and experimentation analysis
- Repeatable reporting and process automation
- Program governance, workstream tracking, and risk management
- Translating analysis into prioritized business actions

## Run locally

Python 3.10+ is recommended.

```bash
pip install -r requirements.txt
python 01_quick_commerce_operations/analyze_operations.py
python 04_automated_kpi_reporting/generate_report.py
```

## Suggested next step

Publish each project with a concise business question, methodology, findings, limitations, and recommended actions. Do not claim that illustrative results are real business outcomes.
