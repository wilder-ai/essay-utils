import openai
import os
from get_subproblems import *
from source_retrieval import *
from write_introduction import *
from add_paragraph import *
from add_conclusion import *
from api_key import KEY
openai.api_key = KEY

def pipeline(problem, sources_per_body = 2, frequency_penalty = 1, verbose = False):
    subproblems = get_subproblems(problem)
    if verbose: print(f"subproblems: {subproblems}")
    
    essay = write_introduction(problem, subproblems)
    if verbose: print("intro done")
    
    urls_used = []
    for subproblem in subproblems:
        sources = get_summaries(subproblem, sources_per_body, urls_to_ignore=urls_used)
        for s in sources:
            urls_used.append(s['URL'])        
        if verbose: print(sources)

        paragraph = add_paragraph(problem, subproblem, sources, essay)
        essay += '\n\n' + paragraph 
        if verbose: print("body pgh done" + '\n\n')


    conclusion = add_conclusion(problem, subproblem, essay)
    essay += '\n\n' + conclusion
    
    return essay


if __name__ == '__main__':
    problem = 'To what extent does intermittent fasting improve our health?'
    essay = pipeline(problem, 2, 1.5, True)
    
    with open('essays/essay.txt', 'w') as f:
        f.write(problem + '\n\n')
        f.write(essay)
