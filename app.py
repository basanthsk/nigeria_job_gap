import streamlit as st
st.set_page_config(page_title="Resume Matcher", page_icon="🧊", layout="wide")
from streamlit_option_menu import option_menu
from apps import home,eda,models,demo





if not "valid_inputs_received" in st.session_state:
    st.session_state["valid_inputs_received"] = False
# image = Image.open('data/logo.png')
# image=image.resize((100,100))
header = st.container()

apps = [
    {"func": home.app, "title": "Home", "icon": "house"},
    {"func": eda.app, "title": "Visualizations and Results", "icon": "bar-chart"},
    {"func": models.app, "title": "Data & Model", "icon": "cpu"},
    {"func": demo.app, "title": "Demo", "icon": "cloud-upload"},
]

titles = [app["title"] for app in apps]
titles_lower = [title.lower() for title in titles]
icons = [app["icon"] for app in apps]



with st.sidebar:
    # logo = st.image(image)
    selected = option_menu(
        "Main Menu",
        options=titles,
        icons=icons,
        menu_icon="cast",
    )

for app in apps:
    if app["title"] == selected:
        app["func"]()
        break
