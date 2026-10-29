-- All examples use the synthetic orders_synthetic.csv dataset.
-- Adapt syntax to your SQL engine (BigQuery/PostgreSQL may differ slightly).

-- 1. Overall operating KPIs
SELECT
    COUNT(*) AS total_orders,
    AVG(CASE WHEN status = 'cancelled' THEN 1.0 ELSE 0.0 END) AS cancellation_rate,
    AVG(CASE WHEN status = 'delivered'
              AND actual_delivery_min <= promised_delivery_min
             THEN 1.0 ELSE 0.0 END) AS on_time_rate
FROM orders;

-- 2. Store-level bottlenecks
SELECT
    store_id,
    COUNT(*) AS orders,
    AVG(CASE WHEN actual_delivery_min > promised_delivery_min
             THEN 1.0 ELSE 0.0 END) AS late_rate,
    AVG(CASE WHEN status = 'cancelled' THEN 1.0 ELSE 0.0 END) AS cancellation_rate
FROM orders
GROUP BY store_id
HAVING COUNT(*) >= 20
ORDER BY late_rate DESC;

-- 3. Time-slot analysis
SELECT
    time_slot,
    COUNT(*) AS orders,
    AVG(CASE WHEN actual_delivery_min > promised_delivery_min
             THEN 1.0 ELSE 0.0 END) AS late_rate
FROM orders
GROUP BY time_slot
ORDER BY late_rate DESC;

-- 4. Rank stores by late rate using a window function
WITH store_kpis AS (
    SELECT store_id,
           COUNT(*) AS order_count,
           AVG(CASE WHEN actual_delivery_min > promised_delivery_min
                    THEN 1.0 ELSE 0.0 END) AS late_rate
    FROM orders
    GROUP BY store_id
)
SELECT *,
       DENSE_RANK() OVER (ORDER BY late_rate DESC) AS late_rate_rank
FROM store_kpis
ORDER BY late_rate_rank;
