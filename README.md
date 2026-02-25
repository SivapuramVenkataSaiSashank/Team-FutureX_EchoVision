# EchoVision — NLP Agentic RAG Document QA 🎙️📚

> **futureX Project**  
> *A fully voice-controlled, multimodal AI workspace for blind learners and professionals.*

---

## 🎯 Problem Statement
Current digital accessibility tools (like Windows Narrator) are linear, "blind" screen readers forcing visually impaired users to slog through hundreds of pages of irrelevant text. General LLMs require manual file uploading and strict graphical interactions, making them difficult to use hands-free.

**Our Solution:** EchoVision is an intelligent, completely **voice-controlled Agentic RAG** (Retrieval-Augmented Generation) workspace allowing users to dynamically upload multiple documents, build a local vector database, ask complex queries across files, and granularly manage their context window—all via natural speech and offline Text-to-Speech playback. 

---

## ✨ Key Features
- **🎙️ Acoustic Intent Retrieval**: Navigate and select local files via pure voice commands bypassing the standard OS GUI file explorer.
- **📚 Multi-Document Aggregation**: Sequentially append PDFs, DOCX, EPUBs, and TXTs into a unified Vector Space context.
- **🗑️ Granular Voice Deletion**: Say *"delete file [filename]"* to eject a specific document from your workspace while intuitively preserving the rest.
- **💬 Semantic RAG Q&A**: Stop reading linearly. Ask *"What does this syllabus say about finals?"* and receive a precise synthesized answer.
- **🔒 100% Offline Auditory Privacy**: Advanced local TTS serving using Coqui TTS and eSpeak NG guarantees sensitive document audio never hits external APIs.
- **⚡ Interruptible Playback**: Halting audio playback via any generic keystroke without breaking the application state.
- **🔖 Persistent Bookmarking & Search**: Semantic search alongside rapid page-jumping.

---

## 🛠️ Technology Stack
| Layer | Tech Stack |
|-------|------------|
| **Backend Framework** | FastAPI, Uvicorn, Python (3.10+) |
| **Frontend UI** | React (18+), Vite, HTML5, Vanilla CSS3 |
| **LLM Inference** | Groq API, LangChain |
| **Vector DB & Search** | ChromaDB, Sentence-Transformers |
| **Speech Generation (TTS)**| Coqui TTS, eSpeak NG |
| **Speech Recognition** | Web Speech API (`webkitSpeechRecognition`) |
| **Document Parsers** | PyMuPDF (`fitz`), `python-docx`, EbookLib, BeautifulSoup4 |
| **Intent Matching** | FuzzyWuzzy / RapidFuzz |

---

## 🚀 Setup & Execution

### 1. Prerequisites
- Python 3.10+
- Node.js (for React frontend)
- [eSpeak NG](https://github.com/espeak-ng/espeak-ng) installed and added to standard Windows PATH (required for Coqui TTS fallback).

### 2. Backend Initialization
```bash
# Clone the repository
git clone https://github.com/your-org/EchoVision.git
cd EchoVision

# Create and activate virtual environment
python -m venv venv
venv\Scripts\activate      # Windows
source venv/bin/activate   # Mac/Linux

# Install dependencies
pip install -r requirements.txt

# Create .env and add API Key
echo 'GROQ_API_KEY="your_groq_api_key_here"' > .env

# Run FastAPI Server
python -m uvicorn api:app --host 0.0.0.0 --port 8080 --reload
```
*(The backend typically runs on http://localhost:8000)*

### 3. Frontend Initialization (New Terminal)
```bash
cd frontend

# Install dependencies
npm install

# Run Vite dev server
npm run dev
```
*(The React UI will launch at http://localhost:5173)*

---

## 🗣️ Core Voice Commands
*(Activate mic with `Ctrl+M` or by clicking the microphone icon)*

| Intent | Expected Phrase |
|--------|-----------------|
| **Open File (Search)** | *"Find my biology notes"* or *"Look for syllabus"* |
| **Read Linear** | *"Read document"* or *"Next page"* or *"Go to page 5"* |
| **Complex RAG Q&A** | *"Ask: What is the main argument of chapter 3?"* |
| **Summarize Action** | *"Give me a detailed summary"* or *"Summarize briefly"* |
| **Granular Deletion** | *"Delete file chemistry"* or *"Remove document"* |
| **Clear Workspace** | *"Delete all"* or *"Close document"* |
| **Stop Audio** | *"Stop"* / *"Quiet"* (or hit any key on the keyboard) |

---

## 📂 Project Architecture
```text
EchoVision/
├── api.py                    ← Main FastAPI backend router & Voice Command Dispatcher
├── requirements.txt
├── .env                      ← Groq API keys
├── src/
│   ├── document_processor.py ← PDF/DOCX/EPUB parsing & ChromaDB embedding logic
│   ├── ai_summarizer.py      ← Langchain & Groq Q&A / Summarization pipeline
│   ├── fuzzy_search.py       ← Local file directory semantic intent matching
│   └── text_chunker.py       
└── frontend/                 ← React / Vite Application
    ├── src/
    │   ├── App.jsx           ← Main UI view and Context state tracking
    │   ├── NetworkBackground.jsx
    │   └── index.css         ← Modern glassmorphic styling
    └── index.html
```

---

*Made with ❤️ for HackXAmrita 2.0*
