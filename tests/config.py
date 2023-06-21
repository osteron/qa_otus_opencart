from selenium.webdriver.common.by import By


class MainSelectors:
    logo = (By.CSS_SELECTOR, '#logo')
    search = (By.ID, 'search')
    cart = (By.ID, 'cart')
    menu = (By.ID, 'menu')
    footer = (By.TAG_NAME, 'footer')
