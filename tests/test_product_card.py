from page_objects.ProductPage import ProductPage


def test_product_card_content(browser):
    browser.get('http://localhost:8081/iphone')
    assert ProductPage(browser).check_title_page('iPhone')
    assert len(ProductPage(browser).elements(ProductPage.IMAGES)) == 6
    ProductPage(browser).element(ProductPage.ADD_TO_WISHLIST)
    ProductPage(browser).element(ProductPage.COMPARE_THIS_PRODUCT)
    ProductPage(browser).element(ProductPage.ADD_TO_CARD)
    assert ProductPage(browser).get_text_of_element(ProductPage.PRODUCT_NAME).lower() in 'iphone'
