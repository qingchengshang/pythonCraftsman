# -*- coding: utf-8 -*-
# Instagram 在 PyCon 2017 的演讲摘要  https://www.zlovezl.cn/articles/instagram-pycon-2017/


def range_7_gen(start, end):
    """生成器版本的 Range7Iterator"""
    num = start
    while num < end:
        if num != 0 and (num % 7 == 0 or "7" in str(num)):
            yield num
        num += 1


for i in range_7_gen(0, 20):
    print(i)
