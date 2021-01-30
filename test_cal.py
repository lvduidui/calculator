'''
    测试calculator类
'''
import time

import pytest
from read_data import read_yml
from homework.calculator import Calculator


class Test_cal:

    def setup_class(self):
        print('-----准备开始-----')
        self.cal = Calculator()
        time.sleep(0.5)

    def teardown_class(self):
        print('-----测试完成-----')

    def setup_method(self):
        print('-----开始计算-----')

    def teardown_method(self):
        print('\n-----计算结束-----')

    @pytest.mark.parametrize('a, b', read_yml('./data.yml')['datas'], ids=read_yml('./data.yml')['myids'])
    def test_add(self, a, b):
        assert self.cal.add(a, b) == a+b

    @pytest.mark.parametrize('a, b', read_yml('./data.yml')['datas'], ids=read_yml('./data.yml')['myids'])
    def test_mul(self, a, b):
        assert self.cal.mul(a, b) == a*b

    @pytest.mark.parametrize('a, b', read_yml('./data.yml')['datas'], ids=read_yml('./data.yml')['myids'])
    def test_sub(self, a, b):
        assert self.cal.sub(a, b) == a-b

    @pytest.mark.parametrize('a, b', read_yml('./data.yml')['datas'], ids=read_yml('./data.yml')['myids'])
    def test_div(self, a, b):
        assert self.cal.div(a, b) == a/b


if __name__ == '__main__':
    pytest.main(['-sv','test_cal.py'])
