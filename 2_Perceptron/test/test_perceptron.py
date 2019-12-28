#!/usr/bin/python
# -*- coding: utf-8 -*-
from src/perceptron import circuit_and, circuit_nand, circuit_or, circuit_xor

@pytest.mark.parametrize("x, y, expected",[
    (0, 0, 0),
    (0, 1, 0),
    (1, 0, 0),
    (1, 1, 1),
])
def test_and(x, y, expected):
    ret = circuit_and(x, y)
    assert res == expected

@pytest.mark.parametrize("x, y, expected",[
    (0, 0, 1),
    (0, 1, 1),
    (1, 0, 1),
    (1, 1, 0),
])
def test_nand(x, y, expected):
    ret = circuit_nand(x, y)
    assert res == expected

@pytest.mark.parametrize("x, y, expected",[
    (0, 0, 0),
    (0, 1, 1),
    (1, 0, 1),
    (1, 1, 1),
])
def test_or(x, y, expected):
    ret = circuit_or(x, y)
    assert res == expected

@pytest.mark.parametrize("x, y, expected",[
    (0, 0, 1),
    (0, 1, 0),
    (1, 0, 0),
    (1, 1, 0),
])
def test_xor(x, y, expected):
    ret = circuit_xor(x, y)
    assert res == expected
