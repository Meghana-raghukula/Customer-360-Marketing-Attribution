# Customer-360-Marketing-Attribution
## Project Overview

The Customer 360 & Marketing Attribution Platform is a data analytics project designed to combine customer information, website activity, and marketing campaign data to generate business insights.

The project uses BigQuery, dbt, Python, and Tableau to transform data, analyze customer behavior, evaluate marketing campaigns, and visualize performance.

## Business Objectives

- Analyze customer behavior and engagement.
- Build a unified customer profile.
- Perform RFM customer analysis.
- Evaluate marketing campaign performance.
- Compare different marketing attribution models.
- Create an interactive Tableau dashboard.

## Technology Stack

| Technology | Purpose |
|---|---|
| Google BigQuery | Data storage and querying |
| dbt | Data transformation and testing |
| Python | Marketing analysis and attribution |
| Tableau | Data visualization and dashboard |
| SQL | Data extraction and transformation |
| GitHub | Version control and documentation |

## Data Sources

- GA4 sample ecommerce dataset from Google BigQuery.
- Synthetic CRM customer dataset.
- Synthetic advertising campaign spend dataset.

**Note:** CRM and advertising data are synthetic. Attribution journeys and revenue calculations are simulated for analytical demonstration.

## Project Workflow

1. Extract website event data from the GA4 sample dataset.
2. Prepare customer and campaign datasets.
3. Store data in Google BigQuery.
4. Transform data using dbt models.
5. Perform customer RFM analysis.
6. Analyze marketing campaigns using Python.
7. Compare First-Touch, Last-Touch, Linear, and Time-Decay attribution models.
8. Visualize campaign performance through Tableau.

## dbt Transformation Models

- `stg_ga4_events.sql`
- `customer_360_profile.sql`
- `customer_rfm.sql`
- `campaign_performance.sql`

dbt tests were executed to validate important fields and customer identifiers.

## Marketing Attribution Models

- First-Touch Attribution
- Last-Touch Attribution
- Linear Attribution
- Time-Decay Attribution

These models help compare how simulated conversion credit is distributed across marketing campaigns.

## Tableau Dashboard

The Tableau dashboard presents campaign performance and marketing insights through KPI metrics and visualizations.

Dashboard screenshots:

- Customer 360 Dashboard
- Attribution Analysis

## Python Analysis

Python scripts used:

- `marketing_attribution.py`
- `attribution_models.py`

These scripts support campaign performance calculations and attribution analysis.

## Project Limitations

- GA4 data comes from a public sample dataset.
- CRM and advertising spend data are synthetic.
- Attribution journeys and revenue are simulated.
- Results demonstrate an analytical workflow and should not be interpreted as actual company marketing performance.

## Future Improvements

- Integrate real-time customer data.
- Implement actual CRM and advertising platform integrations.
- Develop more advanced customer lifetime value analysis.
- Automate data pipelines.
- Improve attribution using real conversion data.

## Author

Data Analytics Project

**Skills Demonstrated:** SQL | Python | BigQuery | dbt | Tableau | Data Analytics | Marketing Attribution
