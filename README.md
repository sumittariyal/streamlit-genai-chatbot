🤖 Generative AI Chatbot

A Generative AI chatbot built using Streamlit, LangChain, and Groq API. It provides an interactive chat interface where users can ask questions and receive AI-generated responses.

🚀 Live Demo [https://app-genai-chatbot-rwpioxxqqrsztcdczvbqky.streamlit.app/]

Try the Generative AI Chatbot

🛠️ Tech Stack

Python — Core programming language

Streamlit — Interactive web interface

LangChain — Integration with the language model

Groq API — AI-powered responses

📋 Prerequisites

Before running the project, make sure you have:

Python installed

Git installed (optional, for cloning the repository)

A Groq API key

⚙️ Steps to Run the Project Locally

1. Clone the repository

git clone <your-github-repository-url>

Navigate to the project directory:

cd chatboat_streamlit

2. Install dependencies

pip install -r requirements.txt

3. Configure the API key

Create a .env file in the project root directory and add your Groq API key:

GROQ_API_KEY=your_groq_api_key

Replace your_groq_api_key with your own API key.

Important: Never share your API key or upload your .env file to GitHub.

4. Run the application

Execute the following command:

streamlit run chatboat.py

The application will open in your browser. If it doesn't, open the local URL shown in your terminal, usually http://localhost:8501.

📁 Project Structure

chatboat_streamlit/
├── chatboat.py
├── requirements.txt
├── .env
├── .gitignore
└── README.md

🔐 Security

Store your Groq API key in the local .env file.

Configure API keys using Streamlit Cloud Secrets when deploying.

Never commit API keys or other sensitive credentials to version control.

👨‍💻 Author

Sumit Tariyal
