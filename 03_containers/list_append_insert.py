def list_append():
    """不断往尾部追加"""
    ls = []
    for i in range(5000):
        ls.append(i)


def list_insert():
    """不断往头部插入"""
    ls = []
    for i in range(5000):
        ls.insert(0, i)


import timeit

# 默认执行 100 万次
append_spent = timeit.timeit(
    setup="from __main__ import list_append",
    stmt="list_append()",
    number=1000,
)
print("list_append:", append_spent)

insert_spent = timeit.timeit(
    setup="from __main__ import list_insert",
    stmt="list_insert()",
    number=1000,
)
print("list_insert", insert_spent)
