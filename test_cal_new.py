import time

import pytest
from read_data import read_yml
from homework.calculator import Calculator


class Test_cal:
    @pytest.mark.run(order=1)
    def test_add(self, get_cal, get_datas, prepare_clear_work):
        assert get_cal.add(get_datas[0], get_datas[1]) == get_datas[2]

    @pytest.mark.run(order=4)
    def test_div(self, get_cal, get_datas, prepare_clear_work):
        assert get_cal.div(get_datas[0], get_datas[1]) == get_datas[2]

    @pytest.mark.run(order=2)
    def test_sub(self, get_cal, get_datas, prepare_clear_work):
        assert get_cal.sub(get_datas[0], get_datas[1]) == get_datas[2]

    @pytest.mark.run(order=3)
    def test_mul(self, get_cal, get_datas, prepare_clear_work):
        assert get_cal.mul(get_datas[0], get_datas[1]) == get_datas[2]
