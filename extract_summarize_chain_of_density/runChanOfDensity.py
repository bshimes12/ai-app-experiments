import os
import sys
from langchain.prompts import PromptTemplate,load_prompt

from langchain_anthropic import AnthropicLLM


from langchain_anthropic import ChatAnthropic
from langchain.prompts.chat import ChatPromptTemplate

# Get the absolute path of the root directory
ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
# Add the root directory to the Python path
sys.path.append(ROOT_DIR)
from myModules.config import set_environment
set_environment()
os.chdir('/Users/bower/code/justPrompts/extract_summarize_chain_of_density/')
template = load_prompt('CoD_template.yaml')
# Create a PromptTemplate instance from the loaded template
#prompt = PromptTemplate.from_template(template)
#prompt = ChatPromptTemplate(template=template, input_variables=["human_prompt"])
prompt = PromptTemplate(template=template, input_variables=["human_prompt"])
llm = AnthropicLLM(model='claude-2.1')

# Use the prompt template
human_prompt = "What is the capital of France?"
formatted_prompt = prompt.format(human_prompt=human_prompt)
result = llm.generate([formatted_prompt])
print(result.generations[0][0].text)