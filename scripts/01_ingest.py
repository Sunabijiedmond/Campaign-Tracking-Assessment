from pathlib import Path
import pandas as pd

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

print(tracks.head())
print(tracks.columns)