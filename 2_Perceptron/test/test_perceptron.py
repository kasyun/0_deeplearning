#!/usr/bin/python
# -*- coding: utf-8 -*-
from perceptron import circuit_and, circuit_nand, circuit_or, circuit_xor
import pytest

import sys
# sys.path.append('C:/Users/shint/dev/0_deeplearning/2_Perceptron/src')
sys.path.append('/mnt/c/Users/shint/dev/0_deeplearning/2_Perceptron/src')


@pytest.mark.parametrize("x, y, expected", [
    (0, 0, 0),
    (0, 1, 0),
    (1, 0, 0),
    (1, 1, 1),
])
def test_and(x, y, expected):
    res = circuit_and(x, y)
    assert res == expected


@pytest.mark.parametrize("x, y, expected", [
    (0, 0, 1),
    (0, 1, 1),
    (1, 0, 1),
    (1, 1, 0),
])
def test_nand(x, y, expected):
    res = circuit_nand(x, y)
    assert res == expected


@pytest.mark.parametrize("x, y, expected", [
    (0, 0, 0),
    (0, 1, 1),
    (1, 0, 1),
    (1, 1, 1),
])
def test_or(x, y, expected):
    res = circuit_or(x, y)
    assert res == expected


@pytest.mark.parametrize("x, y, expected", [
    (0, 0, 0),
    (0, 1, 1),
    (1, 0, 1),
    (1, 1, 0),
])
def test_xor(x, y, expected):
    res = circuit_xor(x, y)
    assert res == expected
