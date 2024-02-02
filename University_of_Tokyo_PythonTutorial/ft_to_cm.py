#!/user/bin/env python3
# -*- coding: utf-8 -*-
import math
import numpy as np

def ft_to_cm(f, i):
    f = f * 30.48
    i = i * 2.54
    return f + i

assert round(ft_to_cm(5, 2) - 157.48, 6) == 0
assert round(ft_to_cm(6, 5) - 195.58, 6) == 0