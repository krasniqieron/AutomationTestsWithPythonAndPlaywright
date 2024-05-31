class BasketPage:
    def __init__(self, page):
        self.page = page

    def navigate_to_basket(self):
        self.page.click('#nav-cart')
        self.page.wait_for_timeout(1000)
    def update_quantity(self, quantity):
        self.page.click("//*[@class='a-button-text a-declarative']")
        self.page.wait_for_timeout(1000)
        self.page.click(f"//a[@data-value='{{\"stringVal\":\"{quantity}\"}}']")
        self.page.wait_for_timeout(1000)

    def get_quantity(self):
        quantity_element = self.page.query_selector("//span[@class='a-dropdown-prompt']")
        return int(quantity_element.inner_text())