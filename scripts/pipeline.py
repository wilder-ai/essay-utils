import openai
import os
from get_subproblems import *
from source_retrieval import *
from write_introduction import *
from add_paragraph import *
from add_conclusion import *

openai.api_key = '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'


def pipeline(problem, sources_per_body = 2, frequency_penalty = 1):
    subproblems = get_subproblems(problem)
    print(subproblems)
    essay = write_introduction(problem, subproblems)
    
    urls_used = []
    for subproblem in subproblems:
        sources = get_summaries(subproblem, sources_per_body, urls_to_ignore=urls_used)
        for s in sources:
            urls_used.append(s['URL'])
        essay += '\n\n' + add_paragraph(problem, subproblem, sources, essay)
    essay += '\n\n' + add_conclusion(problem, subproblem, essay)
    
    return essay


if __name__ == '__main__':
    problem = 'How good would life be in a post-scarcity civilization?'
    
    with open('essays/essay.txt', 'w') as f:
        f.write(problem + '\n\n')
        f.write(pipeline(problem, 2, 1.25))
