# -*- coding: utf-8 -*-


# MRO: Method Resolution Order, 方法解析顺序. 解决：多重继承时，子类应该继承哪一个父类的方法
class A:
    def say(self):
        print("I'm A")


class B(A):
    pass


class C(A):
    def say(self):
        print("I'm C")


class D(B, C):
    pass


if __name__ == '__main__':
    d = D()
    d.say()
    print(D.__mro__)
