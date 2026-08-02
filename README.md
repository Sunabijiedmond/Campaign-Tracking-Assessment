Campaign Tracking Assessment – Geospatial Coverage Analysis
Project Overview

This project develops an automated geospatial workflow for analysing campaign field activities using GPS tracking data.

The workflow processes raw GPS records, performs quality checks, cleans unreliable observations, matches field movements with target settlements, calculates campaign coverage, and generates spatial visualization outputs.

The objective is to provide an evidence-based understanding of field performance and identify areas requiring follow-up.
Objectives

The project aims to:

Process and analyse GPS tracking data from field teams.
Identify GPS data quality issues.
Remove unreliable GPS observations.
Link field movements to targeted settlements.
Measure settlement visitation and campaign coverage.
Generate GIS outputs for operational decision-making.

Technology Stack
Python 3.x
GeoPandas
Pandas
Shapely
Matplotlib
Pyogrio
GeoPackage

Workflow
1. GPS Quality Assessment

GPS records are evaluated based on:

Location accuracy
Movement speed anomalies
Duplicate locations

Quality assessment results:

Total GPS points analysed: 956,702
Poor accuracy points identified: 113,079
Implausible speed points identified: 4,702
Duplicate location points identified: 54,121

2. GPS Cleaning

Quality filters are applied to remove unreliable observations.

Results:

Original GPS records: 956,702
Clean GPS records retained: 820,528

Output:

Cleaned GPS dataset (cleaned_tracks.gpkg)

3. Settlement Matching

Clean GPS records are spatially matched against target settlement locations using GIS-based proximity analysis.

Results:

Total settlements analysed: 2,562
Visited settlements: 2,483
Missed settlements: 79
4. Coverage Analysis

Settlement coverage was calculated at multiple administrative levels:

Settlement level
Ward level
LGA level

Overall campaign coverage:

96.92%

Outputs:

Ward coverage summary
LGA coverage summary

5. Spatial Visualization

The workflow generates GIS maps showing:

Settlement visitation status
Field movement patterns
Coverage gaps

Generated outputs:

Settlement Coverage Map
Campaign Activity Map

Project Structure

Campaign-Tracking-Assessment/

├── scripts/
│   ├── 02_quality_check.py
│   ├── 03_clean_tracks.py
│   ├── 04_settlement_matching.py
│   ├── 05_coverage_analysis.py
│   └── 06_mapping.py
│
├── outputs/
│   ├── settlement_coverage_map.png
│   ├── campaign_activity_map.png
│   ├── ward_coverage_summary.csv
│   └── lga_coverage_summary.csv
│
├── database/
│
├── requirements.txt
└── README.md

Key Findings

The analysis demonstrates:

High campaign reach with 96.92% settlement coverage.
Successful validation and cleaning of GPS field data.
Automated identification of coverage gaps.
A reproducible GIS workflow for monitoring field operations.

Running the Workflow

Install required packages:
pip install -r requirements.txt
Run the processing workflow:
python scripts/02_quality_check.py
python scripts/03_clean_tracks.py
python scripts/04_settlement_matching.py
python scripts/05_coverage_analysis.py
python scripts/06_mapping.py

# AI Use Disclosure

## AI Tool Used

- OpenAI ChatGPT

## How AI Was Used

AI was used as an assistant throughout this assessment. Specifically, it was used for:

- Assisting with debugging runtime errors and interpreting error messages.
- Reviewing and improving the project documentation (README).
- ## My Contribution

I completed the implementation by:

- validating each script.
- Debugging and resolving issues encountered during execution.
- Verifying outputs, maps, and coverage statistics.
- - reviewing all code before committing it.


Author

Edmond Sunabiji Waziri