from langchain.prompts import PromptTemplate
from langchain_openai import OpenAI
from langchain_openai import ChatOpenAI
from datetime import datetime
from langchain_core.output_parsers import StrOutputParser, CommaSeparatedListOutputParser, JsonOutputParser
from langchain_core.pydantic_v1 import BaseModel, Field
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
theProblem = "There are too many citizens not registered to vote that are therefore not represented."
##################################
##################################
##################################
##################################


def call_string_output_parser():
    prompt = PromptTemplate(input_variables=["problem"], template=theDefinition)
    parser = StrOutputParser()
    chain = prompt | model | parser
    return  chain.invoke({"problem": theProblem})

#print(call_string_output_parser())
def call_list_output_parser():
    prompt = PromptTemplate(input_variables=["problem"], template=theDefinition)
    parser = CommaSeparatedListOutputParser()
    chain = prompt | model | parser
    return  chain.invoke({"problem": theProblem})

#print(call_list_output_parser())
def call_json_output_parser():
    prompt = PromptTemplate(input_variables=["problem"], template=theDefinition)
    class Problem(BaseModel):
        problem_statement: str = Field(description="Introduction, Background")
        factors_involved: str = Field(description="FACTORS_INVOLVED:")

    parser = JsonOutputParser(pydantic_object=Problem)
    chain = prompt | model | parser
    return  chain.invoke({"problem": theProblem, "format_instructions":parser.get_format_instructions()})
print(call_json_output_parser())


"""
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
"""