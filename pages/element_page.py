import random


from generator.generator import generated_person
from locators.element_page_locators import TextBoxPageLocators, CheckBoxPageLocators, RadioButtonLocators
from pages.base_page import BasePage


class TextBoxPage(BasePage):
    locators = TextBoxPageLocators()

    def fill_fields(self):
        person_info = next(generated_person())
        name = person_info.full_name
        email = person_info.email
        current_address = person_info.current_address
        permanent_address = person_info.permanent_address
        self.element_is_visible(self.locators.FULL_NAME).send_keys(name)
        self.element_is_visible(self.locators.EMAIL).send_keys(email)
        self.element_is_visible(self.locators.CURRENT_ADDRESS).send_keys(current_address)
        self.element_is_visible(self.locators.PERMANENT_ADDRESS).send_keys(permanent_address)
        self.element_is_visible(self.locators.BTN_SUBMIT).click()
        return name, email, current_address, permanent_address

    def check_field(self):
        output_name = self.element_is_present(self.locators.OUTPUT_FULL_NAME).text.split(':')[1]
        output_email = self.element_is_present(self.locators.OUTPUT_EMAIL).text.split(':')[1]
        output_current_address = self.element_is_present(self.locators.OUTPUT_CURRENT_ADDRESS).text.split(':')[1]
        output_permanent_address = self.element_is_present(self.locators.OUTPUT_PERMANENT_ADDRESS).text.split(':')[1]
        return output_name, output_email, output_current_address, output_permanent_address



class CheckBoxPage(BasePage):
    locators = CheckBoxPageLocators()

    def open_full_list(self):
        self.element_is_visible(self.locators.EXPAND_ALL_BUTTON).click()

    def click_random_check_box(self):
        item_list = self.elements_all_visible(self.locators.ITEM_LIST)
        count = 10
        while count != 0:
            item = item_list[random.randint(1, 15)]
            if count > 0:
                self.scroll_to_element(item)
                item.click()
                count -= 1
            else:
                break

    def get_checked_checkbox(self):
        checked_checkbox = self.elements_is_present(self.locators.CHECKED_ITEMS)
        data = []
        for item in checked_checkbox:
            title_item = item.find_element(*self.locators.TITLE_ITEM)
            data.append(title_item.text.lower())
        return str(data).replace(' ', '').replace('.doc', '').lower()

    def get_checked_output(self):
        output_data = self.elements_is_present(self.locators.OUTPUT_ITEM)
        data = []
        for item in output_data:
            data.append(item.text.lower())
        return str(data).replace(' ', '').lower()


class RadioButtonPage(BasePage):
    locators = RadioButtonLocators()

    def click_radio_button(self, choice):
        choices = {
            'yes': self.locators.RADIO_YES,
            'impressive': self.locators.RADIO_IMPRESSIVE,
            'no': self.locators.RADIO_NO
        }
        self.element_is_visible(choices[choice]).click()

    def get_output_result(self):
        return self.element_is_present(self.locators.OUTPUT_RESULT).text