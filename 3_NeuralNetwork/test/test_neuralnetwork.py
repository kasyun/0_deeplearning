#!/usr/bin/python
# -*- coding: utf-8 -*-
from src.neuralnetwork import step_function
import pytest
import numpy as np


@pytest.mark.parametrize("x, expected", [
    ([-1.0, 1.0, 2.0], [0, 1, 1]),
])
def test_step_fucntion(x, expected):
    res = step_function(np.array(x))
    print(res, type(res))
    assert list(res) == expected
