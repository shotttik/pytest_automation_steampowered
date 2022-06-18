import pytest
from task2.Locators.AboutPageLocators import AboutLocators
from task2.Pages.MainPage import MainPage
from task2.Pages.AboutPage import AboutPage
from task2.Pages.TopSellersPage import TopSellersPage
from task2.Pages.GamePage import GamePage
from task2.utils import clean_stats_number


@pytest.mark.usefixtures("init_driver")
class Test_Case_1():

    def compare_stats(self):
        online = self.get_element_text(AboutLocators.ONLINE)
        playing = self.get_element_text(AboutLocators.PLAYING)
        clean_online = self.clean_stats_number(online)
        clean_playing = self.clean_stats_number(playing)
        return clean_playing < clean_online

    def test_case(self):
        # Main page
        self.main_page = MainPage(self.driver, self.wait_time)
        assert self.main_page.verify_page(), "Main Page couldn't be verified"
        self.main_page.click_about_button()
        # About Page
        self.about_page = AboutPage(self.driver, self.wait_time)
        assert self.about_page.verify_page(), "About Page couldn't be verified'"
        playing, online = self.about_page.get_stats_to_compare()
        clean_online = clean_stats_number(online)
        clean_playing = clean_stats_number(playing)
        assert clean_playing < clean_online, "Cannot compare stats"
        self.about_page.click_store_button()
        assert self.main_page.verify_page(), "Main Page couldn't be verified'"


@pytest.mark.usefixtures("init_driver")
class Test_Case_2():
    def test_case(self):
        # Main Page
        self.main_page = MainPage(self.driver, self.wait_time)
        assert self.main_page.verify_page(), "Main Page couldn't be verified"
        self.main_page.click_top_sellers()

        # Top Sellers Page
        self.top_sellers_page = TopSellersPage(
            self.driver, self.wait_time, self.search_options)
        assert self.top_sellers_page.verify_page(), "Top Sellers Page couldn't be verified"
        self.top_sellers_page.check_filter()
        block, game_store_info = self.top_sellers_page.get_specific_game_info()

        self.top_sellers_page.do_click_with_action(block)

        # Game Page
        self.game_page = GamePage(self.driver, self.wait_time)
        assert self.game_page.verify_page(), "Game Page couldn't be verified"
        game_details_info = self.game_page.get_detail_game_info()
        assert game_details_info == game_store_info, "Game's details don't match in the game store"
