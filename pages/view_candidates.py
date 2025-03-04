import streamlit as st
import pandas as pd
from database import get_all_candidates

# Set the page to wide layout
st.set_page_config(layout="wide")

st.title("Candidates")

st.markdown("""
    <style>
        section[data-testid="stSidebar"] {
            display: none;
        }
        div[data-testid="collapsedControl"] {
            visibility: hidden !important;
        }
    </style>
""", unsafe_allow_html=True)

candidates = get_all_candidates()  # Fetch data from DB
if candidates:
    df = pd.DataFrame(candidates, columns=["ID", "Name", "Email", "Phone", "Experience", "Position", "Location", "Tech Stack"])
    st.dataframe(df, use_container_width=True, hide_index = True)  # Expands the table width
else:
    st.warning("No candidates found.")
