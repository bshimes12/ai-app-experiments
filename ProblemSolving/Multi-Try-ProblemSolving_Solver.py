from langchain.prompts import PromptTemplate
from langchain_openai import OpenAI
from langchain_openai import ChatOpenAI
from datetime import datetime
import ProblemSolvingTechniques
import theProblems

import sys
import os

# Get the absolute path of the root directory
ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
# Add the root directory to the Python path
sys.path.append(ROOT_DIR)

from myModules.config import set_environment
set_environment()

#theModel = 'gpt-3.5-turbo-instruct' # Use model=OpenAI and from langchain_openai import OpenAI
theModel = 'gpt-3.5-turbo-0125' # use model = ChatOpenAI and from langchain_openai import ChatOpenAI

model = ChatOpenAI(
    model=theModel,
    temperature=1.0, verbose=True)


#### Importing a complicated problem statement
"""
theSituation = theProblems.TheNoisyPickleballGame()
theProblem = theSituation["THE_PROBLEM"]  
"""
#### Simple String
theProblem = "The report I generate for every customer works for most customers but not everyone. I do not have resources to customize a report for each customer." 

#### How do you want to solve it
myTechnique = ProblemSolvingTechniques.FailureModeAnalysis

prompt = PromptTemplate(input_variables=["problem"], template=myTechnique)
chain = prompt | model
outputFromModel = chain.invoke({"problem": theProblem})

print(outputFromModel.content)

#####Output a file 
"""
# get current date and time
current_datetime = datetime.now().strftime("%Y-%m-%d %H-%M-%S")
# convert datetime obj to string
str_current_datetime = str(current_datetime)
 
# create a file object along with extension
file_name = str_current_datetime+".txt"

f = open("f_ProblemSolving_" + theModel + "_" + str_current_datetime+ ".txt", "x")
f.write(outputFromModel.content)
f.close()
"""


if __name__ == "__main__":
    pass
