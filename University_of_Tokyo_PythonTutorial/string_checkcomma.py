#!/user/bin/env python3
# -*- coding: utf-8 -*-
import math
import numpy as np

def remove_clause(str_engsentences):
    if ',' in str_engsentences:
        return False
    else:
        return True
print(remove_clause("It's being seen, but you aren't observing.") == "But you aren't observing.")