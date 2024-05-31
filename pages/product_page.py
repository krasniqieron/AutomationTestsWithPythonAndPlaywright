class ProductPage:
    def __init__(self, page):
        self.page = page

    def add_to_basket(self):
        self.page.click("#a-autoid-5-announce")
        self.page.wait_for_timeout(1000)