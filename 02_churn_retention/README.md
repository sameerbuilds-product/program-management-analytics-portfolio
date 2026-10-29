# 02 — Customer Churn & Retention Analysis

## Business question
Which customer cohorts show higher churn, and what retention experiments should be prioritized?

## Dataset
`data/customers_synthetic.csv` is fictional practice data. Churn is represented as a binary label.

## Analysis plan
- Define churn clearly before analysis.
- Compare churn by tenure, order frequency, and customer segment.
- Avoid confusing correlation with causation.
- Prioritize interventions by addressable population, expected value, cost, and measurement quality.

## SQL
`sql/churn_analysis.sql` contains churn-rate and cohort queries.

## Recommended output
A short decision memo with: highest-risk cohorts, evidence, proposed intervention, success metric, guardrail metric, and experiment duration.

## Limitations
This dataset is synthetic and does not model real customer behavior. It should not be used to make real customer-level decisions.
