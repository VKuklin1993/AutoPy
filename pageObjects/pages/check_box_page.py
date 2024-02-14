import allure
import random

from pageObjects.locators.check_box_page_locators import CheckBoxPageLocators
from pageObjects.pages.base_page import BasePage


class CheckBoxPage(BasePage):
    locators = CheckBoxPageLocators()

    def open_full_list(self):
        with allure.step('Expanding lists of all check boxes'):
            self.element_is_visible(self.locators.EXPAND_ALL_BUTTON).click()

    def click_random_check_box(self):
        with allure.step('Selection of different checkboxes'):
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
        with allure.step('Wrote down the selected check boxes'):
            checked_checkbox = self.elements_is_present(self.locators.CHECKED_ITEMS)
            data = []
            for item in checked_checkbox:
                title_item = item.find_element(*self.locators.TITLE_ITEM)
                data.append(title_item.text.lower())
            return str(data).replace(' ', '').replace('.doc', '').lower()

    def get_checked_output(self):
        with allure.step('Recorded the values after selecting the checkboxes'):
            output_data = self.elements_is_present(self.locators.OUTPUT_ITEM)
            data = []
            for item in output_data:
                data.append(item.text.lower())
            return str(data).replace(' ', '').lower()
