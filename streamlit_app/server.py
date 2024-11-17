from fastapi import FastAPI
from langchain.prompts import ChatPromptTemplate
from langchain.chat_models import ChatOpenAI
from langserve import add_routes
import uvicorn
import os
from langchain_community.llms import Ollama
from dotenv import load_dotenv

load_dotenv()

os.environ['OPENAI_API_KEY']=os.getenv("OPENAI_API_KEY")

app=FastAPI(
    title="Langchain Server",
    version="1.0",
    decsription="A simple API Server"
)

# openai api
openai_model = ChatOpenAI()
# ollama llama2 api
ollama_model = Ollama(model="gemma2:2b")
# Prompt Templates with embedded input variables
prompt1 = ChatPromptTemplate.from_template("Write me an essay about {topic} with 100 words")
prompt2 = ChatPromptTemplate.from_template("Write me an poem about {topic} for a 5 years child with 100 words")

# Openai
add_routes(
    app,
    prompt1|openai_model,
    path="/openai/essay"
)
add_routes(
    app,
    prompt2|openai_model,
    path="/openai/poem"
)

# Ollama
add_routes(
    app,
    prompt1|ollama_model,
    path="/ollama/essay"
)
add_routes(
    app,
    prompt2|ollama_model,
    path="/ollama/poem"
)

if __name__=="__main__":
    uvicorn.run(app, host="localhost", port=8000)
