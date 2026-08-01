from pathlib import Path
import geopandas as gpd
import pandas as pd
# Load GPS tracks from GeoPackage

input_file = Path("database/campaign_tracks.gpkg")

tracks = gpd.read_file(
    input_file,
    layer="gps_tracks"
)

print(f"Total GPS points loaded: {len(tracks)}")
print(tracks.head())

# QA Rule 1: Flag poor GPS accuracy

accuracy_limit = 50

tracks["accuracy_flag"] = tracks["accuracy_m"] > accuracy_limit

print(
    "Poor accuracy points:",
    tracks["accuracy_flag"].sum()
)
# QA Rule 2: Flag implausible speeds

speed_limit = 100

tracks["speed_flag"] = tracks["speed_kmh"] > speed_limit

print(
    "Implausible speed points:",
    tracks["speed_flag"].sum()
)
# QA Rule 3: Flag duplicate GPS locations

tracks["duplicate_flag"] = tracks.duplicated(
    subset=["longitude", "latitude"],
    keep=False
)

print(
    "Duplicate location points:",
    tracks["duplicate_flag"].sum()
)

