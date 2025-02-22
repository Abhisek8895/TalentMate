import streamlit as st
import pandas as pd
from database import get_all_candidates

st.title("Candidates")
st.markdown("""
    <style>
        section[data-testid="stSidebar"] {
            display: none;
        }
        div[data-testid="collapsedControl"] {
            visibility: hidden !important;}
        
    </style>
""", unsafe_allow_html=True)

candidates = get_all_candidates()  # Fetch data from DB
if candidates:
    df = pd.DataFrame(candidates, columns=["ID", "Name", "Email", "Phone", "Experience", "Position", "Location", "Tech Stack"])
    st.dataframe(df, hide_index=True)
else:
    st.warning("No candidates found.")