import streamlit as st
from PIL import Image

st.set_page_config(page_title="Kaden McKeen")#, layout="wide")

# Get style
with open("style.css") as f:
    st.markdown('<style>{}</style>'.format(f.read()), unsafe_allow_html=True)

# Header 
st.write('''# Kaden McKeen''')

# Centered headshot image
me_img = Image.open('me.png')
col1, col2, col3 = st.columns([1, 1, 1])
col2.image(me_img)

# Socials
github = "PD94bWwgdmVyc2lvbj0iMS4wIiBzdGFuZGFsb25lPSJubyI/Pgo8IURPQ1RZUEUgc3ZnIFBVQkxJQyAiLS8vVzNDLy9EVEQgU1ZHIDIwMDEwOTA0Ly9FTiIKICJodHRwOi8vd3d3LnczLm9yZy9UUi8yMDAxL1JFQy1TVkctMjAwMTA5MDQvRFREL3N2ZzEwLmR0ZCI+CjxzdmcgdmVyc2lvbj0iMS4wIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciCiB3aWR0aD0iNTEyLjAwMDAwMHB0IiBoZWlnaHQ9IjUxMi4wMDAwMDBwdCIgdmlld0JveD0iMCAwIDUxMi4wMDAwMDAgNTEyLjAwMDAwMCIKIHByZXNlcnZlQXNwZWN0UmF0aW89InhNaWRZTWlkIG1lZXQiPgoKPGcgdHJhbnNmb3JtPSJ0cmFuc2xhdGUoMC4wMDAwMDAsNTEyLjAwMDAwMCkgc2NhbGUoMC4xMDAwMDAsLTAuMTAwMDAwKSIKZmlsbD0iIzAwMDAwMCIgc3Ryb2tlPSJub25lIj4KPHBhdGggZD0iTTIzNjAgNTA0OSBjLTE1NCAtMTEgLTM1NyAtNDcgLTUxNiAtOTMgLTkwMiAtMjU5IC0xNjAzIC0xMDE3IC0xNzkwCi0xOTM0IC0xMzYgLTY2OSAtOCAtMTM1NSAzNTQgLTE5MDggMjU1IC0zOTAgNTgwIC02ODYgOTY4IC04ODYgMTQxIC03MyAzNDEKLTE1NCA0MDMgLTE2NCA1OCAtOSAxMDkgMTkgMTMzIDczIDE4IDQwIDE4IDYwIDEyIDI4NiBsLTcgMjQzIC04NiAtMTQgYy05NwotMTUgLTI1NiAtOSAtMzg2IDEzIC0xMDUgMTkgLTIxMSA3MSAtMjc4IDEzOSAtNTMgNTMgLTY3IDc2IC0xMzYgMjI5IC02MyAxMzkKLTEzNSAyMzEgLTIzMiAyOTcgLTY2IDQ2IC0xMjEgMTA2IC0xMTcgMTI4IDYgMzAgNDggNDMgMTIxIDM4IDE0MSAtMTAgMjg4Ci0xMTMgMzkzIC0yNzQgNzIgLTExMCAxNDMgLTE3OSAyMzAgLTIyMiA2MiAtMzEgNzkgLTM1IDE2OSAtMzggMTAzIC00IDIwNyAxMgoyOTEgNDQgNDEgMTYgNDMgMTggNTggODUgMTkgODYgNTYgMTY0IDEwNiAyMjggbDM5IDQ5IC04MiAxMSBjLTI2NCAzOCAtNDUyCjEwMiAtNjI3IDIxNSAtMjI5IDE0OCAtMzY1IDM3OSAtNDMxIDczMSAtMjAgMTA5IC0yMyAzODkgLTUgNDkyIDI5IDE2NyA5OAozMTkgMjAwIDQ0NSBsNDUgNTUgLTIwIDYyIGMtNTIgMTY4IC00MiAzNzIgMjggNTc0IDE4IDUwIDIyIDUyIDEwMyA0OCAxMTggLTYKMzcxIC0xMDggNTQzIC0yMTggbDcxIC00NiA1NiAxMSBjMzAgNiA4NyAxOCAxMjcgMjcgMjcxIDU4IDY1NSA1OCA5MjYgMCA0MAotOSA5NyAtMjEgMTI3IC0yNyBsNTUgLTEwIDk1IDU4IGMyMjYgMTM3IDQ4NCAyMzAgNTc1IDIwNiAyNiAtNyAzMyAtMTcgNTMKLTc1IDQzIC0xMjUgNTUgLTIxMCA1MCAtMzUxIC00IC05NSAtMTEgLTE0OCAtMjYgLTE5NSBsLTIxIC02NCA0NCAtNTQgYzg5Ci0xMDkgMTU1IC0yNDQgMTkyIC0zODkgMjIgLTg5IDI1IC00MTcgNCAtNTQ0IC0zMiAtMTk4IC0xMTQgLTQwNiAtMjEwIC01MzIKLTE2NSAtMjE3IC00NjQgLTM2NiAtODQzIC00MTggbC04NyAtMTIgMzkgLTQ5IGM0NyAtNjAgODUgLTEzNyAxMDYgLTIyMSAxNAotNTIgMTcgLTEzNyAyMCAtNTAzIDUgLTQ5MCA1IC00ODkgNzIgLTUyMSA0NiAtMjEgODMgLTE1IDIyOSA0MiA3MzggMjg0IDEzMjAKOTMyIDE1MzMgMTcwMyAxNDEgNTEzIDExMSAxMTA4IC04MCAxNjAxIC0xNzIgNDQwIC00NzUgODQyIC04NDggMTEyMiAtNDA1CjMwMyAtODY1IDQ3NCAtMTM2NyA1MDcgLTE3NSAxMiAtMTkyIDEyIC0zNzUgMHoiLz4KPC9nPgo8L3N2Zz4K"
linkedin = "PD94bWwgdmVyc2lvbj0iMS4wIiBzdGFuZGFsb25lPSJubyI/Pgo8IURPQ1RZUEUgc3ZnIFBVQkxJQyAiLS8vVzNDLy9EVEQgU1ZHIDIwMDEwOTA0Ly9FTiIKICJodHRwOi8vd3d3LnczLm9yZy9UUi8yMDAxL1JFQy1TVkctMjAwMTA5MDQvRFREL3N2ZzEwLmR0ZCI+CjxzdmcgdmVyc2lvbj0iMS4wIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciCiB3aWR0aD0iNTEyLjAwMDAwMHB0IiBoZWlnaHQ9IjUxMi4wMDAwMDBwdCIgdmlld0JveD0iMCAwIDUxMi4wMDAwMDAgNTEyLjAwMDAwMCIKIHByZXNlcnZlQXNwZWN0UmF0aW89InhNaWRZTWlkIG1lZXQiPgoKPGcgdHJhbnNmb3JtPSJ0cmFuc2xhdGUoMC4wMDAwMDAsNTEyLjAwMDAwMCkgc2NhbGUoMC4xMDAwMDAsLTAuMTAwMDAwKSIKZmlsbD0iIzAwMDAwMCIgc3Ryb2tlPSJub25lIj4KPHBhdGggZD0iTTM5NSA1MTEwIGMtMTc2IC0yOCAtMzEyIC0xNDUgLTM3MSAtMzIwIC0xOCAtNTMgLTE5IC0xMzAgLTE5IC0yMjMwCjAgLTIxMDAgMSAtMjE3NyAxOSAtMjIzMCA0OSAtMTQ2IDE0OCAtMjQ3IDI5NCAtMzAzIGw1NyAtMjIgMjE4NSAwIDIxODUgMCA1NwoyMiBjMTQ2IDU2IDI0NSAxNTcgMjk0IDMwMyAxOCA1MyAxOSAxMzAgMTkgMjIzMCAwIDIxMDAgLTEgMjE3NyAtMTkgMjIzMCAtNDkKMTQ2IC0xNDggMjQ3IC0yOTQgMzAzIGwtNTcgMjIgLTIxNTAgMSBjLTExODIgMSAtMjE3MiAtMiAtMjIwMCAtNnogbTg4MCAtNTY1CmMyMDcgLTQ0IDM4MiAtMjE4IDQyNCAtNDIzIDc4IC0zNzYgLTI2MiAtNzI0IC02MzQgLTY0OSAtMjAwIDQxIC0zNTUgMTc1Ci00MjEgMzY2IC0zMSA4OSAtMzUgMjI4IC05IDMxOCA0MiAxNDggMTUwIDI3NiAyODkgMzQzIDEyNCA2MCAyMjIgNzIgMzUxIDQ1egptMjYyNSAtMTI5OCBjMTY5IC00NCAyNzYgLTEwNCAzODMgLTIxNSAxNjYgLTE3MCAyNTMgLTM5OSAyODggLTc1NyA5IC05MSAxMwotMzUzIDE0IC04NzUgMCAtNzAyIC0xIC03NDcgLTE4IC03NzMgLTEwIC0xNiAtMzIgLTM3IC01MCAtNDcgLTMwIC0xOSAtNTMKLTIwIC0zNjUgLTIwIC0zNjMgMCAtMzcwIDEgLTQxMSA1OCAtMTkgMjggLTIwIDQ2IC0yNCA3NjMgLTMgNjIzIC02IDc0NCAtMTkKNzk5IC0zOCAxNTQgLTk4IDI1NCAtMTg4IDMwOCAtNzggNDYgLTEyMSA1NyAtMjM1IDU2IC0xMzEgMCAtMTkyIC0yMyAtMjc5Ci0xMDUgLTcyIC02NyAtMTIzIC0xNTkgLTE1OSAtMjg3IC0yMSAtNzUgLTIyIC05NyAtMjcgLTc5MiAtNSAtNjY4IC02IC03MTcKLTIzIC03NDIgLTM4IC01NSAtNTYgLTU4IC00MDQgLTU4IC0zNTYgMCAtMzY4IDIgLTQwNSA3MSAtMTcgMzIgLTE4IDkyIC0xOAoxMjY3IDAgMTM2OCAtNCAxMjgxIDY0IDEzMjMgMjkgMTggNTYgMTkgMzYxIDE5IDMxMCAwIDMzMiAtMSAzNjIgLTIwIDUyIC0zMQo2MyAtNjQgNjMgLTE5MiBsMSAtMTEzIDIyIDMwIGM3NCAxMDIgMjAyIDIwNiAzMDkgMjUzIDE0MSA2MSAyNzEgODIgNDg4IDc4CjE0NyAtMyAxOTAgLTggMjcwIC0yOXogbS0yMzc5IC0zMCBjMTkgLTEyIDQyIC0zOCA1MiAtNTcgMTYgLTMzIDE3IC0xMDkgMTUKLTEyNzIgLTMgLTEyMzMgLTMgLTEyMzcgLTI0IC0xMjY1IC00NSAtNjEgLTU4IC02MyAtNDAyIC02MyAtMzM4IDAgLTM0MSAwCi0zOTIgNTUgbC0yNSAyNyAtMyAxMjUwIGMtMiAxMjA2IC0yIDEyNTIgMTYgMTI4MCAxMSAxNiAzMiAzOCA0OCA0OSAyNyAxOCA1MQoxOSAzNTUgMTkgMzIyIDAgMzI2IDAgMzYwIC0yM3oiLz4KPC9nPgo8L3N2Zz4K"
linkedin_html = r'<a href="https://www.linkedin.com/in/kadenmckeen/" target="_blank"><img width="7%%" src="data:image/svg+xml;base64, %s"/></a>' % linkedin
github_html = r'<a href="https://github.com/KadenMc/" target="_blank"><img width="7%%" src="data:image/svg+xml;base64,%s"/></a>' % github
html = """
  <style>
    .img-container {
      text-align: center;
    }
  </style>
  
  <div class="img-container">""" + linkedin_html + '&nbsp;'*5 + github_html + "</div>"
