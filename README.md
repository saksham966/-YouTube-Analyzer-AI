# 🎥 YouTube Analyzer AI

An AI-powered YouTube video analyzer built using **Streamlit** and **Agno Framework**. This application allows users to paste a YouTube video URL and instantly receive an AI-generated summary of the video's content, helping users quickly understand long videos without watching them entirely.

---

## 🚀 Features

* 🔗 Accepts YouTube video links as input
* 🤖 AI-powered video content analysis
* 📝 Generates concise and meaningful summaries
* ⚡ Fast and user-friendly interface built with Streamlit
* 🎯 Saves time by extracting key information from lengthy videos
* 🔍 Easy-to-use web-based application

---

## 🛠️ Technologies Used

* **Python**
* **Streamlit** – Interactive web UI
* **Agno Framework** – AI Agent orchestration
* **Groq LLM** – High-speed AI inference
* **YouTube Transcript API** – Extract video transcripts
* **Python Dotenv** – Environment variable management

---

## 📂 Project Structure

```bash
youtube-analyzer/
│
├── app.py                 # Main Streamlit application
├── agent.py               # Agno AI agent configuration
├── requirements.txt       # Project dependencies
├── .env                   # API keys and environment variables
├── README.md              # Project documentation
└── assets/                # Optional images and resources
```

---

## ⚙️ Installation

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/youtube-analyzer.git
cd youtube-analyzer
```

### 2. Create Virtual Environment

```bash
python -m venv venv
```

Activate the environment:

**Windows**

```bash
venv\Scripts\activate
```

**Linux/Mac**

```bash
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure Environment Variables

Create a `.env` file and add your API credentials:

```env
GROQ_API_KEY=your_groq_api_key
```

### 5. Run the Application

```bash
streamlit run app.py
```

---

## 🎯 How It Works

1. User enters a YouTube video URL.
2. The application extracts the video's transcript.
3. An Agno AI Agent processes the transcript.
4. The Groq LLM analyzes the content.
5. A concise summary is generated and displayed on the Streamlit interface.

---

## 📸 User Workflow

```text
Paste YouTube URL
        ↓
Fetch Transcript
        ↓
AI Analysis using Agno
        ↓
Generate Summary
        ↓
Display Results
```

---

## 💡 Use Cases

* Educational video summarization
* Research and content analysis
* Quick understanding of lengthy lectures
* Podcast and interview summarization
* Productivity enhancement for students and professionals

---

## 🔮 Future Enhancements

* Multi-language support
* Key points extraction
* Sentiment analysis
* Question-answering from video content
* Downloadable summary reports
* Video topic classification

---

## 🤝 Contributing

Contributions are welcome! Feel free to fork the repository, create a new branch, and submit a pull request.

---

## 📜 License

This project is licensed under the MIT License.

---

## 👨‍💻 Author

Developed with Python, Streamlit, Agno, and Groq to make YouTube content more accessible and easier to understand.
