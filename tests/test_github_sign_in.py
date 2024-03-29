from selene import browser


def test_open_github_sign_in_page_desktop(desktop_size):
    browser.open('/')
    browser.element('.HeaderMenu-link--sign-in').click()


def test_open_github_sign_in_page_mobile(mobile_size):
    browser.open('/')
    browser.element('.Button--link .Button-content').click()
    browser.element('.HeaderMenu-link--sign-in').click()
