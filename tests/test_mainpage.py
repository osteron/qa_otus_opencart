from selenium.webdriver.common.by import By

from tests import wait_of_element, wait_and_return_elements


def test_mainpage_elements(browser):
    logo = (By.CSS_SELECTOR, '#logo')
    search = (By.ID, 'search')
    cart = (By.ID, 'cart')
    menu = (By.ID, 'menu')
    slideshow = (By.CLASS_NAME, 'slideshow')
    product_layout = (By.CLASS_NAME, 'product-layout')
    footer = (By.TAG_NAME, 'footer')

    browser.get('http://localhost:8081')
    assert browser.title in 'Your Store'
    wait_of_element(browser, logo)
    wait_of_element(browser, search)
    wait_of_element(browser, cart)
    wait_of_element(browser, menu)
    wait_of_element(browser, slideshow)
    assert len(wait_and_return_elements(browser, product_layout)) == 4
    wait_of_element(browser, footer)
