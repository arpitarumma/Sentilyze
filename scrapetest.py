import requests
from bs4 import BeautifulSoup
import re

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)",
    "Accept-Language": "en-US, en;q=0.5"
}

def get_reviews(asin):
    url = f"https://www.amazon.in/product-reviews/{asin}/"
    response = requests.get(url, headers=headers)

    if response.status_code != 200:
        print("Failed to fetch page:", response.status_code)
        return []

    soup = BeautifulSoup(response.content, "html.parser")
    review_blocks = soup.find_all("span", {"data-hook": "review-body"})

    reviews = [review.get_text(strip=True) for review in review_blocks]
    return reviews

# Test
asin = "935333845X"
reviews = get_reviews(asin)
print(f"Fetched {len(reviews)} reviews.")
for r in reviews[:3]:
    print("-", r)
