from pages.register_selectors import RegisterSelectors
from tests import wait_and_return_element, wait_and_return_elements, IP_ADDRESS


def test_admin_page_elements(browser):

    browser.get(f'{IP_ADDRESS}:8081/index.php?route=account/register')
    assert len(wait_and_return_elements(browser, RegisterSelectors.radio_inlines)) == 2
    wait_and_return_element(browser, RegisterSelectors.agree_checkbox)
    wait_and_return_element(browser, RegisterSelectors.submit)
    assert len(wait_and_return_elements(browser, RegisterSelectors.column_right)) == 13
