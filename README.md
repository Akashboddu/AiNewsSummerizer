# 📰 AI News Summarizer

A **Streamlit-based web application** that fetches the latest and most relevant news articles from **multiple sources** (NewsAPI & Tavily) and allows you to **summarize each article on demand** using a **Hugging Face BART model** — without any API usage limits.

---

## 🚀 Features
- **Multi-source search** → Combines **NewsAPI** and **Tavily** for both breadth and depth of coverage.
- **Dual relevance filtering** → Uses **keyword matching** + **semantic similarity (SentenceTransformer)** to ensure only highly relevant articles are shown.
- **On-demand summarization** → Summarize individual articles instantly with a click (faster than summarizing everything at once).
- **Persistent results** → Uses `st.session_state` so results stay on screen after interactions.
- **No OpenAI quota issues** → Uses **Hugging Face's `facebook/bart-large-cnn`** model locally for summarization.
- **Responsive UI** built with Streamlit.

---

## 🛠 Tech Stack
- **Python 3.9+**
- **Streamlit** → Interactive UI
- **Requests** → API calls
- **Hugging Face Transformers** → Local summarization model
- **SentenceTransformers** → Semantic similarity filtering
- **Tavily API** → Deep web news search
- **NewsAPI** → Real-time headlines
- **dotenv** → Manage API keys securely

---

## 📂 Project Structure
```
NewsSummarizer/
│── app.py               # Main Streamlit application
│── news_fetcher.py      # Fetch news from NewsAPI
│── tavily_agent.py      # Fetch news from Tavily
│── requirements.txt     # Python dependencies
│── .env                 # API keys (not shared in repo)
│── README.md            # Project documentation
```

---

## ⚙️ Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/news-summarizer.git
   cd news-summarizer
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # Mac/Linux
   venv\Scripts\activate     # Windows
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Create a `.env` file** in the root folder:
   ```
   NEWSAPI_KEY=your_newsapi_key
   TAVILY_API_KEY=your_tavily_api_key
   ```

5. **Run the application**
   ```bash
   streamlit run app.py
   ```

---

## 🔑 Getting API Keys
- **NewsAPI** → [https://newsapi.org/](https://newsapi.org/)  
- **Tavily API** → [https://tavily.com/](https://tavily.com/)  

---

## 📸 How It Works
1. Enter a **topic** (e.g., "Coolie movie collections", "India elections", "AI").
2. Click **Fetch News** to get articles from **both NewsAPI and Tavily**.
3. Only **highly relevant articles** (via keyword + semantic filter) are displayed in expandable sections.
4. Click **Summarize Article** for any article you want to condense.
5. Read a **short, AI-generated summary** instantly.

---

## 📝 Example Search
**Topic:** `recent words of trump on india`  
✅ Found **highly relevant articles**.  
🔗 Clicked "Summarize" → Generated a **clear and concise summary** in seconds.

---

## 📌 Notes
- The summarizer runs **locally** via Hugging Face; first load might be slower due to model download.
- You can tweak semantic similarity threshold in:
  ```python
  return score >= 0.5
  ```
- Internet connection required for fetching news.

---

## 📜 License
This project is licensed under the MIT License.
