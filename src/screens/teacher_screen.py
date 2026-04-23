import time

import streamlit as st

from src.components.dialog_add_photo import add_photos_dialog
from src.components.dialog_create_subject import create_subject_dialogue
from src.components.dialog_share_subject import share_subject_dialog
from src.components.header import header_dashboard
from src.components.Subject_card import subject_card
from src.database.db import (
    check_teacher_exists,
    create_teacher,
    get_teacher_subjects,
    teacher_login,
)
from src.UI.base_layout import style_background_dashboard, style_base_layout


def teacher_screen():
    style_background_dashboard()
    style_base_layout()
    st.markdown(
        """
        <style>
            h2 {
                color: black !important;
            }
            .stTextInput > label {
                color: black !important;
            }
        </style>
        """,
        unsafe_allow_html=True,
    )

    if "teacher_data" in st.session_state:
        teacher_dashboard()
    elif (
        "teacher_login_type" not in st.session_state
        or st.session_state.teacher_login_type == "login"
    ):
        teacher_screen_login()
    elif st.session_state.teacher_login_type == "register":
        teacher_screen_register()


def teacher_dashboard():
    st.markdown(
        """
        <style>
            h3 {
                color: black !important;
            }
            .stTextInput > label {
                color: black !important;
            }
        </style>
        """,
        unsafe_allow_html=True,
    )
    teacher_data = st.session_state.teacher_data

    c1, c2 = st.columns(2, vertical_alignment="center", gap="xxlarge")

    with c1:
        header_dashboard()
    with c2:
        st.subheader(f"""Welcome, {teacher_data["name"]} """)
        if st.button(
            "Logout",
            type="secondary",
            key="loginbackbtn",
            shortcut="control + backspace",
        ):
            st.session_state["is_logged_in"] = False
            del st.session_state.teacher_data
            st.rerun()

    st.space()

    if "current_teacher_tab" not in st.session_state:
        st.session_state.current_teacher_tab = "take_attendance"

    tab1, tab2, tab3 = st.columns(3)
    with tab1:
        type1 = (
            "primary"
            if st.session_state.current_teacher_tab == "take_attendance"
            else "tertiary"
        )
        if st.button(
            "Take Attendance", type=type1, width="stretch", icon=":material/ar_on_you:"
        ):
            st.session_state.current_teacher_tab = "take_attendance"
            st.rerun()

    with tab2:
        type2 = (
            "primary"
            if st.session_state.current_teacher_tab == "manage_subjects"
            else "tertiary"
        )
        if st.button(
            "Manage Subjects",
            type=type2,
            width="stretch",
            icon=":material/book_ribbon:",
        ):
            st.session_state.current_teacher_tab = "manage_subjects"
            st.rerun()

    with tab3:
        type3 = (
            "primary"
            if st.session_state.current_teacher_tab == "attendance_records"
            else "tertiary"
        )
        if st.button(
            "Attendance Records",
            type=type3,
            width="stretch",
            icon=":material/cards_stack:",
        ):
            st.session_state.current_teacher_tab = "attendance_records"
            st.rerun()

    st.divider()

    if st.session_state.current_teacher_tab == "take_attendance":
        teacher_tab_take_attendance()
    if st.session_state.current_teacher_tab == "manage_subjects":
        teacher_tab_manage_subjects()
    if st.session_state.current_teacher_tab == "attendance_records":
        teacher_tab_attendance_records()


def teacher_tab_take_attendance():
    st.markdown(
        """
        <style>
            .stSelectbox > label {
                color: black !important;
            }
        </style>
        """,
        unsafe_allow_html=True,
    )
    teacher_id = st.session_state.teacher_data["teacher_id"]
    st.header("Take Attendance")

    if "attendance_images" not in st.session_state:
        st.session_state.attendance_images = []

    subjects = get_teacher_subjects(teacher_id)

    if not subjects:
        st.warning("You haven't created any subjects yet! Please create one to begin!")
        return

    subject_options = {
        f"{s['name']} - {s['subject_code']}": s["subject_id"] for s in subjects
    }

    col1, col2 = st.columns([3, 1])
    with col1:
        selected_subject_label = st.selectbox(
            "Select Subjects", options=list(subject_options.keys())
        )

    with col2:
        if st.button(
            "Add Photos",
            type="primary",
            icon=":material/photo_prints:",
            width="stretch",
        ):
            add_photos_dialog()

    selected_subject_id = subject_options[selected_subject_label]

    st.divider()


