import json
import streamlit as st
from streamlit_lottie import st_lottie
from PIL import Image
#import pandas as pd

def app():
    #st.set_page_config(page_title="Visualizations and Results", page_icon=":flag_ghana:", layout="wide")

    # ---- LOAD ASSETS ----

    img_job_cat_jobs = Image.open("./visualizations/5.jpg")
    img_job_cat_app = Image.open("./visualizations/6.jpg")
    img_seniority_level_jobs = Image.open("./visualizations/9.jpg")
    img_experience_level_jobs = Image.open("./visualizations/8.jpg")
    
    img_education_level_jobs = Image.open("./visualizations/7.jpg")

    img_skills_match_level = Image.open("./visualizations/10.jpg")
    img_skills_academy_comparison = Image.open("./visualizations/11_str.png")
    img_skills_academy_industry_comparison = Image.open("./visualizations/12_str.png")

    lottie_animation = ("visualizations/lottie_animation.json")

    # Use local CSS
    def local_css(file_name):
        with open(file_name) as f:
            st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


    local_css("style/style.css")


    # ---- HEADER SECTION ----
    with st.container():
        st.subheader("Visualizations and Results")
        text_col, lottie_col = st.columns(([0.6, 0.4]), gap="large")
        with text_col:
            st.write(
            """
            By leveraging the power of natural language processing techniques, 
            we have gained invaluable insights into the factors contributing to the growing gap
            between job demands and the skills available in today's Ghanaian labor market. 
            Through this section, we aim to highlight the key discoveries, trends, and patterns 
            uncovered during our analysis, shedding light on the complex dynamics 
            of this issue and offering potential avenues for bridging the divide.
            """
            )
        with lottie_col:
            with open(lottie_animation,"r") as file:
                url = json.load(file)
            st_lottie(url,
            reverse=True,
            height=200,
            width=200,
            speed=1,
            loop=True,
            quality='high',
            key='Results'
            )

    tab1, tab2 = st.tabs(["EDA", "Gap-img"])
    # ---- TAB 1 ----
    with tab1:
        st.header("Jobs and Job Applicants")
        with st.container():
            st.write("---")
            st.subheader("Available Jobs Categories")
            st.write("##")
            app_column, jobs_column = st.columns(2)
            with app_column:
                st.image(img_job_cat_app)
                expander = st.expander("See explanation")
                expander.write('''The diagram above illustrates the distribution of job applicants by job category. 
                                The demand for jobs is highest in the IT, Finance, and Health categories, which are 
                                similarly the categories with the most job seekers. Other job categories with available 
                                positions include Tourism and Hospitality, Management and Secretarial Services, and 
                                Logistics and Transport.''')
            with jobs_column:
                st.image(img_job_cat_jobs)
                expander = st.expander("See explanation")
                expander.write('''The diagram above displays the distribution of available jobs across different categories. 
                    The majority of available jobs fall under the following categories: Engineering, Finance, IT, Management, 
                    and Health. Other categories are not as well represented on online job portals.''')

        with st.container():
            st.write("---")
            st.subheader("Experience and Seniority Levels")
            st.write("##")
            app_column, jobs_column = st.columns(2)
            with app_column:
                st.image(img_seniority_level_jobs)
                expander = st.expander("See explanation")
                expander.write('''The above chart depicts the distribution of available jobs’ 
                seniority levels. As expected, most of the jobs are entry-level jobs. 
                Mid-Senior and Senior level positions represent the second and third biggest categories. 
                The internships compose less than two per cent of jobs, making it harder for penultimate 
                students to gain the necessary experience and enter the job market.''')
            with jobs_column:
                st.image(img_experience_level_jobs)
                expander = st.expander("See explanation")
                expander.write('''The diagram above illustrates the experience level (in years)
                            employers typically require for available positions. 
                            The majority of jobs (a significant percentage) require 2 to 5 years of experience, 
                            while an additional third of positions demand 5 to 10 years of experience. 
                            Some employers mandate more than 10 years of experience for specific roles. 
                            A mere 3 percent of available jobs are open to employees with less than 2 years of experience. 
                            This leaves new graduates with limited job opportunities and forces them to expend additional 
                            effort to secure their first job.''')
                
        with st.container():
            st.write("---")
            st.subheader("Education level of job seekers and employers")
            st.write("##")
            st.image(img_education_level_jobs)
            expander = st.expander("See explanation")
            expander.write('''The graph above displays a comparison between the level of education that job 
            providers require and the level of education held by job seekers. The number of job seekers with 
            Bachelor's degrees is twice the number of employers requiring this level of education. This trend 
            is also evident for job seekers with Master's degrees and Doctorates. Employers rarely require 
            college diplomas, but approximately a quarter of job seekers mention holding them on their resumes. 
            High school certificates and Technical and Vocational diplomas are not required by employers, 
            but job seekers tend to list them on their resumes.''')
                
    with tab2:
        st.header("Gap Analysis")
        st.write("##")
        with st.container():
            st.write('''The following charts depict the skills gap between the top five
                universities in Ghana and the industry. As a case study, we selected Computer Science programs 
                at each university. We then compared the taught skills to the top 1000 skills required in 
                the IT jobs market.''')
            st.write("---")
            st.subheader("Skills match level of the top five universities in Ghana to IT industry requirements")
            st.write("##")
            st.image(img_skills_match_level)
            expander = st.expander("See explanation")
            expander.write('''Based on the chart provided, it appears that the educational curriculums 
            being taught are not meeting the needs of the job market. Even the most closely aligned program 
            from the University of Mines and Technology is lacking in nearly 50% of the necessary skills. 
            The Bachelor of Science program in Computer Science from KNUST university has the least amount of 
            required skills covered, with less than 10% matching up.''')

        with st.container():
            st.write("---")
            st.subheader("Skills comparison between the top five universities in Ghana for IT programs")
            st.write("##")
            st.image(img_skills_academy_comparison)
            expander = st.expander("See explanation")
            expander.write('''The visualization above illustrates the comparison of the 25 most commonly 
            taught skills among various universities. The University of Mines and Technology has the most 
            comprehensive curriculum, followed by the University of Ghana. As demonstrated in the previous graph, 
            KNUST University has the least favourable outcomes regarding available skills. While subjects 
            such as Math, Operating Systems, and Software Engineering are included in every curriculum, 
            not all universities offer courses in Embedded Systems, Robotics, Artificial Intelligence, 
            and Networking. Therefore, students who are interested in these areas of study should carefully 
            plan their enrollment accordingly.''')
            st.write("---")
            st.subheader("Skills gap between the top five universities in Ghana and IT jobs market")
            st.write("##")
            st.image(img_skills_academy_industry_comparison)
            expander = st.expander("See explanation")
            expander.write('''The chart above displays the discrepancy between the skills taught in university 
            curriculums and those required by the IT job market. The analysis focuses on the top 20 skills in 
            demand. Among these skills, Operating Systems is the only one taught in all five universities, with 
            Computer Science and Software Engineering following closely behind. Project Management ranks as the 
            second most sought-after skill in the IT industry, but only the Ghana Institute of Management offers 
            it as a course for Computer Science students. Additionally, risk management, a crucial component of 
            project management, is not currently included in any Ghanaian university curriculum, which differs 
            from the standards in the United States, where most CS programs cover these topics. Web development 
            skills, including HTML and CSS, are also highly valued in the job market but are rarely included in 
            university programs, if at all.''')

    '''
    with tab3:
        st.header("Gap - interactive")
        st.write("##")

        #read data
        uni_skills = pd.read_csv("data/univercities_skills_comparison.csv")
        uni_ind_skills = pd.read_csv("data/univercities_industry_skills_comparison.csv")

        with st.container():
    '''

