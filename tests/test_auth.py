import pytest
from playwright.sync_api import Playwright, expect
import random
from dotenv import load_dotenv
import os

load_dotenv()

# Add this to store email between tests
email = None

@pytest.fixture
def browser_context(playwright: Playwright):
    browser = playwright.chromium.launch(headless=True)
    context = browser.new_context()
    page = context.new_page()
    yield page
    context.close()
    browser.close()

def test_user_registration(browser_context):    
    global email
    url = os.getenv("BASE_URL", "https://vcst-qa-storefront.govirto.com")
    page = browser_context
    
    # Navigate to registration page
    page.goto(url)
    print(page.content())
    page.wait_for_timeout(1000)
    expect(page.get_by_text("Sign up now")).to_be_visible()
    page.get_by_text("Sign up now").click()
    
    # Fill registration form
    page.get_by_role("textbox", name="First name").fill("John")
    page.get_by_role("textbox", name="Last name").fill("Playwright")
    global email
    email = "johnplaywright" + str(random.randint(1000,9999)) + "@example.com"
    page.get_by_role("textbox", name="Email").fill(email)
    print(email)
    page.get_by_role("textbox", name="Password", exact=True).fill("Password1")
    page.get_by_role("textbox", name="Confirm password").fill("Password1")
    
    # Submit registration
    page.get_by_role("button", name="Sign up").click()
    
    # Verify registration success
    expect(page.get_by_role("heading", name="Registration completed")).to_be_visible()
    
    # Navigate home
    page.get_by_role("link", name="Home page").click()

def test_user_login(browser_context): 
    global email
    url = os.getenv("BASE_URL", "https://vcst-qa-storefront.govirto.com")
    page = browser_context
    
    # Navigate to login page
    page.goto(url)
    expect(page.get_by_text("Sign in")).to_be_visible()
    page.get_by_text("Sign in").click()
    
    # Fill login form
    page.get_by_role("textbox", name="Email").fill(email)
    page.get_by_role("textbox", name="Password", exact=True).fill("Password1")
    
    # Submit login
    page.get_by_role("button", name="Log in").click()
    
    # Verify successful login (you may want to add appropriate verification)
    # For example, check if user menu or profile elements are visible
