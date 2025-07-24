# 📝 Meeting Summariser with DeepSeek + Ollama

![Build](https://img.shields.io/badge/build-passing-brightgreen)
![License](https://img.shields.io/badge/license-MIT-blue)
![Python](https://img.shields.io/badge/Python-3.10%2B-blue)

A simple, local-first meeting summariser that uses **[DeepSeek](https://github.com/deepseek-ai)** via **[Ollama](https://ollama.com/)** to generate clean summaries of meeting notes using a custom system prompt.

---

## ✨ Features

- 💻 Run everything **locally** — no external API needed
- 🤖 Uses **DeepSeek** model via **Ollama**
- 🗂️ Accepts raw meeting notes as plain text
- 📄 Outputs well-structured summaries (Subject, Topics, Key Points, etc.)
- 🧠 Prompt engineered for clarity and completeness

---

## 📦 Installation

<details>
<summary>🔧 Requirements</summary>

- Python 3.10+
- [Ollama](https://ollama.com/)
- DeepSeek model installed locally (`ollama run deepseek`)
</details>

```bash
# 1. Clone the repo
git clone https://github.com/Talkzy-py/MeetingSummarizer.git
cd meeting-summariser

# 2. Set up Python environment
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# 3. Install dependencies
pip install ollama datetime

# 4. Run the app
python main.py
