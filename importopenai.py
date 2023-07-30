import openai

openai.api_key = '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'

response = openai.Completion.create(
    engine="text-davinci-002",
    prompt="Translate the following English text to French: '{}'",
    max_tokens=60
)

print(response.choices[0].text.strip())
