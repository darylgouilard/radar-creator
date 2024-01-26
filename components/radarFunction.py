"""
This file contains the functions that are used to plot the radar.
"""

# Necessary imports
import streamlit as st  # Everything Streamlit-related
from mplsoccer import Radar, FontManager, grid  # Draw radars

# Change resolution of plot
import matplotlib as mpl

mpl.rcParams["figure.dpi"] = 700

# -------------------------------------------------------------------------------------------------


# Function to set up the font
def importFont(URL):
    font = FontManager(URL)
    return font


# Function to plot the radar
def plotRadar(
    params,
    values,
):
    # -------------------------------------------------------------------------------------------------
    # Set up the radar

    # Arrays to store min and max values for each param
    min_values = []
    max_values = []

    # Retrieve the min and max values for each param
    for param in params:
        min_values.append(min(values))
        max_values.append(max(values))

    # Set up the font
    robotto_thin = importFont(
        "https://raw.githubusercontent.com/googlefonts/roboto/main/src/hinted/Roboto-Thin.ttf"
    )
    robotto_bold = importFont(
        "https://raw.githubusercontent.com/googlefonts/roboto/main/src/hinted/Roboto-Bold.ttf"
    )

    # creating the figure using the grid function from mplsoccer:
    fig, axs = grid(
        figheight=14,
        grid_height=0.915,
        title_height=0.06,
        endnote_height=0.025,
        title_space=0,
        endnote_space=0,
        grid_key="radar",
        axis=False,
    )

    # Draw the radar with the created arrays of data
    radar = Radar(
        params,
        min_values,
        max_values,
        # Round values to integer or keep them as float values
        round_int=[False] * len(params),
        num_rings=6,  # The number of concentric circles (excluding center circle)
        ring_width=0.65,
        center_circle_radius=0.5,
    )

    # -------------------------------------------------------------------------------------------------
    # Plot the radar

    radar.setup_axis(ax=axs["radar"])  # format axis as a radar
    rings_inner = radar.draw_circles(
        ax=axs["radar"], facecolor="#747375", edgecolor="#39353f"
    )  # draw circles
    radar_output = radar.draw_radar(
        values,
        ax=axs["radar"],
        kwargs_radar={"facecolor": "#aa65b2"},
        kwargs_rings={"facecolor": "#66d8ba"},
    )  # draw the radar
    radar_poly, rings_outer, vertices = radar_output
    range_labels = radar.draw_range_labels(
        ax=axs["radar"], fontsize=20, fontproperties=robotto_thin.prop
    )  # draw the range labels
    param_labels = radar.draw_param_labels(
        ax=axs["radar"], fontsize=20, fontproperties=robotto_bold.prop
    )  # draw the param labels
    axs["radar"].scatter(
        vertices[:, 0],
        vertices[:, 1],
        c="#eeb743",
        edgecolors="#070707",
        marker="o",
        s=200,
        zorder=2,
    )

    fig.set_facecolor("#ffffff")  # Set the background colour of the figure
    fig.set_figwidth(13)  # Set the width of the figure
    fig.set_figheight(13)  # Set the height of the figure

    st.pyplot(fig)  # Display the figure
