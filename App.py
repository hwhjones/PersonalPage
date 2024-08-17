import streamlit as st
from pathlib import Path
from PIL import Image 

current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"
resume_file = current_dir / "assets" / "CV.pdf"
profile_pic = current_dir / "assets" / "profile-pic.jpg"

# --- GENERAL SETTINGS ---
PAGE_TITLE = "Digital CV | Harry Jones"
PAGE_ICON = ":random:"
NAME = "Harry Jones"
DESCRIPTION = """
Senior Data Analyst, assisting enterprises by supporting data-driven decision-making.
"""

EMAIL = "johndoe@email.com"
SOCIAL_MEDIA = {
    "YouTube": "https://youtube.com/c/codingisfun",
    "LinkedIn": "https://linkedin.com",
    "GitHub": "https://github.com",
    "Twitter": "https://twitter.com",
}
PROJECTS = {
    "🏆 Hello": "https://youtu.be/Sb0A9i6d320",
}

st.set_page_config(page_title = PAGE_TITLE, page_icon = PAGE_ICON)

# --- LOAD CSS, PDF & PROFIL PIC ---
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()
profile_pic = Image.open(profile_pic)

# --- LOAD CSS, PDF & PROFIL PIC ---

col1, col2 = st.columns(2, gap = "small")

col1.image(profile_pic, width=320)

col2.title(NAME)
col2.write(DESCRIPTION)
col2.download_button(
    label="Download Resume",
    data=PDFbyte,
    file_name=resume_file.name,
    mime="application/octet-stream"
)
col2.write(f" {EMAIL}")

cols = st.columns(len(SOCIAL_MEDIA))

for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
    cols[index].write(f"[{platform}]({link})")

# --- EXPERIENCE & QUALIFICATIONS ---
st.write('\n')
st.subheader("Experience & Qualifications")
st.write(
    """
- ✔️ Over 14 years of experience in technical project management and engineering, specializing in signalling and telecommunications
- ✔️ Proven expertise in software integration, system design, and deployment for complex engineering projects
- ✔️ Strong skills in data analysis and machine learning with Python to drive informed decision-making
- ✔️ Effective leader in managing cross-functional teams and ensuring timely project delivery
"""
)

# --- SKILLS ---
st.write('\n')
st.subheader("Technical Skills")
st.write(
    """
- 🛠️ Software Development: Python, CI/CD, Version Control (Git)
- 📊 Data Analysis: MS Excel
- 🤖 Machine Learning: Regression models, Decision trees, Neural Networks
- 📡 Telecommunications: Fibre Optics, GSM-R, TETRA, RFOF systems
"""
)

st.write('\n')
st.subheader("Project Management Skills")
st.write(
    """
- 📈 Project Planning and Execution
- 🤝 Stakeholder Management and Client Interface
- 🔄 System Integration and Third-party Coordination
- 🚀 Agile and Traditional Project Management Methodologies
- 💼 Commercial and Technical Supplier Management
- 🔍 Risk Assessment and Mitigation Strategies
"""
)

st.write('\n')
st.subheader("Professional Experience")
st.write(
    """
- 🏗️ Technical Project Manager / Senior Project Engineer, Siemens Mobility (2024 - Present)
  - Leading interface management for Sydney Metro West, ensuring seamless client and subcontractor engagement
  - Overseeing technical deployment and integration for major infrastructure projects

- 🌏 Technical Project Manager / Senior Project Engineer, Siemens Mobility, New Zealand (2021 - 2024)
  - Managed delivery of signalling systems for Auckland City Rail Link, coordinating with clients and subcontractors

- 🇬🇧 Signalling Interface Manager / Senior Project Engineer, Siemens Mobility, UK (2019 - 2021)
  - Delivered interface solutions for Crossrail C620, managing third-party integrations and client communications

- 📡 Senior Project Engineer, Siemens Mobility (2016 - Present)
  - Managed telecommunications projects, including design, construction, and commissioning for various rail projects

- 🔧 Senior Telecommunications Engineer / Tester in Charge (2015 - 2016)
  - Led testing and commissioning for Thameslink London Bridge Area Programme, overseeing network upgrades

- 🚄 Project Engineer, Ansaldo STS, Australia (2014 - 2015)
  - Managed engineering and testing for Roy Hill Railway Signalling and Telecommunications Project

- 🛠️ Communications and Control Systems Engineer, Sydney, Australia (2010 - 2012)
  - Engaged in project management and systems engineering, including smart grid and SCADA opportunities

- 🔬 Research Assistant, Industrial Research Limited, New Zealand (2008 - 2009)
  - Designed data acquisition systems and conducted optical hardware investigations

- 📡 Honours Researcher, Australian National University (2009)
  - Conducted research on channel sounding with software-defined radio
"""
)

# --- Projects & Accomplishments ---
st.write('\n')
st.subheader("Projects & Accomplishments")
st.write("---")
for project, link in PROJECTS.items():
    st.write(f"[{project}]({link})")