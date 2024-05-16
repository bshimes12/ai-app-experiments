## Tree of Thoughts: Deliberate Problem Solving with Large Language Models
## https://arxiv.org/abs/2305.10601

## python3 Advanced_tree_of_thought_Solver.py > my_solutions.txt

from langchain.prompts import PromptTemplate
from langchain.chains import SequentialChain
from langchain.chains.llm import LLMChain
from langchain_openai import ChatOpenAI
import theProblems
import sys
import os

from langchain.callbacks import StdOutCallbackHandler
from contextlib import redirect_stdout


# Get the absolute path of the root directory
ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
# Add the root directory to the Python path
sys.path.append(ROOT_DIR)

from myModules.config import set_environment
set_environment()

#llm = ChatOpenAI(temperature=0.7, model_name="gpt-3.5-turbo")
llm = ChatOpenAI(temperature=0.7, model_name="gpt-3.5-turbo-0125")
#llm = ChatOpenAI(temperature=0.7, model_name="gpt-4-0613")

solutions_template = """
You are a public policy expert with experience in implementing major programs. You think outside the box for creatives solutions.
Generate {num_solutions} distinct solutions for <problem>{problem}</problem>. 
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

handler = StdOutCallbackHandler()

tot_chain = SequentialChain(
   chains=[solutions_chain, evalutation_chain, reasoning_chain, ranking_chain],
   input_variables=["problem", "factors", "num_solutions"],
   output_variables=["ranked_solutions"],
   verbose=True,
   return_all=True,
   callbacks=[handler]
)


theProblem = """

**Introduction**: The lack of defined core metrics, ownership, and oversight is hindering the effectiveness of the organization in achieving its goals and objectives. Without clear metrics to measure progress, it is difficult to track performance and make informed decisions.

**Background**: In the past, the organization has struggled with setting and tracking key performance indicators (KPIs) due to a lack of clarity on ownership and oversight. This has led to confusion, inefficiencies, and missed opportunities for improvement. Previous attempts to address this issue have been short-lived and ineffective.

**Problem Description**: The core metrics are not clearly defined, leading to confusion and inconsistency in measuring performance. Without ownership of these metrics, there is no accountability for tracking and improving them. Additionally, the lack of oversight means that there is no mechanism in place to ensure that the metrics are being monitored and acted upon.

**Scope**: This problem statement focuses specifically on the lack of defined core metrics, ownership, and oversight within the organization. It does not address other potential issues that may be present in the organization.

"""

theFactors = """
**Factors Influencing the Problem**: Internal factors such as unclear roles and responsibilities, lack of communication, and resistance to change are contributing to the problem. External factors such as market competition and regulatory requirements may also impact the organization's ability to define and track core metrics effectively.
""" 

theNumSolutions = 3

output = (tot_chain.invoke(
        {
        "problem": theProblem,
        "factors": theFactors, 
        "num_solutions": theNumSolutions
        }
    ))

with open("output.txt", "w") as file:
    # Redirect stdout to the file
    with redirect_stdout(file):
        # Run the chain
        output = (tot_chain.invoke(
        {
        "problem": theProblem,
        "factors": theFactors, 
        "num_solutions": theNumSolutions
        }
    ))
    file.write("\nRanked Solutions:\n")
    file.write(str(output['ranked_solutions'])) 


#print(output['ranked_solutions'])


if __name__ == "__main__":
    pass
