import streamlit as st

def main():
    st.markdown('''
    ## Publications
    ''')

    st.markdown('''
    <style>
    li.normal { font-size: 1.3rem;}
    p.normal { font-size: 1.3rem; }
    p.sub { font-size: 1rem; }
    </style>
    
    <section class="main-content">
    Coming soon:
    <br>
    <br>
        <ol>
            <li class="normal">
                <p class="normal">Unsupervised deep-learning method for deformable, pairwise brain tissue image registration on tissue cleared microscopy data</p>
                <p class="sub">Research at Sunnybrook's BrainLab under Dr. Maged Goubran &amp; Ahmadreza Attarpour</p>
            </li><br>
            <li class="normal">
                <p class="normal">Deep-learning framework for personalized offline handwritten text recognition</p>
            </li>
        </ol>
    </section>
    ''', unsafe_allow_html=True)
