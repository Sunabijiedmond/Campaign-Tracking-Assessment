import pandas as pd
import geopandas as gpd
from dash import Dash, html, dcc, dash_table
import plotly.express as px


# =============================
# LOAD DATA
# =============================

ward_summary = pd.read_csv(
    "outputs/ward_coverage_summary.csv"
)

lga_summary = pd.read_csv(
    "outputs/lga_coverage_summary.csv"
)

# Sort performance rankings
ward_summary = ward_summary.sort_values(
    "coverage_percentage",
    ascending=False
)

lga_summary = lga_summary.sort_values(
    "coverage_percentage",
    ascending=False
)


settlements = gpd.read_file(
    "outputs/settlement_coverage.gpkg"
)

settlements = settlements.to_crs(epsg=4326)


print("Ward records:", len(ward_summary))
print("LGA records:", len(lga_summary))
print("Settlement records:", len(settlements))


# =============================
# KPI VALUES
# =============================

total_gps = 956702
clean_gps = 820528
visited_settlements = 2483
coverage_percentage = 96.92


# =============================
# LGA COVERAGE CHART
# =============================

lga_chart = px.bar(
    lga_summary,
    x="lga_name",
    y="coverage_percentage",
    text="coverage_percentage",
    title="LGA Coverage Performance (%)"
)

lga_chart.update_traces(
    texttemplate="%{text:.2f}%",
    textposition="outside"
)


lga_chart.update_layout(
    xaxis_title="LGA",
    yaxis_title="Coverage (%)"
)


# =============================
# WARD COVERAGE CHART
# =============================

ward_chart = px.bar(
    ward_summary,
    x="ward_name",
    y="coverage_percentage",
    text="coverage_percentage",
    title="Ward Coverage Performance (%)"
)

ward_chart.update_traces(
    texttemplate="%{text:.2f}%",
    textposition="outside"
)


ward_chart.update_layout(
    xaxis_title="Ward",
    yaxis_title="Coverage (%)"
)


# =============================
# SETTLEMENT MAP
# =============================

settlements["latitude"] = settlements.geometry.y
settlements["longitude"] = settlements.geometry.x


settlement_map = px.scatter_map(
    settlements,
    lat="latitude",
    lon="longitude",
    color="visited",
    hover_name="settlement_name",
    hover_data=[
        "ward_name",
        "lga_name",
        "settlement_type",
        "visited"
    ],
    title="Settlement Coverage Status",
    zoom=7,
    height=600
)


settlement_map.update_layout(
    map_style="open-street-map"
)


# =============================
# LGA TABLE
# =============================

lga_table = dash_table.DataTable(

    data=lga_summary.to_dict("records"),

    columns=[
        {
            "name": column.replace("_", " ").title(),
            "id": column
        }
        for column in lga_summary.columns
    ],

    page_size=10,

    style_table={
        "overflowX": "auto"
    },

    style_cell={
        "textAlign": "center",
        "padding": "10px"
    },

    style_header={
        "fontWeight": "bold"
    }

)



# =============================
# DASH APPLICATION
# =============================

app = Dash(__name__)


app.layout = html.Div([


    html.H1(
        "Campaign Tracking Dashboard",
        style={
            "textAlign": "center"
        }
    ),


    html.H3(
        "Geospatial Coverage Analysis",
        style={
            "textAlign": "center"
        }
    ),


    html.P(
        [
            "GPS-based monitoring of campaign field activities, settlement visits and coverage performance.",
            html.Br(),
            "Developed by Edmond Sunabiji Waziri | GIS & Geospatial Analyst"
        ],
        style={
            "textAlign": "center"
        }
    ),


    html.Hr(),


    # KPI SECTION

    html.Div([


        html.Div([
            html.H4("Total GPS Records"),
            html.H2(f"{total_gps:,}")
        ],
        className="card"),



        html.Div([
            html.H4("Clean GPS Records"),
            html.H2(f"{clean_gps:,}")
        ],
        className="card"),



        html.Div([
            html.H4("Visited Settlements"),
            html.H2(f"{visited_settlements:,}")
        ],
        className="card"),



        html.Div([
            html.H4("Coverage"),
            html.H2(f"{coverage_percentage}%")
        ],
        className="card")


    ],

    style={
        "display": "flex",
        "justifyContent": "space-around",
        "marginBottom": "40px"
    }),



    # VISUAL ANALYSIS

    dcc.Graph(
        figure=lga_chart
    ),


    dcc.Graph(
        figure=ward_chart
    ),


    dcc.Graph(
        figure=settlement_map
    ),



    html.H2(
        "LGA Coverage Summary"
    ),


    lga_table



],

style={
    "margin": "40px"
})



# =============================
# RUN DASHBOARD
# =============================

if __name__ == "__main__":

    app.run(debug=True)