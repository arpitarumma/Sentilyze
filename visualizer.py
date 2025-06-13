# visualizer.py
import plotly.express as px

def plot_sentiment_distribution(summary):
    data = {
        'Sentiment': list(summary.keys()),
        'Count': list(summary.values())
    }
    fig = px.pie(data, names='Sentiment', values='Count', title='Sentiment Distribution')
    return fig
