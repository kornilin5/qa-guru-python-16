import pytest
from selene import browser


@pytest.mark.parametrize('browser_size', [(400, 800)], indirect=True)
def test_open_github_sign_in_page_desktop():
    if browser.config.window_width == 400 and browser.config.window_height == 800:
        pytest.skip("Передано значение мобильного")
    else:
        browser.open('/')
        browser.element('.HeaderMenu-link--sign-in').click()


@pytest.mark.parametrize('browser_size', [(1920, 1080)], indirect=True)
def test_open_github_sign_in_page_mobile():
    if browser.config.window_width == 1920 and browser.config.window_height == 1080:
        pytest.skip("Передано значение десктопа")
    else:
        browser.open('/')
        browser.element('.Button--link .Button-content').click()
        browser.element('.HeaderMenu-link--sign-in').click()
