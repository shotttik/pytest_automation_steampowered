from calendar import c

from task2.Pages.GamePage import GamePage
from .BasePage import BasePage
from task2.Locators.TopSellersLocators import TopSellersLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


class TopSellersPage(GamePage):

    def __init__(self, driver, wait_time, search_options):
        super().__init__(driver, wait_time)
        self.search_options = search_options

    # verifying page by page header
    def verify_page(self):
        return self.verify_page_by_url_params('topsellers')

    def check_filter(self):
        for option in self.search_options['main']:
            option_element = TopSellersLocators.main_check_boxes(option)
            self.scroll_to_element(option_element)
            self.do_click_with_action(
                option_element)

        for option in self.search_options['additional']:
            block, check_box, all_checkbox = TopSellersLocators.additional_check_boxes(
                option['block'], option['data'])
            self.scroll_to_element(block)
            self.do_click_with_action(block)
            # wait for all elements in checkbox block
            self.wait_all_element_located(all_checkbox)
            self.driver.refresh()  # sometimes without this mypy isnot smart enough
            self.scroll_to_element(check_box)
            self.do_click_with_action(check_box)
            # WAITING FOR SEARCH RESULT
            self.wait_for_element_to_dissapear(
                TopSellersLocators.RESULT_WARNING_TEXT)

    def get_specific_game_info(self):
        # get game info and then go to the game details
        block, locators = TopSellersLocators.game_info(
            self.search_options['game_number'])
        self.scroll_to_element(block)

        title, date, price = self.get_game_info(
            *locators
        )
        return block, (title, date, price)
