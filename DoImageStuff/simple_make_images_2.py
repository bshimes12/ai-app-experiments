from openai import OpenAI
import requests
import os
import sys

# Get the absolute path of the root directory
ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
# Add the root directory to the Python path
sys.path.append(ROOT_DIR)

from myModules.config import set_environment
set_environment()


prompt = """
Develop a offbeat brand identity for a new silly website called \"AI Art Barf.\" The brand focuses on creating funny and entertaining images that are from AI hallucinations. AI Art Barf is in good taste and not mean-spirited.\n\nThe brand identity should achieve the following goals:\n1. Make people laugh.\n2. Be a commentary on AI Art and that it is sometimes weird and funny.\n3. A key point is that humans are critics and robots (AI) are not.\n4. Make it funny and a bit retro and odd like an AI hallucination.
"""
#prompt = 'cute bunny being chased by fox'

client = OpenAI()

response = client.images.generate(
    prompt=prompt,
    n=1,
    size="1024x1024",
    response_format="url",
    quality="standard",
    model="dall-e-3",
)

if response:
    image_url = response.data[0].url
    
    image_data = requests.get(image_url).content
    
    file_name = 'generated_image.png'
    with open(file_name, 'wb') as file:
        file.write(image_data)
    
    print(f'Image saved as {file_name}')
else:
    print('Request failed.')