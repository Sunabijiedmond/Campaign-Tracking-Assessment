from pathlib import Path
import geopandas as gpd
# Load GPS tracks

input_file = Path("database/campaign_tracks.gpkg")

tracks = gpd.read_file(
    input_file,
    layer="gps_tracks"
)

print(f"GPS records loaded: {len(tracks)}")
# Remove unreliable GPS observations

clean_tracks = tracks[
    (tracks["accuracy_m"] <= 50) &
    (tracks["speed_kmh"] <= 100)
]

print(f"Clean GPS records remaining: {len(clean_tracks)}")
# Export cleaned GPS tracks

output_file = Path("database/cleaned_tracks.gpkg")

clean_tracks.to_file(
    output_file,
    layer="clean_gps_tracks",
    driver="GPKG"
)

print("Clean GPS database created successfully")