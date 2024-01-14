from pathlib import Path

import streamlit as st
from PIL import Image


# --- PATH SETTINGS ---
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"
resume_file = current_dir / "assets" / "Abir Hasan Munna.pdf"
profile_pic = current_dir / "assets" / "profile.png"


# --- GENERAL SETTINGS ---
PAGE_TITLE = "Md. Abir Hasan Munna"
PAGE_ICON = "📜"
NAME = "Md. Abir Hasan Munna"
DESCRIPTION = """
Python developer skilled in building robust and scalable applications, proficient in 
front-end tech like ReactJS, TailwindCSS, Zustand etc. Expertise in tools and frameworks
like FastAPI, Scikit-Learn, Pandas, TensorFlow, and OpenCV.
"""
EMAIL = "abirmunna091@gmail.com"
SOCIAL_MEDIA = {
    "LinkedIn": "https://www.linkedin.com/in/munna91",
    "GitHub": "https://github.com/abirmunna",
    "HuggingFace": "https://huggingface.co/abirmunna",
    "Google Scholar": "https://scholar.google.com/citations?user=uCFZ3J0AAAAJ&hl=en",
}
PROJECTS = {    
    "🏆 Road Sign Detection: Project developed with Python and Tensorflow": "https://huggingface.co/spaces/abirmunna/road_sign_recognition",
    "🏆 Dormitory Management: Web-based project developed by PHP": "https://github.com/abirmunna/dorm",
    "🏆 Implementation of MobileNET with gradio to show": "https://huggingface.co/spaces/abirmunna/ML_ui_Mobilenet",
    "🏆 The Fast and the Furious: Developed a High-Performance Blog API with FastAPI": "https://blogapi.abirmunna.me/docs",
    "🏆 Built a RESTful ToDo App with FastAPI and Python": "https://github.com/abirmunna/todo_app",
    "🏆 TaskRunner: An app to open your most used softwares in a single click.": "https://github.com/abirmunna/TaskRunner",
    "🏆 NASA SPACE APPS CHALLENGE 2020 Global Nominee": "https://2020.spaceappschallenge.org/challenges/connect/space-exploration-your-backyard/teams/trojans/project",
    "🏆 GreenBD: An initiative of A.I.T GreeNEX to solve solid waste maagement problem in Bangladesh": "https://youtu.be/u1GK763I1PI",
    "🏆 Smart Home Automation Operated by Bluetooth Expertise (Bangladesh Perspective), Best Paper Award by IRAJ": "https://www.digitalxplore.org/up_proc/pdf/431-15644808681-5.pdf",
    "🏆 Static-gesture word recognition in Bangla sign language using convolutional neural network": "http://telkomnika.uad.ac.id/index.php/TELKOMNIKA/article/view/24096",
}


st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)


# --- LOAD CSS, PDF & PROFIL PIC ---
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()
profile_pic = Image.open(profile_pic)


# --- HERO SECTION ---
col1, col2 = st.columns(2, gap="large")
with col1:
    st.image(profile_pic, width=350)

with col2:
    st.title(NAME)
    st.write(DESCRIPTION)
    st.download_button(
        label=" 📄 Download Resume",
        data=PDFbyte,
        file_name=resume_file.name,
        mime="application/octet-stream",
    )
    st.write("📫", EMAIL)


# --- SOCIAL LINKS ---

st.write('\n')
st.subheader("Professional Profiles")
cols = st.columns(len(SOCIAL_MEDIA))
for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
    cols[index].write(f"[{platform}]({link})")


# --- EXPERIENCE & QUALIFICATIONS ---
st.write('\n')
st.subheader("Experience & Qualifications")
st.write(
    """
- ✔️ Recognized thrice for excellence: Awarded BUP's prestigious Senate Award
- ✔️ Ai enthusiastic, Head of Ai and Data Science teams at A.I.T GreeNEX
- ✔️ 3+ years experience in Machine Learning and Data Science
- ✔️ Conference Speaker and Technical/Scientific Researcher
- ✔️ Co-Founder and CEO of A.I.T GreeNEX
"""
)


# --- SKILLS ---
st.write('\n')
st.subheader("Hard Skills")
st.write(
    """
- 👨‍💻 Programming and Web: Python (sklearn, pandas, numpy, tensorflow, keras, opencv, FastAPI), PHP, HTML, CSS, JavaScript(ReactJS), SQL.
- 📊 Data Visulization: Matplotlib, Plotly, Seaborn, Streamlit, Gradio
- 📚 Modeling: Classic ML, Neural Networks, Time Series, NLP, Computer Vision
- 🗄️ Databases: PostgreSQL, MySQL
- 💾 Operating Systems: Linux(Ubuntu, CentOS), Windows
- 🏭 MLOps: Git, mlflow, Docker.
"""
)


# --- WORK HISTORY ---

st.write('\n')
st.subheader("Work History")
st.write("---")


# --- JOB 1
st.write("🚧", "**Software Engineer | Beacon Pharmaceuticals Limited**")
st.write("06/2023 - Present")


st.write(
    """
- ► Developing the backend of the company's applications using FastAPI.
- ► Working on IoT projects to connect factory machines, various sensors and make production more efficient.
- ► Leveragin AI/ML and computer vision to help the company grow and stay ahead of the competition.

"""
)

# --- JOB 2
st.write("🚧", "**Co-Founder and CEO | A.I.T GreeNEX**")
st.write("09/2020 - 05/2023")



st.write(
    """
- ► Led a team of 25+ developers to develop and deploy smartBin, an innovative IoT product promoting sustainable waste management in GreenBD.
- ► Leveraged expertise in IoT, Python, and data science to drive the development of cutting-edge solutions for real-world challenges.
- ► Fostered a culture of innovation and collaboration, supporting individual growth while driving organizational success.
"""
)

# --- JOB 3
st.write('\n')
st.write("🚧", "**AI Ambassador | SOCIAN Ltd.**")
st.write("05/2021 - 06/2022")
st.write(
    """
- ► Represented their cutting-edge technologies deployed in products and services
- ► Got vigorous technological training and mentorship
- ► Communicated about the technological plans and structure to other ambassadors

"""
)

# --- JOB 4
st.write('\n')
st.write("🚧", "**Pesident | BUP ROBOTICS CLUB**")
st.write("05/2021 - 03/2022")
st.write(
    """
- ► Launched Seminar on Robotics and Ongoing technologies
- ► Led event management teams in World Arduino day by BUP Robotics Club
- ► Led event management teams in MindExperia by BUP Robotics Club
- ► personally taught more than 100 students about Robotics and AI
"""
)



# --- Projects & Accomplishments ---
st.write('\n')
st.subheader("Projects & Accomplishments")
st.write("---")
for project, link in PROJECTS.items():
    st.write(f"[{project}]({link})") 

st.write('\n')
st.subheader("References")
st.write("---")
st.write(":post_office:","Ms. Nandita Barman")
st.write("""
- Asst. Professor, Dept. of ICT, BUP, BD
- Email: nanditabarmandu12@gmail.com
""")
st.write(":post_office:","Dr. M. Arifur Rahman")
st.write("""
- Senior Lecturer, Dept. of CS, NTU, UK
- Email: muhammad.rahman02@ntu.ac.uk
""")
