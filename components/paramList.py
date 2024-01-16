"""
This file contains the code for the parameters list component of the radar creator app.
"""

# Necessary imports
import streamlit as st
import pandas as pd

# Keys for the editable table
st.session_state.dataEditor_key = 0
st.session_state.dataEditor_reset = False


# Function to reset editable table
def dataEditor_reset():
    st.session_state.dataEditor_key += 1
    st.session_state.dataEditor_reset = True


# Main function to initialise the parameters list
def paramList():
    # Header for list of params
    st.header("List of parameters")

    # Initialise blank DataFrame for editable table
    df = pd.DataFrame()

    # Convert dict to a DataFrame
    if st.session_state.dataEditor_reset != True:
        st.session_state.persistent_df = pd.DataFrame(st.session_state.radar_params)
        df = st.session_state.persistent_df
    else:
        st.session_state.radar_params = []
        st.session_state.persistent_df = pd.DataFrame()
        st.session_state.dataEditor_reset = False

    # Display list of params as an editable table
    edited_df = st.data_editor(
        df,
        column_config={
            "Score": st.column_config.NumberColumn(min_value=0, max_value=5, step=1)
        },
        hide_index=True,
        key=f"editor_{st.session_state.dataEditor_key}",
    )

    # Button to clear the editable table
    st.button(label="Clear list", type="primary", on_click=dataEditor_reset)
