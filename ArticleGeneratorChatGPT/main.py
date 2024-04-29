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
    response = openai.Completion.create(
        model="text-davinci-003",  # Change the model as needed
        prompt=f"Write a SEO optimized {word} word article about {keyword} in style {writing_style}.",
        max_tokens=word * 5  # Rough estimate for word to token conversion
    )

    return response.choices[0].text.strip()

keyword = st.text_input("Enter the topic of your article")
writing_style = st.selectbox("Select a writing style", ["Balanced", "Creative", "Precise"])
word_count = st.slider("Select word count", min_value=300, max_value=1000, value=400)
submit_button = st.button("Generate Article")

if submit_button:
    message = st.empty()
    message.text("Generating article....")
    article = generate_article(keyword, writing_style, word_count)
    message.text("")
    st.write(article)
    st.download_button(label="Download Article", data=article, file_name="article.txt", mime="text/plain")

