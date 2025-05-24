import streamlit as st
from wordcloud import WordCloud
import matplotlib.pyplot as plt

# Streamlit UI
st.title("🎨 Word Cloud Generator")

# Text input box for user input
user_text = st.text_area("✍️ Enter your text below:", height=200, value="Python Streamlit Data Visualization Machine Learning AI")

# Dropdown to choose background color
background_color = st.selectbox(
    "Choose a background color:",
    options=["white", "black", "violet", "skyblue", "yellow", "lightgray"]
)

# Generate word cloud only if there is some input
if user_text.strip():
    wordcloud = WordCloud(
        width=600,
        height=300,
        margin=2,
        background_color=background_color,
        colormap='Accent',
        mode='RGBA'
    ).generate(user_text)

    # Display the image using matplotlib
    fig, ax = plt.subplots(figsize=(10, 5))
    ax.imshow(wordcloud, interpolation='bilinear')
    ax.axis("off")
    st.pyplot(fig)
else:
    st.warning("Please enter some text above to generate a word cloud.")