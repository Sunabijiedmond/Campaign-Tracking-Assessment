# Campaign Tracking Assessment – Geospatial Coverage Analysis

## Project Overview

This project develops an automated geospatial workflow for analysing field campaign activities using GPS tracking data.

The objective is to transform raw GPS movement data into operational intelligence by assessing field coverage, identifying visited and missed settlements, and providing decision-support outputs through GIS analysis and an interactive dashboard.

The workflow includes GPS data ingestion, quality assessment, data cleaning, settlement matching, coverage analysis, spatial visualization, and dashboard development.

---

# Project Objectives

The project aims to:

- Process and analyse GPS tracking records from field teams.
- Assess GPS data quality and identify unreliable observations.
- Clean GPS datasets for accurate spatial analysis.
- Determine settlement visitation status using spatial matching.
- Calculate campaign coverage at settlement, ward, and LGA levels.
- Generate GIS outputs and interactive visual analytics.

---

# Workflow Overview

The complete workflow follows the pipeline below:


Raw GPS Data
|
↓
Data Ingestion
|
↓
GPS Quality Assessment
|
↓
GPS Cleaning
|
↓
Settlement Matching
|
↓
Coverage Analysis
|
↓
GIS Mapping
|
↓
Interactive Dashboard


---

# Technology Stack

## Programming

- Python 3.x

## Python Libraries

- Pandas
- GeoPandas
- Shapely
- Pyogrio
- Plotly
- Dash
- Matplotlib

## GIS Formats

- GeoPackage (.gpkg)
- CSV
- Spatial datasets

---

# Project Structure


Campaign-Tracking-Assessment/

├── database/
│ ├── campaign_tracks.gpkg
│ └── cleaned_tracks.gpkg
│
├── outputs/
│ ├── settlement_coverage.gpkg
│ ├── ward_coverage_summary.csv
│ ├── lga_coverage_summary.csv
│ └── generated maps
│
├── scripts/
│ ├── 01_ingest.py
│ ├── 02_quality_check.py
│ ├── 03_clean_tracks.py
│ ├── 04_settlement_matching.py
│ ├── 05_coverage_analysis.py
│ ├── 06_mapping.py
│ └── dashboard.py
│
├── requirements.txt
│
└── README.md


---

# Processing Workflow

## 1. Data Ingestion

Script:


scripts/01_ingest.py


The script imports raw GPS tracking records and converts them into a spatial dataset.

Output:


database/campaign_tracks.gpkg


---

## 2. GPS Quality Assessment

Script:


scripts/02_quality_check.py


Quality checks include:

- Location accuracy assessment
- Speed anomaly detection
- Duplicate location detection

Results:

- Total GPS records analysed: **956,702**
- Poor accuracy points: **113,079**
- Implausible speed points: **4,702**
- Duplicate locations: **54,121**

---

## 3. GPS Cleaning

Script:


scripts/03_clean_tracks.py


Unreliable observations are removed using defined quality rules.

Results:

- Original records: **956,702**
- Clean GPS records retained: **820,528**

Output:


database/cleaned_tracks.gpkg


---

## 4. Settlement Matching

Script:


scripts/04_settlement_matching.py


Clean GPS records are spatially matched against target settlements to determine whether field teams reached each location.

Results:

- Total settlements analysed: **2,562**
- Visited settlements: **2,483**
- Missed settlements: **79**

---

## 5. Coverage Analysis

Script:


scripts/05_coverage_analysis.py


Coverage is calculated at different administrative levels.

Coverage formula:


Coverage (%) =
Visited Settlements / Total Settlements × 100


Overall campaign coverage:


96.92%


Outputs:

- Ward coverage summary
- LGA coverage summary

---

## 6. GIS Mapping

Script:


scripts/06_mapping.py


The workflow generates spatial outputs showing:

- Settlement coverage status
- Field activity distribution
- Coverage gaps

---

# Dashboard

The project includes an interactive dashboard built using Dash and Plotly.

Run dashboard:

python scripts/dashboard.py

Access:

http://127.0.0.1:8050/


Dashboard features:

- Campaign KPIs
- LGA coverage chart
- Ward coverage chart
- Interactive settlement coverage map
- Coverage summary table

---

# Key Findings

The analysis demonstrates:

- Successful processing of **956,702 GPS observations**.
- Improved data reliability through GPS quality filtering.
- Retention of **820,528 cleaned GPS records**.
- Identification of settlement-level coverage performance.
- Overall campaign coverage of **96.92%**.
- Automated GIS workflow suitable for operational monitoring.

---

# Reproducibility

Install required dependencies:

pip install -r requirements.txt

Run processing workflow:

python scripts/01_ingest.py

python scripts/02_quality_check.py

python scripts/03_clean_tracks.py

python scripts/04_settlement_matching.py

python scripts/05_coverage_analysis.py

python scripts/06_mapping.py

Run dashboard:

python scripts/dashboard.py

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