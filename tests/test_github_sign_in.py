import pytest
from selene import browser


@pytest.mark.parametrize('setup_browser', ['desktop'], indirect=True)
def test_open_github_sign_in_page_desktop():
    browser.open('/')
    browser.element('.HeaderMenu-link--sign-in').click()


@pytest.mark.parametrize('setup_browser', ['mobile'], indirect=True)
def test_open_github_sign_in_page_mobile():
    browser.open('/')
    browser.element('.Button--link .Button-content').click()
    browser.element('.HeaderMenu-link--sign-in').click()
