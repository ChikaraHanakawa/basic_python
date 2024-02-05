#!/user/bin/env python3
# -*- coding: utf-8 -*-
import math
import numpy as np

def check_lower(str_engsentences):
    if str_engsentences.islower():
        return False
    else:
        return True
print(check_lower('down down down') == True)
print(check_lower('There were doors all round the hall, but they were all locked') == False)