[README.md](https://github.com/user-attachments/files/29705959/README.md)
# PathosAI
An AI that helps you think instead of doing everything by itself.
# 🧠 Pathos AI (Work in Progress)

> **Status: ⚠️ Work in Progress (WIP)**  
> Pathos is currently under active development. Core features, pipeline modularization, and web UI integrations are being actively built and refined.

Pathos is an advanced, multi-module reflective AI agent designed to move past surface-level interactions. Instead of providing immediate, generic answers, Pathos processes user input through parallel cognitive channels—**Deconstructive Reflection** and **Creative Perspective Shifting**—before synthesizing a deeply conscious, natural, and conversational response.

---

## 🚀 System Architecture

Pathos operates using a pipeline approach that processes ideas before generating user-facing dialogue:

```
                  [ User Input ]
                        │
         ┌──────────────┴──────────────┐
         ▼                             ▼
 ┌───────────────┐             ┌───────────────┐
 │  Reflection   │             │  Creativity   │
 │    Module     │             │    Module     │
 └───────┬───────┘             └───────┬───────┘
         │                             │
         └──────────────┬──────────────┘
                        ▼
             ┌───────────────────┐
             │ Synthesizer Core  │ (Pathos Persona)
             └──────────┬────────┘
                        ▼
               [ Final Response ]
```

1. **Reflection Module (`Modules/reflection.py`):** Unpacks the user statement to identify hidden assumptions, systemic contradictions, emotional undercurrents, and underlying motivations.
2. **Creativity Module (`Modules/creativity.py`):** Generates structural reframings, inversions, lateral alternatives, and unique constraints for the same input.
3. **Synthesizer Core (`main.py`):** Blends the outputs from both processing layers into a unified, concise conversational voice that prompts deeper user reflection without prematurely "solving" the problem.

---

## 🛠️ Tech Stack & Requirements

- **Language:** Python 3.11+
- **LLM Engine:** Google Gemini (`gemini-2.5-flash`)
- **SDK Library:** Modern `google-genai` SDK
- **Interface:** Command-Line Interface (CLI) / Streamlit Web Interface (Incoming)

---

## 📦 Installation & Setup

### 1. Clone & Navigate
Ensure you are in your project root directory:
```bash
cd C:\Users\vova_\ai-agent-project
```

### 2. Virtual Environment Setup
Make sure your environment is activated and up to date:
```bash
# Verify packages are installed within your environment
.venv\Scripts\pip install google-genai streamlit
```

### 3. API Key Configuration
Pathos utilizes the modern Google GenAI SDK. To protect credentials, store your Gemini API key inside your environment variables or a configuration framework. Ensure all internal engine modules initialize using the modern client syntax:
```python
from google import genai
client = genai.Client(api_key="YOUR_SECURE_KEY")
```

---

## 🎮 How to Run

### Command Line Interface (CLI)
To run the primary conversational loop directly in your console terminal:
```bash
.venv\Scripts\python.exe my_agent\main.py
```

### Web Interface (Streamlit)
To launch the responsive browser-based frontend dashboard locally:
```bash
.venv\Scripts\streamlit run my_agent\app.py
```

---

## 📝 Roadmap & Current Tasks

- [x] Establish multi-module cognitive architecture (Reflection + Creativity splits).
- [x] Migrate to the modern `google-genai` SDK backend to prevent legacy quota throttling.
- [ ] Implement system configuration rules (`.streamlit/config.toml`) to enforce proper light-theme styling.
- [ ] Abstract hardcoded API keys out of core files into environment secrets for cloud staging.
- [ ] Deploy live sandbox environments via Hugging Face Spaces or Streamlit Community Cloud.

---

## ⚖️ License
Internal private build. All rights reserved.
