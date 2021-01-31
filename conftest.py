import pytest
from read_data import read_yml
from homework.calculator import Calculator
import os

file_path = os.path.dirname(__file__) + '/data.yml'


@pytest.fixture(scope='module')
def get_cal():
    # 实例化计算器并返回
    cal = Calculator()
    return cal


@pytest.fixture(params=read_yml(file_path)['datas'])
def get_datas(request):
    datas = request.param
    return datas


@pytest.fixture()
def prepare_clear_work():
    print('\n-----开始计算-----')
    yield
    print('\n-----计算结束-----')


if __name__ == '__main__':
    get_datas()
