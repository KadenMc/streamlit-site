import streamlit as st
import hydralit_components as hc
import webbrowser

import home
import projects
import publications

st.set_page_config(page_title="Kaden McKeen")



# Create navbar
menu_data = [
    {'label':"Home"},
    {'label':"Projects"},
    {'label':"Publications"},
    {'label':"CV"},
]



theme = {'txc_inactive':'white', 'menu_background':'#A9A9A9','txc_active':'black', 'option_active':'#EFEFEF'}

menu_id = hc.nav_bar(menu_definition=menu_data, override_theme=theme, sticky_nav=True, sticky_mode='pinned')
if menu_id == "Home":
  home.main()
elif menu_id == "Projects":
  projects.main()
elif menu_id == "Publications":
  publications.main()
elif menu_id == "CV":
  webbrowser.open_new_tab("https://kadenmc.github.io/cv/cv.html")