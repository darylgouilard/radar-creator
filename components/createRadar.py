"""
This file contains the code for the radar creator component of the app.
"""

# Necessary imports
import streamlit as st  # Everything Streamlit-related
from components import radarFunction  # Functions to plot the radar


# -------------------------------------------------------------------------------------------------


# Main function for the radar creator component
def radarCreator():
    # Header for the component
    st.header("Radar")
    # Button to start creating radar
    createRadar = st.button(label="Create radar", type="primary")

    # If button is clicked,
    if createRadar == True:
        # 1. Check the length of the params list
        # 2a. If it has less than 3 params, display warning message
        if len(st.session_state.radar_params) < 3:
            st.warning("Please add three parameters or more before creating a radar.")
            return
        # 2b. If it has more than 10 params, also display a warning message
        elif len(st.session_state.radar_params) >= 10:
            st.warning(
                "Too many parameters were added. Please clear the list and try again."
            )
            return
        # 3. If it passes both checks, create the radar
        else:
            with st.spinner("Creating radar..."):
                # Call the plotRadar function from radarFunction.py
                radarFunction.plotRadar(
                    st.session_state.persistent_df["Name"].tolist(),
                    st.session_state.persistent_df["Score"].tolist(),
                )
