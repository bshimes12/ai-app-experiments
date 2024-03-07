## Tree of Thoughts: Deliberate Problem Solving with Large Language Models
## https://arxiv.org/abs/2305.10601

from langchain.prompts import PromptTemplate
from langchain.chains import SequentialChain
from langchain.chains.llm import LLMChain
from langchain_openai import ChatOpenAI
import theProblems
from config import set_environment

set_environment()

#llm = ChatOpenAI(temperature=0.7, model_name="gpt-3.5-turbo")
llm = ChatOpenAI(temperature=0.7, model_name="gpt-3.5-turbo-0125")
#llm = ChatOpenAI(temperature=0.7, model_name="gpt-4-0613")

solutions_template = """
You are a system engineer with a strong command of technical problem solving techniques 
to decompose problems. 
Generate {num_solutions} distinct solutions for {problem}. 
Consider factors like {factors}. 
Solutions:
"""
solutions_prompt = PromptTemplate(
   template=solutions_template,
   input_variables=["problem", "factors", "num_solutions"]
)
evaluation_template = """
Evaluate each solution in {solutions} by analyzing pros, cons, feasibility, and probability of success.

Evaluations:
"""
evaluation_prompt = PromptTemplate(
  template=evaluation_template,
  input_variables=["solutions"]
)
reasoning_template = """
For the most promising solutions in {evaluations}, explain scenarios, implementation strategies, partnerships needed, and handling potential obstacles. 
Enhanced Reasoning: 
"""
reasoning_prompt = PromptTemplate(
  template=reasoning_template,
  input_variables=["evaluations"]
)
ranking_template = """
Based on the evaluations and reasoning, rank the solutions in {enhanced_reasoning} from most to least promising.
If you doubt anything about the solutions, write questions that are needed to address those doubts.
Ranked Solutions:
"""
ranking_prompt = PromptTemplate(
  template=ranking_template,
  input_variables=["enhanced_reasoning"]
)

solutions_chain = LLMChain(
   llm=llm,
   prompt=solutions_prompt,
   output_key="solutions",
   verbose=True
)
evalutation_chain = LLMChain(
   llm=llm,
   prompt=evaluation_prompt,
   output_key="evaluations",
   verbose=True
)
reasoning_chain = LLMChain(
   llm=llm,
   prompt=reasoning_prompt,
   output_key="enhanced_reasoning",
   verbose=True
)
ranking_chain = LLMChain(
   llm=llm,
   prompt=ranking_prompt,
   output_key="ranked_solutions",
   verbose=True
)
tot_chain = SequentialChain(
   chains=[solutions_chain, evalutation_chain, reasoning_chain, ranking_chain],
   input_variables=["problem", "factors", "num_solutions"],
   output_variables=["ranked_solutions"],
   verbose=True
)

theSituation = theProblems.TheRestaurantDefinition()
theProblem = theSituation["THE_PROBLEM"]  
theFactors = theSituation["THE_FACTORS"]  

theNumSolutions = 5

result = (tot_chain.invoke(
        {
        "problem": theProblem,
        "factors": theFactors, 
        "num_solutions": theNumSolutions
        }
    ))
print(result['ranked_solutions'])


if __name__ == "__main__":
    pass
