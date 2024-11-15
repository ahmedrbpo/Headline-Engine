from dotenv import load_dotenv
import os

load_dotenv()
API_KEY = os.getenv("NEWS_API_KEY")
print(os.getenv("NEWS_API_KEY"))