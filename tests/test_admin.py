from page_objects.AdminPage import AdminPage


def test_admin_page_content(browser):
    browser.get('http://localhost:8081/admin/')
    assert AdminPage(browser).check_title_page('Administration')
    AdminPage(browser).element(AdminPage.HEADER_LOGO)
    AdminPage(browser).element(AdminPage.CENTER_PANEL)
    AdminPage(browser).element(AdminPage.USERNAME_INPUT)
    AdminPage(browser).element(AdminPage.PASSWORD_INPUT)
    AdminPage(browser).element(AdminPage.FORGOTTEN_PASSWORD)
    assert AdminPage(browser).get_text_of_element(AdminPage.PANEL_TITLE) in AdminPage.PANEL_TITLE_TEXT
    assert AdminPage(browser).get_text_of_element(AdminPage.USERNAME_LABEL) in AdminPage.USERNAME_LABEL_TEXT
    assert AdminPage(browser).get_text_of_element(AdminPage.PASSWORD_LABEL) in AdminPage.PASSWORD_LABEL_TEXT
    assert AdminPage(browser).get_text_of_element(AdminPage.SUBMIT) in AdminPage.SUBMIT_TEXT


def test_add_new_product(browser):
    browser.get('http://localhost:8081/admin/')
    AdminPage(browser).admin_login()
    AdminPage(browser).add_new_product('test', 'test', 'test')


def test_delete_product(browser):
    browser.get('http://localhost:8081/admin/')
    AdminPage(browser).admin_login()
    AdminPage(browser).delete_product('HTC Touch HD')
