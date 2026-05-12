import streamlit as st
from dotenv import load_dotenv
from langchain_core.prompts import ChatPromptTemplate
from langchain_mistralai import ChatMistralAI

# Load environment variables
load_dotenv()

# Streamlit page config
st.set_page_config(
    page_title="Movie Information Extractor", page_icon="🎬", layout="centered"
)

# Title
st.title("🎬 Movie Information Extractor")

# Text Area
para = st.text_area("Enter the movie description:", height=250)

# Model
model = ChatMistralAI(model="mistral-medium-3.5")

# Prompt Template
prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            """You are an expert movie information extractor and analyst.

Your task is to extract structured information from unstructured movie descriptions and generate a concise summary.

Do not return JSON.
Return the response in clean readable text format.

Extract the following fields:
- movie_name
- release_year
- director
- cast
- genre
- themes
- key_events
- production_studio
- box_office_reception
- critic_reception
- rating_estimate
- summary
""",
        ),
        ("human", "{paragraph}"),
    ]
)

# Button
if st.button("Generate Response"):

    if para.strip() == "":
        st.warning("Please enter a movie description.")
    else:

        final_prompt = prompt.invoke({"paragraph": para})

        response = model.invoke(final_prompt)

        st.subheader("Response")
        st.write(response.content)
