"""
This file is used to initialize the session state variables.
"""

# Necessary imports
import streamlit as st  # Everything Streamlit-related
import pandas as pd  # For all things data science-related

# -------------------------------------------------------------------------------------------------


# Initialize session state variables
def sessionStateInit():
    # Set up dict to store param names and scores in the session state
    try:
        if (len(st.session_state.radar_params) == 1) and (
            st.session_state.radar_params[0]["Name"] == None
        ):
            st.session_state.radar_params.clear()
    except AttributeError:
        st.session_state.radar_params = []

    try:
        st.session_state.persistent_df = pd.DataFrame(st.session_state.radar_params)
    except AttributeError:
        st.session_state.persistent_df = pd.DataFrame()

    try:
        if st.session_state.dataEditor_key == 1:
            st.session_state.dataEditor_key = 1
        else:
            st.session_state.dataEditor_key = 0
    except AttributeError:
        st.session_state.dataEditor_key = 0

    try:
        if st.session_state.dataEditor_reset == True:
            st.session_state.dataEditor_reset = True
        else:
            st.session_state.dataEditor_reset = False
    except AttributeError:
        st.session_state.dataEditor_reset = False
