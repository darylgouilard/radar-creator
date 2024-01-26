"""
This file contains the code for the clear list button component of the app.
"""

# Necessary imports
import streamlit as st


# Function to reset editable table
def dataEditor_reset():
    st.session_state.dataEditor_key += 1
    st.session_state.dataEditor_reset = True


def clearListButton():
    # Button to clear the editable table
    st.button(label="Clear list", type="primary", on_click=dataEditor_reset)
