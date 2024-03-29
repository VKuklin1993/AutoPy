import allure

from data.data import Person
from pageObjects.locators.text_box_page_locators import TextBoxPageLocators
from pageObjects.pages.base_page import BasePage


class TextBoxPage(BasePage):
    locators = TextBoxPageLocators()

    def fill_fields(self):
        with allure.step('Entering data into fields'):
            person_info = Person()
            name = person_info.full_name
            email = person_info.email
            current_address = person_info.current_address
            permanent_address = person_info.permanent_address
            self.element_is_visible(self.locators.FULL_NAME).send_keys(name)
            self.element_is_visible(self.locators.EMAIL).send_keys(email)
            self.element_is_visible(self.locators.CURRENT_ADDRESS).send_keys(current_address)
            self.element_is_visible(self.locators.PERMANENT_ADDRESS).send_keys(permanent_address)
            self.element_is_visible(self.locators.BTN_SUBMIT).click()
            return *name, *email, *current_address, permanent_address

    def check_field(self):
        with allure.step('Output of entered data in the second field'):
            output_name = self.element_is_present(self.locators.OUTPUT_FULL_NAME).text.split(':')[1]
            output_email = self.element_is_present(self.locators.OUTPUT_EMAIL).text.split(':')[1]
            output_current_address = self.element_is_present(self.locators.OUTPUT_CURRENT_ADDRESS).text.split(':')[1]
            output_permanent_address = self.element_is_present(self.locators.OUTPUT_PERMANENT_ADDRESS).text.split(':')[1]
            return output_name, output_email, output_current_address, output_permanent_address
