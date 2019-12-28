#!/usr/bin/python
# -*- coding: utf-8 -*-
import pytest
import numpy as np

import sys
sys.path.append('/mnt/c/Users/shint/dev/0_deeplearning//3_NeuralNetwork/src')
from neuralnetwork import step_function

@pytest.mark.parametrize("x, expected",[
    ([-1.0, 1.0, 2.0], [0, 1, 1]),
])
def test_step_fucntion(x, expected):
    res = step_function(np.array(x))
    print(res, type(res))
    assert list(res) == expected
