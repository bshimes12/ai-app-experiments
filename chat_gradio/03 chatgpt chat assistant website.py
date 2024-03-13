import openai
import gradio

openai.api_key = "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"

messages = [{"role": "system", "content": "I want you to act as a mathematical history teacher and provide information about the historical development of mathematical concepts and the contributions of different mathematicians. You should only provide information and not solve mathematical problems. Use the following format for your responses: {mathematician/concept} - {brief summary of their contribution/development}. My first question is What is the contribution of Pythagoras in mathematics?"}]

def CustomChatGPT(user_input):
    messages.append({"role": "user", "content": user_input})
    response = openai.chat.completions.create(
        model = "gpt-3.5-turbo",
        messages = messages
    )
    ChatGPT_reply = response.choices[0].message.content
    messages.append({"role": "assistant", "content": ChatGPT_reply})
    return ChatGPT_reply

demo = gradio.Interface(fn=CustomChatGPT, inputs = "text", outputs = "text", title = "Real Estate Pro")

#demo.launch(share=True)
demo.launch()