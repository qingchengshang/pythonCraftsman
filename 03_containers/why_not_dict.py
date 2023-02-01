# -*- coding: utf-8 -*-
class UpperDict(dict):
    """总是把 key 转为大写"""

    def __setitem__(self, key, value):
        super().__setitem__(key.upper(), value)


# 解释：为什么不直接继承字典dict
d = UpperDict()
d["name"] = "Yuan"
print(d)

d.update(age=18)
print(d)
