import streamlit as st
import pandas as pd
import requests
from bs4 import BeautifulSoup
import re
from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt
from datetime import datetime

st.set_option('deprecation.showPyplotGlobalUse', False)

st.title(f"What they talk about today.")


today = datetime.now().strftime('%Y/%b/%d').lower()

web_adress = 'https://www.theguardian.com/uk'


def get_links(web_adress):
    website = requests.get(web_adress)
    soup = BeautifulSoup(website.content, 'html.parser')

    all_links = []

    for line in soup.find_all('a', href=True):
        link = line['href']
        if 'https://' in link:
            try:
                l = link.split('/')[3]
                all_links.append(link)
            except:
                continue
    return set(all_links)
    

def get_categories(all_links, date):
    daily = list(all_links)
    cat = []

    for line in all_links:
        if today not in line:
            daily.remove(line)
        elif 'video' in line:
            daily.remove(line)

    for l in daily:
        cat.append(l.split('/')[3])
    return set(cat)


def create_wordcloud(cat, all_links):
    daily = list(all_links)
    articles = ''

    art_adress = [web for web in daily if cat in web]    

    for adress in art_adress:
        website = requests.get(adress)
        soup_article = BeautifulSoup(website.content, 'html.parser')
        articles += soup_article.find(id='maincontent').text
    return articles

all_links = get_links(web_adress)
category = get_categories(all_links, today)

st.sidebar.image('https://images.unsplash.com/photo-1551406483-3731d1997540?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=987&q=80')
st.sidebar.header('select category and number of words')
cat = st.sidebar.selectbox('category', category)
words = st.sidebar.selectbox('number of words', range(50, 201, 50))

if cat is not None:


    articles = create_wordcloud(cat, all_links)

    st.markdown(f'### {cat} articles')

    stopwords = set(STOPWORDS)
    wordcloud = WordCloud(background_color='black', max_words=words, stopwords=stopwords, width=800, height=600).generate(articles)

    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis('off')
    plt.show()
    st.pyplot()