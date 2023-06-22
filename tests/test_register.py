from pages.register_selectors import RegisterSelectors
from tests import wait_of_element, get_text, wait_and_return_elements


def test_admin_page_elements(browser):

    browser.get('http://10.0.2.15:8081/index.php?route=account/register')
    assert len(wait_and_return_elements(browser, RegisterSelectors.personal_details_inputs)) == 7
    assert len(wait_and_return_elements(browser, RegisterSelectors.radio_inlines)) == 2
    wait_of_element(browser, RegisterSelectors.agree_checkbox)
    wait_of_element(browser, RegisterSelectors.submit)
    assert len(wait_and_return_elements(browser, RegisterSelectors.column_right)) == 13
