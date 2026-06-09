# 📰 AI News Summarizer Automation

An automation tool that fetches the latest business news, summarizes them using Large Language Models (LLMs), and delivers the insights straight to your email.

## 🚀 Features
- Fetches top headlines from **NewsAPI**
- Summarizes articles using **Gemini (Google GenAI)** or **OpenAI GPT**
- Sends summarized news directly to your **email inbox**
- Configurable API keys via `.env` file
- Simple, modular project structure (`main.py`, `send_email.py`, `simple_ai.py`)

## 📂 Project Workflow
```mermaid```
flowchart TD
    A[URL Input] --> B[News API Request]
    B --> C[Latest News in Dictionary]
    C --> D[LLM Summarizer]
    D --> E[Summarized News]
    E --> F[Send to Email]

## Installation
Clone the repo: 
`git clone https://github.com/prachipujarii-ai/ai-news-summarizer-automation.git
cd ai-news-summarizer-automation`

## Install dependencies
`pip install -r requirements.txt`

## Setup
Create a `.env` file in the project root:
`NEWS_API_KEY=your_newsapi_key
GOOGLE_API_KEY=your_google_api_key
EMAIL_USER=your_email@gmail.com
EMAIL_PASS=your_app_password`

## Usage
Run the main script:
`python main.py`

## Screenshots

<img width="862" height="947" alt="image" src="https://github.com/user-attachments/assets/b25e9c37-354b-4417-b7a4-e25572ea1072" />



<img width="947" height="361" alt="image" src="https://github.com/user-attachments/assets/950620e5-f128-40b5-a737-22f7df48fb71" />



<img width="780" height="885" alt="image" src="https://github.com/user-attachments/assets/21efd1f3-c20c-4f7b-980f-5a8b5f49a5ab" />

## Example LLM Config
**OpenAI**
`model = init_chat_model(
    model="gpt-5-mini",
    model_provider="openai"
 )`

**Gemini**
`model = init_chat_model(
    model="gemini-3-flash-preview",
    model_provider="google-genai",
    api_key=GOOGLE_API_KEY
 )`

## Pricing Limits
 OpenAI Pricing: https://openai.com/api/pricing?utm_source=copilot.coming
 Gemini Pricing: https://ai.google.dev/pricing?utm_source=copilot.com

## Author
Prachi Pujari
Github: @prachipujarii-ai

## License
MIT License






