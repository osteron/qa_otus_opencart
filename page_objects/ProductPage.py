from selenium.webdriver.common.by import By

from page_objects.BasePage import BasePage


class ProductPage(BasePage):
    IMAGES = (By.CSS_SELECTOR, '#content .row .thumbnail')
    ADD_TO_WISHLIST = (By.XPATH, '//div[@class="btn-group"]/button[@data-original-title="Add to Wish List"]')
    COMPARE_THIS_PRODUCT = (By.XPATH, '//div[@class="btn-group"]/button[@data-original-title="Compare this Product"]')
    PRODUCT_NAME = (By.CSS_SELECTOR, '.col-sm-4 h1')
    ADD_TO_CARD = (By.CSS_SELECTOR, '#product .form-group button')
