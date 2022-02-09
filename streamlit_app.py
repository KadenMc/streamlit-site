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
  st.markdown('''
    <style>
      button {
        position: relative;
        margin: 0;
        padding: 5px 12px;
        height: 60px;
        width: 150px;
        outline: none;
        text-decoration: none;
        display: flex;
        justify-content: center;
        align-items: center;
        cursor: pointer;
        text-transform: uppercase;
        background-color: #ffffff;
        border: 1px solid rgba(22, 76, 167, 0.6);
        border-radius: 10px;
        color: #1d89ff;
        font-weight: 400;
        font-size: 20px;
        font-family: inherit;
        z-index: 0;
        overflow: hidden;
        transition: all 0.3s cubic-bezier(0.02, 0.01, 0.47, 1);
        span {
          color: #164ca7;
          font-size: 12px;
          font-weight: 500;
          letter-spacing: 0.7px;
      }
    </style>

    <a href="https://kadenmc.github.io/cv/cv.html" target="_blank" style="text-decoration: none;">
      <button class="btn-slide-line center">
        <span>Curriculum Vitae</span>
      </button>
    </a>
''', unsafe_allow_html=True)