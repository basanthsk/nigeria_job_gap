import streamlit as st
from streamlit_echarts import st_echarts
import pandas as pd
from io import StringIO
from annotated_text import annotated_text, annotation
from src.utils import load_skill_extractor, create_dfs
from src.utils import clean_text, predict_cat, load_model,get_match
from src.file_uploader import extract_text_from_file,get_file_type
from src. gauge_components import gauge


model = load_model()
skill_extractor = load_skill_extractor()

def app():
    session_items = ['input_text','match','job_cat','rerun']
    if any(session_items) not in st.session_state:
        st.session_state.input_text = ''
        st.session_state.job_cat = ''
        st.session_state.match = 0
        st.session_state.rerun = False 
    
    st.markdown(f"""<h1 
                style= "text-align:-webkit-center;
                font-size: xx-large;
                font-weight: bold; 
                font-family:sans-serif;">
                Compare resume skills to the top skills of industry
                </h1>""", unsafe_allow_html=True)
     
    st.markdown("""<h1 
                style= "text-align:-webkit-center;
                font: caption;
                font-family:sans-serif;">
        Match your resume skills to top industry skills, 
        identify skill gaps, and prioritize development
        </h1>""",unsafe_allow_html=True)
    
  
    
    
                    
    uploaded_file = st.file_uploader("Choose a file",label_visibility = "collapsed")  
    
    if uploaded_file is not None:
            st.session_state.input_text,st.session_state.rerun = extract_text_from_file(uploaded_file)
            
    else:
        st.session_state.rerun = False        
    
              
      
    # st.title("Uploaded resume ")
    # with st.form(key="text_val"):
        # if text is not None:
        #     default_text = text
        # # input_text = st.text_area('', value=default_text, height=200)
        # submit_button = st.form_submit_button(label="Submit")
    
    if st.session_state.rerun:
        with st.spinner('Processing.....'):
            
        
            cls_text = clean_text(st.session_state.input_text)
            prob,st.session_state.job_cat  = predict_cat(model, cls_text)
            annotations = skill_extractor.annotate(cls_text,tresh=1)
            text = annotations['text']
            annotations = annotations['results']    
            df = create_dfs(annotations)
            st.session_state.match = get_match(st.session_state.job_cat ,df)

    
    col1, col2,= st.columns(2)
    gaugeData,option = gauge(value=0)
    with st.form(key='result'):
        if st.session_state.rerun:
            gaugeData[0]['value']=st.session_state.match
            with col1:
                st.markdown(f"""<h1 style= "text-align: -webkit-center;font-family: sans-serif;">Job Category</h1>""", unsafe_allow_html=True)
                html_str = f"""
                            <div  
                            style = "text-align: -webkit-center;
                                    font-size: x-large;
                                    color: #ff4d4f;
                                    font-family: sans-serif;
                                    font-weight: bold;">
                                    {st.session_state.job_cat }
                            </div>
                            """
                
                
                st.markdown(html_str, unsafe_allow_html=True )
            
                # st.title("Probability")
                
                # st.markdown("<h1 style='text-align: center; color: #05A4E9;'>Probability</h1>", unsafe_allow_html=True)
                html_match_str = f"""<div 
                                style = "text-align: -webkit-center ;
                                font-size: x-large; 
                                font-weight: bold; 
                                word-wrap: break-word;">
                                Match percentage with top skills
                                </div>"""
                st.markdown(html_match_str,unsafe_allow_html=True )
                st_echarts(options=option, key="1")

            with col2:
                # st.markdown('-----------')
                df = create_dfs(annotations)
                st.markdown(f"""<h1 style= "text-align: -webkit-center;font-family: sans-serif;">Extracted Skill</h1>""",unsafe_allow_html=True)
                st.write(", \n".join(df))  
        
    
        
    
    #file upload widget
    