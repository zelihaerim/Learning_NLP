from fastapi import FastAPI
from langchain.prompts import ChatPromptTemplate
from langserve import add_routes
import uvicorn
from langchain_core.output_parsers import StrOutputParser
from langchain_ollama import OllamaLLM

model= OllamaLLM(model="gemma2:2b")
output_parser=StrOutputParser()
prompt=ChatPromptTemplate.from_messages(
    [
        ("system","I am a professional expert computer scientist. Give me answers based on my expertise."),
        ("user","{question}")
    ]
)

app=FastAPI(
    title="Langchain Server",
    version="1.0",
    decsription="A simple API Server"
)

add_routes(
    app,
    prompt|model|output_parser,
    path="/ollama"
)


if __name__=="__main__":
    uvicorn.run(app,host="localhost",port=8000)