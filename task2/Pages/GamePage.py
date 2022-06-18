from multiprocessing.connection import wait

from task2.utils import get_datetime_object
from .BasePage import BasePage
from task2.Locators.GamePageLocators import GameLocators


class GamePage(BasePage):
    def __init__(self, driver, wait_time):
        super().__init__(driver, wait_time)

    # verifying page by the game title element
    def verify_page(self):
        return self.verify_page_by_element(GameLocators.GAME_NAME)

    def get_detail_game_info(self):
        title, date, price = self.get_game_info(
            GameLocators.GAME_NAME,
            GameLocators.REALASE_DATE,
            GameLocators.PRICE
        )
        return title, date, price

    def get_game_info(self, title_loc, date_loc, price_loc):
        title = self.get_element_text(title_loc)
        # first we are getting text from element and then converting string to datetime obj
        date = get_datetime_object(self.get_element_text(date_loc))
        price = self.get_element_attribute_value(
            price_loc, 'data-price-final')
        return title, date, price
