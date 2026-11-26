
{{ config(materialized='view') }}

SELECT
    event_date,
    PARSE_DATE('%Y%m%d', event_date) AS event_day,
    event_timestamp,
    event_name,
    user_pseudo_id,
    platform,
    device_category,
    country,
    ga_session_id,
    page_location,
    first_user_source,
    first_user_medium,
    first_user_campaign
FROM
    `customer-360-marketing-514015.customer360.ga4_events`
WHERE
    user_pseudo_id IS NOT NULL
