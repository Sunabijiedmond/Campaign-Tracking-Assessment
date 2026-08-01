from pathlib import Path
import geopandas as gpd
import matplotlib.pyplot as plt

# Load settlement coverage data

coverage_file = Path("outputs/settlement_coverage.gpkg")

settlements = gpd.read_file(
    coverage_file,
    layer="settlement_coverage"
)

print(f"Settlements loaded: {len(settlements)}")
print(settlements.head())
# Create settlement coverage map

fig, ax = plt.subplots(figsize=(10, 10))

# Plot missed settlements
settlements[
    settlements["visited"] == False
].plot(
    ax=ax,
    color="red",
    markersize=25,
    label="Missed settlements"
)

# Plot visited settlements
settlements[
    settlements["visited"] == True
].plot(
    ax=ax,
    color="green",
    markersize=5,
    label="Visited settlements"
)


ax.set_title(
    "Campaign Settlement Coverage Assessment",
    fontsize=14
)

ax.legend()

ax.set_axis_off()


# Save map

output_map = Path(
    "outputs/settlement_coverage_map.png"
)

plt.savefig(
    output_map,
    dpi=300,
    bbox_inches="tight"
)

plt.close()

print("Settlement coverage map created successfully")

# Load cleaned GPS tracks

gps_file = Path(
    "database/cleaned_tracks.gpkg"
)

tracks = gpd.read_file(
    gps_file,
    layer="clean_gps_tracks"
)

print(f"GPS points loaded: {len(tracks)}")

# Create integrated campaign activity map

fig, ax = plt.subplots(figsize=(12, 10))


# Plot GPS movement points
tracks.plot(
    ax=ax,
    color="blue",
    markersize=1,
    alpha=0.3,
    label="GPS movement"
)


# Plot missed settlements
settlements[
    settlements["visited"] == False
].plot(
    ax=ax,
    color="red",
    markersize=40,
    label="Missed settlements"
)


# Plot visited settlements
settlements[
    settlements["visited"] == True
].plot(
    ax=ax,
    color="green",
    markersize=8,
    label="Visited settlements"
)


ax.set_title(
    "Campaign Field Movement and Settlement Coverage",
    fontsize=15
)

ax.legend()

ax.set_axis_off()


output_map = Path(
    "outputs/campaign_activity_map.png"
)


plt.savefig(
    output_map,
    dpi=300,
    bbox_inches="tight"
)

plt.close()


print("Campaign activity map created successfully")