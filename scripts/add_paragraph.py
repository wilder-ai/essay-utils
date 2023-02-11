import openai
import os
from source_retrieval import get_summaries
from api_key import KEY
openai.api_key = KEY

def add_paragraph(problem, subproblem, source_summaries, current_essay, frequency_penalty=1):
    """ 
    Given input str `problem` (question, essay prompt, etc), 
    str `subproblem` (topic for a paragraph), List[Dict] source_summaries,
    and str `current_essay`, add a paragraph tackling the given subproblem
    to the current essay, with reference to the source.
    """
    
    with open('prompts/add_paragraph.txt', 'r') as file:
        prompt =  file.read()
    prompt += problem + '\n'
    prompt += 'Essay so far:\n'
    prompt += current_essay + '\n\n'
    
    prompt += f'Next paragraph (on {subproblem}):' 
    request = openai.Completion.create(
        model='text-davinci-003',
        prompt=prompt,
        temperature=0.7,
        presence_penalty=0.25,
        frequency_penalty=frequency_penalty,
        max_tokens=500,
        n=1
    )

    paragraph = request['choices'][0]['text'].strip()
    
    prompt = "Read the below sources. Rewrite the above paragraph, by inserting sentences giving specific examples from the sources to illustrate points made in the paragraph, with analysis explaining how the evidence backs up the points. When you use the sources, cite them in (author, year) form. Don't remove any text from the original paragraph.\nSources:\n"
    
    for source in source_summaries:
        prompt += 'Reference: ' + source['REFERENCE'] + '\n'
        prompt += 'Summary: ' + source['SUMMARY'] + '\n\n'
    prompt += 'Paragraph:\n' + paragraph + '\n\n'
    prompt += 'Revised Paragraph using Sources:'
        
    request = openai.Completion.create(
        model='text-davinci-003',
        prompt=prompt,
        temperature=0.7,
        presence_penalty=0.25,
        frequency_penalty=frequency_penalty,
        max_tokens=500,
        n=1
    )

    reinforced = request['choices'][0]['text'].strip()
    
    return reinforced
