import streamlit as st
import streamlit_shadcn_ui as ui
from PIL import Image
import base64

def get_image_as_base64(path):
    with open(path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode()

st.set_page_config(
    page_title="Jordan Hilton | Portfolio",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# Add Google Fonts link to the HTML header
google_fonts_link = '<link href="https://fonts.googleapis.com/css2?family=Poppins:wght@100;200;300;400;500;600;700;800;900&display=swap" rel="stylesheet">'
st.markdown(google_fonts_link, unsafe_allow_html=True)


# Use custom CSS to set the font to Roboto and make it bold
html_code = """
<style>
    h1 {
        font-family: 'Poppins';
        font-weight: 600;
        letter-spacing: -2px;
        font-size: 80px;
        line-height: 0.9em;
    }
    streamlit-expanderHeader>st-emotion-cache-ompuv2>p{
        color: red;
    }
    p, h3, h2, li{
        font-family: 'Poppins';
    }
    /* Media query for larger screens, further adjust line height */
    @media screen and (max-width: 1200px) {
    h1 {
        line-height: 0.6;
    }
    @media screen and (max-width: 768px) {
    h1 {
        line-height: 0.8;
        font-size: 45px;
    }
}
</style>
"""

# Render the HTML code to apply the styling
st.markdown(html_code, unsafe_allow_html=True)

st.markdown("""
    <div style="text-align:center;">
        <img src="https://media.licdn.com/dms/image/C4D03AQE7AI4ND4OHoA/profile-displayphoto-shrink_200_200/0/1652921990290?e=1710979200&v=beta&t=oWx3aPqyVwShLlL42I2P9hgjuUhgGF01rx5uRPSG0N0" alt="Profile Picture" style="width:175px;height:175px;border-radius:50%;">
    </div>
    """, unsafe_allow_html=True)

st.markdown("""
    <style>
    .centered-title-text {
        text-align: center;
        font-size: 85px; /* Adjusted font size of st.title */
        font-weight: bold;
        border-bottom: 2px solid white; /* White line under text */
        padding-bottom: 10px; /* Space between text and line */
    }
    </style>
    <p class="centered-title-text">Jordan Hilton</p>
    """, unsafe_allow_html=True)

# st.markdown("")
link_cols = st.columns(3)

with link_cols[0]:
    st.markdown("""
        <div style="text-align:center;">
            <a href="mailto:jordanh.42.31@gmail.com" target="_blank">
                <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/7/7e/Gmail_icon_%282020%29.svg/320px-Gmail_icon_%282020%29.svg.png" alt="Mail Logo" style="width:50px;height:50px;">
            </a>
        </div>
        """, unsafe_allow_html=True)
    
with link_cols[1]:
    st.markdown("""
        <div style="text-align:center;">
            <a href="https://www.linkedin.com/in/jordanhilton49/" target="_blank">
                <img src="https://content.linkedin.com/content/dam/me/business/en-us/amp/brand-site/v2/bg/LI-Bug.svg.original.svg" alt="LinkedIn Logo" style="width:50px;height:50px;">
            </a>
        </div>
        """, unsafe_allow_html=True)
    
# Assuming your image is in 'portfolio/images/github.svg'
encoded_image = get_image_as_base64('images/github.svg')

with link_cols[2]:
    st.markdown(f"""
    <div style="text-align:center;">
        <a href="https://github.com/jordanh-49" target="_blank">
            <img src="data:image/svg+xml;base64,{encoded_image}" alt="GitHub Logo" style="width:50px;height:50px;">
        </a>
    </div>
    """, unsafe_allow_html=True)

st.markdown("")
st.markdown("")

st.write("Data professional at the Australian Institute of Sport working between the intersection of Olympic sports and high performance. \
        Experienced in leveraging data visualisation and BI tools to drive our understanding of human performance, seeking an environment \
        focused on continuous improvement and change in the sports analytics space.")

st.markdown("")

# into cards
cols = st.columns(3)
with cols[0]:
    ui.metric_card(title="Development", content="Web Apps", description="Streamlit, R Shiny, Dash", key="card1")
with cols[1]:
    ui.metric_card(title="Visualisation", content="BI Tools", description="Tableau, Power BI", key="card2")
with cols[2]:
    ui.metric_card(title="Sports Analytics", content="HP Sport", description="Performance Analysis", key="card3")


st.divider()
#Experience   
st.header("💼 &nbsp; Experience")

# Job 1
st.subheader("Data Analyst")
st.subheader(":gray[Australian Institute of Sport (AIS)]")
st.caption("Sep 2023 - Present&nbsp;&nbsp;|&nbsp;&nbsp;Full Time&nbsp;(ASC5)")
st.caption("Sep 2022 - Sep 2023&nbsp;&nbsp;|&nbsp;&nbsp;Full Time&nbsp;(ASC4)")
st.markdown("- Lead and deliver data products to the entire HP System including the DPE Insights Survey as a part of the 2032+ Strategy.")
st.markdown("- Building end-to-end data products from input to output for Olympic and Paralympic sporting programs including Table Tennis (Para & Able), Winter (Aerial Skiing) and Combat sports.")
st.markdown("- Created an automated data solution for the Career Practitioner Referral Network (CPRN) reducing input time and driving engagement of over 80 practitioners in the network.")
st.markdown("- Delivered a full stack data product for the Community Engagement team driving key operational insights and improving the data literacy of non-technical audiences.")

st.markdown("")

# Job 2
st.subheader("Data Exploration Consultant")
st.subheader(":gray[National University of Singapore (NUS)]")
st.caption("May 2022 - Jun 2022&nbsp;&nbsp;|&nbsp;&nbsp;Contract")
st.markdown("- Explored data governance best-practices to anonymise Wi-Fi contact tracing data in Python to ensure privacy compliance while maintaining data integrity for future analysis.")
st.markdown("- Optimized SQL stored procedures within Neo4j, leveraging the power of graph databases to achieve a reduction in runtime by over 50%. ")

st.markdown("")

# Job 3
st.subheader("Performance Analyst Intern")
st.subheader(":gray[Victorian Institute of Sport (VIS)]")
st.caption("May 2023 - Jun 2023&nbsp;&nbsp;|&nbsp;&nbsp;Part Time")
st.markdown("- Coordinated capture and alignment of vision with spatial data in R to produce match reports in real time for coaching staff.")
st.markdown("- Created a web scraping solution for ingesting and storing Netball match statistics in Python.")
st.markdown("- Developed HUDL code windows for efficient data entry in Canoe Slalom, Netball and Hockey.")

st.divider()

#Skills
st.header("🛠 &nbsp; Skills")

st.subheader(":gray[Programming]")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.write("Python")
    st.write("HTML")
with col2:
    st.write("R")
    st.write("CSS")
with col3:
    st.write("SQL")
with col4:
    st.write("Cypher")
    
st.markdown("")

st.subheader(":gray[General]")
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.write("Data Visualization")
    st.write("Web Scraping")
with col2:
    st.write("App Development")
    st.write("Statistical Modelling")
with col3:
    st.write("Git")
    st.write("Docker")
with col4:
    st.write("Bayesian Statistics")
    st.write("CI/CD")

st.markdown("")

st.subheader(":gray[Libraries and Frameworks]")
col1, col2, col3, col4, col5 = st.columns(5)

with col1:
    st.write("Streamlit")
    st.write("Matplotlib")
    st.write("Plotly")
    st.write("ggplot2 (R)")
with col2:
    st.write("Pandas")
    st.write("Numpy")
    st.write("Polars")
    st.write("Tidyverse (R)")
with col3:
    st.write("BeautifulSoup")
    st.write("Requests")
    st.write("OpenCV")
    st.write("Tidymodels (R)")
with col4:
    st.write("Snowpark")
    st.write("Jupyter")
    st.write("Posit")
    st.write("Dplyr (R)")
    
with col5:
    st.write("PDF Plumber")
    st.write("SQL Alchemy")
    st.write("Boto3")
    st.write("Shiny (R)")

st.markdown("")

st.subheader(":gray[Visualization Tools]")
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.write("Tableau")
with col2:
    st.write("Power BI")
with col3:
    st.write("Excel")

st.subheader(":gray[Databases]")
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.write("Snowflake")
with col2:
    st.write("MySQL")
with col3:
    st.write("S3 Bucket")
with col4:
    st.write("Azure Data Studio")

st.divider()

# Project Section
st.header("🚀 &nbsp; Projects")

# Salary Prediction Engine
st.subheader(":gray[Jobs in Sport Data Pipeline]")
st.markdown("- Developed a CI/CD pipeline to extract and ingest sporting job postings from the Sportspeople webpage on a daily schedule.")
st.markdown("- Created a real-time job search and analytics application in Streamlit designed for users to explore trends in the salaries and job type data.")

st.markdown("")

with st.expander("Tech Stack Used"):

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.write("**:gray[Python]**")
    with col2:
        st.write("**:gray[Github Actions]**")
    with col3:
        st.write("**:gray[Streamlit]**")
    with col4:
        st.write("**:gray[Plotly]**")

# Smart Chat Insights
st.subheader(":gray[Project 2]")
st.markdown("- Dot point 1.")
st.markdown("- Dot point 2.")

st.markdown("")

with st.expander("Tech Stack Used"):

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.write("**:gray[LLM]**")
        st.write("**:gray[Streamlit]**")
    with col2:
        st.write("**:gray[Vector Database]**")
        st.write("**:gray[Knowledge Graph]**")
    with col3:
        st.write("**:gray[SpaCy]**")
    with col4:
        st.write("**:gray[Hugging Face]**")

# Admission Management System
st.subheader(":gray[Project 3]")
st.markdown("- Dot point 1.")
st.markdown("- Dot point 2.")

st.markdown("")

with st.expander("Tech Stack Used"):

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.write("**:gray[PHP]**")
        st.write("**:gray[HTML]**")
    with col2:
        st.write("**:gray[Bootstrap]**")
        st.write("**:gray[CSS]**")
    with col3:
        st.write("**:gray[MySQL]**")
    with col4:
        st.write("**:gray[Javascript]**")

# Education
st.header("📒 &nbsp; Education")

st.markdown("")

#Esmsys
st.subheader("Master's of Sport Analytics")
st.subheader(":gray[La Trobe University]")
st.caption("Jan 2022 - Nov 2023&nbsp;&nbsp;|&nbsp;&nbsp;GPA 6.9")
st.markdown("- Authored a thesis entitled 'Applications of Rating Systems to Single- and Multi-Competitor Olympic Sports' in partner with the Australian Institute of Sport.")
st.markdown("- Developed advanced skills in R, Python, SQL, relational databases, dimensional modeling, and computer vision through coursework.")

st.markdown("")

#Esmsys
st.subheader("Bachelor of Sport and Exercise Science")
st.subheader(":gray[La Trobe University]")
st.caption("Jan 2018 - Nov 2020&nbsp;&nbsp;|&nbsp;&nbsp;GPA 6.5")
st.markdown("- Studied sports Physiology, Biomechanics and Performance Analysis gaining industry and research experience in exercise prescription and sports analytics.")


