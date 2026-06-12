from fastapi import FastAPI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_groq import ChatGroq
import os 
from langserve import add_routes
from dotenv import load_dotenv
load_dotenv()


groq_api_key = os.getenv("GROQ_API_KEY")
model = ChatGroq(model = "llama-3.1-8b-instant", groq_api_key=groq_api_key)


#1. Create a prompt template
system_template = "Translate the following into {language}:"
prompt_template = ChatPromptTemplate.from_messages(
    [
        ("system", system_template),
        ("user", "{text}")
    ]
)

parser = StrOutputParser()

##Create a chain

chain = prompt_template | model | parser

app = FastAPI(title = "Langchain Server",
              version = "1.0",
              description = "A simple server to serve langchain chains using langserve")

add_routes(app, chain, path = "/chain")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host = "localhost", port = 8000)