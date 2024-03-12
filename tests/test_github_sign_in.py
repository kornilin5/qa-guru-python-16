import pytest
from selene import browser


@pytest.mark.parametrize('setup_browser', ['desktop', 'mobile'], indirect=True)
def test_open_github_sign_in_page_desktop():
    if browser.config.window_width == 480 and browser.config.window_height == 800:
        pytest.skip("Пропускаем тест так как размер desktop")
    else:
        browser.open('/')
        browser.element('.HeaderMenu-link--sign-in').click()


@pytest.mark.parametrize('setup_browser', ['desktop', 'mobile'], indirect=True)
def test_open_github_sign_in_page_mobile():
    if browser.config.window_width == 1920 and browser.config.window_height == 1080:
        pytest.skip("Пропускаем тест так как размер mobile")
    else:
        browser.open('/')
        browser.element('.Button--link .Button-content').click()
        browser.element('.HeaderMenu-link--sign-in').click()
