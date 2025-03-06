import pytest
from playwright.sync_api import Playwright, expect
import random
from dotenv import load_dotenv
import os
import re

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
    page.wait_for_timeout(1000)
    #expect(page.get_by_text("Sign up now")).to_be_visible()
    #page.get_by_text("Sign up now").click()
    page.goto(url + "/sign-up")
    
    # Fill registration form
    first_name_input = page.locator("input[name='firstName']")
    first_name_input.wait_for(state="visible", timeout=5000)
    first_name_input.fill("John")
    last_name_input = page.locator("input[name='lastName']")
    last_name_input.wait_for(state="visible", timeout=5000)
    last_name_input.fill("Playwright")
    global email
    email = "johnplaywright" + str(random.randint(1000,9999)) + "@example.com"
    email_input = page.locator("input[name='email']")
    email_input.wait_for(state="visible", timeout=5000)
    email_input.fill(email)
    print(email)
    password_input = page.locator("input[aria-label='Password']")
    password_input.wait_for(state="visible", timeout=5000)
    password_input.fill("Password1")
    confirm_password_input = page.locator("input[aria-label='Confirm password']")
    confirm_password_input.wait_for(state="visible", timeout=5000)
    confirm_password_input.fill("Password1")
    
    # Submit registration
    page.locator("button[type='submit']").click()
    
    # Verify registration success
    expect(page.locator("h1").filter(has_text=re.compile(r"^Registration completed$"))).to_be_visible()
    
    # Navigate home
    page.get_by_role("link", name="Home page").click()

def test_user_login(browser_context): 
    global email
    url = os.getenv("BASE_URL", "https://vcst-qa-storefront.govirto.com")
    page = browser_context
    
    # Navigate to login page
    page.goto(url)
    page.wait_for_timeout(1000)
    #expect(page.get_by_text("Sign in")).to_be_visible()
    #page.get_by_text("Sign in").click()
    page.goto(url + "/sign-in")
    
    # Fill login form
    email_input = page.locator("input[aria-label='Email']")
    email_input.wait_for(state="visible", timeout=5000)
    email_input.fill(email)
    password_input = page.locator("input[aria-label='Password']")
    password_input.wait_for(state="visible", timeout=5000)
    password_input.fill("Password1")
    
    # Submit login
    page.locator("button[type='submit']").click()
    
    # Verify successful login (you may want to add appropriate verification)
    # For example, check if user menu or profile elements are visible
