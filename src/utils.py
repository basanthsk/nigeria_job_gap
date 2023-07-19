import sys
import subprocess
import streamlit as st
import numpy as np
import ast
# from annotated_text import annotation
import collections
import ktrain
import pandas as pd
import os
import neattext.functions as nfx


label_path = ("./data/labels.txt")
top_skills= ("./data/top_50_hard_skills.csv")

cols = ['cat', 'code']
label_df = pd.read_csv(label_path, names=cols, header=0)
skcols = ['cat','skills']
top_skill_df = pd.read_csv(top_skills, names=skcols, header=0)


def default_text():
    with open("./data/sample.txt", 'r') as fs:
        text = fs.read()
    return text

# @st.cache(allow_output_mutation=True,suppress_st_warning=True)
# def load_model():
#     model_path = "./models/distilbert/"
#     model = ktrain.load_predictor(model_path)
#     return model

@st.cache(allow_output_mutation=True,suppress_st_warning=True)
def load_model():
    filepath = "./models/distilbert/tf_model.h5"
    model_path = "./models/distilbert/"
    
	# folder exists?
	
    if not os.path.exists(model_path):
    # create folder
        os.mkdir(model_path)
	
	# file exists?
    if not os.path.exists(filepath):
		# download file
		
        download_file_from_google_drive(id='1Wpld2YwnwjSlpqar-65a0cYTr17QZcey', destination=filepath)
	
	# load model
    model = ktrain.load_predictor(model_path)
    return model



@st.cache(allow_output_mutation=True, suppress_st_warning=True)
def load_skill_extractor():
    # This function will only be run the first time it's called
    import spacy

    from skillNer.skill_extractor_class import SkillExtractor
    from skillNer.general_params import SKILL_DB

    from spacy.matcher import PhraseMatcher
    # init params of skill extractor
    # print('load model')

    nlp = spacy.load('en_core_web_lg')

    # print('load matcher')
    # init skill extractor
    skill_extractor = SkillExtractor(nlp, SKILL_DB, PhraseMatcher,)
    return skill_extractor



def clean_text(text):
    try:
        docx = nfx.TextFrame(text)
        result = docx.remove_emails().remove_urls().remove_dates().remove_html_tags().remove_numbers().remove_puncts().remove_stopwords().remove_special_characters()
        # doc = nlp(result.text)
        # empty_list = []
        # for token in doc:
        # empty_list.append(token.lemma_)
        # final_string = ' '.join(map(str,empty_list))
        return result.text
    except Exception as e:
        print(e)
        return None


def predict_cat(model, text):
    # p = int(model.predict(text,return_proba=True).max()*100)
    # cat =  model.predict(text)
    
    logits = model.predict(text,return_proba=True)
    prob = int(logits.max()*100)
    cat= label_df.iloc[logits.argmax()].values[0]
    
    
    return prob,cat


def grouper(iterable):
    prev = None
    group = []
    for item in iterable:
        if not prev or item - prev <= 1:
            group.append(item)
        else:
            yield group
            group = [item]
        prev = item
    if group:
        yield group


def get_match(job_cat,cv_skills):
    skills =  top_skill_df[top_skill_df['cat'] == job_cat]['skills']
    top_skills =  set(ast.literal_eval(",".join(skills)))
    cv_skills = set(cv_skills)
    matched_skills = top_skills.intersection(cv_skills)
    m = len(matched_skills)
    d = len(top_skills)
    match_p = round((m/10*100), 2)
    return match_p


def install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])



def create_dfs(results):
    try:
        from skillNer.general_params import SKILL_DB
    except:
        # install skillner if not done yet
        os.system('pip install skillner')
        from skillNer.general_params import SKILL_DB

    f_matches = results['full_matches']
    hard_skills =[]
    for match in f_matches:
        id_ = match['skill_id']
        full_name = SKILL_DB[id_]['skill_name']
        type_ = SKILL_DB[id_]['skill_type']
        if type_ == 'Hard Skill':
            hard_skills.append(full_name)
    s_matches = results['ngram_scored']
    s_arr = []
    for match in s_matches:
        id_ = match['skill_id']
        full_name = SKILL_DB[id_]['skill_name']
        type_ = SKILL_DB[id_]['skill_type']
        score = match['score']
        if type_ == 'Hard Skill':
            hard_skills.append(full_name)
    hard_skills =list(set(hard_skills))        
    # df = pd.DataFrame(
    #     # f_arr, columns=['skill id', 'skill name', 'skill type'])
    #     hard_skills, columns=['skill name'])
    
    return hard_skills