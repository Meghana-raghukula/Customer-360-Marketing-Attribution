{{ config(materialized='table') }}

SELECT
    user_pseudo_id,
    COUNT(*) AS total_events,
    COUNT(DISTINCT ga_session_id) AS total_sessions,
    MIN(event_day) AS first_visit_date,
    MAX(event_day) AS last_visit_date,
    COUNTIF(event_name = 'purchase') AS total_purchases,
    ANY_VALUE(country) AS country,
    ANY_VALUE(platform) AS platform
FROM {{ ref('stg_ga4_events') }}
GROUP BY user_pseudo_id