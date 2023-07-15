from selenium.webdriver.common.by import By
from page_objects.BasePage import BasePage


class MainPage(BasePage):
    LOGO = (By.CSS_SELECTOR, '#logo')
    SEARCH = (By.ID, 'search')
    CART = (By.ID, 'cart')
    MENU = (By.ID, 'menu')
    FOOTER = (By.TAG_NAME, 'footer')
    SLIDESHOW = (By.CLASS_NAME, 'slideshow')
    PRODUCT_LAYOUT = (By.CLASS_NAME, 'product-layout')
