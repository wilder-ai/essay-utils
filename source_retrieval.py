try:
    from googlesearch import search
except ImportError:
    print('module {googlesearch} not found')
from newspaper import Article
import openai


def scrape_source_dicts(subproblem, num_sources):
    sources = []
    for url in search(subproblem, tld="com", start=1, stop=num_sources, pause=2):
        print(url)
        source = {}

        article = Article(url)
        article.download()
        article.parse()

        source['title'] = article.title
        if len(article.authors) > 0:
            source['author'] = article.authors[0]
        source['date'] = article.publish_date
        if len(article.text) < 2500:
            source['text'] = article.text
        else:
            source['text'] = article.text[:1250] + article.text[-1250:]
        sources.append(source)
    return sources


task = 'For the following source, write an APA reference then a summary focusing on new information that will help you write a paragraph on: '

def summarize_sources(sources):
    with open('prompts/summarize_sources') as f:
        example = f.read()
    
    
    
    

