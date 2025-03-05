from dotenv import load_dotenv
import os

load_dotenv()

# Required environment variables
BASE_URL = os.getenv("BASE_URL")
if not BASE_URL:
    raise ValueError("BASE_URL environment variable is required")

ADMIN_USERNAME = os.getenv("ADMIN_USERNAME") 
if not ADMIN_USERNAME:
    raise ValueError("ADMIN_USERNAME environment variable is required")

ADMIN_PASSWORD = os.getenv("ADMIN_PASSWORD")
if not ADMIN_PASSWORD:
    raise ValueError("ADMIN_PASSWORD environment variable is required")

# Optional environment variables with defaults
GRAPHQL_ENDPOINT = os.getenv("GRAPHQL_ENDPOINT", "/graphql")
AUTH_TOKEN = os.getenv("ADMIN_TOKEN")

# Headers configuration
DEFAULT_HEADERS = {
    "Content-Type": "application/json",
}

# Only add Authorization header if token exists
if AUTH_TOKEN:
    DEFAULT_HEADERS["Authorization"] = f"Bearer {AUTH_TOKEN}"
