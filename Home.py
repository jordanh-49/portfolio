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

# Path to your image
image_path = "images/profile-pic.jpg"

# Load the image
image = Image.open(image_path)

# Convert the image to base64 to embed in HTML
with open(image_path, "rb") as img_file:
    b64_string = base64.b64encode(img_file.read()).decode()

# Display the image with specific id in HTML
st.markdown(
    f"""
    <div style="text-align:center;">
        <img id="profile-pic" src="data:image/jpeg;base64,{b64_string}" alt="Profile Picture" style="width:175px;height:175px;">
    </div>
    """,
    unsafe_allow_html=True
)

# Apply custom CSS to make the specific image circular
st.markdown(
    """
    <style>
    #profile-pic {
        border-radius: 50%;
        object-fit: cover;
    }
    </style>
    """,
    unsafe_allow_html=True
)

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
link_cols = st.columns(2)
# link_cols = st.columns(3)

# with link_cols[0]:
#     st.markdown("""
#         <div style="text-align:center;">
#             <a href="mailto:jordanh.42.31@gmail.com" target="_blank">
#                 <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/7/7e/Gmail_icon_%282020%29.svg/320px-Gmail_icon_%282020%29.svg.png" alt="Mail Logo" style="width:50px;height:50px;">
#             </a>
#         </div>
#         """, unsafe_allow_html=True)
    
with link_cols[0]:
    st.markdown("""
        <div style="text-align:center;">
            <a href="https://www.linkedin.com/in/jordanhilton49/" target="_blank">
                <img src="https://content.linkedin.com/content/dam/me/business/en-us/amp/brand-site/v2/bg/LI-Bug.svg.original.svg" alt="LinkedIn Logo" style="width:50px;height:50px;">
            </a>
        </div>
        """, unsafe_allow_html=True)
    
# Assuming your image is in 'portfolio/images/github.svg'
encoded_image = get_image_as_base64('images/github.svg')

with link_cols[1]:
    st.markdown(f"""
    <div style="text-align:center;">
        <a href="https://github.com/jordanh-49" target="_blank">
            <img src="data:image/svg+xml;base64,{encoded_image}" alt="GitHub Logo" style="width:50px;height:50px;">
        </a>
    </div>
    """, unsafe_allow_html=True)

st.markdown("")
st.markdown("")

st.write("Data professional at the Orlando Magic working at the intersection between player development and analytics in the NBA. \
    Experienced in leveraging data and working with players/coaches to help improve player on-court performance.")

st.markdown("")

# into cards
cols = st.columns(3)
with cols[0]:
    ui.metric_card(title="Insights", content="Metric Dev", description="R, Python, SQL", key="card1")
with cols[1]:
    ui.metric_card(title="Technical", content="Web Apps", description="Streamlit, R Shiny, Plotly", key="card2")
with cols[2]:
    ui.metric_card(title="Communication", content="Reports", description="Powerpoint, Notion", key="card3")

# with cols[0]:
#     ui.metric_card(title="Development", content="Web Apps", description="Streamlit, R Shiny, Dash", key="card1")
# with cols[1]:
#     ui.metric_card(title="Visualisation", content="BI Tools", description="Tableau, Power BI", key="card2")
# with cols[2]:
#     ui.metric_card(title="Analytics Engineering", content="Orchestration", description="Dagster, DBT", key="card3")


st.divider()
#Experience   
st.header("💼 &nbsp; Experience")

# Job 1
st.subheader("Player Development Analyst")
st.subheader(":gray[Orlando Magic (NBA)]")

st.caption("November 2024 - Present&nbsp;&nbsp;|&nbsp;&nbsp;Full Time")
# st.markdown("- Test")

st.markdown("")

# Job 2
st.subheader("Data Analyst")
st.subheader(":gray[Australian Institute of Sport (AIS)]")

st.caption("Sep 2023 - Nov 2024&nbsp;&nbsp;|&nbsp;&nbsp;Full Time&nbsp;(ASC5)")
st.markdown("- Collaborated with AIS internal staff and National Sporting Organisation stakeholders to optimise 5-8 athlete categorisation frameworks leading to reductions of 10-15% or more in total athletes categorised. Freed up >$50,000 in funds for reallocation into the sporting system to resource athletes with demonstrable medal potential.")
st.markdown("- Led and delivered data products to the entire Australian high performance (HP) sport system including the Daily Performance Environment (DPE) Insights Survey reporting platform (Tableau) enabling insights on the health of the DPE of 50+ NSOs reaching more than 400 athletes and coaches.")
st.markdown("- Liaised with Hockey Australia to convert the Hockey Pathways tool from PowerApps to Streamlit, enhancing user experience and functionality which enabled Hockey Australia to track the longitudinal performance trajectory of 200 pathways athletes.")
st.markdown("- Managed the relationship with and integration of diverse data sources for Paralympics Australia (PA) to eliminate information silos through data pipelines using DBT for SQL transformation and Dagster for orchestration.")
st.markdown("- Partnered with Boccia Australia and PA to develop a data pipeline in Python and Snowflake, automating pre-competition matchup analysis and reducing the time between result and analysis from 1 week post event to instantaneously.")

