import os
import sys
from datetime import datetime
from openai import OpenAI

# Get the absolute path of the root directory
ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
# Add the root directory to the Python path
sys.path.append(ROOT_DIR)

from myModules.config import set_environment
set_environment()


client = OpenAI()

audio_file= open("/Users/bower/Downloads/conv.m4a", "rb")
transcription = client.audio.transcriptions.create(
  model="whisper-1", 
  file=audio_file,
  response_format="text"
)
theText = transcription
print(theText)



#####Output a file 

# get current date and time
current_datetime = datetime.now().strftime("%Y-%m-%d %H-%M-%S")
# convert datetime obj to string
str_current_datetime = str(current_datetime)
 
# create a file object along with extension
filepath= "/Users/bower/code/justPrompts/read_doc_ask_questions/"

print(theText)
"""
f = open(filepath+"conversation.txt", "x")
f.write(theText)
f.close()
"""