import pytest
from selenium import webdriver
from Utils.read_config import get_config

@pytest.fixture()
def setup_and_teardown(request):
    browser_type = get_config('browser', 'type')
    base_url = get_config('server', 'url')
    if browser_type.lower() == "chrome":
        driver = webdriver.Chrome()
    elif browser_type.lower() == "firefox":
        driver = webdriver.Firefox()
    else:
        raise Exception(f"Browser '{browser_type}' is not supported")

    driver.maximize_window()
    driver.get(base_url)
    request.cls.driver = driver
    yield
    driver.quit()
