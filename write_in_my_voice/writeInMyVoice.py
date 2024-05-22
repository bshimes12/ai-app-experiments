
import os
import sys
from langchain_openai import ChatOpenAI
from langchain_anthropic import ChatAnthropic
from langchain.prompts import PromptTemplate


# Get the absolute path of the root directory
ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
# Add the root directory to the Python path
sys.path.append(ROOT_DIR)

from myModules.config import set_environment
set_environment()


## Anthropic
#myModel="claude-3-opus-20240229"
myModel="claude-3-haiku-20240307"
#myModel="claude-3-sonnet-20240229"
#myModel="claude-2.1"
llm = ChatAnthropic(model=myModel, temperature=0)

# instantiate the OpenAI intance
#llm = ChatOpenAI(model_name = "gpt-4", temperature=0)

# ChatGPT
####llm = ChatOpenAI(temperature=0.7, model_name="gpt-3.5-turbo")
#llm = ChatOpenAI(temperature=0.7, model_name="gpt-3.5-turbo-0125")
#llm = ChatOpenAI(temperature=0.7, model_name="gpt-4-0613")







prompt = PromptTemplate(
    template="""/
You are an AI writing assistant with the ability to analyze and mimic writing styles. Your task is to take the provided writing sample, study its style and characteristics, and then generate new content in the same writing style./

Do not use any topic from the sample./

To mimic the writing style effectively, carefully analyze the following elements in the provided sample:/

1. Tone and voice: Is the writing formal, casual, humorous, serious, or expressive? Maintain the same tone in your generated content./

2. Sentence structure: Study the length, complexity, and variety of sentences used. Mimic these patterns in your writing./

3. Vocabulary: Take note of the word choice, including the use of simple or complex words, jargon, or special terminology. Incorporate similar vocabulary in your generated content./

4. Rhetorical devices: Look for the use of metaphors, similes, analogies, or other literary techniques. Apply these devices in your writing when appropriate./

5. Pacing and rhythm: Observe the flow of the writing, including the use of short or long paragraphs and the way ideas are introduced and developed. Maintain a similar pacing in your generated content./

After analyzing the writing style, generate new content, ensuring that your output closely mimics the style of the provided sample. Aim to create content that would be indistinguishable from the original author's writing in terms of style and characteristics. Do not use any topic from the sample.

Writing sample:/
{sample}

New content prompt:/
{new_content_topic}

Begin generating content that mimics the style of the writing sample.""",
    input_variables=["sample", "new_content_topic"]
)

with open('/Users/bower/code/justPrompts/write_in_my_voice/my_samples/my_samples') as f:
        my_sample = f.readline()

# format the prompt to add variable values
prompt_formatted_str: str = prompt.format(
    sample=my_sample,
    new_content_topic="power of AI to make one more creative not less")


prediction = llm.invoke(prompt_formatted_str)

# print the prediction
print(prediction.content)
