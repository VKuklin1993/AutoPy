import allure
import pytest

from pageObjects.check.assertion_test import AssertionTest
from data.constants import Const
from pageObjects.pages.radio_button_page import RadioButtonPage


class TestRadioButton:
    @allure.feature('Radio button')
    @pytest.mark.parametrize(
        'open_page', [{'class': RadioButtonPage, 'url': Const.URL_RADIO_BUTTON}],
        indirect=True)
    def test_radio_button(self, open_page):
        input_data, output_data = open_page.click_and_get_value()
        AssertionTest().equality_of_several_arguments(input_data, output_data)
