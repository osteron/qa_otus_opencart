from selenium.webdriver.common.by import By


class MainpageSelectors:
    logo = (By.CSS_SELECTOR, '#logo')
    search = (By.ID, 'search')
    cart = (By.ID, 'cart')
    menu = (By.ID, 'menu')
    footer = (By.TAG_NAME, 'footer')
    slideshow = (By.CLASS_NAME, 'slideshow')
    product_layout = (By.CLASS_NAME, 'product-layout')
