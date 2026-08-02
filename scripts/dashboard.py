import pandas as pd
import geopandas as gpd
from dash import Dash, html, dcc
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
# LGA CHART
# =============================

lga_chart = px.bar(
    lga_summary,
    x="lga_name",
    y="coverage_percentage",
    text="coverage_percentage",
    title="LGA Coverage (%)"
)

lga_chart.update_traces(
    texttemplate="%{text:.2f}%",
    textposition="outside"
)


# =============================
# WARD CHART
# =============================

ward_chart = px.bar(
    ward_summary,
    x="ward_name",
    y="coverage_percentage",
    text="coverage_percentage",
    title="Ward Coverage (%)"
)

ward_chart.update_traces(
    texttemplate="%{text:.2f}%",
    textposition="outside"
)


# =============================
# SETTLEMENT MAP
# =============================

settlements["latitude"] = settlements.geometry.y
settlements["longitude"] = settlements.geometry.x


# Check available fields
print(settlements.columns)


settlement_map = px.scatter_mapbox(
    settlements,
    lat="latitude",
    lon="longitude",
    title="Settlement Coverage Map",
    zoom=7,
    height=600
)


settlement_map.update_layout(
    mapbox_style="open-street-map"
)



# =============================
# DASH APPLICATION
# =============================

app = Dash(__name__)


app.layout = html.Div([

    html.H1(
        "Campaign Tracking Dashboard",
        style={"textAlign":"center"}
    ),

    html.H3(
        "Geospatial Coverage Analysis",
        style={"textAlign":"center"}
    ),


    html.Hr(),


    html.Div([

        html.Div([
            html.H4("Total GPS Records"),
            html.H2(f"{total_gps:,}")
        ], className="card"),


        html.Div([
            html.H4("Clean GPS Records"),
            html.H2(f"{clean_gps:,}")
        ], className="card"),


        html.Div([
            html.H4("Visited Settlements"),
            html.H2(f"{visited_settlements:,}")
        ], className="card"),


        html.Div([
            html.H4("Coverage"),
            html.H2(f"{coverage_percentage}%")
        ], className="card")


    ],
    style={
        "display":"flex",
        "justifyContent":"space-around"
    }),



    dcc.Graph(
        figure=lga_chart
    ),


    dcc.Graph(
        figure=ward_chart
    ),


    dcc.Graph(
        figure=settlement_map
    )


],
style={
    "margin":"40px"
})



if __name__ == "__main__":
    app.run(debug=True)