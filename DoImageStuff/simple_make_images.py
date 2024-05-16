from openai import OpenAI
import webbrowser
import os
import sys
import json


# Get the absolute path of the root directory
ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
# Add the root directory to the Python path
sys.path.append(ROOT_DIR)

from myModules.config import set_environment
set_environment()

# Replace YOUR_API_KEY with your OpenAI API key
client = OpenAI()

response = client.images.generate(
  model="dall-e-3",
  prompt="Feel like you are getting left behind in the AI craze? Get a 1:1 session with an expert to help answer your questions. Style: soft, calm, natural",
  size="1024x1024",
  quality="standard",
  n=1,
  response_format="url",
)




# Show the result that has been pushed to an url
#webbrowser.open(response.data[0].url)
#response.json

image_url = response.data[0].url
    
image_data = requests.get(image_url).content

file_name = 'generated_image.png'
with open(file_name, 'wb') as file:
    file.write(image_data)

print(f'Image saved as {file_name}')