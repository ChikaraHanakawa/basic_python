#!/user/bin/env python3
# -*- coding: utf-8 -*-
import math
import numpy as np

def atgc_bppair(str_atgc):
    str_pair = str_atgc.translate(str.maketrans('ATGC', 'TACG'))
    return str_pair
print(atgc_bppair('AAGCCCCATGGTAA') == 'TTCGGGGTACCATT')