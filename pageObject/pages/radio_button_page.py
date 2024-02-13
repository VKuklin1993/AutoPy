from pageObject.locators.radio_button_locators import RadioButtonLocators
from pageObject.pages.base_page import BasePage


class RadioButtonPage(BasePage):
    locators = RadioButtonLocators()

    def click_and_get_value(self):
        choices = {
            'Yes': self.locators.RADIO_YES,
            'Impressive': self.locators.RADIO_IMPRESSIVE,
            'No': self.locators.RADIO_NO
        }
        input_value = list(choices)
        output_value = []
        for key in choices.keys():
            self.element_is_visible(choices[key]).click()
            output_value.append(self.element_is_present(self.locators.OUTPUT_RESULT).text)
        return input_value, output_value


