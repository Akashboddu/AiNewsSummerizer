# 📰 AI News Summarizer

An AI-powered news summarization tool built with **Streamlit**, **NewsAPI**, **Tavily API**, and **OpenAI / Hugging Face Transformers**.  
It fetches **latest real-time news** based on user topics and provides **short AI-generated summaries**.

---

## 📌 Features
- **Real-time news fetching** using:
  - [NewsAPI](https://newsapi.org) → For latest headlines & topic-based search
  - [Tavily Search API](https://tavily.com) → For deep search & additional sources
- **AI-powered summarization** using:
  - **OpenAI GPT-3.5** *(or Hugging Face DistilBART for free use)*
- **Interactive UI** built with [Streamlit](https://streamlit.io)
- **Custom topic search** (e.g., *sports, elections, AI, technology, INS vs ENG match updates*)
- **Clickable links** to read the full articles
- **Responsive & easy to use** on both desktop and mobile

---

## 🛠️ Tech Stack
- **Python** → Core programming language
- **Streamlit** → Web app framework
- **Requests** → API calls
- **dotenv** → Environment variable management
- **OpenAI API** → AI summarization
- **Hugging Face Transformers** → Free offline summarization (optional)
- **NewsAPI** → Latest news headlines
- **Tavily API** → Deep web search for news

---

## 📂 Project Structure
NewsSummarizer/
│
├── app.py # Streamlit main application
├── news_fetcher.py # Fetches latest news from NewsAPI
├── tavily_agent.py # Tavily API deep search agent
├── requirements.txt # Python dependencies
├── .env # API keys (not shared publicly)
└── README.md # Project documentation

yaml
Copy code
