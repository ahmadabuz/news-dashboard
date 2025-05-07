with open('app.py', 'w') as f:
    f.write('''
import streamlit as st
import pandas as pd
import firebase_admin
from firebase_admin import firestore
import plotly.express as px

# Initialize Firebase
if not firebase_admin._apps:
    firebase_admin.initialize_app()
db = firestore.client()

def get_news():
    docs = db.collection("news_articles").stream()
    return pd.DataFrame([doc.to_dict() for doc in docs])

st.title("📰 Cloud News Aggregator")
st.subheader("With Sentiment Analysis")

df = get_news()
if not df.empty:
    col1, col2 = st.columns(2)
    with col1:
        st.metric("Total Articles", len(df))
        fig = px.pie(df, names='sentiment', title='Sentiment Distribution')
        st.plotly_chart(fig)

    with col2:
        avg_conf = df['confidence'].mean()
        st.metric("Average Confidence", f"{avg_conf:.2f}")
        fig = px.box(df, x='sentiment', y='confidence', title='Confidence by Sentiment')
        st.plotly_chart(fig)

    st.dataframe(df)
else:
    st.warning("No articles found in database")
''')