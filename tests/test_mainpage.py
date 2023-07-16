import time

from selenium.webdriver.chrome.webdriver import WebDriver

from page_objects.MainPage import MainPage


def test_main_page_content(browser: WebDriver) -> None:
    assert MainPage(browser).check_title_page('Your Store')
    MainPage(browser).element(MainPage.LOGO)
    MainPage(browser).element(MainPage.SEARCH)
    MainPage(browser).element(MainPage.CART)
    MainPage(browser).element(MainPage.MENU)
    MainPage(browser).element(MainPage.SLIDESHOW)
    assert len(MainPage(browser).elements(MainPage.PRODUCT_LAYOUT)) == 4
    MainPage(browser).element(MainPage.FOOTER)


def test_switching_currencies(browser: WebDriver) -> None:
    assert MainPage(browser).get_text_of_element(MainPage.CURRENT_CURRENCY) in '$'
    MainPage(browser).click(MainPage.CURRENCY)
    MainPage(browser).click(MainPage.EURO)
    assert MainPage(browser).get_text_of_element(MainPage.CURRENT_CURRENCY) in '€'
    MainPage(browser).click(MainPage.CURRENCY)
    MainPage(browser).click(MainPage.POUND_STERLING)
    assert MainPage(browser).get_text_of_element(MainPage.CURRENT_CURRENCY) in '£'
    MainPage(browser).click(MainPage.CURRENCY)
    MainPage(browser).click(MainPage.DOLLAR)
    assert MainPage(browser).get_text_of_element(MainPage.CURRENT_CURRENCY) in '$'


