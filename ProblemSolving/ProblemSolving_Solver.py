from langchain.prompts import PromptTemplate
from langchain_openai import OpenAI
from langchain_openai import ChatOpenAI
from datetime import datetime
import ProblemSolvingTechniques
import theProblems


#from config import set_environment

#set_environment()

#theModel = 'gpt-3.5-turbo-instruct' # Use model=OpenAI and from langchain_openai import OpenAI
theModel = 'gpt-3.5-turbo-0125' # use model = ChatOpenAI and from langchain_openai import ChatOpenAI

model = ChatOpenAI(
    model=theModel,
    temperature=1.0, verbose=True)


# The Problem
theSituation = theProblems.TheNoisyPickleballGame()
theProblem = theSituation["THE_PROBLEM"]  
myTechnique = ProblemSolvingTechniques.FeedbackLoopCreation

prompt = PromptTemplate(input_variables=["problem"], template=myTechnique)
chain = prompt | model
outputFromModel = chain.invoke({"problem": theProblem})
#print(outputFromModel)
#print(outputFromModel.content)


# get current date and time
current_datetime = datetime.now().strftime("%Y-%m-%d %H-%M-%S")
# convert datetime obj to string
str_current_datetime = str(current_datetime)
 
# create a file object along with extension
file_name = str_current_datetime+".txt"

f = open("f_ProblemSolving_" + theModel + "_" + str_current_datetime+ ".txt", "x")
f.write(outputFromModel.content)
f.close()


if __name__ == "__main__":
    pass
