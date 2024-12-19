from openai import OpenAI

client = OpenAI(
  api_key="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"
)

completion = client.chat.completions.create(
  model="gpt-4o-mini",
  messages=[
    {"role": "user", "content": "write a haiku about ai"}
  ]
)

print(completion.choices[0].message);
