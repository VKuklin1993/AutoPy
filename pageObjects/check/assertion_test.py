import allure


class AssertionTest:

    @staticmethod
    def equality_of_several_arguments(input_data, output_data):
        with allure.step('Comparison of input and output data'):
            assert input_data == output_data, 'discrepancies in input and output data'
