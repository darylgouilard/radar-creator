"""
This file contains the main code for a radar creator app, deployed onto Streamlit.
"""

# -------------------------------------------------------------------------------------------------

## Necessary imports

import streamlit as st  # Create a front-end for the application
import pandas as pd  # For all things data science-related
from mplsoccer import Radar  # Draw radars
import matplotlib.patheffects as path_effects
import matplotlib.font_manager as fm  # Manage fonts
import matplotlib.pyplot as plt  # Draw plots

# Change resolution of plot
import matplotlib as mpl

mpl.rcParams["figure.dpi"] = 700

# Import components
from components import inputForm, paramList


# Set up radar mosaic
def radar_mosaic(radar_height=0.915, title_height=0.06, figheight=14):
    endnote_height = 1 - title_height - radar_height
    figwidth = figheight * radar_height
    figure, axes = plt.subplot_mosaic(
        [["title"], ["radar"], ["endnote"]],
        gridspec_kw={
            "height_ratios": [title_height, radar_height, endnote_height],
            "bottom": 0,
            "left": 0,
            "top": 1,
            "right": 1,
            "hspace": 0,
        },
        figsize=(figwidth, figheight),
    )
    axes["title"].axis("off")
    axes["endnote"].axis("off")
    return figure, axes


# -------------------------------------------------------------------------------------------------

## Front-end setup

# Set up page configs
st.set_page_config(page_title="Radar creator")

# Create a page title
st.title("Radar creator")

# -------------------------------------------------------------------------------------------------

## User inputs

# Set up dict to store param names and scores in the session state
try:
    if (len(st.session_state.radar_params) == 1) and (
        st.session_state.radar_params[0]["Name"] == ""
    ):
        st.session_state.radar_params.clear()
except AttributeError:
    st.session_state.radar_params = []

# Initialise and display the input form
inputForm.inputForm()

# Initialise and display the param list
paramList.paramList()
