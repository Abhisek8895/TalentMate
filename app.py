import streamlit as st
from database import store_candidate_details

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
        st.success(f"Candidate details saved successfully! Candidate ID: {candidate_id}")

    else:
        st.error("Please fill in all required fields.")
