from pathlib import Path
import geopandas as gpd
import pandas as pd
# Load cleaned GPS tracks

tracks_file = Path("database/cleaned_tracks.gpkg")

tracks = gpd.read_file(
    tracks_file,
    layer="clean_gps_tracks"
)

print(f"Clean GPS points loaded: {len(tracks)}")


# Load settlement master list

settlement_file = Path("data/settlement_masterlist/settlement_masterlist.csv")
settlements = pd.read_csv(
    settlement_file
)

print(f"Settlements loaded: {len(settlements)}")
print(settlements.head())
print(settlements.columns)
# Convert settlements to spatial points

settlements_gdf = gpd.GeoDataFrame(
    settlements,
    geometry=gpd.points_from_xy(
        settlements["longitude"],
        settlements["latitude"]
    ),
    crs="EPSG:4326"
)

print(settlements_gdf.head())
print(settlements_gdf.crs)
# Create 500 metre settlement buffers

settlements_projected = settlements_gdf.to_crs(
    "EPSG:32632"
)

settlements_projected["geometry"] = settlements_projected.buffer(500)

print("Settlement buffers created")
# Match GPS points to settlement buffers

tracks_projected = tracks.to_crs(
    "EPSG:32632"
)

visited_points = gpd.sjoin(
    tracks_projected,
    settlements_projected,
    predicate="within",
    how="inner"
)

print(f"GPS points linked to settlements: {len(visited_points)}")
# Identify visited settlements

visited_settlements = visited_points[
    "settlement_id"
].unique()

settlements_gdf["visited"] = (
    settlements_gdf["settlement_id"]
    .isin(visited_settlements)
)

print(
    "Visited settlements:",
    settlements_gdf["visited"].sum()
)

print(
    "Missed settlements:",
    (~settlements_gdf["visited"]).sum()
)
# Export settlement coverage results

output_file = Path("outputs/settlement_coverage.gpkg")

settlements_gdf.to_file(
    output_file,
    layer="settlement_coverage",
    driver="GPKG"
)

print("Settlement coverage layer created successfully")

