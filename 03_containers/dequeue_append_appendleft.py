from collections import deque


def deque_append():
    """不断往尾部追加"""
    ls = deque()
    for i in range(5000):
        ls.append(i)


def deque_appendleft():
    """不断往头部插入"""
    ls = deque()
    for i in range(5000):
        ls.appendleft(i)


import timeit

# 执行 1 万次
append_spent = timeit.timeit(
    setup="from __main__ import deque_append",
    stmt="deque_append()",
    number=10000,
)
print("deque_append:", append_spent)

appendleft_spent = timeit.timeit(
    setup="from __main__ import deque_appendleft",
    stmt="deque_appendleft()",
    number=10000,
)
print("deque_appendleft:", appendleft_spent)
