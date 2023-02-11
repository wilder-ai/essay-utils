import openai
import os
from get_subproblems import get_subproblems
from api_key import KEY
openai.api_key = KEY

def write_introduction(problem, subproblems):
    """ 
    Given input str `problem` (question, essay prompt, etc), 
    and List[str] of subproblems representing an essay plan, return a str
    introduction to the essay.
    """
    
    with open('prompts/write_introduction.txt', 'r') as file:
        prompt =  file.read()
    prompt += problem + '\n'
    prompt += 'Essay Plan:' + '\n'
    for subproblem in subproblems:
        prompt += subproblem + '\n'
    prompt += 'Introduction:'
    
    request = openai.Completion.create(
        model='text-davinci-003',
        prompt=prompt,
        temperature=0.7,
        presence_penalty=0.25,
        frequency_penalty=0.5,
        max_tokens=300,
        n=1
    )

    return request['choices'][0]['text'].strip()


