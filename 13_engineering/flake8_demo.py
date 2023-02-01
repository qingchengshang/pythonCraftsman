# -*- coding: utf-8 -*-
class Duck:
    """鸭子类

    :param color: 鸭子颜色
    """

    def __init__(self, color):
        self.color = color


# https://www.cnblogs.com/wulixia/p/13349694.html
# 1、检查整个项目的代码：flake8 pythonCraftsman
# 2、检查package的代码：flake8 .\13_engineering
# 3、检查module的代码： flake8 .\13_engineering\flake8_demo.py

# pre-commit 在 python 项目中的使用
# https://www.jianshu.com/p/eba337fe0828
