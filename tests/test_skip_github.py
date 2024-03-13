import pytest
from selene import browser


def test_open_github_sign_in_page_desktop(desktop_mobile_size):
    if browser.config.window_width == 400 and browser.config.window_height == 800:
        pytest.skip("Передано значение мобильного")
    else:
        browser.open('/')
        browser.element('.HeaderMenu-link--sign-in').click()


def test_open_github_sign_in_page_mobile(desktop_mobile_size):
    if browser.config.window_width == 1920 and browser.config.window_height == 1080:
        pytest.skip("Передано значение десктопа")
    else:
        browser.open('/')
        browser.element('.Button--link .Button-content').click()
        browser.element('.HeaderMenu-link--sign-in').click()
