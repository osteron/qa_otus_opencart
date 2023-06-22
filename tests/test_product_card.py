from pages.product_card_selectors import ProductCardSelectors
from tests import wait_of_element, wait_and_return_elements, get_text


def test_product_card_elements(browser):
    product_name = 'iphone'
    browser.get('http://10.0.2.15:8081/iphone')
    assert browser.title.lower() in product_name
    assert len(wait_and_return_elements(browser, ProductCardSelectors.images)) == 6
    wait_of_element(browser, ProductCardSelectors.add_to_wishlist)
    wait_of_element(browser, ProductCardSelectors.compare_this_product)
    assert get_text(browser, ProductCardSelectors.product_name).lower() in product_name
    wait_of_element(browser, ProductCardSelectors.add_to_card)
