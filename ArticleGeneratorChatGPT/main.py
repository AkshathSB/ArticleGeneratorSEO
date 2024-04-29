import streamlit as st
import openai
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Get OpenAI API key from environment variable
api_key = os.getenv("OPENAI_API_KEY")

# Set OpenAI API key
openai.api_key = api_key

st.title("SEO Article writer")

def generate_article(keyword, writing_style, word):
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {api_key}"
    }

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": "Write a SEO optimized word article about " + keyword},
            {"role": "user", "content": "This article should be in style " + writing_style},
            {"role": "user", "content": "The article length should be " + str(word)}
        ],
        headers=headers  # Pass the headers containing the API key
    )

    result = ''
    for choice in response.choices:
        result += choice.message.content

    return result

keyword = st.text_input("Enter the topic of your article")
writing_style = st.selectbox("Select a writing style", ["Balanced", "Creative", "Precise"])
word_count = st.slider("Select word count", min_value=300, max_value=1000, value=400)
submit_button = st.button("Generate Article")

if submit_button:
    message = st.empty()
    message.text("Generating article....")
    article = generate_article(keyword, writing_style, word_count)  # Don't need to pass api_key
    message.text("")
    st.write(article)
    st.download_button(label="Download Article", data=article, file_name="article.txt", mime="text/plain")
