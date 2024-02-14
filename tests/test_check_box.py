import allure
import pytest

from pageObjects.check.assertion_test import AssertionTest
from data.constants import Const
from pageObjects.pages.check_box_page import CheckBoxPage


class TestCheckBox:
    @allure.feature('Checkbox')
    @pytest.mark.parametrize(
        'open_page', [{'class': CheckBoxPage, 'url': Const.URL_CHECK_BOX_PAGE}],
        indirect=True)
    def test_check_box(self, open_page):
        open_page.open_full_list()
        open_page.click_random_check_box()
        input_data = open_page.get_checked_checkbox()
        output_data = open_page.get_checked_output()
        AssertionTest().equality_of_several_arguments(input_data, output_data)