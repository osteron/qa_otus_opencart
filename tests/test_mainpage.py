from page_objects.MainPage import MainPage


def test_main_page_content(browser):
    assert MainPage(browser).check_title_page('Your Store')
    MainPage(browser).element(MainPage.LOGO)
    MainPage(browser).element(MainPage.SEARCH)
    MainPage(browser).element(MainPage.CART)
    MainPage(browser).element(MainPage.MENU)
    MainPage(browser).element(MainPage.SLIDESHOW)
    assert len(MainPage(browser).elements(MainPage.PRODUCT_LAYOUT)) == 3
    MainPage(browser).element(MainPage.FOOTER)


def test_switching_currencies(browser):
    pass
