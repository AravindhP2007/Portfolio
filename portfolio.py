import streamlit as st

st.set_page_config(page_title='Portfolio')

st.header('Aravindh\'s Portfolio')

st.subheader('Bio')

st.markdown('Name : Aravindh.P')
st.markdown('Studies : 1st Year AI&DS')
st.markdown('College : K.S.Rangasamy College of Technology ,KSR Kalvi Nagar,Tirchungode - 638215')

st.subheader('Skills')
st.subheader('Projects')
col1,col2=st.columns([1,10])
with col1:
    pass
with col2:
    st.markdown('AI Chatbot')
    st.text('Still in a project . Not yet  completed')

if st.checkbox('Rate my portfolio'):
    st.radio('choose',('Perfect','Excellent','Good','Not Satisfied','Bad'))
