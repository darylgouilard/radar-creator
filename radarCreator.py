"""
This file contains the main code for a radar creator app, deployed onto Streamlit.
"""

# -------------------------------------------------------------------------------------------------

## Necessary imports

import streamlit as st  # Create a front-end for the application

# Import components
from components import inputForm, paramList, createRadar, sessionStateInit

# -------------------------------------------------------------------------------------------------

## Front-end setup

# Set up page configs
st.set_page_config(page_title="Radar creator")

# Create a page title
st.title("Radar creator")

# -------------------------------------------------------------------------------------------------

## User inputs

# Initialise session state variables
sessionStateInit.sessionStateInit()

# Initialise and display the input form
inputForm.inputForm()

# Initialise and display the param list
paramList.paramList()

# Initialise and display the radar creator
createRadar.radarCreator()
