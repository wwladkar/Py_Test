import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as OptionsChrome
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager


def pytest_addoption(parser):
    parser.addoption('--language',
                     action='store',
                     default=None,
                     help="Choose language: '--language=en' or '--language=ru'")


@pytest.fixture(scope="function")
def browser(request):
    user_language = request.config.getoption("language")

    print("\nstart chrome browser for test..")
    options = OptionsChrome()
    options.add_argument("start-maximized")
    options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
    browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()),
                               options=options)

    yield browser
    print("\nquit browser..")
    browser.quit()
