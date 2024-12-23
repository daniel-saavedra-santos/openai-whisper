from openai import OpenAI

client = OpenAI(
  api_key="PUT_YOUR_API_KEY_HERE"
)

completion = client.chat.completions.create(
  model="gpt-4o-mini",
  messages=[
    {"role": "user", "content": "write a haiku about ai"}
  ]
)

print(completion.choices[0].message);
