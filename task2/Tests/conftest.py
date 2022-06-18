from this import d
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
import json
from .singleton import Singleton


# @TODO NEED TO IMPROVE THIS TWO FUNCTIONS
@pytest.fixture(scope='session')
def config():
    with open('task2/Resources/config.json') as f:
        data = json.load(f)
        f.close()
    return data


@pytest.fixture(scope='session')
def config_browser(config):
    if 'browser' not in config:
        raise Exception('The config file does not contain "browser"')
    elif config['browser'] not in ['chrome', 'firefox']:
        raise Exception(f'"{config["browser"]}" is not a supported browser')
    return config


@pytest.fixture(scope="session")
def test_data():
    with open('task2/Resources/testing_data.json') as f:
        data = json.load(f)
        f.close()
    return data


@pytest.fixture(scope="class")
def init_driver(request, config_browser, test_data):
    c = Singleton(config_browser, test_data["base_url"])
    request.cls.driver = c.driver
    request.cls.wait_time = c.wait_time
    request.cls.search_options = test_data["search_options"]
    c.driver.implicitly_wait(c.wait_time)
    yield c.driver
    c.driver.quit()
