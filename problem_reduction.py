import openai
import os

openai.api_key = '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'


def reduce_problem(problem):
    with open('prompts/reduce_problem.txt', 'r') as file:
        example =  file.read()
        
    request = openai.Completion.create(
        model='text-davinci-003',
        prompt= example + problem,
        temperature=0.7,
        presence_penalty=0.25,
        frequency_penalty=0.25,
        max_tokens=150,
        n=1
    )

    completion = request['choices'][0]['text']
    return completion.split('\n')

print(reduce_problem("how can machine learning researchers act environmentally responsibly?"))

    
