from langchain.chains import LLMChain, SequentialChain
from langchain.prompts import PromptTemplate
from langchain.prompts.chat import ChatPromptTemplate
from langchain_community.llms import Anthropic
from langchain_anthropic import ChatAnthropic
import os
import sys

# Get the absolute path of the root directory
ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
# Add the root directory to the Python path
sys.path.append(ROOT_DIR)
from myModules.config import set_environment
set_environment()

myModel="claude-3-opus-20240229"
#myModel="claude-3-haiku-20240307"
#myModel="claude-3-sonnet-20240229"
#myModel="claude-2.1"

llm = ChatAnthropic(model=myModel)
template_1 = "<human_prompt>Human: You are a outside observer with keen insight, list 3 ambiguities in the followings text\n {wiki_text}\n\n Assistant:"
prompt_1 = ChatPromptTemplate.from_template(template_1)
llm_chain_1 = LLMChain(
    llm=llm,
    prompt=prompt_1,
    output_key='ambiguities',
    verbose=True
)
template_2 = "<human_prompt>Human: List direct follow-up questions about:\n {ambiguities}\n\n Assistant:"
prompt_2 = ChatPromptTemplate.from_template(template_2)
llm_chain_2 = LLMChain(
    llm=llm,
    prompt=prompt_2,
    output_key='questions',
    verbose=True
)

seq_chain = SequentialChain(
    chains=[llm_chain_1, llm_chain_2],
    input_variables=['wiki_text'],
    output_variables=['ambiguities','questions'],
    verbose=True        
)

with open('/Users/bower/code/justPrompts/read_doc_ask_questions/some_article.txt') as f:
        wiki_text = f.readline()


Results = seq_chain.invoke(wiki_text)

print(Results['questions'])

#print(llm_chain.invoke("You are a meditation teacher for beginners. What are 5 easy visualizations for quick meditations to start the day?"))