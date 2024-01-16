"""
This file contains the code for a radar creator app, deployed by Streamlit.
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


# Function to call to append a new parameter to the session state array
def paramAppend(param_name, param_score):
    # Ignore cases where param_name is empty
    if param_name != "":
        # Create a dict to store each parameter
        param = {"Name": param_name, "Score": param_score}

        # Append the new parameter to the session state array
        st.session_state.radar_params.append(param)


# Display a form to input parameters
with st.form(key="params_input", clear_on_submit=True):
    # Set up columns
    col1, col2 = st.columns([3.25, 0.75])

    # Set up text input field for column 1
    param_name = col1.text_input(label="Parameter name", key="param_name")

    # Set up number input field for column 2
    param_score = col2.number_input(
        label="Score", min_value=0, max_value=5, key="param_score"
    )

    # Set up a button to add names and scores to dict
    submit_button = st.form_submit_button(
        label="Add to radar",
        type="primary",
        on_click=paramAppend(param_name, param_score),
    )

    # Clear param_name and param_score in the session state
    del st.session_state.param_name
    del st.session_state.param_score

# Header for list of params
st.header("List of parameters")

# Initialise blank DataFrame for editable table
df = pd.DataFrame()

# Key for the editable table
try:
    st.session_state.dataEditor_key
    st.session_state.dataEditor_reset
except AttributeError:
    st.session_state.dataEditor_key = 0
    st.session_state.dataEditor_reset = False

# Convert dict to a DataFrame
if st.session_state.dataEditor_reset != True:
    st.session_state.persistent_df = pd.DataFrame(st.session_state.radar_params)
    df = st.session_state.persistent_df

# Display list of params as an editable table
edited_df = st.data_editor(
    df,
    column_config={
        "Score": st.column_config.NumberColumn(min_value=0, max_value=5, step=1)
    },
    hide_index=True,
    key=f"editor_{st.session_state.dataEditor_key}",
)


# Function to reset editable table
def dataEditor_reset():
    st.session_state.dataEditor_key += 1
    st.session_state.dataEditor_reset = True


# Button to clear the editable table
st.button(label="Clear list", type="primary", on_click=dataEditor_reset)
