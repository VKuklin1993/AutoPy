import allure
import pytest

from pageObjects.check.assertion_test import AssertionTest
from data.constants import Const
from pageObjects.pages.text_box_page import TextBoxPage


class TestTextBox:
    @allure.feature('Text field')
    @pytest.mark.parametrize(
        'open_page', [{'class': TextBoxPage, 'url': Const.URL_TEXT_BOX_PAGE}],
        indirect=True)
    def test_text_box(self, open_page):
        with allure.step('Entering data into fields'):
            input_data = open_page.fill_fields()
            output_data = open_page.check_field()
            AssertionTest().equality_of_several_arguments(input_data, output_data)
