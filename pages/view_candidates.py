import streamlit as st
import pandas as pd
from database import get_all_candidates

# Set the page to wide layout
st.set_page_config(layout="wide")

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

st.title("View Candidates")

# Fetch all candidates
candidates = get_all_candidates()
if candidates:
    # Display as a table with buttons
    for candidate in candidates:
        candidate_id, name, position, tech_stack = candidate
        col1, col2, col3, col4, col5 = st.columns([2, 2, 2, 2, 1])  # Create columns for alignment
        with col1:
            st.write(candidate_id)
        with col2:
            st.write(f"**{name.strip()}**")
        with col3:
            st.write(position)
        with col4:
            st.write(tech_stack)
        with col5:
            if st.button(f"View Responses", key=candidate_id):
                st.session_state["candidate_id"] = candidate_id
                st.switch_page("pages/responses.py")
else:
    st.write("No candidates to show here")