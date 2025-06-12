import streamlit as st
from sentiment_utils import get_reviews_amazon, analyze_reviews
import plotly.express as px

st.set_page_config(page_title="Sentilyze")
st.title("📊 Sentiment-Powered Product Review Summarizer")

url = st.text_input("Enter Amazon Product URL")

if st.button("Analyze"):
    with st.spinner("Scraping and analyzing reviews..."):
        reviews = get_reviews_amazon(url)
        df = analyze_reviews(reviews)

        st.success(f"Analyzed {len(df)} reviews!")
        
        fig = px.pie(df, names=df['sentiment'], title='Sentiment Distribution')
        st.plotly_chart(fig)

        st.subheader("Sample Reviews")
        for r in df.head(10).itertuples():
            st.write(f"🗨️ {r.review} → *{r.sentiment}*")

