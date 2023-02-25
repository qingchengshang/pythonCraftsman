# -*- coding: utf-8 -*-
import time
from functools import update_wrapper

# import random
# import time
# from functools import wraps
# from typing import Optional
#
#
# 用类来实现装饰器（函数替换）
# class timer:
#     """装饰器：打印函数耗时
#
#     :param print_args: 是否打印被方法名和参数，默认为 False
#     """
#     def __init__(self, print_args: Optional = False):
#         self.print_args = print_args
#
#     def __call__(self, func):
#         @wraps(func)
#         def decorated(*args, **kwargs):
#             st = time.perf_counter()
#             ret = func(*args, **kwargs)
#             if self.print_args:
#                 print(f'"{func.__name__}", args: {args}, kwargs: {kwargs}')
#             print("time cost: {} seconds".format(time.perf_counter() - st))
#             return ret
#
#         return decorated
#
#
# @timer(print_args=True)
# def random_sleep():
#     """随机睡眠一小会儿"""
#     time.sleep(random.random())
#
#
# if __name__ == '__main__':
#     random_sleep()


# 用类来实现装饰器（示例替换）
class DelayedStart:
    """在执行被装饰函数前，等待 1 秒钟"""

    def __init__(self, func):
        update_wrapper(self, func)
        self.func = func

    def __call__(self, *args, **kwargs):
        print("Wait for 1 second before starting...")
        time.sleep(1)
        return self.func(*args, **kwargs)

    def eager_call(self, *args, **kwargs):
        """跳过等待，立刻执行被装饰函数"""
        print("Call without delay")
        return self.func(*args, **kwargs)


@DelayedStart
def hello():
    print("Hello, World.")


# hello()

import functools


class DelayedStart:
    """在执行被装饰函数前，等待一段时间

    :param func: 被装饰的函数
    :param duration: 需要等待的秒数
    """

    def __init__(self, func, *, duration=1):
        update_wrapper(self, func)
        self.func = func
        self.duration = duration

    def __call__(self, *args, **kwargs):
        print(f"Wait for {self.duration} second before starting...")
        time.sleep(self.duration)
        return self.func(*args, **kwargs)

    def eager_call(self, *args, **kwargs):
        """跳过等待，立刻执行被装饰函数"""
        print("Call without delay")
        return self.func(*args, **kwargs)


def delayed_start(**kwargs):
    """装饰器：推迟某个函数的执行。同时提供 .eager_call 方法立即执行"""
    return functools.partial(DelayedStart, **kwargs)


@delayed_start(duration=2)
def hello():
    print("Hello, World.")


hello()
