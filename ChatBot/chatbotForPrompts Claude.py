
import os
import anthropic
import myActAsPrompts as myActAsPrompts
import promptTeamPremortem as promptTeamPremortem
import promptTheBestCoach as promptTheBestCoach

#from config import set_environment
#set_environment()


my_api_key = "sk-ant-api03--a0r-lgAA"
client = anthropic.Anthropic(
    # defaults to os.environ.get("ANTHROPIC_API_KEY")
    api_key=my_api_key
)
"""

response = client.messages.create(
    model="claude-3-opus-20240229",
    max_tokens=1024,
    messages=[
        {"role": "user", "content": "Hello, Claude"}
    ]
)
#print(response.content)
"""





def chatbot():
  messages = [
   # {"role": "user", "content": myActAsPrompts.astrologer},
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
    response = client.messages.create(
      model="claude-3-opus-20240229",
      max_tokens=1024,
      messages=messages,
      temperature=1,
      system="you are an astrologer"
    )

    # Print the response and add it to the messages list
    chat_message = response.content
    #chat_message = response['choices'][0]['message']['content']
    print(f"Bot: {chat_message}")
    messages.append({"role": "assistant", "content": chat_message})

if __name__ == "__main__":
  print("Start chatting with the bot (type 'quit' to stop)!")
  chatbot()