from pages.catalog_selectors import CatalogSelectors
from tests import wait_and_return_element, wait_and_return_elements


def test_catalog_elements(browser):
    browser.get('http://localhost:8081/smartphone')
    assert browser.title in 'Phones & PDAs'
    wait_and_return_element(browser, CatalogSelectors.breadcrumb)
    assert len(wait_and_return_elements(browser, CatalogSelectors.product_layout)) == 3
    wait_and_return_element(browser, CatalogSelectors.list_group)
    assert len(wait_and_return_elements(browser, CatalogSelectors.list_group_items)) == 8
    wait_and_return_element(browser, CatalogSelectors.content)
