def test_ya_ru_title(browser):
    browser.get('https://ya.ru')
    assert 'Яндекс' in browser.title


def test_google_ru_title(browser):
    browser.get('https://google.com')
    assert 'Google' in browser.title
