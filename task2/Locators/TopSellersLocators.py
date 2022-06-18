from selenium.webdriver.common.by import By


class TopSellersLocators:

    RESULT_WARNING_TEXT = (
        By.XPATH, "//div[@id='search_results_filtered_warning_persistent']")

    @staticmethod
    def main_check_boxes(data):
        return (
            By.XPATH, f"//span[@data-loc='{data}']//span[@class='tab_filter_control_checkbox']")

    @staticmethod
    def additional_check_boxes(block, data):
        block_selector = (
            By.XPATH, f"//div[@id='additional_search_options']//div[text()='{block}']")
        check_box_selector = (
            By.XPATH, f"//span[@data-loc='{data}']//span[@class='tab_filter_control_checkbox']")
        all_checkbox_selector = (
            By.XPATH, f"//div[@id='additional_search_options']//div[text()='{block}']//..//..//div[@class='tab_filter_control_row ']")
        return block_selector, check_box_selector, all_checkbox_selector

    @staticmethod
    def game_info(game_number):
        block = (
            By.XPATH, f"//div[@id='search_resultsRows']//a[{game_number}]")
        title = (
            By.XPATH, f"//div[@id='search_resultsRows']//a[{game_number}]//span[@class='title']")
        game_release = (
            By.XPATH, f"//div[@id='search_resultsRows']//a[{game_number}]//div[contains(@class, 'search_released')]")
        price = (
            By.XPATH, f"//div[@id='search_resultsRows']//a[{game_number}]//div[@data-price-final]")
        return block, (title, game_release, price)
