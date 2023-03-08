.PHONY: clean
clean:
	find . -name .mypy_cache -or -name .vscode -or -name __pycache__ -or -name .DS_Store | xargs rm -rf


大纲


07_function

别将可变类型作为参数默认值
仅限关键字参数

函数返回
1. 尽量只返回一种类型
2. 谨慎返回None
3. 早返回，多返回

常用函数模块：functools  re
  functools.partial()  functools.lru_cache()   functools.wraps()  functools.reduce()
  re.search()  re.match()  re.sub()

函数与状态
1.全局变量  2. 闭包  3. 类

别写大复杂的函数
1. 长度：65～200行
2.圈复杂度 <= 10  radon cc xx.py -s
3. 一个函数只包含一层抽象
