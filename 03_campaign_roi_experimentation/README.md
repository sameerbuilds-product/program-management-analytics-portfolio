# 03 — Campaign ROI & Experimentation

## Business question
Which fictional campaigns appear most efficient, and how should a team evaluate an experiment beyond click-through rate?

## Dataset
`data/campaigns_synthetic.csv` contains fictional campaign-level spend, reach, clicks, conversions, and attributed revenue.

## Metrics
- CTR = clicks / impressions
- Conversion rate = conversions / clicks
- CPA = spend / conversions
- ROAS = attributed revenue / spend
- ROI = (attributed revenue - spend) / spend

## Interpretation cautions
Attribution is not the same as incrementality. A campaign with high ROAS may still have weak incremental impact. For causal conclusions, use a randomized holdout or a well-designed quasi-experiment.

## SQL
`sql/campaign_roi.sql` calculates comparable campaign metrics.
