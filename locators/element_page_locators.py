from selenium.webdriver.common.by import By


class TextBoxPageLocators:
    FULL_NAME = (By.CSS_SELECTOR, "input[id = 'userName']")
    EMAIL = (By.CSS_SELECTOR, "input[id = 'userEmail']")
    CURRENT_ADDRESS = (By.CSS_SELECTOR, "textarea[id = 'currentAddress']")
    PERMANENT_ADDRESS = (By.CSS_SELECTOR, "textarea[id = 'permanentAddress']")
    BTN_SUBMIT = (By.CSS_SELECTOR, "button[id = 'submit']")
    OUTPUT_FULL_NAME = (By.XPATH, "//p[@id = 'name']")
    OUTPUT_EMAIL = (By.XPATH, "//p[@id = 'email']")
    OUTPUT_CURRENT_ADDRESS = (By.XPATH, "//p[@id = 'currentAddress']")
    OUTPUT_PERMANENT_ADDRESS = (By.XPATH, "//p[@id = 'permanentAddress']")


class CheckBoxPageLocators:
    EXPAND_ALL_BUTTON = (By.XPATH, "//button[@title = 'Expand all']")
    ITEM_LIST = (By.XPATH, "//span[@class= 'rct-title']")
    CHECKED_ITEMS = (By.CSS_SELECTOR, "svg[class = 'rct-icon rct-icon-check']")
    TITLE_ITEM = (By.XPATH, ".//ancestor::span[@class = 'rct-text']")
    OUTPUT_ITEM = (By.XPATH, "//span[@class = 'text-success']")


class RadioButtonLocators:
    RADIO_YES = (By.CSS_SELECTOR, "label[for = 'yesRadio']")
    RADIO_IMPRESSIVE = (By.CSS_SELECTOR, "label[for = 'impressiveRadio']")
    RADIO_NO = (By.CSS_SELECTOR, "label[for = 'noRadio']")
    OUTPUT_RESULT = (By.XPATH, "//span[@class = 'text-success']")

