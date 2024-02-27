from langchain_community.llms import HuggingFaceEndpoint
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate


from config import set_environment
set_environment()

#repo_id = "mistralai/Mistral-7B-Instruct-v0.2"
#repo_id = "google/gemma-7b"
#repo_id = "google/gemma-2b"
#repo_id = "google/gemma-7b-it"
#repo_id = "google/flan-t5-xxl"
repo_id = "mistralai/Mixtral-8x7B-Instruct-v0.1"

question = "why is the sky blue? "

template = """
Question: {question}
Answer: You are a scientist and will explain answers in simple, easy to understand language. Let's think step by step. Don't make up an answer. If you don't know, say "I don't know!"
"""

prompt = PromptTemplate.from_template(template)



llm = HuggingFaceEndpoint(
    repo_id=repo_id, temperature=1
)

llm_chain = LLMChain(prompt=prompt, llm=llm)
resp = llm_chain.invoke(question)

print(resp['text'])

