import pytest
from selene import browser


@pytest.fixture(params=[(1920, 1080)], scope='function')
def browser_size(request):
    return request.param


@pytest.fixture(scope='function', autouse=True)
def setup_browser(browser_size):
    width, height = browser_size
    browser.config.base_url = "https://github.com/"
    browser.config.window_width = width
    browser.config.window_height = height
    yield
    browser.quit()
