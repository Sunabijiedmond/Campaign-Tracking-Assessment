from pathlib import Path
import geopandas as gpd
import matplotlib.pyplot as plt
from matplotlib_scalebar.scalebar import ScaleBar
from datetime import datetime


# =====================================================
# PROJECT INFORMATION
# =====================================================

AUTHOR = "Edmond Sunabiji Waziri"
DATA_SOURCE = "Campaign GPS Tracking Data"
DATE = datetime.now().strftime("%Y-%m-%d")


# =====================================================
# NORTH ARROW FUNCTION
# =====================================================

def add_north_arrow(ax):

    ax.annotate(
        "N",
        xy=(0.08, 0.90),
        xytext=(0.08, 0.78),
        xycoords="axes fraction",
        textcoords="axes fraction",
        ha="center",
        va="center",
        fontsize=14,
        fontweight="bold",
        bbox=dict(
            facecolor="white",
            edgecolor="black",
            boxstyle="round,pad=0.3"
        ),
        arrowprops=dict(
            facecolor="black",
            edgecolor="black",
            width=3,
            headwidth=10
        )
    )


# =====================================================
# FOOTER FUNCTION
# =====================================================

def add_footer():

    plt.figtext(
        0.5,
        0.02,
        f"Source: {DATA_SOURCE} | Author: {AUTHOR} | Date: {DATE}",
        ha="center",
        fontsize=8
    )


# =====================================================
# LOAD SETTLEMENT COVERAGE DATA
# =====================================================

coverage_file = Path(
    "outputs/settlement_coverage.gpkg"
)


settlements = gpd.read_file(
    coverage_file,
    layer="settlement_coverage"
)


print(
    f"Settlements loaded: {len(settlements)}"
)


# Project CRS for accurate scale

if settlements.crs.is_geographic:

    settlements = settlements.to_crs(
        epsg=32632
    )


# =====================================================
# MAP 1: SETTLEMENT COVERAGE MAP
# =====================================================

fig, ax = plt.subplots(
    figsize=(12,10)
)


# Missed settlements

settlements[
    settlements["visited"] == False
].plot(
    ax=ax,
    color="red",
    marker="X",
    markersize=80,
    label="Missed Settlement"
)



# Visited settlements

settlements[
    settlements["visited"] == True
].plot(
    ax=ax,
    color="green",
    marker="o",
    markersize=35,
    label="Visited Settlement"
)



ax.set_title(
    "Campaign Settlement Coverage Assessment",
    fontsize=18,
    fontweight="bold"
)



ax.legend(
    title="Coverage Status",
    loc="lower left",
    frameon=True
)



add_north_arrow(ax)



ax.add_artist(
    ScaleBar(
        1,
        units="m",
        location="lower right"
    )
)



for spine in ax.spines.values():

    spine.set_visible(True)



ax.set_xticks([])
ax.set_yticks([])



add_footer()



plt.savefig(
    "outputs/settlement_coverage_map.png",
    dpi=300,
    bbox_inches="tight"
)



plt.close()



print(
    "Settlement coverage map created successfully"
)



# =====================================================
# LOAD CLEAN GPS TRACKS
# =====================================================

gps_file = Path(
    "database/cleaned_tracks.gpkg"
)


tracks = gpd.read_file(
    gps_file,
    layer="clean_gps_tracks"
)


print(
    f"GPS points loaded: {len(tracks)}"
)



if tracks.crs.is_geographic:

    tracks = tracks.to_crs(
        settlements.crs
    )


# =====================================================
# MAP 2: CAMPAIGN ACTIVITY MAP
# =====================================================

fig, ax = plt.subplots(
    figsize=(14,12)
)



# GPS movement

tracks.plot(
    ax=ax,
    color="blue",
    markersize=0.5,
    alpha=0.15,
    label="GPS Movement"
)



# Missed settlements

settlements[
    settlements["visited"] == False
].plot(
    ax=ax,
    color="red",
    marker="X",
    markersize=120,
    label="Missed Settlement"
)



# Visited settlements

settlements[
    settlements["visited"] == True
].plot(
    ax=ax,
    color="green",
    marker="o",
    markersize=45,
    label="Visited Settlement"
)



# Zoom map to settlement area

xmin, ymin, xmax, ymax = settlements.total_bounds


buffer_x = (xmax - xmin) * 0.08
buffer_y = (ymax - ymin) * 0.08



ax.set_xlim(
    xmin - buffer_x,
    xmax + buffer_x
)



ax.set_ylim(
    ymin - buffer_y,
    ymax + buffer_y
)



ax.set_title(
    "Campaign Field Movement and Settlement Coverage",
    fontsize=18,
    fontweight="bold"
)



ax.legend(
    title="Map Features",
    loc="lower left",
    frameon=True
)



add_north_arrow(ax)



ax.add_artist(
    ScaleBar(
        1,
        units="m",
        location="lower right"
    )
)



for spine in ax.spines.values():

    spine.set_visible(True)



ax.set_xticks([])
ax.set_yticks([])



add_footer()



plt.savefig(
    "outputs/campaign_activity_map.png",
    dpi=300,
    bbox_inches="tight"
)



plt.close()



print(
    "Campaign activity map created successfully"
)