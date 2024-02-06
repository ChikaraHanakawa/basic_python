#!/user/bin/env python3
# -*- coding: utf-8 -*-
import math
import numpy as np

def swap_colon(str1):
    if ':' in str1:
        parts = str1.split(':')
        return ':'.join(parts[::-1])
    else:
        return str1
print(swap_colon('hello:world') == 'world:hello')