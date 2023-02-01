# -*- coding: utf-8 -*-
import time
from functools import lru_cache


@lru_cache(maxsize=None)
def calculate_score(class_id):
    print(f"Calculating score for class: {class_id}...")
    time.sleep(5)
    return 42


print(calculate_score(100))
print(calculate_score(100))
