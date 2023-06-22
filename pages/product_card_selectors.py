from selenium.webdriver.common.by import By


class ProductCardSelectors:
    images = (By.CSS_SELECTOR, '#content .row .thumbnail')
    add_to_wishlist = (By.XPATH, '//div[@class="btn-group"]/button[@data-original-title="Add to Wish List"]')
    compare_this_product = (By.XPATH, '//div[@class="btn-group"]/button[@data-original-title="Compare this Product"]')
    product_name = (By.CSS_SELECTOR, '.col-sm-4 h1')
    add_to_card = (By.CSS_SELECTOR, '#product .form-group button')
