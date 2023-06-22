from pages.admin_selectors import AdminSelectors
from tests import wait_of_element, get_text


def test_admin_page_elements(browser):
    panel_title = 'Please enter your login details.'
    username_label = 'Username'
    password_label = 'Password'
    submit = 'Login'

    browser.get('http://10.0.2.15:8081/admin')
    assert browser.title.lower() in 'administration'
    wait_of_element(browser, AdminSelectors.header_logo)
    wait_of_element(browser, AdminSelectors.center_panel)
    assert get_text(browser, AdminSelectors.panel_title) in panel_title
    assert get_text(browser, AdminSelectors.username_label) in username_label
    wait_of_element(browser, AdminSelectors.username_input)
    assert get_text(browser, AdminSelectors.password_label) in password_label
    wait_of_element(browser, AdminSelectors.password_input)
    wait_of_element(browser, AdminSelectors.forgotten_password)
    assert get_text(browser, AdminSelectors.submit) in submit
