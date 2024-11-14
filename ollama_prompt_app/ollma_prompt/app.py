"""from fastapi import FastAPI
from langserve import add_routes
import uvicorn
from langchain_core.output_parsers import StrOutputParser
# from langchain_community.llms import Ollama
from langchain_ollama import OllamaLLM
from langchain_community.chat_models import ChatOllama
from langchain_core.prompts import ChatPromptTemplate



llm = OllamaLLM(model="gemma2:2b")
output_parser=StrOutputParser()

prompt=ChatPromptTemplate.from_messages(
    [
        ("system","You are not an meteorologist, beside this you are a professional exper biologist. Give me answers based on your expertise."),
        ("user","{question}")
    ]
)
print(f"Prompt : {prompt}")
## chain 
chain=prompt|llm|output_parser
response=chain.invoke({"question":"Can you tell me about altitude?"})
print(f"Prompt : {prompt}")
print(f"_."*75)
print(f"{response}")


app=FastAPI(
    title="Langchain Server",
    version="1.0",
    decsription="A simple API Server"
)

add_routes(
    app,
    prompt|llm|output_parser,
    path="/ollama"
)

if __name__=="__main__":
    uvicorn.run(app,host="localhost",port=8000)
"""

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
        ("system","You are not an meteorologist, beside this you are a professional exper biologist. Give me answers based on your expertise."),
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