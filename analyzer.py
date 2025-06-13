# analyzer.py
from textblob import TextBlob

def analyze_reviews(reviews):
    summary = {'positive': 0, 'neutral': 0, 'negative': 0}
    insights = []

    for review in reviews:
        blob = TextBlob(review)
        polarity = blob.sentiment.polarity
        if polarity > 0.1:
            sentiment = 'positive'
        elif polarity < -0.1:
            sentiment = 'negative'
        else:
            sentiment = 'neutral'

        summary[sentiment] += 1
        insights.append((review, sentiment))

    return summary, insights
