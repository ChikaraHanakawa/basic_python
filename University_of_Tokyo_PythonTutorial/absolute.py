#!/user/bin/env python3
# -*- coding: utf-8 -*-
import math
import numpy as np

def absolute(x):
    if x > 0:
        return x
    else:
        return -x

assert absolute(5) == 5
assert absolute(-5) == 5
assert absolute(0) == 0