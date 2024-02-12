import pytest
import check.assertion_test

from pages.text_box_page import TextBoxPage
from pages.check_box_page import CheckBoxPage
from pages.radio_button_page import RadioButtonPage


class TestElement:
    class TestTextBox:
        @pytest.mark.parametrize(
            'open_page', [{'class': TextBoxPage, 'url': 'https://demoqa.com/text-box'}],
            indirect=True)
        def test_text_box(self, open_page):
            input_data = open_page.fill_fields()
            output_data = open_page.check_field()
            assertion = check.assertion_test.AssertionTest()
            assertion.equality_of_several_arguments(input_data, output_data)

    class TestCheckBox:
        @pytest.mark.parametrize(
            'open_page', [{'class': CheckBoxPage, 'url': 'https://demoqa.com/checkbox'}],
            indirect=True)
        def test_check_box(self, open_page):
            open_page.open_full_list()
            open_page.click_random_check_box()
            input_data = open_page.get_checked_checkbox()
            output_data = open_page.get_checked_output()
            assertion = check.assertion_test.AssertionTest()
            assertion.equality_of_several_arguments(input_data, output_data)

    class TestRadioButton:
        @pytest.mark.parametrize(
            'open_page', [{'class': RadioButtonPage, 'url': 'https://demoqa.com/radio-button'}],
            indirect=True)
        def test_radio_button(self, open_page):
            input_data, output_data = open_page.click_and_get_value()
            assertion = check.assertion_test.AssertionTest()
            assertion.equality_of_several_arguments(input_data, output_data)

