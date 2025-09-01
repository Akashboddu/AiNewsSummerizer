import streamlit as st
from news_fetcher import get_latest_news
from tavily_agent import search_news
from transformers import pipeline
from sentence_transformers import SentenceTransformer, util
import re

# ----------------------------
# Streamlit Page Config
# ----------------------------
st.set_page_config(page_title="📰 AI News Summarizer", layout="centered")

# ----------------------------
# Load Models
# ----------------------------
@st.cache_resource
def load_summarizer():
    return pipeline(
        "summarization",
        model="facebook/bart-large-cnn",
        device=-1  # CPU
    )

@st.cache_resource
def load_embedder():
    return SentenceTransformer('all-MiniLM-L6-v2', use_auth_token=False)

summarizer = load_summarizer()
embedder = load_embedder()

# ----------------------------
# Helper: Dual Relevance Check
# ----------------------------
def is_relevant(article, query, threshold=0.5):
    title = article.get("title", "")
    desc = article.get("content", "")

    # 1️⃣ Keyword filter (exact match check, case-insensitive)
    query_words = query.lower().split()
    text_to_search = (title + " " + desc).lower()
    if not any(re.search(rf"\b{re.escape(qw)}\b", text_to_search) for qw in query_words):
        return False

    # 2️⃣ Semantic similarity filter
    query_emb = embedder.encode(query, convert_to_tensor=True)
    text_emb = embedder.encode(title + " " + desc, convert_to_tensor=True)
    score = util.pytorch_cos_sim(query_emb, text_emb).item()
    return score >= threshold

# ----------------------------
# UI Layout
# ----------------------------
st.title("📰 AI News Summarizer")
st.markdown("Get **accurate and relevant** news from multiple sources, summarized instantly.")

if "articles" not in st.session_state:
    st.session_state.articles = []

query = st.text_input("🔍 Enter a topic:", placeholder="e.g. Coolie movie collections, elections, AI...")

# ----------------------------
# Fetch News
# ----------------------------
if st.button("Fetch News"):
    if not query.strip():
        st.warning("⚠️ Please enter a topic first.")
    else:
        with st.spinner("🔄 Fetching news from multiple sources..."):
            # Get news from APIs
            newsapi_articles = get_latest_news(topic=query, page_size=10)
            tavily_articles = search_news(query)

            # Merge into a common format
            all_articles = newsapi_articles + [
                {"title": art["title"], "url": art["url"], "content": art.get("content", "")}
                for art in tavily_articles
            ]

            # Apply dual relevance filter
            st.session_state.articles = [a for a in all_articles if is_relevant(a, query)]

# ----------------------------
# Display Results
# ----------------------------
if st.session_state.articles:
    st.success(f"✅ Found {len(st.session_state.articles)} highly relevant articles.")

    for idx, article in enumerate(st.session_state.articles, start=1):
        with st.expander(f"{idx}. {article['title']}"):
            st.markdown(f"🔗 [Read more]({article['url']})")
            st.write(article.get("content", "No description available."))

            # Summarize button
            if st.button(f"Summarize Article {idx}", key=f"sum_{idx}"):
                with st.spinner("✍ Summarizing..."):
                    summary = summarizer(
                        article.get("content", article["title"]),
                        max_length=180,
                        min_length=60,
                        do_sample=False
                    )[0]['summary_text']
                st.markdown(f"🧾 **Summary:** {summary}")
else:
    st.info("No news loaded yet. Enter a topic and click **Fetch News**.")
