import pytest
from selene import browser


@pytest.mark.parametrize('browser_size', [(1280, 920)], indirect=True)
def test_open_github_sign_in_page_desktop():
        browser.open('/')
        browser.element('.HeaderMenu-link--sign-in').click()


@pytest.mark.parametrize('browser_size', [(600, 900)], indirect=True)
def test_open_github_sign_in_page_mobile():
        browser.open('/')
        browser.element('.Button--link .Button-content').click()
        browser.element('.HeaderMenu-link--sign-in').click()