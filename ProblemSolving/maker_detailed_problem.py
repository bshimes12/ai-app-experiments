from langchain.prompts import PromptTemplate
from langchain_openai import OpenAI
from langchain_openai import ChatOpenAI
from datetime import datetime
import detailed_problem_statement_template
import sys
import os
##################################
##################################
######   SETUP AND CONFIG   ######
##################################
##################################
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

##################################
##################################
##################################
##################################
##################################



##################################
##################################
########   The Action   ##########
##################################
##################################


# The definition template
theDefinition = detailed_problem_statement_template.outline_template
##################################
##################################
theProblem = "There is a property dispute between neighbors A and B. Neighbor A just planted landscaping on back of their property. Neighbor B claims that it is their property and they want to reclaim it even though it was previously unused. Neighbor B has some evidence this it is their propery but Neighbor A would like some sort of compromise because the property is neglected."
##################################
##################################
##################################
##################################

prompt = PromptTemplate(input_variables=["problem"], template=theDefinition)
chain = prompt | model
outputFromModel = chain.invoke({"problem": theProblem})

# get current date and time
current_datetime = datetime.now().strftime("%Y-%m-%d %H-%M-%S")
# convert datetime obj to string
str_current_datetime = str(current_datetime)
 
# create a file object along with extension
file_name = str_current_datetime+".txt"

f = open("f_THE_PROBLEM_" + theModel + "_" + str_current_datetime+ ".txt", "x")
f.write(outputFromModel.content)
f.close()


if __name__ == "__main__":
    pass
