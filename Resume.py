import streamlit as st
from pathlib import Path
from PIL import Image

current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"
resume_file = current_dir / "assets" / "Harry Jones Technical PM CV.pdf"
profile_pic = current_dir / "assets" / "profile-pic.jpg"

# --- GENERAL SETTINGS ---
PAGE_TITLE = "Digital CV | Harry Jones"
PAGE_ICON = ":random:"
NAME = "Harry Jones"
DESCRIPTION = """
Technical Project Manager skilled in engineering and telecommunications, with 14 years of experience focused on successful project delivery and effective stakeholder management.
"""

EMAIL = "hwh.jones@gmail.com"
SOCIAL_MEDIA = {
    "LinkedIn": "https://www.linkedin.com/in/harry-jones-97436342/",
    "GitHub": "https://github.com/hwhjones",
}
PROJECTS = {
    "🏆 PersonalPage": "https://github.com/hwhjones/PersonalPage",
    "🏆 JobScrapper": "https://github.com/hwhjones/jobscrape",
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

col1.image(profile_pic, width=280)

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
- ✔️ Over 14 years of experience in technical project management and engineering, specializing in telecommunications and railway signalling
- ✔️ Proven expertise in software integration, system design, and deployment for complex engineering projects
- ✔️ Effective leader in managing cross-functional teams and ensuring timely project delivery
- ✔️ Skills in machine learning with Python to drive informed decision-making, with experience in cloud deployment
"""
)

st.write('\n')
st.subheader("Project Management Skills")
st.write(
    """
- 📈 Project Management, Planning and Execution
- 🤝 Stakeholder Management and Client Interface
- 🔄 System Integration and Third-party Coordination
- 💼 Commercial and Technical Supplier Management
- 🔍 Risk Assessment and Mitigation Strategies
"""
)

# --- SKILLS ---
st.write('\n')
st.subheader("Technical Skills")
st.write(
    """
- 🛠️ Software Development: Python, CI/CD, Version Control (Git)
- 📊 Data Analysis: MS Excel, Pandas
- 🤖 Machine Learning: Regression models, Decision trees, Neural Networks
- 📡 Telecommunications: Fibre Optics, GSM-R, TETRA, RFOF systems
"""
)

st.write('\n')
st.subheader("Professional Experience")


st.write("**Technical Project Manager / Senior Project Engineer | Siemens Mobility**")
st.write("2024 - Present")
st.write(
    """
- ► Leading interface management for Sydney Metro West Sydney Airport, ensuring seamless client and subcontractor engagement.
- ► Overseeing technical deployment and integration for major infrastructure projects.
"""
)

st.write('\n')
st.write("**Technical Project Manager / Senior Project Engineer | Siemens Mobility, New Zealand**")
st.write("2021 - 2024")
st.write(
    """
- ► Managed delivery of signalling systems for Auckland City Rail Link, coordinating with clients and subcontractors.
"""
)

st.write('\n')
st.write("**Technical Project Manager / Senior Project Engineer | Siemens Mobility, UK**")
st.write("2019 - 2021")
st.write(
    """
- ► Interface Management for Crossrail C620, managing third-party integrations and client communications.
"""
)

st.write('\n')
st.write("**Technical Project Manager / Senior Project Engineer | Siemens Mobility, UK**")
st.write("2016 - 2019")
st.write(
    """
- ► Managed telecommunications projects, including design, construction, and commissioning for various rail projects.
"""
)

st.write('\n')
st.write("**Senior Telecommunications Engineer / Tester in Charge | Siemens Mobility, UK**")
st.write("2015 - 2016")
st.write(
    """
- ► Led testing and commissioning for Thameslink London Bridge Area Programme, overseeing network upgrades. 
"""
)

st.write('\n')
st.write("**Project Engineer | Ansaldo STS, Australia**")
st.write("2014 - 2015")
st.write(
    """
- ► Managed engineering and testing for Roy Hill Railway Signalling and Telecommunications Project.
"""
)

st.write('\n')
st.write("**Communications and Control Systems Engineer | Arup, Australia**")
st.write("2010 - 2012")
st.write(
    """
- ► Engaged in project management and systems engineering, including fibre optic and radio design. 
"""
)

# --- Projects & Accomplishments ---
st.write('\n')
st.subheader("Projects")
st.write("---")
for project, link in PROJECTS.items():
    st.write(f"[{project}]({link})")