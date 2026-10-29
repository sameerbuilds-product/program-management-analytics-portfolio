-- All data is synthetic. Protect against division by zero with NULLIF.
SELECT
    campaign_name,
    channel,
    impressions,
    clicks,
    conversions,
    spend_inr,
    attributed_revenue_inr,
    clicks * 1.0 / NULLIF(impressions, 0) AS ctr,
    conversions * 1.0 / NULLIF(clicks, 0) AS click_to_conversion_rate,
    spend_inr * 1.0 / NULLIF(conversions, 0) AS cost_per_acquisition,
    attributed_revenue_inr * 1.0 / NULLIF(spend_inr, 0) AS roas,
    (attributed_revenue_inr - spend_inr) * 1.0 / NULLIF(spend_inr, 0) AS roi
FROM campaigns
ORDER BY roas DESC;
