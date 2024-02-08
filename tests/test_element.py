from pages.element_page import TextBoxPage
import time


class TestElement:
    class TestTextBox:
        def test_text_box(self, driver):
            text_box_page = TextBoxPage(driver, 'https://demoqa.com/text-box')
            text_box_page.open_url()
            input_data = text_box_page.fill_fields()
            output_data = text_box_page.check_field()
            assert input_data == output_data, 'discrepancies in input and output data'
