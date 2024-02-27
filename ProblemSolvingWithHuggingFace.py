from langchain.chains import LLMChain
from langchain_community.llms import HuggingFaceEndpoint
from langchain.prompts import PromptTemplate
from datetime import datetime
from config import set_environment

set_environment()

#repo_id = "mistralai/Mistral-7B-Instruct-v0.2"
#repo_id = "google/gemma-7b"
#repo_id = "google/gemma-2b"
#repo_id = "google/gemma-7b-it"
#repo_id = "google/flan-t5-xxl"
repo_id = "mistralai/Mixtral-8x7B-Instruct-v0.1"

myProblem = "Data for counting students getting on and off the bus is inaccurate."
# https://pawandongre.medium.com/32-chatgpt-prompts-to-improve-problem-solving-5440fed9c2f3
## Scenario Simulation Prompt:##
#myTemplate = "Simulate potential scenarios arising from implementing a solution to ( <situation> {myProblem} </situation>. Assess probable outcomes and repercussions."
## SWOT ## 
#myTemplate = "Conduct a SWOT analysis (Strengths, Weaknesses, Opportunities, Threats) for a proposed solution to a (specific problem: {problem})."

## Systems Thinking Approach ##
#myTemplate = "Analyze this specific problem: {problem} using a systems thinking approach. Map out interconnected elements, feedback loops, and potential leverage points."

## Predictive Modeling Prompt ##
#myTemplate = "Craft a predictive model to forecast outcomes of this specific situation: <situation> {problem} </situation>. Discuss assumptions, variables, and potential accuracy."

myTemplate = "Create a visual representation (e.g., mind map, flowchart) of <situation> {problem} </situation> detailing its facets, causes, and potential solutions."

prompt = PromptTemplate.from_template(myTemplate)

llm = HuggingFaceEndpoint(
    repo_id=repo_id, temperature=1
)

llm_chain = LLMChain(prompt=prompt, llm=llm)
outputFromModel = llm_chain.invoke(myProblem)

#print(outputFromModel['text'])


# get current date and time
current_datetime = datetime.now().strftime("%Y-%m-%d %H-%M-%S")
# convert datetime obj to string
str_current_datetime = str(current_datetime)
itHasForwardSlash = repo_id
# Remove all forward slashes
itDoesntHaveForwardSlash = itHasForwardSlash.replace("/", "")

f = open("file "+ itDoesntHaveForwardSlash + " " + str_current_datetime+ ".txt", "x")
f.write(outputFromModel['text'])
f.close()


if __name__ == "__main__":
    pass
