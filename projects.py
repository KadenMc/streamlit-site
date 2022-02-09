import streamlit as st

def main():
    st.markdown('''
    ## Projects
    ''')

    st.markdown('''
    ### 2022
    ''')

    st.markdown('''
    <h4><a href="https://vectorinstitute.ai" target="_blank">Vector Institute</a> – Cyclops: An Evaluative Framework for Clinical ML</h4>

    Performing feature extraction, developing models, and practicing MLOps for project Cyclops.<br><br>
    Cyclops is a continuous evaluative framework of clinical machine learning models currently being developed and validated on datasets <a href="https://www.geminimedicine.ca" target="_blank">GEMINI</a> and <a href="https://mimic.mit.edu/docs/iv" target="_blank">MIMIC-IV</a> with targets delirium and length of stay.<br><br>
    The MLOps framework consists of monitoring and evaluation tools capable of testing model performance and generalizability across time and hospitals using drift detection methods.<br><br>

    ''', unsafe_allow_html=True)

    st.markdown('''
    <h4><a href="http://brainlab.ca" target="_blank">BrainLab</a> – Unsupervised 3D Image Registration</h4>

    Developing a pipeline for deformable, unsupervised, pairwise image registration under the tutorage of Dr. Maged Goubran &amp; Ahmadreza Attarpour at Sunnybrook's BrainLab.<br>

    ''', unsafe_allow_html=True)

    st.warning("GitHub - Coming Soon!")

    st.markdown('''
    <br>
    
    <h4><a href="https://kadenmc.github.io/projects/LearnAI-2021Syllabus.pdf" target="_blank">LearnAI</a> – UofT AI's Director of Education &amp; LearnAI Lead</h4>
    ''', unsafe_allow_html=True)

    st.markdown('''
        UofT AI is a club at the University of Toronto; LearnAI, its subsidiary course, teaches U of T undergraduates practical ML. I proudly spearheaded LearnAI as the club Director of Education for three years.<br>

    In 2021, we partnered with <a href="https://ai-commons.org/" target="_blank">AI Commons</a> to expand our reach and empower people in emerging countries!
    <br>''', unsafe_allow_html=True)

    st.markdown('''
    ### 2021
    ''')

    st.markdown('''
    <h4><a href="https://github.com/KadenMc/notMNIST_model" target="_blank">notMNIST</a> – Letter Classification Model</h4>

    This classification project on the `notMNIST_small` dataset was more an exercise in proper argument parsing, visualization, and using TensorBoard with PyTorch.
    It was also an exploration of PyTorch’s dataloaders (such as ImageFolder), transforms, optimizers, and sequential modelling functionalities!
    <br><br>

    <h4><a href="https://github.com/KadenMc/PreprocessingHTR" target="_blank">Illegible</a> – Full-Page Preprocessing for Handwriting Recognition</h4>
    ''', unsafe_allow_html=True)

    st.markdown('''
    This project was an exercise in computer vision preprocessing: Take an image of a full-page handwritten document and prepare it as singular word images for offline handwriting recognition.<br><br>

    <style>.img-container {text-align: center;}</style>
    <div class="img-container"><img src="https://kadenmc.github.io/projects/PreprocessingConversion.png" width="75%%" style="border-radius:50px;"/></div>
    ''', unsafe_allow_html=True)

    st.warning("Demo - Coming Soon!")

    st.markdown('''
    <br>
    <h4><a href="https://github.com/KadenMc/TranscriptGeneratingLSTM" target="_blank">Reincarnating Bob Ross</a> – Text Generation of YouTube Transcripts</h4>
    ''', unsafe_allow_html=True)

    st.markdown('''
        Perform LSTM character-level generation on automatically extracted YouTube transcripts. I tackled this project to recreate the late Bob Ross' painting videos.<br>
    ''', unsafe_allow_html=True)

    st.success("Text Generation Demo")

    # === TEXT GENERATION DEMO ===
    col1, col2 = st.columns([1, 1])
    length = col1.number_input(label="Length", min_value=1, max_value=200, value=100, step=1)
    diversity = col2.number_input(label="Diversity (Temperature/Generation 'Randomness')", min_value=0.1, max_value=0.9, value=0.5, step=0.1,format="%.2f")

    input = st.text_input("Prompt:")
    if input != "":
        with st.spinner('Loading...'):
            import textGeneration.demo  as tgd
            st.success(tgd.demo(input, length, diversity))



    st.markdown('''
    <br>
    <h4><a href="https://github.com/KadenMc/EmotionRecognition" target="_blank">Facing Racial Bias</a> – Unbiased Emotion Recognition</h4>
    
    Emotion recognition is fraught with racial bias, which I aim to investigate and minimize.<br><br>
    ''', unsafe_allow_html=True)