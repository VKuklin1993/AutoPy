from pages.element_page import TextBoxPage, CheckBoxPage
import time


class TestElement:
    class TestTextBox:
        def test_text_box(self, driver):
            text_box_page = TextBoxPage(driver, 'https://demoqa.com/text-box')
            text_box_page.open_url()
            input_data = text_box_page.fill_fields()
            output_data = text_box_page.check_field()
            assert input_data == output_data, 'discrepancies in input and output data'

    class TestCheckBox:
        def test_check_box(self, driver):
            check_box_page = CheckBoxPage(driver, 'https://demoqa.com/checkbox')
            check_box_page.open_url()
            check_box_page.open_full_list()
            check_box_page.click_random_check_box()
            input_data = set(check_box_page.get_checked_checkbox())
            output_data = set(check_box_page.get_checked_output())
            assert input_data == output_data