st.write(html, unsafe_allow_html=True)


st.markdown('## Summary', unsafe_allow_html=True)
st.info('''
- Applied machine learning intern at the Vector Institute
- Machine learning researcher at Sunnybrook's BrainLab
- 4th year Computer Science student at the University of Toronto
''')

#####################
# Navigation
st.markdown('<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">', unsafe_allow_html=True)
st.markdown("""
<nav class="navbar fixed-top navbar-expand-lg navbar-dark" style="background-color: #16A2CB;">
  <a class="navbar-brand" href="https://www.linkedin.com/in/kadenmckeen/" target="_blank">Kaden McKeen</a>
  <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
    <span class="navbar-toggler-icon"></span>
  </button>
  <div class="collapse navbar-collapse" id="navbarNav">
    <ul class="navbar-nav">
      <li class="nav-item active">
        <a class="nav-link disabled" href="/">Home <span class="sr-only">(current)</span></a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#projects">Projects</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#publications">Publications</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="https://kadenmc.github.io/cv/cv.html" target="_blank">CV</a>
      </li>
    </ul>
  </div>
</nav>
""", unsafe_allow_html=True)



#####################
st.markdown('''
## Projects
''')

st.markdown('''
  <h4>BrainLab – Unsupervised Image Registration</h4>
	GitHub - <i>Coming soon!</i><br><br>

  Developing a pipeline for deformable, unsupervised, pairwise image registration under the tutorage of Dr. Maged Goubran &amp; Ahmadreza Attarpour at Sunnybrook's <a href="http://brainlab.ca" target="_blank">BrainLab</a>.<br>
  <br><br>
''', unsafe_allow_html=True)

