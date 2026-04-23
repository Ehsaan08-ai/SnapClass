import streamlit as st
from src.database.db import create_subject


@st.dialog("Add New Subject")
def create_subject_dialogue(teacher_id):
    st.write("Enter the details of new subject")
    sub_id = st.text_input("Subject ID", placeholder="CS101")
    sub_name = st.text_input(
        "Subject Name", placeholder="Introduction to Computer Science"
    )
    sub_sec = st.text_input("Sections", placeholder="A")

    if st.button("Add Subject", type="primary", width="stretch"):
        if sub_id and sub_name and sub_sec:
            try:
                create_subject(sub_id, sub_name, sub_sec, teacher_id)
                st.toast("Subject Created Successfully!!")
                st.rerun()
            except Exception as e:
                st.error(f"An Error Occurred {str(e)}")
        else:
            st.warning("Please Fill All the Fields")
