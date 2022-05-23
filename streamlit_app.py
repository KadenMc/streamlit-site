import streamlit as st
import hydralit_components as hc
import webbrowser

import home
import projects
import publications

# Page config
st.set_page_config(
  page_title="Kaden McKeen",
  page_icon="🤖"
)

# Create navbar
menu_data = [
    {'label':"Home"},
    {'label':"Projects"},
    #{'label':"Publications"},
]

theme = {'txc_inactive':'white', 'menu_background':'#A9A9A9','txc_active':'black', 'option_active':'#EFEFEF'}

menu_id = hc.nav_bar(menu_definition=menu_data, override_theme=theme, sticky_nav=True, sticky_mode='pinned')
if menu_id == "Home":
  home.main()
elif menu_id == "Projects":
  projects.main()
elif menu_id == "Publications":
  publications.main()