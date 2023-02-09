import openai
import os
from source_retrieval import get_summaries

openai.api_key = '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'


def add_conclusion(problem, subproblem, current_essay, frequency_penalty=1):
    """ 
    Given input str `problem` (question, essay prompt, etc), 
    str `subproblem` (topic for a paragraph), List[Dict] source_summaries,
    and str `current_essay`, add a paragraph tackling the given subproblem
    to the current essay, with reference to the source.
    """
    
    with open('prompts/add_conclusion.txt', 'r') as file:
        prompt =  file.read()
    prompt += problem + '\n'
    prompt += 'Essay so far:\n'
    prompt += current_essay
    prompt += f'Conclusion, answering the question ({problem}):' 
    request = openai.Completion.create(
        model='text-davinci-003',
        prompt=prompt,
        temperature=0.7,
        presence_penalty=0.25,
        frequency_penalty=frequency_penalty,
        max_tokens=500,
        n=1
    )

    return request['choices'][0]['text'].strip()