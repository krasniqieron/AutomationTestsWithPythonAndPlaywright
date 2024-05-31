from playwright.sync_api import sync_playwright

class Browser:
    def __init__(self, headless=True):
        self.playwright = sync_playwright().start()
        self.browser = self.playwright.chromium.launch(headless=headless)

    def new_page(self):
        page = self.browser.new_page()
        #page.set_viewport_size({"width": 1920, "height": 1080})
        return page

    def close(self):
        self.browser.close()
        self.playwright.stop()