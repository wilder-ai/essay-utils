try:
    from googlesearch import search
except ImportError:
    print('module {googlesearch} not found')
from newspaper import Article
import openai


def scrape_source_dicts(subproblem, num_sources, urls_to_ignore = ()):
    """ 
    Given input string `subproblem` (usually a question), search Google for the
    top urls not contained in `urls_to_ignore`, and parse each into a dict
    with fields for author, date, title, url, and text of webpage.
    Returns a List[dict] of sources, with length `num_sources`.
    """
    
    sources = []
    for url in search(subproblem, tld="com", start=1, pause=2):
        print('tried one')
        if url in urls_to_ignore:
            continue
        
        try:
            article = Article(url)
            article.download()
            article.parse()
            
            source = {}
            if len(article.authors != 0):
                source['AUTHOR'] = article.authors[0]
            source['DATE'] = article.publish_date.strftime("%m/%Y")
            source['TITLE'] = article.title
            source['URL'] = url
            source['TEXT'] = article.text[:3000]
                
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
    
    with open('prompts/summarize_sources') as f:
        example = f.read()
    
    for source in sources:
        summary = []
        
        prompt = example + subproblem + '\n'
        for field, entry in source:
            prompt += field + ': ' + entry + '\n'
            
        prompt += 'REFERENCE:'
        
        request = openai.Completion.create(
            model='text-davinci-003',
            prompt= examples + problem + '\n',
            temperature=0.7,
            presence_penalty=0.25,
            frequency_penalty=0.25,
            max_tokens=150,
            n=1
        )

        completion = request['choices'][0]['text'].strip().split('SUMMARY:')
        summary.append({
            'REFERENCE' : completion[0].strip(), 
            'SUMMARY' : completion[1].strip()})
        summaries.append(summary)
    
    return summaries
        
x = scrape_source_dicts("Are utilitarianism or kantian ethics better?", 3)
print(x)

# print(summarize_sources("In what ways does utilitarianism better address modern life than Kantian ethics?"))
    
    
    
    

