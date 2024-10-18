# -*- coding: utf-8 -*-
import pytest
import os


@pytest.fixture
def lab1_string_array():
    return [
        ['python', 'perl', 'java', 'c', 'haskell', 'ruby'],
        ['perl', 'python', 'java', 'c', 'haskell', 'ruby'],
        ['', 'perl', 'java', 'c', 'haskell', 'ruby'],
        ['1', '11', '3', '01', '2', 'python'],
        ['python', 'perl', 'java', 'c', 'haskell', 'ruby']
    ]


@pytest.fixture
def lab1_unique_array():
    return [
        ['python', 'python', 'ruby', 'java', 'c', 'c++', 'ruby', 'ruby'],
        ['1', '1', 1, 'c', 1, 'aaaaaa'],
        ['', 3.15, '', 'c', 3.16, 'ruby'],
        [1, 11, 3, 1, 2, "python"],
        ['python', ' ', ' ', 'c', 0, '0000']
    ]


@pytest.fixture(scope="function")
def x(request):
    return request.param * 3


# def pytest_addoption(parser):
#     parser.addoption("--path", action="store", default=None)
#
#
# def pytest_generate_tests(metafunc):
#     option_value = metafunc.config.option.path
#     if 'path' in metafunc.fixturenames and option_value is not None:
#         metafunc.parametrize("path", [option_value])
