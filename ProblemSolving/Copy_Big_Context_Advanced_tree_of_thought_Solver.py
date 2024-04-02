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


# Get the absolute path of the root directory
ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
# Add the root directory to the Python path
sys.path.append(ROOT_DIR)

from myModules.config import set_environment
set_environment()

#llm = ChatOpenAI(temperature=0.7, model_name="gpt-3.5-turbo")
#llm = ChatOpenAI(temperature=0.7, model_name="gpt-3.5-turbo-0125")
llm = ChatOpenAI(temperature=0.7, model_name="gpt-4-0613")

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
tot_chain = SequentialChain(
   chains=[solutions_chain, evalutation_chain, reasoning_chain, ranking_chain],
   input_variables=["problem", "factors", "num_solutions"],
   output_variables=["ranked_solutions"],
   verbose=True,
   return_all=True
)


theProblem = """

**Introduction**: The report generated for customers is not meeting the needs of all customers due to lack of customization.

**Background**: The current report generation process has been in place for some time, and while it works for most customers, there have been growing complaints about its inability to meet the unique needs of some customers. Previous attempts to address this issue have been limited by resource constraints.

**Problem Description**: The current report generation process is unable to provide customized reports for each individual customer, leading to dissatisfaction among some customers. This lack of customization impacts the ability of customers to extract value from the reports and may hinder their overall satisfaction with the product.

**Scope**: This problem statement focuses specifically on the limitations of the current report generation process and does not encompass broader issues related to customer satisfaction or product development.

"""

theFactors = """
**Factors Influencing the Problem**: Internal factors such as resource constraints and technological limitations are influencing the inability to customize reports for each customer. External factors such as differing customer needs and expectations also contribute to the problem.
""" 

theNumSolutions = 3

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
