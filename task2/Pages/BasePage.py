from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from datetime import datetime
import re
import time


class BasePage:
    def __init__(self, driver, wait_time):
        self.driver = driver
        self.wait_time = wait_time
        self.actions = ActionChains(driver)

    def get_title(self, title):
        WebDriverWait(self.driver, self.wait_time).until(EC.title_is(title))
        return self.driver.title

    def do_click(self, by_locator):
        WebDriverWait(self.driver, self.wait_time).until(
            EC.visibility_of_element_located(by_locator)).click()

    def do_click_with_action(self, by_locator):
        el = WebDriverWait(self.driver, self.wait_time).until(
            EC.presence_of_element_located(by_locator))
        self.actions.move_to_element(el).click().perform()

    def wait_all_element_located(self, by_locator):
        WebDriverWait(self.driver, self.wait_time).until(
            EC.visibility_of_all_elements_located(by_locator))

    def wait_for_element_to_dissapear(self, by_locator):
        WebDriverWait(self.driver, self.wait_time).until(
            EC.invisibility_of_element_located(by_locator))

    def get_element_text(self, by_locator):
        element = WebDriverWait(self.driver, self.wait_time).until(
            EC.visibility_of_element_located(by_locator)
        )
        return element.text

    def verify_page_by_element(self, by_locator):
        element = WebDriverWait(self.driver, self.wait_time).until(
            EC.visibility_of_element_located(by_locator)
        )
        return bool(element)

    def verify_page_by_element_text(self, by_locator, text):
        element = WebDriverWait(self.driver, self.wait_time).until(
            EC.visibility_of_element_located(by_locator)
        )
        return element.text == text

    def verify_page_by_url_params(self, filter_name):
        return f'?filter={filter_name}' in self.driver.current_url

    def get_element_attribute_value(self, by_locator, attribute):
        element = WebDriverWait(self.driver, self.wait_time).until(
            EC.visibility_of_element_located(by_locator)
        )
        val = element.get_attribute(attribute)
        return int(val) if val is not None else None

    def scroll(self, page_split):
        self.driver.execute_script(
            f"window.scrollTo(0, document.body.scrollHeight/{page_split});")

    def scroll_to_element(self, by_locator):
        element = WebDriverWait(self.driver, self.wait_time).until(
            EC.visibility_of_element_located(by_locator)
        )
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
