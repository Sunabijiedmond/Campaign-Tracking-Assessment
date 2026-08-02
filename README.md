# Campaign Tracking Assessment – Geospatial Coverage Analysis

## Project Overview

This project develops an automated GIS workflow for analysing campaign field activities using GPS tracking data.

The workflow processes raw GPS records, performs GPS quality assessment, cleans unreliable observations, matches field movements with target settlements, calculates campaign coverage, and generates cartographic and dashboard outputs.

The objective is to provide evidence-based insights into field performance, campaign reach, and coverage gaps.

---

# Project Objectives

The project aims to:

- Process GPS tracking data collected during field operations.
- Assess GPS data quality and identify unreliable records.
- Clean and prepare GPS movement data for analysis.
- Match field activities against targeted settlements.
- Calculate settlement, ward, and LGA coverage.
- Generate GIS maps and dashboard outputs for decision-making.

---

# Technology Stack

- Python 3.x
- GeoPandas
- Pandas
- Shapely
- Matplotlib
- Plotly
- Dash
- GeoPackage

---

# Workflow

## 1. GPS Data Processing

Raw GPS tracking records were imported and converted into spatial datasets.

Output:

- Campaign GPS database

---

## 2. GPS Quality Assessment

GPS records were evaluated based on:

- Location accuracy
- Duplicate observations
- Movement anomalies

Results:

- Total GPS records analysed: **956,702**
- Poor accuracy records identified: **113,079**
- Implausible movement records identified: **4,702**

---

## 3. GPS Cleaning

Unreliable records were removed to produce a clean operational dataset.

Results:

- Original GPS records: **956,702**
- Clean GPS records retained: **820,528**

---

## 4. Settlement Matching

Clean GPS tracks were spatially analysed against target settlements.

Results:

- Total settlements analysed: **2,562**
- Visited settlements: **2,483**
- Missed settlements: **79**

---

## 5. Coverage Analysis

Campaign coverage was calculated at multiple administrative levels:

- Settlement level
- Ward level
- LGA level

Overall campaign coverage:

**96.92%**

---

# Cartographic Outputs

The project produces professional GIS maps containing:

- Map title
- Legend
- North arrow
- Scale bar
- Data source
- Author information
- Date produced

Generated maps:

1. Settlement Coverage Assessment Map

2. Campaign Field Movement and Settlement Coverage Map

---

# Dashboard

An interactive dashboard was developed using Dash and Plotly.

Dashboard components:

- Total GPS records
- Clean GPS records
- Settlement coverage statistics
- LGA coverage charts
- Interactive spatial visualization

Run dashboard:

```bash
python scripts/dashboard.py

Project Structure
Campaign-Tracking-Assessment/

├── scripts/
│   ├── 01_ingest.py
│   ├── 02_quality_check.py
│   ├── 03_clean_tracks.py
│   ├── 04_settlement_matching.py
│   ├── 05_coverage_analysis.py
│   ├── 06_mapping.py
│   └── dashboard.py
│
├── database/
│   ├── campaign_tracks.gpkg
│   └── cleaned_tracks.gpkg
│
├── outputs/
│   ├── settlement_coverage.gpkg
│   ├── settlement_coverage_map.png
│   ├── campaign_activity_map.png
│   ├── ward_coverage_summary.csv
│   └── lga_coverage_summary.csv
│
├── requirements.txt
└── README.md
Key Findings

The analysis demonstrates:

High campaign reach with 96.92% settlement coverage.
Successful GPS data validation and cleaning.
Automated identification of missed settlements.
Reproducible GIS workflow for operational monitoring.

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