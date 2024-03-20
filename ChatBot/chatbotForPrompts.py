
import os
import sys
import openai
import myActAsPrompts as myActAsPrompts

# Get the absolute path of the root directory
ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
# Add the root directory to the Python path
sys.path.append(ROOT_DIR)

from myModules.config import set_environment
set_environment()

from openai import OpenAI
client = OpenAI()

def chatbot():
  # Create a list to store all the messages for context
  messages = [
    {"role": "system", "content": myActAsPrompts.advertiser},
  ]

  # Keep repeating the following
  while True:
    # Prompt user for input
    message = input("User: ")

    # Exit program if user inputs "quit"
    if message.lower() == "quit":
      break

    # Add each new message to the list
    messages.append({"role": "user", "content": message})

    # Request gpt-3.5-turbo for chat completion
    response = client.chat.completions.create(
      model="gpt-3.5-turbo",
      messages=messages,
      temperature=1,
      max_tokens=150
    )

    # Print the response and add it to the messages list
    chat_message = response.choices[0].message.content
    #chat_message = response['choices'][0]['message']['content']
    print(f"Bot: {chat_message}")
    messages.append({"role": "assistant", "content": chat_message})

if __name__ == "__main__":
  print("Start chatting with the bot (type 'quit' to stop)!")
  chatbot()