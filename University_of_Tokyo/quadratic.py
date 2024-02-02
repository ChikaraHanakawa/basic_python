#!/user/bin/env python3
# -*- coding: utf-8 -*-
import math
import numpy as np

def quadratic(a, b, c, x):
    return a * x ** 2 + b * x + c
assert quadratic(1, 2, 1, 3) == 16
assert quadratic(1, -5, -2, 7) == 12