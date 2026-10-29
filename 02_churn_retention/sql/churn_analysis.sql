-- All data is synthetic.
-- 1. Overall churn rate
SELECT AVG(CASE WHEN churned = 1 THEN 1.0 ELSE 0.0 END) AS churn_rate
FROM customers;

-- 2. Churn by tenure band
SELECT
    tenure_band,
    COUNT(*) AS customers,
    AVG(CASE WHEN churned = 1 THEN 1.0 ELSE 0.0 END) AS churn_rate
FROM customers
GROUP BY tenure_band
ORDER BY churn_rate DESC;

-- 3. Churn by customer segment
SELECT
    segment,
    COUNT(*) AS customers,
    AVG(CASE WHEN churned = 1 THEN 1.0 ELSE 0.0 END) AS churn_rate,
    AVG(monthly_orders) AS avg_monthly_orders
FROM customers
GROUP BY segment
ORDER BY churn_rate DESC;
