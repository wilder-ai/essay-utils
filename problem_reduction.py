import openai
import os

openai.api_key = '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'

def get_fewshot_examples():
    with open('problem_reduction.txt', 'r') as file:
        return file.read()
    
def reduce_problem(problem):
    examples = get_fewshot_examples()
    request = openai.Completion.create(
        model='text-davinci-003',
        prompt= examples + problem,
        temperature=0.7,
        presence_penalty=0.25,
        frequency_penalty=0.25,
        max_tokens=150,
        n=1
    )

    completion = request['choices'][0]['text']
    return completion


    
    