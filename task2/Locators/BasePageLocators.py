from selenium.webdriver.common.by import By


class BaseLocators:
    STORE_BUTTON = (
        By.XPATH, "//a[contains(@class, 'menuitem') and contains(text(), 'STORE')]")
    ABOUT_BUTTON = (
        By.XPATH, "//a[contains(@class, 'menuitem') and contains(text(), 'ABOUT')]")
