"""
-*- coding: UTF-8 -*-
@author: yuanhai
@time: 2024/9/5 10:17
desc:

"""
import pytest


@pytest.fixture(scope="session")
def login():
    a = 1
    return a