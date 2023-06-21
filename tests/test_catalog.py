from selenium.webdriver.common.by import By
from config import MainSelectors
from tests import wait_of_element, wait_and_return_elements


def test_catalog_elements(browser):
    breadcrumb = (By.CLASS_NAME, 'breadcrumb')
    product_layout = (By.CLASS_NAME, 'product-layout')
    list_group = (By.CLASS_NAME, 'list-group')
    list_group_items = (By.CLASS_NAME, 'list-group-item')
    content = (By.ID, 'content')

    browser.get('http://localhost:8081/smartphone')
    assert browser.title in 'Phones & PDAs'
    wait_of_element(browser, MainSelectors.logo)
    wait_of_element(browser, MainSelectors.search)
    wait_of_element(browser, MainSelectors.cart)
    wait_of_element(browser, MainSelectors.menu)
    wait_of_element(browser, breadcrumb)
    assert len(wait_and_return_elements(browser, product_layout)) == 3
    wait_of_element(browser, list_group)
    assert len(wait_and_return_elements(browser, list_group_items)) == 8
    wait_of_element(browser, MainSelectors.footer)
    wait_of_element(browser, content)
