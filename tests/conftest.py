import pytest

from selene import browser


@pytest.fixture(params=[(1920, 1080), (1600, 900)], scope='function')
def desktop_size(request):
    browser.config.base_url = 'https://github.com'
    [width, height] = request.param
    browser.config.window_width = width
    browser.config.window_height = height
    yield browser
    browser.quit()


@pytest.fixture(params=[(400, 800), (500, 900)], scope='function')
def mobile_size(request):
    browser.config.base_url = 'https://github.com'
    width, height = request.param
    browser.config.window_width = width
    browser.config.window_height = height
    yield browser
    browser.quit()


@pytest.fixture(params=[(1920, 1080), (400, 800)],
                scope='function')
def desktop_mobile_size(request):
    browser.config.base_url = 'https://github.com'
    width, height = request.param
    browser.config.window_width = width
    browser.config.window_height = height
    yield browser
    browser.quit()
