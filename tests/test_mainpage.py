from pages.mainpage_selectors import MainpageSelectors
from tests import wait_of_element, wait_and_return_elements


def test_main_page_elements(browser):
    browser.get('http://localhost:8081')
    assert browser.title in 'Your Store'
    wait_of_element(browser, MainpageSelectors.logo)
    wait_of_element(browser, MainpageSelectors.search)
    wait_of_element(browser, MainpageSelectors.cart)
    wait_of_element(browser, MainpageSelectors.menu)
    wait_of_element(browser, MainpageSelectors.slideshow)
    assert len(wait_and_return_elements(browser, MainpageSelectors.product_layout)) == 4
    wait_of_element(browser, MainpageSelectors.footer)
