import re
import requests
from bs4 import BeautifulSoup

def extract_asin(url):
    match = re.search(r"/dp/([A-Z0-9]{10})", url)
    if match:
        return match.group(1)
    return None

def get_reviews_amazon(url):
    asin = extract_asin(url)
    if not asin:
        return []

    review_url = f"https://www.amazon.in/product-reviews/{asin}/"
    headers = {
        'User-Agent': 'Mozilla/5.0',
        'Accept-Language': 'en-US,en;q=0.9'
    }

    page = requests.get(review_url, headers=headers)
    if page.status_code != 200:
        print("Failed to fetch review page:", page.status_code)
        return []

    soup = BeautifulSoup(page.content, "html.parser")
    reviews = []

    for review in soup.select('span[data-hook="review-body"]'):
        reviews.append(review.get_text(strip=True))

    return reviews[:100]  # Return max 100 reviews
