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

"""
prompt = 
Develop a offbeat brand identity for a new website called \"ideaatoms.\" 
The brand focuses on exploring the cool hands-on capabilities of generative AI. ideaatoms is calm and a place where there are no stupid questions.\n\n
The brand identity should achieve the following goals:\n
1. Make people curious.\n
2. Be a commentary on AI as a cognitive advancement.\n
3. A key point is that humans now computers can reason.\n
4. Make it fresh and clear and simple.\n
Do not make spelling mistakes.
"""

prompt = """
dog riding a pony next to a fox
"""
#prompt = 'cute bunny being chased by fox'

client = OpenAI()

response = client.images.generate(
    prompt=prompt,
    n=1,
    size="1792x1024",
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