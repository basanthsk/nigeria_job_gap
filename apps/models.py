import streamlit as st



def app():
    st.title("Data & Model")

    st.write("""

 ## Data

 The project utilized online data sources, such as publicly available resumes, job listings, and curricula information.

 The data collection process involved scraping three key data points with various libraries, such as Selenium, BeautifulSoup, request_html, and similar tools. Focus was placed on job postings across diverse industries, including agriculture, education, legal, healthcare, IT, advertising, and more. A total of 17,650 job records were extracted from local websites.
Resume data were also scraped to gain a deeper understanding and compare the skills required by employers and skills possessed by job applicants. A total of 10,495 applicants' resumes were gathered from multiple public platforms. This allowed a detailed comparison of the skills listed in these resumes against the skills mentioned in the job postings. 
Additionally, in order to identify the root causes of the skill gap, curriculum data was gathered from five post-secondary institutions. This involved obtaining detailed information about the skills taught in specific programs and comparing them to the skills demanded by the job industry. These curriculum insights provided a holistic view of the factors contributing to the skill gap in Ghana.
   

## Behavioral Analysis of the Model 

We employed 15000 samples of data from 21 distinct types of job categories to train the model, which was constructed via a transfer learning approach using the open-source **DistilBERT** transformer developed by researchers at Hugging Face.
We used job requirements and other relevant data to train our final model. Resumes and curriculums were used to make gap predictions on the trained model. The percentage of matching between resumes and job requirements was shown to measure the gap in job supply and demand. All the skills were extracted using SkillNER based on the Spacy library.

Model Limitation: One of the main limitations of the model is the dataset it was trained on. The original dataset had 62 categories, but due to insufficient data in many categories, some of them were combined, resulting in 21 categories. This approach of combining categories can make accurate CV segmentation more difficult. Additionally, the model was trained on an unbalanced dataset, which may lead to bias in certain situations. To overcome this limitation, larger and balanced datasets for each category would allow for more precise CV segmentation and lead to better output.

### The model is scalable for other countries; however, country-specific data will be required to retrain the model.


    """)