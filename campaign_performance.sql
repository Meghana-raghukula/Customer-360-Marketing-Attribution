{{ config(materialized='table') }}

SELECT
    campaign_id,
    campaign_name,
    channel,
    SUM(ad_spend) AS total_ad_spend,
    SUM(clicks) AS total_clicks,
    SUM(impressions) AS total_impressions,
    SAFE_DIVIDE(SUM(ad_spend), SUM(clicks)) AS cost_per_click,
    SAFE_DIVIDE(SUM(ad_spend), SUM(impressions)) * 1000 AS cost_per_thousand
FROM
    `customer-360-marketing-514015.customer360.ad_spend`
GROUP BY
    campaign_id,
    campaign_name,
    channel