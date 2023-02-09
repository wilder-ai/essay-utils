try:
    from googlesearch import search
except ImportError:
    print('module {googlesearch} not found')
from newspaper import Article
import os
import openai

openai.api_key = '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'


def scrape_source_dicts(subproblem, num_sources, num_chars = 3000, urls_to_ignore = ()):
    """ 
    Given input str `subproblem` (usually a question), search Google for the
    top urls not contained in `urls_to_ignore`, and parse each into a dict
    with fields for author, date, title, url, and text of webpage.
    Returns a List[dict] of sources, with length `num_sources`.
    """
    
    sources = []
    for url in search(subproblem, tld="com", start=1, pause=2):
        if url in urls_to_ignore:
            continue
        
        try:
            article = Article(url)
            article.download()
            article.parse()
            
            source = {}
            if len(article.authors) != 0:
                source['AUTHOR'] = article.authors[0]
            source['DATE'] = article.publish_date.strftime("%m/%Y")
            source['TITLE'] = article.title
            source['URL'] = url
            source['TEXT'] = article.text[:num_chars]
                
            sources.append(source)
            if len(sources) == num_sources:
                break 
        except:
            continue
        
    return sources


def summarize_sources(subproblem, sources):
    """ 
    Given a str `subproblem` and List[dict] `sources`, summarise each source
    with respect to the subproblem. Returns a List[dict] where each dict has
    fields for reference and summary of its index-corresponding source.
    """
    source_summaries = []
    
    with open('prompts/summarize_sources.txt') as f:
        example = f.read()
    
    for source in sources:
        
        prompt = example + subproblem + '\n'
        for field, entry in source.items():
            prompt += field + ': ' + entry + '\n'
            
        prompt += 'REFERENCE:'
        
        request = openai.Completion.create(
            model='text-davinci-003',
            prompt= prompt,
            temperature=0.7,
            presence_penalty=0.25,
            frequency_penalty=0.5,
            max_tokens=300,
            n=1
        )

        completion = request['choices'][0]['text'].strip().split('SUMMARY:')
        source_summaries.append({
            'REFERENCE' : completion[0].strip(), 
            'SUMMARY' : completion[1].strip(),
            'URL': source['URL']})
    
    return source_summaries


def get_summaries(subproblem, num_sources, num_chars = 3000, urls_to_ignore = ()):
    return summarize_sources(subproblem, scrape_source_dicts(subproblem, num_sources, num_chars, urls_to_ignore))
        



    
    
    

