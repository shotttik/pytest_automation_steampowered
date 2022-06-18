from selenium.webdriver.common.by import By


class MainLocators:
    MAIN_HEADER = (
        By.XPATH, "//div[@class='home_page_content']//div[@id='store_header']")
    NEWS_NOTEWORTHY = (
        By.XPATH, "//div[@class='store_nav']//a[text()='New & Noteworthy']")
    TOP_SELLERS = (
        By.XPATH, "//div[@class='store_nav']//a[@class='popup_menu_item' and contains(text(), 'Top Sellers')]")
