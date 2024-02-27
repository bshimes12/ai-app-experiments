from langchain_community.llms import HuggingFaceEndpoint
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
import myPrompts 
import PromptsActAsThis 

from config import set_environment
set_environment()

#repo_id = "mistralai/Mistral-7B-Instruct-v0.2"
#repo_id = "google/gemma-7b"
repo_id = "HuggingFaceTB/cosmo-1b"

#repo_id = "google/gemma-2b"
#repo_id = "google/gemma-7b-it"
#repo_id = "google/flan-t5-xxl"
#repo_id = "mistralai/Mixtral-8x7B-Instruct-v0.1"


llm = HuggingFaceEndpoint(
    repo_id=repo_id, temperature=1,max_new_tokens=64
)
prompt = PromptsActAsThis.standupComedian
completion = llm.invoke(prompt)

resp = llm.invoke(prompt)
print(completion)