st.markdown('''
  <h4>LearnAI – UofT AI's Director of Education &amp; LearnAI Lead</h4>

  <a href="https://kadenmc.github.io/projects/LearnAI-2021Syllabus.pdf" target="_blank">Syllabus</a> - 2021-2022 LearnAI Syllabus<br>
''', unsafe_allow_html=True)

st.markdown('''
	UofT AI is a club at the University of Toronto; LearnAI, its subsidiary course, teaches U of T undergraduates practical ML. I proudly spearheaded LearnAI as the club Director of Education for three years.<br>

  In 2021, we partnered with <a href="https://ai-commons.org/" target="_blank">AI Commons</a> to expand our reach and empower people in emerging countries!
  <br><br>

  <h4>notMNIST – PyTorch Letter Classification Model</h4>
  <a href="https://github.com/KadenMc/notMNIST_model" target="_blank">GitHub</a><br><br>

  This classification project on the `notMNIST_small` dataset was an exercise in proper argument parsing, visualization, and using TensorBoard with PyTorch.
  It was also an exploration of PyTorch’s dataloaders (such as ImageFolder), transforms, optimizers, and sequential modelling functionalities!
  <br><br>

  <h4>Illegible – Full-Page Preprocessing for Handwriting Recognition</h4>
  <a href="https://github.com/KadenMc/PreprocessingHTR" target="_blank">GitHub</a><br><br>
''', unsafe_allow_html=True)

