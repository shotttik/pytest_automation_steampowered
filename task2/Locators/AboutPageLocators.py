from selenium.webdriver.common.by import By


class AboutLocators:
    ABOUT_GREETING = (By.XPATH, "//div[@id='about_greeting']")
    ONLINE = (By.XPATH, "//div[contains(@class,'gamers_online')]/..")
    PLAYING = (By.XPATH, "//div[contains(@class,'gamers_in_game')]/..")
