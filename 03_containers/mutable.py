# -*- coding: utf-8 -*-


def add_str(in_func_obj):
    print(f'In add [before]: in_func_obj="{in_func_obj}"')
    in_func_obj += " suffix"
    print(f'In add [after]: in_func_obj="{in_func_obj}"')


# 不可变类型     函数外函数内 id(var) 不一样
orig_obj = "foo"
print(f'Outside [before]: orig_obj="{orig_obj}"')
add_str(orig_obj)
print(f'Outside [after]: orig_obj="{orig_obj}"')


def add_list(in_func_obj):
    print(f'In add [before]: in_func_obj="{in_func_obj}"')
    in_func_obj += ["baz"]
    print(f'In add [after]: in_func_obj="{in_func_obj}"')


# 可变类型      函数外函数内 id(ls) 一样
orig_obj = ["foo", "bar"]
print(f'Outside [before]: orig_obj="{orig_obj}"')
add_list(orig_obj)
print(f'Outside [after]: orig_obj="{orig_obj}"')
