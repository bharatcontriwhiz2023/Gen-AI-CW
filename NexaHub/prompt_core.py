from dotenv import load_dotenv
from langchain_core.prompts import ChatPromptTemplate
from langchain_mistralai import ChatMistralAI

load_dotenv()

model = ChatMistralAI(model="mistral-medium-3.5")

prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            """You are an expert movie information extractor and analyst.

Your task is to extract structured information from unstructured movie descriptions and generate a concise summary.

Always respond with a valid JSON object. Do not include any markdown, backticks, or extra text.

Extract the following fields:
- movie_name: Full official movie title
- release_year: Year the movie was released (integer)
- director: Director name(s) as a list
- cast: List of character/actor mentions in the text
- genre: List of genres that best describe the movie
- themes: Core thematic elements (e.g., loyalty, betrayal, accountability)
- key_events: Top 4-6 major plot events as brief bullet strings
- production_studio: Studio that produced the movie
- box_office_reception: Brief note on box office performance if mentioned
- critic_reception: Any mentioned audience or critic opinions
- rating_estimate: Your estimated rating out of 10 based on description tone
- summary: A concise 3-4 sentence summary of the movie in professional language
""",
        ),
        ("human", "{paragraph}"),
    ]
)

para = input("Enter the movie description: ")

final_prompt = prompt.invoke({"paragraph": para})

response = model.invoke(final_prompt)

print(response.content)
