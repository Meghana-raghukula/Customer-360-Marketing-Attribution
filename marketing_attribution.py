
import pandas as pd
import numpy as np
import random
from pathlib import Path

# Reproducible simulated customer journeys
random.seed(42)
np.random.seed(42)

base_folder = Path(__file__).resolve().parent.parent
data_folder = base_folder / "data"

campaigns = pd.read_csv(data_folder / "ad_spend.csv")

# Create simulated customer journeys
journeys = []

for customer in range(1, 501):
    number_of_touches = random.randint(1, 5)
    selected = campaigns.sample(number_of_touches)

    revenue = round(random.uniform(50, 1000), 2)

    # Older touchpoints have larger age_days
    ages = sorted(
        [random.randint(0, 30) for _ in range(number_of_touches)],
        reverse=True
    )

    for index, (_, campaign) in enumerate(selected.iterrows()):
        journeys.append({
            "customer_id": f"CUST{customer:05d}",
            "campaign_id": campaign["campaign_id"],
            "campaign_name": campaign["campaign_name"],
            "channel": campaign["channel"],
            "age_days": ages[index],
            "conversion_revenue": revenue
        })

touchpoints = pd.DataFrame(journeys)

# Calculate attribution using four models
results = []

for customer_id, group in touchpoints.groupby("customer_id"):

    group = group.sort_values("age_days", ascending=False)
    revenue = group["conversion_revenue"].iloc[0]
    count = len(group)

    # First-touch: credit the oldest touchpoint
    first = group.iloc[0]
    results.append({
        "model": "First-Touch",
        "campaign_id": first["campaign_id"],
        "campaign_name": first["campaign_name"],
        "channel": first["channel"],
        "attributed_revenue": revenue
    })

    # Last-touch: credit the newest touchpoint
    last = group.iloc[-1]
    results.append({
        "model": "Last-Touch",
        "campaign_id": last["campaign_id"],
        "campaign_name": last["campaign_name"],
        "channel": last["channel"],
        "attributed_revenue": revenue
    })

    # Linear: distribute credit equally
    for _, touch in group.iterrows():
        results.append({
            "model": "Linear",
            "campaign_id": touch["campaign_id"],
            "campaign_name": touch["campaign_name"],
            "channel": touch["channel"],
            "attributed_revenue": revenue / count
        })

    # Time-decay: newer touchpoints receive more credit
    weights = 0.5 ** (group["age_days"].to_numpy() / 7)
    weights = weights / weights.sum()

    for position, (_, touch) in enumerate(group.iterrows()):
        results.append({
            "model": "Time-Decay",
            "campaign_id": touch["campaign_id"],
            "campaign_name": touch["campaign_name"],
            "channel": touch["channel"],
            "attributed_revenue": revenue * weights[position]
        })

# Summarize attribution results
attribution = pd.DataFrame(results)

summary = attribution.groupby(
    ["model", "campaign_id", "campaign_name", "channel"],
    as_index=False
)["attributed_revenue"].sum()

# Add advertising spend
spend = campaigns.groupby(
    ["campaign_id", "campaign_name", "channel"],
    as_index=False
)["ad_spend"].sum()

summary = summary.merge(
    spend,
    on=["campaign_id", "campaign_name", "channel"],
    how="left"
)

summary["ROAS"] = (
    summary["attributed_revenue"] / summary["ad_spend"]
)

summary["ROI_percent"] = (
    (summary["attributed_revenue"] - summary["ad_spend"])
    / summary["ad_spend"]
) * 100

# Save results
output_file = data_folder / "attribution_results.csv"
summary.to_csv(output_file, index=False)

print("Attribution analysis completed successfully!")
print(summary.to_string(index=False))
print(f"\nResults saved to: {output_file}")
print("\nNOTE: Customer journeys and conversion revenue are simulated.")
