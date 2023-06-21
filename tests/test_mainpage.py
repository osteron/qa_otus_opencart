from selenium.webdriver.common.by import By
from config import MainSelectors
from tests import wait_of_element, wait_and_return_elements


def test_mainpage_elements(browser):
    slideshow = (By.CLASS_NAME, 'slideshow')
    product_layout = (By.CLASS_NAME, 'product-layout')

    browser.get('http://localhost:8081')
    assert browser.title in 'Your Store'
    wait_of_element(browser, MainSelectors.logo)
    wait_of_element(browser, MainSelectors.search)
    wait_of_element(browser, MainSelectors.cart)
    wait_of_element(browser, MainSelectors.menu)
    wait_of_element(browser, slideshow)
    assert len(wait_and_return_elements(browser, product_layout)) == 4
    wait_of_element(browser, MainSelectors.footer)
