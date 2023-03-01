# -*- coding: utf-8 -*-
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __setattr__(self, key, value):
        # 不允许设置年龄小于 0
        if key == "age" and value < 0:
            raise ValueError(f"Invalid age value: {value}")
        super().__setattr__(key, value)

    def say(self):
        print(f"Hi, My name is {self.name}, I'm {self.age}")


class Fun:
    # __init__() 每个属性赋值，都会先调用一次 __setattr__()
    def __init__(self):
        self.name = "Liu"
        self.age = 12
        self.male = True
        print(self.__dict__)

    def __setattr__(self, key, value):
        print("*" * 50)
        print("setting:{},  with:{}".format(key, value))
        print("current __dict__ : {}".format(self.__dict__))
        # 属性注册
        self.__dict__[key] = value


fun = Fun()
