# app.py
import streamlit as st
from scraper import get_reviews_amazon
from analyzer import analyze_reviews
from visualizer import plot_sentiment_distribution

st.title("🧠 Sentiment-Powered Product Review Summarizer")

product_url = st.text_input("Enter Amazon Product URL")

if product_url:
    with st.spinner("Scraping reviews..."):
        reviews = get_reviews_amazon(product_url)

    with st.spinner("Analyzing sentiment..."):
        summary, insights = analyze_reviews(reviews)

    st.subheader("📊 Sentiment Summary")
    st.write(f"""
        - Positive: {summary['positive']}  
        - Neutral: {summary['neutral']}  
        - Negative: {summary['negative']}
    """)

    st.plotly_chart(plot_sentiment_distribution(summary))

    st.subheader("📝 Top Reviews")
    for review, sentiment in insights[:10]:
        st.write(f"**[{sentiment.upper()}]** {review}")


