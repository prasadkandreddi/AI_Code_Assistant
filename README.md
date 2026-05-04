```md
# 🧩 AI Code Assistant (Generative AI Project)

An AI-powered coding assistant built using **Google Gemini API** and **Streamlit**.  
This tool helps developers generate, debug, and understand code with structured outputs.

---

## 🚀 Features

- 💻 Code generation (clean, optimized code)
- 🛠 Debugging support
- 🧠 Short explanations (interview-ready)
- 🎯 Coding interview questions generation
- 🚫 Coding-only mode with input validation
- 💬 Chat-based interface
- ⚙️ Model tuning (temperature, top-p, top-k)

---

## 🛠 Tech Stack

- **Python**
- **Streamlit**
- **Google Gemini API**
- **Prompt Engineering**

---

## 🌐 Live Demo

👉 [Streamlit App](https://huggingface.co/spaces/prasad1232123212/AI_Code_Assistant_)

---

## 📌 How It Works

1. User enters a coding query  
2. System checks if input is coding-related  
3. If valid → generates:
   - Code  
   - Short explanation  
   - Interview questions  
4. If not → rejects input  

The system uses **prompt engineering + parameter tuning** to ensure structured and accurate responses.

---

## 🧠 Key Concepts

- Prompt Engineering  
- LLM Response Structuring  
- Input Classification (Coding vs Non-coding)  
- API Rate Limit Handling  
- Chat-based UI Design  

---

## 🔐 Security

- API keys are stored using **environment variables**
- Secrets are managed securely (no keys exposed in code)

---

## 📂 Project Structure

```

ai-code-assistant/
│
├── app.py
├── requirements.txt
├── README.md
└── .gitignore

````

---

## ▶️ Run Locally

```bash
git clone https://github.com/prasadkandreddi/ai-code-assistant.git
cd ai-code-assistant

pip install -r requirements.txt
streamlit run app.py
````

---

## ⚙️ Environment Setup

Create a `.env` file:

```
GEMINI_API_KEY=your_api_key_here
```

---

##

---

## ⭐ Future Improvements

* Add code execution feature
* Add multi-language support
* Improve UI/UX
* Add response streaming

---

## 💼 Resume Highlights

* Built a **Gen AI-based coding assistant** using Gemini API
* Applied **prompt engineering** for structured outputs
* Implemented **input filtering & response control**
* Deployed using **Hugging Face Spaces**

---

## 🤝 Contributing

Feel free to fork and improve this project.

---

## 📜 License

This project is for educational and portfolio purposes.

```
```