def teacher_tab_manage_subjects():
    teacher_id = st.session_state.teacher_data["teacher_id"]
    col1, col2 = st.columns(2)
    with col1:
        st.header("Manage Subjects", width="stretch")
    with col2:
        if st.button("Add New Subject", width="stretch"):
            create_subject_dialogue(teacher_id)

    # LIST ALL SUBJECTS
    subjects = get_teacher_subjects(teacher_id)
    if subjects:
        for sub in subjects:
            stats = [
                ("👥", "Students", sub["total_students"]),
                ("🕰️", "Classes", sub["total_classes"]),
            ]

        def share_btn():
            if st.button(
                f"Share Code: {sub['name']}",
                key=f"share_{sub['subject_code']}",
                icon=":material/share:",
            ):
                share_subject_dialog(sub["name"], sub["subject_code"])
            st.space()

        subject_card(
            name=sub["name"],
            code=sub["subject_code"],
            section=sub["sections"],
            stats=stats,
            footer_callback=share_btn,
        )
    else:
        st.info("NO SUBJECTS FOUND. CREATE ONE ABOVE")


def teacher_tab_attendance_records():
    st.header("Attendance Records")


def login_teacher(username, password):
    if not username or not password:
        return False
    teacher = teacher_login(username, password)
    if teacher:
        st.session_state.user_role = "teacher"
        st.session_state.teacher_data = teacher
        st.session_state.is_logged_in = True
        return True
    return False


def teacher_screen_login():
    c1, c2 = st.columns(2, vertical_alignment="center", gap="xxlarge")

    with c1:
        header_dashboard()
    with c2:
        if st.button(
            "Go back to Home",
            type="secondary",
            key="loginbackbtn",
            shortcut="control + backspace",
        ):
            st.session_state["login_type"] = None
            st.rerun()

    st.header("Login using password", text_alignment="center")

    st.space()
    st.space()

    teacher_username = st.text_input("Enter username", placeholder="Username")

    teacher_password = st.text_input(
        "Enter password", type="password", placeholder=" Enter Password"
    )

    st.divider()

    btnc1, btnc2 = st.columns(2, gap="large")

    with btnc1:
        if st.button(
            "Login",
            icon=":material/passkey:",
            shortcut="control + enter",
            width="stretch",
        ):
            if login_teacher(teacher_username, teacher_password):
                st.toast("Login successful! Redirecting to dashboard...")
                time.sleep(1)
                st.rerun()
            else:
                st.error("Invalid username or password. Please try again.")

    with btnc2:
        if st.button(
            "Register Instead",
            type="primary",
            icon=":material/passkey:",
            width="stretch",
        ):
            st.session_state.teacher_login_type = "register"
            st.rerun()


def register_teacher(
    teacher_username, teacher_name, teacher_password, teacher_confirm_password
):
    if not teacher_username or not teacher_name or not teacher_password:
        return False, "All fields are required."
    if check_teacher_exists(teacher_username):
        return False, "Username already exists. Please choose another."
    if teacher_password != teacher_confirm_password:
        return False, "Passwords do not match."

    try:
        create_teacher(teacher_username, teacher_password, teacher_name)
        return True, "Registration successful! Please login."
    except Exception:
        return False, "Unexpected error occurred during registration. Please try again."


def teacher_screen_register():
    c1, c2 = st.columns(2, vertical_alignment="center", gap="xxlarge")

    with c1:
        header_dashboard()
    with c2:
        if st.button(
            "Go back to Home",
            type="secondary",
            key="loginbackbtn",
            shortcut="control + backspace",
        ):
            st.session_state["login_type"] = None
            st.rerun()

    st.header("Register as a Teacher", text_alignment="center")

    st.space()
    st.space()

    teacher_username = st.text_input("Enter username", placeholder="Username")

    teacher_name = st.text_input("Enter name", placeholder="Name")

    teacher_password = st.text_input(
        "Enter password", type="password", placeholder=" Enter Password"
    )

    teacher_confirm_password = st.text_input(
        "Confirm password", type="password", placeholder=" Confirm Password"
    )

    st.divider()

    btnc1, btnc2 = st.columns(2, gap="large")

    with btnc1:
        if st.button(
            "Register now",
            icon=":material/passkey:",
            shortcut="control + enter",
            width="stretch",
        ):
            success, message = register_teacher(
                teacher_username,
                teacher_name,
                teacher_password,
                teacher_confirm_password,
            )
            if success:
                st.success(message)
                time.sleep(2)
                st.session_state.teacher_login_type = "login"
                st.rerun()
            else:
                st.error(message)

    with btnc2:
        if st.button(
            "Go back to Login",
            type="primary",
            icon=":material/passkey:",
            width="stretch",
        ):
            st.session_state.teacher_login_type = "login"
            st.rerun()
