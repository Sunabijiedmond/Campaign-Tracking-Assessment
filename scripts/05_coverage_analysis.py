from pathlib import Path
import geopandas as gpd
import pandas as pd
# Load settlement coverage layer

coverage_file = Path("outputs/settlement_coverage.gpkg")

settlements = gpd.read_file(
    coverage_file,
    layer="settlement_coverage"
)

print(f"Settlement records loaded: {len(settlements)}")
print(settlements.head())
# Calculate overall coverage statistics

total_settlements = len(settlements)

visited = settlements["visited"].sum()

missed = total_settlements - visited

coverage_percentage = (
    visited / total_settlements
) * 100


print(f"Total settlements: {total_settlements}")
print(f"Visited settlements: {visited}")
print(f"Missed settlements: {missed}")
print(
    f"Coverage percentage: {coverage_percentage:.2f}%"
)
# Ward-level coverage analysis

ward_summary = (
    settlements
    .groupby("ward_name")
    .agg(
        total_settlements=("settlement_id", "count"),
        visited_settlements=("visited", "sum")
    )
    .reset_index()
)

ward_summary["missed_settlements"] = (
    ward_summary["total_settlements"]
    - ward_summary["visited_settlements"]
)

ward_summary["coverage_percentage"] = (
    ward_summary["visited_settlements"]
    / ward_summary["total_settlements"]
    * 100
)


print("\nWard Coverage Summary")
print(ward_summary.head())

# LGA-level coverage analysis

lga_summary = (
    settlements
    .groupby("lga_name")
    .agg(
        total_settlements=("settlement_id", "count"),
        visited_settlements=("visited", "sum")
    )
    .reset_index()
)

lga_summary["missed_settlements"] = (
    lga_summary["total_settlements"]
    - lga_summary["visited_settlements"]
)

lga_summary["coverage_percentage"] = (
    lga_summary["visited_settlements"]
    / lga_summary["total_settlements"]
    * 100
)


print("\nLGA Coverage Summary")
print(lga_summary.head())

# Export analysis tables

outputs = Path("outputs")

outputs.mkdir(exist_ok=True)


ward_summary.to_csv(
    outputs / "ward_coverage_summary.csv",
    index=False
)


lga_summary.to_csv(
    outputs / "lga_coverage_summary.csv",
    index=False
)

print("Coverage summary tables exported successfully")

