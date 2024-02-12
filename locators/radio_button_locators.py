from selenium.webdriver.common.by import By


class RadioButtonLocators:
    RADIO_YES = (By.CSS_SELECTOR, "label[for = 'yesRadio']")
    RADIO_IMPRESSIVE = (By.CSS_SELECTOR, "label[for = 'impressiveRadio']")
    RADIO_NO = (By.CSS_SELECTOR, "label[for = 'noRadio']")
    OUTPUT_RESULT = (By.XPATH, "//span[@class = 'text-success']")
