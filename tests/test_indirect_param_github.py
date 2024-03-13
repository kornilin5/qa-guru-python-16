import pytest
from selene import browser


@pytest.mark.parametrize('desktop_size', [(1280, 920)], indirect=True)
def test_open_github_sign_in_page_desktop(desktop_size):
    browser.open('/')
    browser.element('.HeaderMenu-link--sign-in').click()


@pytest.mark.parametrize('mobile_size', [(700, 900)], indirect=True)
def test_open_github_sign_in_page_mobile(mobile_size):
    browser.open('/')
    browser.element('.Button--link .Button-content').click()
    browser.element('.HeaderMenu-link--sign-in').click()
