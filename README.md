<div align="center">

<img src="https://i.ibb.co/YTYGn5qV/logo.png" alt="SnapClass Logo" width="100"/>

# SnapClass

### AI-Powered Attendance Management System

[![Live on Vercel](https://img.shields.io/badge/Live%20on-Vercel-black?style=for-the-badge&logo=vercel)](https://snap-class-landing-page-mu.vercel.app/)
[![Built with Streamlit](https://img.shields.io/badge/Built%20with-Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)](https://streamlit.io/)
[![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Supabase](https://img.shields.io/badge/Database-Supabase-3ECF8E?style=for-the-badge&logo=supabase&logoColor=white)](https://supabase.com/)

</div>

---

## 🌐 Live Demo

> **🚀 The web app is live! Visit the landing page here:**
> **[https://snap-class-landing-page-mu.vercel.app/](https://snap-class-landing-page-mu.vercel.app/)**

---

## 📌 Overview

**SnapClass** is an intelligent, AI-driven attendance management system designed to eliminate the friction of traditional roll-calls in educational institutions. By leveraging cutting-edge **facial recognition** and **voice recognition** technologies, SnapClass enables teachers to take attendance in seconds — simply by scanning the room — while providing students with a seamless, contactless check-in experience.

Built with a focus on speed, accuracy, and ease of use, SnapClass modernizes the classroom experience for both educators and students.

---

## ✨ Key Features

### 👩‍🏫 For Teachers
- **AI-Powered Face Attendance** — Instantly recognize enrolled students via webcam using deep learning face recognition pipelines.
- **Voice-Based Attendance** — Take attendance through voice identification for an entirely hands-free experience.
- **Subject Management** — Create and manage multiple subjects from a dedicated dashboard.
- **QR Code & Link Sharing** — Generate unique enrollment QR codes and shareable links for students to join subjects effortlessly.
- **Attendance Results Dashboard** — View real-time attendance results after every session.

### 🎓 For Students
- **One-Click Enrollment** — Join subjects by scanning a QR code or clicking a shared enrollment link.
- **Auto-Enrollment Flow** — Smart redirection and auto-enrollment dialog when accessing a subject invite link.
- **Face Registration** — Register face photos to enable AI-based attendance detection.
- **Contactless Check-In** — No manual input required; the AI identifies and marks attendance automatically.

---

## 🧠 Tech Stack

| Layer | Technology |
|---|---|
| **Frontend / UI** | [Streamlit](https://streamlit.io/) |
| **Face Recognition** | [dlib](http://dlib.net/), [face_recognition_models](https://github.com/ageitgey/face_recognition_models) |
| **Voice Recognition** | [Resemblyzer](https://github.com/resemble-ai/Resemblyzer), [Librosa](https://librosa.org/) |
| **Database** | [Supabase](https://supabase.com/) (PostgreSQL) |
| **Authentication** | [bcrypt](https://pypi.org/project/bcrypt/) |
| **QR Code Generation** | [Segno](https://segno.readthedocs.io/) |
| **Image Processing** | [Pillow](https://pillow.readthedocs.io/), [NumPy](https://numpy.org/) |
| **Data Handling** | [Pandas](https://pandas.pydata.org/), [scikit-learn](https://scikit-learn.org/) |
| **Landing Page** | HTML, CSS, JavaScript — Deployed on [Vercel](https://vercel.com/) |

---

## 🗂️ Project Structure

```
SnapClass/
├── app.py                  # Application entry point
├── requirements.txt        # Python dependencies
├── src/
│   ├── screens/
│   │   ├── home_screen.py          # Landing / login screen
│   │   ├── teacher_screen.py       # Teacher dashboard & tabs
│   │   └── student_screen.py       # Student portal
│   ├── components/
│   │   ├── dialog_create_subject.py
│   │   ├── dialog_share_subject.py
│   │   ├── dialog_enrol.py
│   │   ├── dialog_auto_enrol.py
│   │   ├── dialog_add_photo.py
│   │   ├── dialog_attendance_results.py
│   │   ├── dialog_voice_attendance.py
│   │   ├── Subject_card.py
│   │   └── header.py
│   ├── pipelines/
│   │   ├── face_pipeline.py        # Face detection & recognition
│   │   └── voice_pipeline.py       # Voice identification
│   ├── database/                   # Supabase DB interaction layer
│   └── UI/                         # Shared UI utilities
└── .streamlit/                     # Streamlit configuration
```

---

## 🚀 Getting Started

### Prerequisites

- Python 3.10+
- A [Supabase](https://supabase.com/) project with the required schema
- [CMake](https://cmake.org/) and a C++ compiler (required for `dlib`)

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/Ehsaan08-ai/SnapClass.git
   cd SnapClass
   ```

2. **Create and activate a virtual environment**
   ```bash
   python -m venv venv
   # Windows
   venv\Scripts\activate
   # macOS / Linux
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure Supabase secrets**

   Create a `.streamlit/secrets.toml` file:
   ```toml
   [supabase]
   url = "your_supabase_project_url"
   key = "your_supabase_anon_key"
   ```

5. **Run the application**
   ```bash
   streamlit run app.py
   ```

---

## 🔐 Authentication

SnapClass supports two distinct user roles:

- **Teacher** — Can create subjects, manage enrollments, and run AI attendance sessions.
- **Student** — Can enroll in subjects, register their face, and be identified during attendance.

Passwords are securely hashed using **bcrypt** before being stored in the database.

---

## 📄 License

This project is licensed under the [MIT License](LICENSE).

---

<div align="center">

Made with ❤️ by the SnapClass Team

[🌐 Visit Landing Page](https://snap-class-landing-page-mu.vercel.app/)

</div>
