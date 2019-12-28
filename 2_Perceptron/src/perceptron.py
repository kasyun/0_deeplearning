#!/usr/bin/python
# -*- coding: utf-8 -*-

def circuit_and(x1, x2):
    w1, w2, theta = 0.5, 0.5, 0.7
    tmp = x1*w1 + x2*w2
    if tmp <= theta:
        return 0
    elif tmp > theta:
        return 1
    else:
        # error
        return -1

def circuit_nand(x1, x2):
    return 0

def circuit_or(x1, x2):
    return 0

def circuit_xor(x1, x2):
    return 0
