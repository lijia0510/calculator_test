import order as order
import pytest
import allure

from common.HandleData import get_yaml, yaml_data_with_key
from common.calculator import Calculator


class TestCalculator:
    # file = get_yaml('test_data.yaml')

    def setup_class(self):
        self.cal = Calculator()

    def teardown(self):
        print("结束计算")

    def teardown_class(self):
        print('结束测试')

    @pytest.mark.parametrize("test_add", yaml_data_with_key('add_case'))
    def test_add(self, test_add):

        allure.dynamic.title(test_add['title'])
        a = test_add['a']
        b = test_add['b']
        assert self.cal.add(a, b) == test_add['expected_result']
