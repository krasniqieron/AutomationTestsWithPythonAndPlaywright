class HomePage:
    def __init__(self, page):
        self.page = page

    def navigate(self):
        self.page.goto("https://www.amazon.de")
        self.page.wait_for_timeout(1000)


    def search_for_product(self, product_name):
        self.page.fill('#twotabsearchtextbox', product_name)
        self.page.wait_for_timeout(1000)
        self.page.press('#twotabsearchtextbox', 'Enter')
        self.page.wait_for_timeout(1000)