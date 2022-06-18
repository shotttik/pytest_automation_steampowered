from .BasePage import BasePage
from task2.Locators.AboutPageLocators import AboutLocators
from task2.Locators.BasePageLocators import BaseLocators


class AboutPage(BasePage):

    def __init__(self, driver, wait_time):
        super().__init__(driver, wait_time)

    def verify_page(self):
        return self.verify_page_by_element(AboutLocators.ABOUT_GREETING)

    def click_store_button(self):
        element = self.driver.find_element(*BaseLocators.STORE_BUTTON)
        element.click()

    def get_stats_to_compare(self):
        online = self.get_element_text(AboutLocators.ONLINE)
        playing = self.get_element_text(AboutLocators.PLAYING)
        return playing, online
