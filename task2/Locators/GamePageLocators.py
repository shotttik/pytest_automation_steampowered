from selenium.webdriver.common.by import By


class GameLocators:
    GAME_NAME = (By.XPATH, "//div[@id='appHubAppName']")
    REALASE_DATE = (By.XPATH, "//div[@class='date']")
    PRICE = (
        By.XPATH, "//div[@class='game_purchase_action_bg']//div[@data-price-final]")
