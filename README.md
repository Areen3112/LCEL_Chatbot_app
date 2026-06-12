# LCEL Chatbot App 🚀

An AI-powered chatbot application built using **LangChain Expression Language (LCEL)**, **FastAPI**, and **Groq LLMs**. This project demonstrates how to create and serve LangChain chains as REST APIs using **LangServe**, enabling easy integration of LLM-powered workflows into web applications.

## ✨ Features

* 🤖 AI-powered chatbot using **Groq's Llama 3.1 models**
* 🔗 Built with **LangChain Expression Language (LCEL)** for modular and composable AI workflows
* ⚡ High-performance API backend using **FastAPI**
* 🌐 Serve LangChain chains as REST endpoints with **LangServe**
* 🔄 Prompt templating using **ChatPromptTemplate**
* 📝 Output parsing using **StrOutputParser**
* 🚀 Production-ready ASGI server with **Uvicorn**
* 🔐 Secure API key management using environment variables (`.env`)

## 🛠️ Tech Stack

* **Python**
* **FastAPI**
* **Uvicorn**
* **LangChain**
* **LangChain Core**
* **LangServe**
* **LangChain Groq**
* **Groq API**
* **Python-dotenv**
* **Pydantic**

## 📂 Project Structure

```text
LCEL_app/
│
├── serve.py          # Main FastAPI application
├── .env              # Environment variables (not tracked by Git)
├── .gitignore
├── requirements.txt
└── README.md
```

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/Areen3112/LCEL_Chatbot_app.git
cd LCEL_Chatbot_app
```

### 2. Create a virtual environment

```bash
python -m venv venv
```

Activate the environment:

**macOS/Linux**

```bash
source venv/bin/activate
```

**Windows**

```bash
venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

## 🔑 Environment Variables

Create a `.env` file in the root directory:

```env
GROQ_API_KEY=your_groq_api_key_here
```

> **Note:** Never commit your `.env` file or API keys to GitHub.

## ▶️ Running the Application

Start the FastAPI server using:

```bash
python serve.py
```

Alternatively:

```bash
uvicorn serve:app --reload
```

The application will run at:

```text
http://localhost:8000
```

## 📡 API Endpoints

LangServe automatically creates endpoints for interacting with the chain.

Main endpoint:

```text
/chain
```

Interactive API documentation:

```text
http://localhost:8000/docs
```

## 🔄 Example Workflow

This project currently demonstrates a translation chain:

1. User provides text and target language.
2. LCEL composes the prompt template.
3. Groq's Llama model generates the response.
4. Output parser extracts the final text response.
5. FastAPI serves the result via REST APIs.

## 🎯 Learning Objectives

This project was built to explore:

* Building LLM applications using LCEL
* Integrating Groq models with LangChain
* Serving AI chains with FastAPI and LangServe
* Managing environment variables securely
* Creating production-ready AI APIs

## 🚀 Future Improvements

* Add conversational memory
* Integrate Retrieval-Augmented Generation (RAG)
* Add authentication and rate limiting
* Deploy using Docker and cloud platforms
* Build a frontend interface for chatbot interaction

## 🤝 Contributing

Contributions, suggestions, and improvements are welcome. Feel free to fork the repository and submit a pull request.

## 📜 License

This project is licensed under the MIT License.

---

**Built with ❤️ using LangChain, FastAPI, and Groq**
