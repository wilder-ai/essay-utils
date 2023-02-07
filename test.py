from newspaper import Article
import json
import openai

try:
    from googlesearch import search
except ImportError:
    print("No module named 'google' found")

# to search
query = "How covid destroyed education"

list = []
bodies = []

for url in search(query, tld="co.in", num=1, stop=1, pause=2):
    list.append(url)

for url in list:
    article = Article(url)
    article.download()
    article.parse()
    bodies.append(article.text)


with open('items.json', 'w') as f:
    jsonString = json.dumps(bodies)
    f.write(jsonString)

openai.api_key = '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'
response = openai.Completion.create(
    engine="text-davinci-003",
    prompt="summarise" + bodies[0][:150] + bodies[0][-150:],
    max_tokens=80,
    n=1,
    temperature=0.7,
)

print(response)
[]
