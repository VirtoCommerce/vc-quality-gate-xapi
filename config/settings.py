from dotenv import load_dotenv
import os

load_dotenv()

BASE_URL = os.getenv("BASE_URL")
ADMIN_USERNAME = os.getenv("ADMIN_USERNAME")
ADMIN_PASSWORD = os.getenv("ADMIN_PASSWORD")
GRAPHQL_ENDPOINT = os.getenv("GRAPHQL_ENDPOINT")
AUTH_TOKEN = os.getenv("ADMIN_TOKEN")
DEFAULT_HEADERS = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {AUTH_TOKEN}",
}
