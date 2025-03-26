import streamlit as st
from database import return_responses

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


st.title("Response of the candidate:")
candidate_id = st.session_state["candidate_id"]
st.write(f"Candidate id: {candidate_id}")

result = return_responses(candidate_id=candidate_id)
# print(result)

for res in result:
    st.write("Question:")
    st.write(res[2])
    st.write("Answer:")
    st.write(res[3])