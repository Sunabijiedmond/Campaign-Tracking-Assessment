from pathlib import Path
import pandas as pd

import geopandas as gpd
from shapely.geometry import Point

# Project folder
project_path = Path(__file__).resolve().parent.parent

# GPS tracks folder
tracks_folder = project_path / "data" / "tracks"

# Find all GPS track files
track_files = list(tracks_folder.glob("*.csv"))

print(f"Number of track files found: {len(track_files)}")

# Read all GPS files into one table

gps_data = []

for file in track_files:
    df = pd.read_csv(file)
    gps_data.append(df)

tracks = pd.concat(gps_data, ignore_index=True)

print(f"Total GPS records: {len(tracks)}")

# Create spatial points from longitude and latitude

geometry = [
    Point(xy) for xy in zip(tracks["longitude"], tracks["latitude"])
]

tracks_gdf = gpd.GeoDataFrame(
    tracks,
    geometry=geometry,
    crs="EPSG:4326"
)

print(tracks_gdf.head())
print(tracks_gdf.crs)

# Save GPS tracks as GeoPackage

output_path = Path("database/campaign_tracks.gpkg")

tracks_gdf.to_file(
    output_path,
    layer="gps_tracks",
    driver="GPKG"
)

print("Spatial database created successfully")