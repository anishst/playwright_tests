

def test_new_pages(playwright):
    browser = playwright.chromium.launch(headless=False, slow_mo=500)
    context1 = browser.new_context()
    page = context1.new_page()
    # https://playwright.dev/python/docs/emulation
    page.set_viewport_size({"width": 1600, "height": 1200})
    page.goto("http://playwright.dev/")

