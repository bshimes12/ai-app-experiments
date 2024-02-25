from langchain.prompts import PromptTemplate
from langchain_openai import OpenAI
from langchain_openai import ChatOpenAI
from datetime import datetime


from config import set_environment

set_environment()

#theModel = 'gpt-3.5-turbo-instruct' # Use model=OpenAI and from langchain_openai import OpenAI
theModel = 'gpt-3.5-turbo-0125' # use model = ChatOpenAI and from langchain_openai import ChatOpenAI

model = ChatOpenAI(
    model=theModel,
    temperature=1.0)

#myTemplate = "Classify the sentiment of this text: {text}"

## SWOT ## 
#myTemplate = "Conduct a SWOT analysis (Strengths, Weaknesses, Opportunities, Threats) for a proposed solution to a (specific problem: {problem})."

## Systems Thinking Approach ##
#myTemplate = "Analyze this specific problem: {problem} using a systems thinking approach. Map out interconnected elements, feedback loops, and potential leverage points."

## Predictive Modeling Prompt ##
#myTemplate = "Craft a predictive model to forecast outcomes of this specific situation: <situation> {problem} </situation>. Discuss assumptions, variables, and potential accuracy."

## Scenario Simulation Prompt:##
myTemplate = "Simulate potential scenarios arising from implementing a solution to ( <situation> {problem} </situation>. Assess probable outcomes and repercussions."

# The Problem
myProblem = "We never know what is for dinner and it is always a topic but usually it is too late in the day so that we are very hard pressed to come up with healthy and easy options."

prompt = PromptTemplate(input_variables=["problem"], template=myTemplate)
chain = prompt | model
outputFromModel = chain.invoke({"problem": myProblem})
#print(outputFromModel)
#print(outputFromModel.content)


# get current date and time
current_datetime = datetime.now().strftime("%Y-%m-%d %H-%M-%S")
# convert datetime obj to string
str_current_datetime = str(current_datetime)
 
# create a file object along with extension
file_name = str_current_datetime+".txt"

f = open("file "+ theModel + " " + str_current_datetime+ ".txt", "x")
f.write(outputFromModel.content)
f.close()


if __name__ == "__main__":
    pass
