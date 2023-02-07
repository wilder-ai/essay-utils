from googlesearch import search
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
        
        if len(article.authors) > 0:
            source['author'] = article.authors[0]
        source['date'] = article.publish_date
        words = article.text.split()
        if len(words) < 500:
            source['text'] = ' '.join(words)
        else:
            source['text'] = ' '.join(words[:250] + words[-250:])
            
        print(source)
        print('--------------------------\n\n\n')

scrape_source_dicts("what is intermittent fasting", 5)



