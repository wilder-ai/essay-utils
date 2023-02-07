try:
    from googlesearch import search
except ImportError:
    print('module {googlesearch} not found')
from newspaper import Article
import openai


def scrape_source_dicts(subproblem, num_sources): 
    sources = []
    for url in search(subproblem, tld="com", num=num_sources, stop=num_sources, pause=2):
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
            
        print(source['title'])
        print(source['text'][:500])
        print('--------------------------\n\n\n')

scrape_source_dicts("how much exercise do adults need?", 5)



