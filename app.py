import streamlit as st 
from langchain import PromptTemplate,LLMChain
from langchain_google_genai import ChatGoogleGenerativeAI
# Design the page
st.title("Movir Recommender Systems...")
user_input = st.text_input("Enter the Movie title,genre or keyword")

demo_template = '''Based on {user_input}provide Movie recommendations'''
template = PromptTemplate(
    input_variables=['user_input'],
    template=demo_template
)

llm=ChatGoogleGenerativeAI(model="gemini-pro",api_key="AIzaSyD-amDnx0ZJJ81xwyoX929z_m14D_-5Yvk")

if user_input:
    prompt = template.format(user_input=user_input)
    recommendations=llm.predict(text=prompt)
    st.write(f"Recommendations for you:\n{recommendations}")
else:
    st.write("Please enter the movie name")