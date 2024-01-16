"""
This file contains the code for the input form component of the radar creator app.
"""

# Necessary imports
import streamlit as st


# Function to call to append a new parameter to the session state array
def paramAppend(param_name, param_score):
    # Ignore cases where param_name is empty
    if param_name != "":
        # Create a dict to store each parameter
        param = {"Name": param_name, "Score": param_score}

        # Append the new parameter to the session state array
        st.session_state.radar_params.append(param)


# Main function to initiate the input form on the application
def inputForm():
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
