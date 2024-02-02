#!/user/bin/env python3
# -*- coding: utf-8 -*-
import math
import numpy as np
#le-5 = 1 * 10^-5 == 0.00001
def golden_ratio(f, a, b, tol=1e-5):
    #abs = absolute value
    while abs(b - a) > tol:
        c = (a + b) / 2
        if f(c) == 0:
            return c
        if f(a) * f(c) < 0:
            b = c
        else:
            a = c
    return (a + b) / 2
#np.cos = cos
#math.pi = pi
ans = golden_ratio(np.cos, 0, math.pi)
print(ans)
print((math.sqrt(5) + 1) / 2)