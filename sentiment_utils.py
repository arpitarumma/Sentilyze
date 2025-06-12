from bs4 import BeautifulSoup
import requests
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import pandas as pd

def get_reviews_amazon(url, max_reviews=20):
    headers = {"User-Agent": "Mozilla/5.0"}
    r = requests.get(url, headers=headers)
    soup = BeautifulSoup(r.content, "html.parser")
    reviews = [tag.get_text(strip=True) for tag in soup.find_all('span', {'data-hook': 'review-body'})][:max_reviews]
    return reviews

def analyze_reviews(reviews):
    sid = SentimentIntensityAnalyzer()
    data = []
    for r in reviews:
        score = sid.polarity_scores(r)['compound']
        sentiment = "Positive" if score > 0.05 else "Negative" if score < -0.05 else "Neutral"
        data.append({"review": r, "compound": score, "sentiment": sentiment})
    return pd.DataFrame(data)

