from playwright.async_api import expect
from playwright.sync_api import Page


def test_new_pages(playwright):
    browser = playwright.chromium.launch(headless=False, slow_mo=500)
    context1 = browser.new_context()
    page = context1.new_page()
    page.goto("http://playwright.dev/")

    context2 = browser.new_context()
    page = context2.new_page()
    page.goto("http://playwright.dev/")


