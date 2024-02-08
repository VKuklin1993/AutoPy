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
