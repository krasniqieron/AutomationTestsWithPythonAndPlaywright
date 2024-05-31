import pytest
from pages.browser import Browser
from pages.home_page import HomePage
from pages.product_page import ProductPage
from pages.basket_page import BasketPage

def test_amazon_shopping():
    browser = Browser(headless=True)
    page = browser.new_page()

    home_page = HomePage(page)
    product_page = ProductPage(page)
    basket_page = BasketPage(page)

    home_page.navigate()
    home_page.search_for_product("gaming computer")
    product_page.add_to_basket()
    basket_page.navigate_to_basket()
    basket_page.update_quantity(2)
    assert basket_page.get_quantity() == 2

    browser.close()