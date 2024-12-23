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
