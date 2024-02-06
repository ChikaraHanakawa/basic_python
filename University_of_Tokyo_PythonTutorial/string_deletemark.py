#!/user/bin/env python3
# -*- coding: utf-8 -*-
import math
import numpy as np

def remove_punctuations(str_engsentences):
    if ',' in str_engsentences:
        return False
    elif '.' in str_engsentences:
        return False
    elif '!' in str_engsentences:
        return False
    elif '?' in str_engsentences:
        return False
    elif ';' in str_engsentences:
        return False
    elif ':' in str_engsentences:
        return False
    else:
        return True
print(remove_punctuations('Quiet, uh, donations, you want me to make a donation to the coast guard youth auxiliary?') == 'Quiet uh donations you want me to make a donation to the coast guard youth auxiliary')
