import requests
from send_email import send_email
from langchain.chat_models import init_chat_model
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv("NEWS_API_KEY")
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

url = (
    "https://newsapi.org/v2/top-headlines?"
    "category=business&"
    "language=en&"
    "pageSize=8&"
    "sortBy=publishedAt&apikey=" + api_key
)

request = requests.get(url)
content = request.json()
articles = content["articles"]
print(articles)

model = init_chat_model(
    model="gemini-3-flash-preview",
    model_provider="google-genai",
    api_key=GOOGLE_API_KEY
)

prompt = f"""
You're a news summarizer.
Write a short paragraph analyzing those news.
Add another second paragraph to tell me 
how they affect the stock market.
Here are the news articles:
{articles}
"""

response = model.invoke(prompt)
response_str = str(response.content)

body = "Subject: News Summary\n\n" + response_str + "\n\n"

send_email(message=body)
