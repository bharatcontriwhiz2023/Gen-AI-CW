from dotenv import load_dotenv
from langchain_core.prompts import ChatPromptTemplate
from langchain_mistralai import ChatMistralAI
from pydantic import BaseModel
from typing import List, Optional
from langchain_core.output_parsers import PydanticOutputParser

load_dotenv()

model = ChatMistralAI(model="mistral-medium-3.5")


# this is a schema
class Movie(BaseModel):
    title: str
    release_year: Optional[int]
    genre: List[str]
    director: Optional[str]
    cast: List[str]
    box_office_collection: int
    summary: str


parser = PydanticOutputParser(pydantic_object=Movie)


prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            """ 

Extract movie information from the paragraph 
    {format_instructions}
""",
        ),
        ("Human", "{paragraph}"),
    ]
)

para = input("Enter the movie description: ")

final_prompt = prompt.invoke(
    {"paragraph": para, "format_instructions": parser.get_format_instructions}
)

response = model.invoke(final_prompt)

print(response.content)


# import streamlit as st
# from dotenv import load_dotenv
# from langchain_core.prompts import ChatPromptTemplate
# from langchain_mistralai import ChatMistralAI
# from pydantic import BaseModel
# from typing import List, Optional
# from langchain_core.output_parsers import PydanticOutputParser

# # Load environment variables
# load_dotenv()

# # Streamlit page config
# st.set_page_config(
#     page_title="Movie Information Extractor", page_icon="🎬", layout="centered"
# )

# # Title
# st.title("🎬 Movie Information Extractor")

# # Text Area
# para = st.text_area("Enter the movie description:", height=250)

# # Model
# model = ChatMistralAI(model="mistral-medium-3.5")


# # Schema
# class Movie(BaseModel):
#     title: str
#     release_year: Optional[int]
#     genre: List[str]
#     director: Optional[str]
#     cast: List[str]
#     box_office_collection: int
#     summary: str


# # Parser
# parser = PydanticOutputParser(pydantic_object=Movie)

# # Prompt
# prompt = ChatPromptTemplate.from_messages(
#     [
#         (
#             "system",
#             """
# Extract movie information from the paragraph.

# {format_instructions}
# """,
#         ),
#         ("human", "{paragraph}"),
#     ]
# )

# # Button
# if st.button("Generate Response"):

#     if para.strip() == "":
#         st.warning("Please enter a movie description.")
#     else:

#         final_prompt = prompt.invoke(
#             {"paragraph": para, "format_instructions": parser.get_format_instructions()}
#         )

#         response = model.invoke(final_prompt)

#         st.subheader("Response")
#         st.write(response.content)
