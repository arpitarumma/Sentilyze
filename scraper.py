# scraper.py
from bs4 import BeautifulSoup
import requests

def get_reviews_amazon(url):
    headers = {'User-Agent': 'Mozilla/5.0'}
    page = requests.get(url, headers=headers)
    soup = BeautifulSoup(page.content, "html.parser")
    reviews = []

    for review in soup.select('.review-text-content span'):
        reviews.append(review.text.strip())

    return reviews[:100]  # Limit to first 100 reviews
