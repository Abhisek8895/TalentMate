import streamlit as st
from database import store_candidate_details
import time
from utils import *

st.set_page_config(page_title="TalentMate", layout="wide", initial_sidebar_state="collapsed")

st.markdown("""
    <style>
        section[data-testid="stSidebar"] {
            display: none;
        }
        div[data-testid="collapsedControl"] {
            visibility: hidden;}
        
    </style>
""", unsafe_allow_html=True)

st.title("TalentMate - AI Hiring Assistant")
st.header("Candidate Information Form")

# Form for input fields
with st.form("candidate_form", clear_on_submit=True):
    name = st.text_input("Full Name")
    email = st.text_input("Email")
    phone = st.text_input("Phone Number")
    experience = st.number_input("Years of Experience", min_value=0, step=1)
    position = st.text_input("Desired Position")
    location = st.text_input("Current Location")
    tech_stack = st.text_area("Tech Stack")

    # Submit button
    submitted = st.form_submit_button("Submit")

if submitted:
    if name and email and phone and position and tech_stack:
        candidate_id = store_candidate_details(name, email, phone, experience, position, location, tech_stack)
        raw_questions = generate_questions(tech_stack)
        # print(raw_questions)
        questions_list = question_cleaning(raw_questions)

        st.session_state['candidate_id'] = candidate_id
        st.session_state['questions_list'] = questions_list

        st.success(f"Candidate details saved successfully! Candidate ID: {candidate_id}")

        st.info("Navigating to the interview page...")

        # Wait for 3 seconds
        time.sleep(3)

        # Redirect to interview page
        st.switch_page("pages/interview.py")

    else:
        st.error("Please fill in all required fields.")
