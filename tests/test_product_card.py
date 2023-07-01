from pages.product_card_selectors import ProductCardSelectors
from tests import wait_and_return_element, wait_and_return_elements, get_text, IP_ADDRESS


def test_product_card_elements(browser):
    product_name = 'iphone'
    browser.get(f'{IP_ADDRESS}:8081/iphone')
    assert browser.title.lower() in product_name
    assert len(wait_and_return_elements(browser, ProductCardSelectors.images)) == 6
    wait_and_return_element(browser, ProductCardSelectors.add_to_wishlist)
    wait_and_return_element(browser, ProductCardSelectors.compare_this_product)
    assert get_text(browser, ProductCardSelectors.product_name).lower() in product_name
    wait_and_return_element(browser, ProductCardSelectors.add_to_card)
