import anthropic
my_api_key = "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"

client = anthropic.Anthropic(
    # defaults to os.environ.get("ANTHROPIC_API_KEY")
    api_key=my_api_key,
)
message = client.messages.create(
    model="claude-3-opus-20240229",
    
    max_tokens=1024,
    messages=[
        {"role": "user", "content": "Hello, Claude"}
    ]
)
print(message.content)