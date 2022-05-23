import streamlit as st

def checkout_cv():
    st.markdown('''
    For up-to-date information, check out <a href="https://kadenmc.github.io/cv/cv.html" target="_blank">my CV</a>!
    ''', unsafe_allow_html=True)

def main():
    st.markdown('''
    ## Projects
    ''')

    st.markdown('''
    ### 2022
    ''')

    st.markdown('''
    <h4><a href="https://vectorinstitute.ai" target="_blank">Vector Institute</a> – CyclOps: An Evaluation Framework for Clinical ML</h4>
    ''', unsafe_allow_html=True)
    
    checkout_cv()

    st.markdown('''
    <h4><a href="http://brainlab.ca" target="_blank">BrainLab</a> – <a href="https://github.com/KadenMc/MONAIRegistration" target="_blank">Unsupervised 3D Image Registration</a></h4>
    ''', unsafe_allow_html=True)

    checkout_cv()

    st.markdown('''
    <h4><a href="https://www.uoft.ai/" target="_blank">UofT AI</a> - Director of Education &amp; <a href="https://kadenmc.github.io/projects/LearnAI-2021Syllabus.pdf" target="_blank">LearnAI</a> Lead</h4>
    ''', unsafe_allow_html=True)

    checkout_cv()
    
    st.markdown('''
    <br>
    ''', unsafe_allow_html=True)

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