import os
import sys
import anthropic


# Get the absolute path of the root directory
ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
# Add the root directory to the Python path
sys.path.append(ROOT_DIR)
from myModules.config import set_environment


set_environment()

client = anthropic.Anthropic()
#model="claude-3-sonnet-20240229"
model="claude-3-opus-20240229"

message = client.messages.create(
    model=model,
    max_tokens=1000,
    temperature=1,
    system="Your task is to create a comprehensive design brief for a holistic brand identity based on the given specifications. The brand identity should encompass various elements such as the brand name, logo, color palette, typography, visual style, tone of voice, and overall brand personality. Ensure that all elements work together harmoniously to create a cohesive and memorable brand experience that effectively communicates the brand's values, mission, and unique selling proposition to its target audience.",
    messages=[
        {"role": "user", "content": "Develop a offbeat brand identity for a new silly website called \"AI Art Barf.\" The brand focuses on creating funny and entertaining images that are from AI hallucinations. AI Art Barf is in good taste and not mean-spirited.\n\nThe brand identity should achieve the following goals:\n1. Make people laugh.\n2. Be a commentary on AI Art and that it is sometimes weird and funny.\n3. A key point is that humans are critics and robots (AI) are not.\n4. Make it funny and a bit retro and odd like an AI hallucination."}
    ]
)
print(message.content[0].text)

