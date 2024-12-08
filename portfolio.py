import streamlit as st

st.set_page_config(page_title='Portfolio')
c1,c2,c3=st.columns([1,1,1])
with c2:
    st.header('Hi, I am Aravindh')

st.header('Who Am I?')
st.write('Erode,Tamilnadu,India')
st.header('17 YEARS OLD')
c1,c2,c3=st.columns([1,1,1])
with c3:
    st.header('About Me')
c1,c2=st.columns([1,10])
with c2:
    st.markdown('I am Aravindh from Erode, Currently pursuing B.Tech Artificial Intelligence& Data Science 1st year in K.S.Rangasamy College of Technology.')
    st.markdown('I am always interest in developing my skills')
st.header('Skills')
c1,c2=st.columns([1,10])
with c2:
    st.subheader('Languages')
c1,c2,c3=st.columns([1,1,1])
with c2:
    st.header('C')
    progress_value = 35
    st.markdown(f'{progress_value}%')
    st.progress(progress_value)
with c3:
    st.header('Python')
    progress_value = 35
    st.markdown(f'{progress_value}%')
    st.progress(progress_value)
c1,c2=st.columns([1,10])
with c2:
    st.subheader('Frame work')
c1,c2=st.columns([1,1])
with c2:
    st.header('Streamlit-Python')
st.header('Projects')
col1,col2=st.columns([3,10])
with col1:
    pass
with col2:
    st.subheader('AI Chatbot')
    st.markdown('Still working in this project . Not yet  completed')

st.header('Experiences')
st.header('Awards')
st.header('Achievements')


if st.checkbox('Rate my portfolio'):
    st.radio('choose',('Perfect','Excellent','Good','Not Satisfied','Bad'))
