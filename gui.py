import streamlit as st
from streamlit_option_menu import option_menu
from pages import home, mapvis, predpage, report  # import your app modules here



st.set_page_config(page_title="African Swine Fever Forecast", layout="wide")
[theme]
base="light"
primaryColor="#ffb6c1"



pages = [
    {"func": home.app, "title": "Home", "icon": "house"},
    {"func": predpage.app, "title": "Forecast an Outbreak", "icon": "activity"},
    {"func": mapvis.app, "title": "Map Visualisation", "icon": "map"},
    {"func": report.app, "title": "Correlation Analysis Report", "icon": "file-earmark-text"},
]

titles = [app["title"] for app in pages]
titles_lower = [title.lower() for title in titles]
icons = [app["icon"] for app in pages]

params = st.experimental_get_query_params()

if "page" in params:
    default_index = int(titles_lower.index(params["page"][0].lower()))
else:
    default_index = 0

with st.sidebar:
    selected = option_menu(
        "Main Menu",
        options=titles,
        icons=icons,
        menu_icon="cast",
        default_index=default_index,
    )


for app in pages:
    if app["title"] == selected:
        app["func"]()
        break
