import streamlit as st
from news_fetcher import get_latest_news
from transformers import pipeline

# Load Hugging Face summarization pipeline
@st.cache_resource
def load_summarizer():
    return pipeline("summarization", model="facebook/bart-large-cnn")

summarizer = load_summarizer()

# Summarization function using Hugging Face
def summarize_with_hf(text):
    try:
        summary = summarizer(text, max_length=100, min_length=30, do_sample=False)
        return summary[0]['summary_text']
    except Exception as e:
        st.error(f"Summarization failed: {e}")
        return text

# Streamlit UI
st.set_page_config(page_title="📰 AI News Summarizer (Free)", layout="centered")
st.title("📰 Struggler's AI News Summarizer (Free)")
st.markdown("Search for **latest news** and get **free AI-powered summaries** using NewsAPI + Hugging Face.")

topic = st.text_input("🔍 Enter a topic:", placeholder="e.g. sports, elections, AI, technology...")

if st.button("Fetch & Summarize"):
    if not topic.strip():
        st.warning("⚠️ Please enter a topic first.")
    else:
        with st.spinner("🔄 Fetching latest news..."):
            articles = get_latest_news(topic=topic)

        if articles:
            st.success(f"✅ Found {len(articles)} articles.")
            for idx, article in enumerate(articles, start=1):
                st.markdown(f"### {idx}. {article['title']}")
                st.markdown(f"🔗 [Read more]({article['url']})")
                summary = summarize_with_hf(article['content'])
                st.markdown(f"🧾 **AI Summary:** {summary}")
                st.markdown("---")
        else:
            st.info("🙁 No news found. Try a different topic.")
