from openai import OpenAI
 
# pip install openai 
# if you saved the key under a different environment variable name, you can do something like:
client = OpenAI(
  api_key="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",
)

completion = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "system", "content": "You are a virtual assistant named jarvis skilled in general tasks like Alexa and Google Cloud"},
    {"role": "user", "content": "what is coding"}
  ]
)

print(completion.choices[0].message.content)