from flask import Flask, render_template
from newsapi import NewsApiClient

app = Flask(__name__)

@app.route('/')
def Index():
    newsapi = NewsApiClient(api_key="e8902ba0f9454263b59e19a6f175c99c")
    topheadlines = newsapi.get_top_headlines(sources="bitcoin.com")

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
@app.route('/bbc')
def bbc():
    newsapi = NewsApiClient(api_key="e8902ba0f9454263b59e19a6f175c99c")
    topheadlines = newsapi.get_top_headlines(sources="bbc-news")

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


    return render_template('bbc.html', context = mylist)
    
@app.route('/fox')
def fox():
    newsapi = NewsApiClient(api_key="e8902ba0f9454263b59e19a6f175c99c")
    topheadlines = newsapi.get_top_headlines(sources="fox-news")

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


    return render_template('fox.html', context = mylist)
@app.route('/nbc')
def nbc():
    newsapi = NewsApiClient(api_key="e8902ba0f9454263b59e19a6f175c99c")
    topheadlines = newsapi.get_top_headlines(sources="nbc-news")

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


    return render_template('nbc.html', context = mylist)
    
if __name__ == "__main__":
    app.run(debug=True)
    app.run