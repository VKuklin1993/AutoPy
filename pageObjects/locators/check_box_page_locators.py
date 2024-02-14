from selenium.webdriver.common.by import By


class CheckBoxPageLocators:
    EXPAND_ALL_BUTTON = (By.XPATH, "//button[@title = 'Expand all']")
    ITEM_LIST = (By.XPATH, "//span[@class= 'rct-title']")
    CHECKED_ITEMS = (By.CSS_SELECTOR, "svg[class = 'rct-icon rct-icon-check']")
    TITLE_ITEM = (By.XPATH, ".//ancestor::span[@class = 'rct-text']")
    OUTPUT_ITEM = (By.XPATH, "//span[@class = 'text-success']")