st.caption("Sep 2022 - Sep 2023&nbsp;&nbsp;|&nbsp;&nbsp;Full Time&nbsp;(ASC4)")
st.markdown("- Worked with and maintained a portfolio of 30 sports including Table Tennis (Para & Able), Winter and Combat sports creating value using innovative, open-sourced tools such as Streamlit to answer more than 100 performance questions.")
st.markdown("- Delivered a full stack data product for the Community Engagement team that centralised the storage and reporting of more than 750 program engagements across 13 programs over a 4-year period.")
st.markdown("- Created an automated data solution for the Career Practitioner Referral Network (CPRN) reducing input time, enabling automatic quarterly reporting, and delivering educational webinars reaching over 80 non-technical practitioners in the network.")
st.markdown("- Validated and developed business cases for agile data analysis tools including Streamlit, Tableau format and design, S3 bucket best practices and Snowflake, integrating them as a part of the AIS data stack.")

st.markdown("")

# Job 3
st.subheader("Data Exploration Consultant")
st.subheader(":gray[National University of Singapore (NUS)]")
st.caption("May 2022 - Jun 2022&nbsp;&nbsp;|&nbsp;&nbsp;Contract")
st.markdown("- Explored data governance best-practices to anonymise Wi-Fi contact tracing data in Python to ensure privacy compliance while maintaining data integrity for future analysis.")
st.markdown("- Optimized SQL stored procedures within Neo4j, leveraging the power of graph databases to achieve a reduction in runtime by over 50%. ")

st.markdown("")

# Job 4
st.subheader("Performance Analyst Intern")
st.subheader(":gray[Victorian Institute of Sport (VIS)]")
st.caption("Oct 2021 - Oct 2022&nbsp;&nbsp;|&nbsp;&nbsp;Part Time")
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
    st.write("Dimensional Modelling")
with col3:
    st.write("Data Orchestration")
    st.write("Docker")
with col4:
    st.write("Git")
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
    st.write("DuckDB")
    st.write("Dplyr (R)")
    
with col5:
    st.write("PDF Plumber")
    st.write("SQL Alchemy")
    st.write("Boto3")
    st.write("Shiny (R)")

st.markdown("")

st.subheader(":gray[Orchestration Tools]")
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.write("Dagster")
with col2:
    st.write("DBT")
with col3:
    st.write("Airflow")

st.markdown("")

st.subheader(":gray[Visualisation Tools]")
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.write("Tableau")
with col2:
    st.write("Power BI")
with col3:
    st.write("Excel")

st.markdown("")

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

# Project 1
col1,col2 = st.columns([1.25,1])
col1.subheader(":gray[NBA Playoff Predictor]")
col2.markdown(f"""
                <a href="https://github.com/jordanh-49/nba_playoff_predictor" target="_blank">
                    <img src="data:image/svg+xml;base64,{encoded_image}" style="padding-top: 10px;" width="25">
                </a>
                """, unsafe_allow_html=True
                )
st.markdown("- Developed a XG boosted tree model to predict the outcome of NBA playoff games and series.")
st.markdown("- [Link to HTML output](https://jordanh-49.github.io/nba_playoff_predictor/)")

st.markdown("")
with st.expander("Tech Stack Used", expanded=True):
    col1, col2, = st.columns(2)
    with col1:
        st.markdown("""
                    <img src="https://www.r-project.org/Rlogo.png" width="25" 
                    style='vertical-align: middle;'> &nbsp; <span style='color: #808496;'>**R/RStudio**</span>
                    """, unsafe_allow_html=True
                    )
    with col2:
        st.markdown("""
                    <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/3/38/HTML5_Badge.svg/1200px-HTML5_Badge.svg.png" width="25" 
                    style='vertical-align: middle;'> &nbsp; <span style='color: #808496;'>**HTML**</span>
                    """, unsafe_allow_html=True
                    )

st.markdown("")

# Project 2
col1,col2 = st.columns([1.25,1])
col1.subheader(":gray[Jobs in Sport Data Pipeline]")
col2.markdown(f"""
                <a href="https://github.com/jordanh-49/sportspeople-scraper" target="_blank">
                    <img src="data:image/svg+xml;base64,{encoded_image}" style="padding-top: 10px;" width="25">
                </a>
                """, unsafe_allow_html=True
                )
st.markdown("- Developed a CI/CD pipeline to extract and ingest sporting job postings from the Sportspeople webpage on a daily schedule.")
st.markdown("")
with st.expander("Tech Stack Used", expanded=True):
    col1, col2, = st.columns(2)
    with col1:
        st.markdown("""
                    <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/c/c3/Python-logo-notext.svg/1869px-Python-logo-notext.svg.png" width="25" 
                    style='vertical-align: middle;'> &nbsp; <span style='color: #808496;'>**Python**</span>
                    """, unsafe_allow_html=True
                    )
    with col2:
        st.markdown(f"""
                    <img src="data:image/svg+xml;base64,{encoded_image}" width="25" 
                    style='vertical-align: middle;'> &nbsp; <span style='color: #808496;'>**Github Actions**</span>
                    """, unsafe_allow_html=True
                    )

