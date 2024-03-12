import pytest
from selene import browser


@pytest.fixture(params=['desktop', 'mobile'], scope='function', autouse=True)
def setup_browser(request):
    if request.param == 'desktop':
        browser.config.base_url = "https://github.com/"
        browser.config.window_width = 1920
        browser.config.window_height = 1080
    elif request.param == 'mobile':
        browser.config.base_url = "https://github.com/"
        browser.config.window_width = 480
        browser.config.window_height = 800
    else:
        browser.config.base_url = "https://github.com/"
        browser.config.window_width = 1920
        browser.config.window_height = 1080

    yield
    browser.quit()
