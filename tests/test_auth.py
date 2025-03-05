#import pytest

#def test_authentication(rest_client):
#    headers = rest_client.get_headers()
#    assert "Authorization" in headers
#    assert rest_client.token is not None

import re
from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.get_by_role("textbox", name="First name").click()
    page.get_by_role("textbox", name="First name").fill("Elena")
    page.get_by_role("textbox", name="Last name").click()
    page.get_by_role("textbox", name="Last name").fill("Mutykova")
    page.get_by_role("textbox", name="Email").click()
    page.get_by_role("textbox", name="Email").fill("mutykovaelena@gmail.com")
    page.get_by_role("textbox", name="Email").click()
    page.get_by_role("textbox", name="Email").fill("mutykovaelena2@gmail.com")
    page.get_by_role("textbox", name="Password", exact=True).click()
    page.get_by_role("textbox", name="Password", exact=True).fill("Password1")
    page.get_by_role("textbox", name="Confirm password").click()
    page.get_by_role("textbox", name="Confirm password").fill("Password1")
    page.get_by_role("button", name="Sign up").click()
    page.get_by_role("heading", name="Registration completed").click()
    page.get_by_role("link", name="Home page").click()

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)




