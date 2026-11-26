{{ config(materialized='table') }}

WITH rfm_base AS (
    SELECT
        user_pseudo_id,
        DATE_DIFF(
            (SELECT MAX(event_day) FROM {{ ref('stg_ga4_events') }}),
            last_visit_date,
            DAY
        ) AS recency_days,
        total_purchases AS frequency,
        total_purchases AS monetary_proxy
    FROM {{ ref('customer_360_profile') }}
)

SELECT
    *,
    CASE
        WHEN recency_days <= 30 THEN 'Recent'
        WHEN recency_days <= 90 THEN 'Active'
        ELSE 'Inactive'
    END AS recency_segment,
    CASE
        WHEN frequency >= 3 THEN 'High Frequency'
        WHEN frequency >= 1 THEN 'Low Frequency'
        ELSE 'No Purchases'
    END AS purchase_segment
FROM rfm_base