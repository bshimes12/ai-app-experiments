from langchain_community.llms import HuggingFaceEndpoint
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
import myPrompts 
import ChatBot.myActAsPrompts as myActAsPrompts 

from config import set_environment
set_environment()

repo_id = "mistralai/Mistral-7B-Instruct-v0.2"
#repo_id = "google/gemma-7b"
#repo_id = "google/gemma-2b"
#repo_id = "google/gemma-7b-it"
#repo_id = "google/flan-t5-xxl"
#repo_id = "mistralai/Mixtral-8x7B-Instruct-v0.1"

question = "what is that smell in the kitchen?"
ActAs = myActAsPrompts.lunatic
template = """
Question: {question}
Context:""" + ActAs

prompt = PromptTemplate.from_template(template)



llm = HuggingFaceEndpoint(
    repo_id=repo_id, temperature=1
)

llm_chain = LLMChain(prompt=prompt, llm=llm)
resp = llm_chain.invoke(question)

print(resp['text'])

