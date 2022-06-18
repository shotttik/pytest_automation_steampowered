from task2.Locators.MainPageLocators import MainLocators
from task2.Locators.BasePageLocators import BaseLocators
from selenium.webdriver.common.action_chains import ActionChains
from .BasePage import BasePage


class MainPage(BasePage):
    '''
    The super() builtin returns a proxy object that allows us to access methods of the base class.
    '''

    def __init__(self, driver, wait_time):
        super().__init__(driver, wait_time)

    def click_about_button(self):
        element = self.driver.find_element(*BaseLocators.ABOUT_BUTTON)
        element.click()

    def verify_page(self):
        # verifying main page by main page main header
        return self.verify_page_by_element(MainLocators.MAIN_HEADER)

    def click_top_sellers(self):
        '''
        Move pointer to 'New & Noteworthy' at page's menu. Using explicit waits wait until popup menu shows up.
        '''
        actions = ActionChains(self.driver)
        nav_element = self.driver.find_element(
            *MainLocators.NEWS_NOTEWORTHY)
        actions.move_to_element(nav_element).perform()
        self.do_click(MainLocators.TOP_SELLERS)
