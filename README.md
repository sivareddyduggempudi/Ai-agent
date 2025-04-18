# 🌐 AI Web Browsing Agent using Gemini

An intelligent web browsing assistant that uses Google's Gemini Pro LLM to search, read, and answer user questions based on real-time web content — complete with markdown citations.

---

## 🚀 Features

- 🔍 **Web Search via SerpAPI**
- 🧠 **Answer generation using Gemini Pro**
- 📄 **Web scraping for top search results**
- 📎 **Markdown citation for each fact**
- 🧼 Clean UI built with Streamlit

---

## 🛠️ Setup Instructions

### 1. Clone the repo
```bash
git clone https://github.com/your-username/ai-web-browsing-agent.git
cd ai-web-browsing-agent
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Set up API keys

Create a `.env` file in the project root:

```env
GOOGLE_API_KEY=your_gemini_api_key
SERPAPI_API_KEY=your_serpapi_api_key
```

> 🔑 Get your Gemini API key from [Google AI Studio](https://makersuite.google.com/app/apikey)  
> 🔍 Get your SerpAPI key from [https://serpapi.com](https://serpapi.com)

---

## ▶️ Run the App

```bash
streamlit run app.py
```

---

## 💡 Example

**Question:**  
> "What is Gemini Pro and how does it compare to GPT-4?"

**Response:**  
> Gemini Pro is Google's latest large language model designed for advanced reasoning, code generation, and multimodal capabilities. It supports up to 1 million tokens of context. [source](https://blog.google/ai/gemini-1-5)  
> Compared to GPT-4, Gemini Pro performs better on several benchmarks. [source](https://arxiv.org/pdf/gemini.pdf)

---

## 📂 Project Structure

```
📁 ai-web-browsing-agent/
├── app.py              # Streamlit app
├── web_agent.py        # Agent logic (Gemini + Web search)
├── .env                # API keys
├── requirements.txt    # Python dependencies
└── README.md           # You're here!
```

---

## 📌 To Do / Ideas

- [ ] Multi-turn memory (chat history)
- [ ] Summary toggle (short vs detailed)
- [ ] Voice input/output
- [ ] Multi-agent mode (researcher + summarizer)

---

## 📄 License

MIT License – free to use, modify, and distribute.

---

## 🤝 Contributing

Pull requests are welcome! For major changes, open an issue first to discuss what you'd like to change.

---

## 🙌 Credits

Built with ❤️ using [Google Gemini](https://ai.google.dev) and [Streamlit](https://streamlit.io)
