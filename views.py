from flask import Flask, render_template
from newsapi import NewsApiClient

app = Flask(__name__)

@app.route('/')
def Index():
    newsapi = NewsApiClient(api_key="bbb081415b6b417eb5d3fbfe57199cf8")
    topheadlines = newsapi.get_top_headlines(sources="the-wall-street-journal")

    articles = topheadlines['articles']

    desc = []
    news = []
    img = []
    url = []
    publAt = []

    for i in range(len(articles)):
        myarticles = articles[i]

        news.append(myarticles['title'])
        desc.append(myarticles['description'])
        img.append(myarticles['urlToImage'])
        url.append(myarticles['url'])
        publAt.append(myarticles['publishedAt'])
        

    mylist = zip(news, desc, img,url,publAt)

    return render_template('index.html', context = mylist)
@app.route('/reuters')
def reuters():
    newsapi = NewsApiClient(api_key="bbb081415b6b417eb5d3fbfe57199cf8")
    topheadlines = newsapi.get_top_headlines(sources="reuters")

    articles = topheadlines['articles']

    desc = []
    news = []
    img = []
    url = []
    publAt = []

    for i in range(len(articles)):
        myarticles = articles[i]

        news.append(myarticles['title'])
        desc.append(myarticles['description'])
        img.append(myarticles['urlToImage'])
        url.append(myarticles['url'])
        publAt.append(myarticles['publishedAt'])

    mylist = zip(news, desc, img,url,publAt)


    return render_template('reuters.html', context = mylist)
    
@app.route('/techcrunch')
def techcrunch():
    newsapi = NewsApiClient(api_key="bbb081415b6b417eb5d3fbfe57199cf8")
    topheadlines = newsapi.get_top_headlines(sources="techcrunch")

    articles = topheadlines['articles']

    desc = []
    news = []
    img = []
    url = []
    publAt = []

    for i in range(len(articles)):
        myarticles = articles[i]

        news.append(myarticles['title'])
        desc.append(myarticles['description'])
        img.append(myarticles['urlToImage'])
        url.append(myarticles['url'])
        publAt.append(myarticles['publishedAt'])

    mylist = zip(news, desc, img,url,publAt)


    return render_template('techcrunch.html', context = mylist)
@app.route('/insider')
def insider():
    newsapi = NewsApiClient(api_key="bbb081415b6b417eb5d3fbfe57199cf8")
    topheadlines = newsapi.get_top_headlines(sources="business-insider")

    articles = topheadlines['articles']

    desc = []
    news = []
    img = []
    url = []
    publAt = []

    for i in range(len(articles)):
        myarticles = articles[i]

        news.append(myarticles['title'])
        desc.append(myarticles['description'])
        img.append(myarticles['urlToImage'])
        url.append(myarticles['url'])
        publAt.append(myarticles['publishedAt'])

    mylist = zip(news, desc, img,url,publAt)


    return render_template('insider.html', context = mylist)
    
if __name__ == "__main__":
    app.run(debug=True)
    app.run