st.markdown('''
	This project was an exercise in computer vision preprocessing: Take an image of a full-page handwritten document and prepare it as singular word images for offline handwriting recognition.<br><br>

  <img src="https://kadenmc.github.io/projects/PreprocessingConversion.png" style="max-height: 300px; border-radius:50px; margin-left: 25%;" />
  <br><br>

  <h4>Reincarnating Bob Ross – Text Generation of YouTube Transcripts</h4>
	<a href="https://github.com/KadenMc/TranscriptGeneratingLSTM" target="_blank">GitHub</a><br><br>
''', unsafe_allow_html=True)

st.markdown('''
	Perform LSTM character-level generation on automatically extracted YouTube transcripts. I tackled this project to recreate the late Bob Ross' painting videos:<br>

  <b>Prompt</b>: “welcome back. certainly glad you could join us today, it's a fantastic day here. let's have them run all”<br>

  <b>Generated</b>: ... “the colors across the screen, there we go. now then, we'll take a little bit of the bright-red and let's put some of the same colors and then we'll put a little bit of the bright-red in the sky. there we go. now, little touch of the bristles, we'll go right into the yellow-ochre”
  <br><br>

  <h4><a href="https://github.com/KadenMc/EmotionRecognition" target="_blank">Facing Racial Bias</a> – Unbiased Emotion Recognition</h4>
	<a href="https://github.com/KadenMc/EmotionRecognition" target="_blank">GitHub</a> - <i>Work in progress</i><br><br>
  
  Emotion recognition is fraught with <a href="https://papers.ssrn.com/sol3/papers.cfm?abstract_id=3281765" target="_blank">racial bias</a>, which I aim to investigate and minimize.<br><br>
''', unsafe_allow_html=True)


st.markdown('''
## Publications
''')

st.markdown('''
<section class="main-content">
  Coming soon:
  <br>
  <br>
	<ol>
		<li>
      Unsupervised deep-learning method for deformable, pairwise brain tissue image registration on tissue cleared microscopy data
      <p class="lisub">Research at Sunnybrook's BrainLab under Dr. Maged Goubran &amp; Ahmadreza Attarpour</p>
    </li><br>
		<li>
      Deep-learning framework for personalized offline handwritten text recognition
    </li>
	</ol>
</section>
''', unsafe_allow_html=True)