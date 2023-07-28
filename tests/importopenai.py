import openai

openai.api_key = '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'

response = openai.Completion.create(
    engine="text-davinci-002",
    prompt="Translate the following English text to French: '{}'",
    max_tokens=60
)

print(response.choices[0].text.strip())
