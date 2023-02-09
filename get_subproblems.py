import openai
import os

openai.api_key = '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'


def get_subproblems(problem):
    """ 
    Given input string `problem` (question, essay prompt, etc), 
    return a List[str] of subproblems which can be sequentially answered to 
    answer the problem.
    """
    
    with open('prompts/reduce_problem.txt', 'r') as file:
        examples =  file.read()
        
    request = openai.Completion.create(
        model='text-davinci-003',
        prompt= examples + problem + '\n',
        temperature=0.7,
        presence_penalty=0.25,
        frequency_penalty=0.25,
        max_tokens=150,
        n=1
    )

    completion = request['choices'][0]['text'].strip()
    return [subproblem[4:] for subproblem in completion.split('\n')]

print(get_subproblems("Are utilitarianism or kantian ethics better?"))
