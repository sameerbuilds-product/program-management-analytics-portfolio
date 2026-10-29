# 01 — Quick Commerce Operations Analytics

## Business question
Which stores and operating conditions are associated with late deliveries and cancellations, and what should an operations program manager investigate first?

## Dataset
`data/orders_synthetic.csv` contains synthetic order-level records created for portfolio practice. All figures are fictional.

## KPIs
- Orders
- On-time delivery rate
- Average delivery duration
- Cancellation rate
- Late-order rate by store and time slot

## How to run
From the repository root:

```bash
python 01_quick_commerce_operations/analyze_operations.py
```

The script prints summary metrics and the store/time-slot groups with the highest late-order rates.

## SQL
Open `sql/operations_analysis.sql` for example queries using aggregation, CTEs, and window functions.

## Example decision framework
1. Validate that delays are not caused by data quality issues.
2. Segment by store, hour, weather, and order volume.
3. Identify the largest contribution to late orders, not just the highest percentage.
4. Pilot one intervention, such as peak-hour staffing or dispatch-process changes.
5. Compare pre/post results while controlling for demand mix.

## Limitations
The dataset is synthetic and does not include real route, rider, inventory, or weather feeds. Findings are illustrative, not operational facts.
