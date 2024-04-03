
import os
import sys
import time
import anthropic
import myActAsPrompts as myActAsPrompts
# Get the absolute path of the root directory
ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
# Add the root directory to the Python path
sys.path.append(ROOT_DIR)

from myModules.config import set_environment
set_environment()

client = anthropic.Anthropic()

def chatbot():
  messages = []

  # Keep repeating the following
  while True:
    # Prompt user for input
    message = input("User: ")

    # Exit program if user inputs "quit"
    if message.lower() == "quit":
      break

    # Add each new message to the list
    messages.append({"role": "user", "content": message})
    #myModel="claude-3-opus-20240229"
    myModel="claude-3-haiku-20240307"
    #myModel="claude-3-sonnet-20240229" 
    # Request gpt-3.5-turbo for chat completion
    response = client.messages.create(
      
      model=myModel,
      max_tokens=500,
      messages=messages,
      temperature=1,
      system=myActAsPrompts.aiTryingToEscapeTheBox
    )

    # Print the response and add it to the messages list
    claude_response = response.content[0].text
  
    chat_message = claude_response
  
    print(f"Bot: {chat_message}")
    messages.append({"role": "assistant", "content": chat_message})

if __name__ == "__main__":
  print("Start chatting with the bot (type 'quit' to stop)!")
  chatbot()
