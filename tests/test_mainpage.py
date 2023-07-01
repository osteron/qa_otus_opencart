from pages.mainpage_selectors import MainpageSelectors
from tests import wait_and_return_element, wait_and_return_elements, IP_ADDRESS


def test_main_page_elements(browser):
    browser.get(f'{IP_ADDRESS}:8081')
    assert browser.title in 'Your Store'
    wait_and_return_element(browser, MainpageSelectors.logo)
    wait_and_return_element(browser, MainpageSelectors.search)
    wait_and_return_element(browser, MainpageSelectors.cart)
    wait_and_return_element(browser, MainpageSelectors.menu)
    wait_and_return_element(browser, MainpageSelectors.slideshow)
    assert len(wait_and_return_elements(browser, MainpageSelectors.product_layout)) == 4
    wait_and_return_element(browser, MainpageSelectors.footer)
