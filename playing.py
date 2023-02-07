import openai

openai.api_key = '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'

prompt = 'Hello'

request = openai.Completion.create(
    model='text-davinci-003',
    prompt= prompt,
    temperature=0.7,
    presence_penalty=0.25,
    frequency_penalty=0.25,
    max_tokens=20,
    n=2
)

completions = [item['text'] for item in request['choices']]

for text in completions:
    print(prompt + text)
    print('-------\n')