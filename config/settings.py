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
# Check if GRAPHQL_ENDPOINT is explicitly set, otherwise construct from BASE_URL
GRAPHQL_ENDPOINT = os.getenv("GRAPHQL_ENDPOINT") or f"{BASE_URL}/graphql"

# Get admin token from ADMIN_TOKEN env var
AUTH_TOKEN = os.getenv("ADMIN_TOKEN")
if AUTH_TOKEN and not AUTH_TOKEN.startswith("Bearer "):
    AUTH_TOKEN = f"Bearer {AUTH_TOKEN}"

# Headers configuration
DEFAULT_HEADERS = {
    "Content-Type": "application/json",
}

# Only add Authorization header if token exists
if AUTH_TOKEN:
    DEFAULT_HEADERS["Authorization"] = AUTH_TOKEN
