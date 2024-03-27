# import the necessary Python libraries
import streamlit as st
from langchain.llms import OpenAI

# st title
st.title('🦜🔗 First LLM App Built by CC')

# text input for the user to enter openAI key
openai_api_key = st.sidebar.text_input('OpenAI API Key', type='password')

# define response function
def generate_response(input_text):
    llm = OpenAI(temperature=0.7, openai_api_key=openai_api_key)
    st.info(llm(input_text))

# create a text box for user input
with st.form('my_form'):
    text = st.text_area('Enter text:', 'What are the three key pieces of advice for learning how to code?')
    submitted = st.form_submit_button('Submit')
    if not openai_api_key.startswith('sk-'):
        st.warning('Please enter your OpenAI API key!', icon='⚠')
    if submitted and openai_api_key.startswith('sk-'):
        generate_response(text)