st.markdown("")

# Project 2
col1,col2 = st.columns([1.25,1])
col1.subheader(":gray[Personal Portfolio Website]")
col2.markdown(f"""
                <a href="https://github.com/jordanh-49/portfolio" target="_blank">
                    <img src="data:image/svg+xml;base64,{encoded_image}" style="padding-top: 10px;" width="25">
                </a>
                """, unsafe_allow_html=True
                )
st.markdown("- Create a personal portfolio using Streamlit that has a UI/UX built with custom CSS and HTML.")
st.markdown("- Digitise the resume as a means of continuous updating and displaying current analytical experience.")
st.markdown("")
with st.expander("Tech Stack Used", expanded=True):
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.markdown("""
                    <img src="https://streamlit.io/images/brand/streamlit-mark-color.png" width="25" 
                    style='vertical-align: middle;'> &nbsp; <span style='color: #808496;'>**Streamlit**</span>
                    """, unsafe_allow_html=True
                    )  
    with col2:
        st.markdown("""
                    <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/3/38/HTML5_Badge.svg/1200px-HTML5_Badge.svg.png" width="25" 
                    style='vertical-align: middle;'> &nbsp; <span style='color: #808496;'>**HTML**</span>
                    """, unsafe_allow_html=True
                    )
    with col3:
        st.markdown("""
                    <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/6/62/CSS3_logo.svg/2048px-CSS3_logo.svg.png" width="25" 
                    style='vertical-align: middle;'> &nbsp; <span style='color: #808496;'>**CSS**</span>
                    """, unsafe_allow_html=True
                    )
    
    with col4:
        st.markdown(f"""
                    <img src="data:image/svg+xml;base64,{encoded_image}" width="25" 
                    style='vertical-align: middle;'> &nbsp; <span style='color: #808496;'>**Ghub Actions**</span>
                    """, unsafe_allow_html=True
                    )

st.markdown("")

# Project 3
col1,col2 = st.columns([1.25,1])
col1.subheader(":gray[Para Table-Tennis Pipeline]")
col2.markdown(f"""
                <a href="https://github.com/jordanh-49/ipttc" target="_blank">
                    <img src="data:image/svg+xml;base64,{encoded_image}" style="padding-top: 10px;" width="25">
                </a>
                """, unsafe_allow_html=True
                )
st.markdown("- Develop a pipeline for processing match results and player profiles for Para Table-Tennis using Dagster, dbt, and Snowflake.")
st.markdown("- Leverages Python for data extraction from the IPTTC website, transforming this data in Snowflake with RBAC best practices using dbt Core and orchestrating using software-defined assets in Dagster.")
with st.expander("Tech Stack Used", expanded=True):
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.markdown("""
                    <img src="https://dagster.io/images/brand/logos/dagster-primary-mark.svg" width="25" 
                    style='vertical-align: middle;'> &nbsp; <span style='color: #808496;'>**Dagster**</span>
                    """, unsafe_allow_html=True
                    )
    with col2:
        st.markdown("""
                    <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/c/c3/Python-logo-notext.svg/1869px-Python-logo-notext.svg.png" width="25" 
                    style='vertical-align: middle;'> &nbsp; <span style='color: #808496;'>**Python**</span>
                    """, unsafe_allow_html=True
                    )
    with col3:
        st.markdown("""
                    <img src="https://seeklogo.com/images/D/dbt-logo-500AB0BAA7-seeklogo.com.png" width="25" 
                    style='vertical-align: middle;'> &nbsp; <span style='color: #808496;'>**dbt Core**</span>
                    """, unsafe_allow_html=True
                    )
    with col4:
        st.markdown("""
                    <img src="https://companieslogo.com/img/orig/SNOW-35164165.png?t=1634190631" width="25" 
                    style='vertical-align: middle;'> &nbsp; <span style='color: #808496;'>**Snowflake**</span>
                    """, unsafe_allow_html=True
                    )

st.divider()

# Education
st.header("📒 &nbsp; Education")

st.markdown("")

#Esmsys
st.subheader("Master's of Sport Analytics")
st.subheader(":gray[La Trobe University]")
st.caption("Jan 2022 - Nov 2023&nbsp;&nbsp;|&nbsp;&nbsp;GPA 6.9")
st.markdown("- Authored a thesis entitled 'Applications of Rating Systems to Single- and Multi-Competitor Olympic Sports' in partner with the Australian Institute of Sport.")
st.markdown("- Developed advanced skills in R, Python, SQL, relational databases, dimensional modeling, and computer vision through coursework.")
st.markdown("- Recipient of The Provost's Commendation award for sustained academic excellence across a 24 month period.")


st.markdown("")

#Esmsys
st.subheader("Bachelor of Sport and Exercise Science")
st.subheader(":gray[La Trobe University]")
st.caption("Jan 2018 - Nov 2020&nbsp;&nbsp;|&nbsp;&nbsp;GPA 6.5")
st.markdown("- Studied sports Physiology, Biomechanics and Performance Analysis, gaining industry and research experience in exercise prescription and sports analytics.")