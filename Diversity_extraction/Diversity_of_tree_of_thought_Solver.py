

## python3 Diversity_of_tree_of_thought_Solver.py > the_statments.txt

from langchain.prompts import PromptTemplate
from langchain.chains import SequentialChain
from langchain.chains.llm import LLMChain
from langchain_openai import ChatOpenAI
from langchain_anthropic import ChatAnthropic
import sys
import os


# Get the absolute path of the root directory
ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
# Add the root directory to the Python path
sys.path.append(ROOT_DIR)

from myModules.config import set_environment
set_environment()



#llm = ChatOpenAI(temperature=0.7, model_name="gpt-3.5-turbo")
#llm = ChatOpenAI(temperature=0.7, model_name="gpt-3.5-turbo-0125")
#llm = ChatOpenAI(temperature=0.7, model_name="gpt-4-0613")


## Anthropic
myModel="claude-3-opus-20240229"
#myModel="claude-3-haiku-20240307"
#myModel="claude-3-sonnet-20240229"
#myModel="claude-2.1"
llm = ChatAnthropic(model=myModel)



statement_template = """
When I give you a {the_statement}, follow the <instruction> and output the <output> format.
<instruction>
Tell me opinions about the statement as many as possible from different people with, “Agree” or “Disagree,” one-word or one-phrase criteria that is important for their opinions. Provide a wide variety of viewpoints, more viewpoints are better.
</instruction>
<output>
<output>
1:“Stance”: “Agree”,
“Criteria”: [“personal boundaries”, “autonomy”]
2:“Stance”: “Disagree”,
“Criteria”: [“transparency”, “trust”],
</output>
Viewpoints:
"""
statement_prompt = PromptTemplate(
   template=statement_template,
   input_variables=["the_statement"]
)
Evaluate_template = """
Evaluate each Stance in {the_viewpoints} and write a well thought out Reason from the perspective of the speaker based on the Criteria listed for each.
Reasons:
"""
evaluation_prompt = PromptTemplate(
  template=Evaluate_template,
  input_variables=["the_viewpoints"]
)
reasoning_template = """
For each {reasons}, detailed counter strategies to engage with the this viewpoint because you disagree with them but want to convince them they are wrong. Use their Criteria of the Reason in your strategy to convince them of your arguement. 
counter-reasons: 
"""
reasoning_prompt = PromptTemplate(
  template=reasoning_template,
  input_variables=["reasons"]
)
ranking_template = """
Based on the counter-reasons, create a ficticious conversation between two people based on the {counter_reasons}. A mind is changed. Be optimistic and kind but it might not be a pleasant conversation.
Conversation:
"""
ranking_prompt = PromptTemplate(
  template=ranking_template,
  input_variables=["counter_reasons:"]
)

solutions_chain = LLMChain(
   llm=llm,
   prompt=statement_prompt,
   output_key="the_viewpoints",
   verbose=True
)
evalutation_chain = LLMChain(
   llm=llm,
   prompt=evaluation_prompt,
   output_key="reasons",
   verbose=True
)
reasoning_chain = LLMChain(
   llm=llm,
   prompt=reasoning_prompt,
   output_key="counter_reasons",
   verbose=True
)
ranking_chain = LLMChain(
   llm=llm,
   prompt=ranking_prompt,
   output_key="Conversation",
   verbose=True
)
tot_chain = SequentialChain(
   chains=[solutions_chain, evalutation_chain, reasoning_chain, ranking_chain],
   input_variables=["the_statement"],
   output_variables=["Conversation"],
   verbose=True,
   return_all=True
)


result = (tot_chain.invoke(
        {
        "the_statement": "I should be able to do whatever I want on a public beack as long as it is not illegal.",
        }
    ))
print(result['Conversation'])


if __name__ == "__main__":
    pass
