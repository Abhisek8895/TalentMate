import streamlit as st
from database import store_responses
st.markdown("""
    <style>
        section[data-testid="stSidebar"] {
            display: none;
        }
        div[data-testid="collapsedControl"] {
            visibility: hidden;}
        
    </style>
""", unsafe_allow_html=True)

st.title("Welcome Interview Page")
try:
    if "candidate_id" in st.session_state and "questions_list" in st.session_state:
        candidate_id = st.session_state["candidate_id"]
        st.write(candidate_id)
        questions = st.session_state["questions_list"]

        st.write(f"### Welcome to the interview, Candidate ID: {candidate_id}")
        st.write("Please answer the following questions:")

        responses = {}

        # Using st.form for structured input
        with st.form("interview_form"):
            for i, question in enumerate(questions, start=1):
                st.write(f"**{i}. {question}**")
                responses[i] = st.text_area(f"Your Answer:", key=f"answer_{i}")

            # Submit button inside form
            submitted = st.form_submit_button("Submit Answers")

        if submitted:
            # Ensure all answers are filled
            if all(responses.values()):
                store_responses(candidate_id, questions, responses)
                st.success("Your answers have been submitted successfully! 🎉")
            else:
                st.error("Please answer all questions before submitting.")
    else:
        st.error("No candidate ID or questions found. Please register first.")
except Exception as e:
    print(e)