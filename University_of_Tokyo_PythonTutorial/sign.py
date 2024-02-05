#!/user/bin/env python3
# -*- coding: utf-8 -*-
import math
import numpy as np

def sign(x):
    if x > 0:
        return 1
    elif x < 0:
        return -1
    else:
        return 0
assert sign(5) == 1
assert sign(-5) == -1
assert sign(0) == 0