from page_objects.CatalogPage import CatalogPage


def test_catalog_page_content(browser):
    browser.get('http://localhost:8081/smartphone')
    assert CatalogPage(browser).check_title_page('Phones & PDAs')
    CatalogPage(browser).element(CatalogPage.BREADCRUMB)
    assert len(CatalogPage(browser).elements(CatalogPage.PRODUCT_LAYOUT)) == 3
    CatalogPage(browser).element(CatalogPage.LIST_GROUP)
    assert len(CatalogPage(browser).elements(CatalogPage.LIST_GROUP_ITEMS)) == 8
    CatalogPage(browser).element(CatalogPage.CONTENT)
