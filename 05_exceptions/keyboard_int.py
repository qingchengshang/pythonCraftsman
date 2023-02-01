import time

# while True:
#     s = input('Input a string: ')
#     print(s)


def input_a_number():
    """要求用户输入一个 0-100 的数字，，如果无效则重新输入"""

    while True:
        number = input("Please input a number (0-100): ")

        # 下面三条 if 语句都是对输入值的校验代码
        if not number:
            print("Input can not be empty!")
            continue
        if not number.isdigit():
            print("Your input is not a valid number!")
            continue
        if not (0 <= int(number) <= 100):
            print("Please input a number between 0 and 100!")
            continue

        number = int(number)
        break

    print(f"Your number is {number}")


# input_a_number()


# ------ 不要手动校验数据，使用专业的数据校验模块 ------

from pydantic import BaseModel, ValidationError, conint


class NumberInput(BaseModel):
    # 使用类型注解 conint 定义 number 属性的取值范围
    number: conint(ge=0, le=100)


def input_a_number_with_pydantic():
    while True:
        number = input("Please input a number (0-100): ")

        # 实例化 pydantic 模型，捕获校验错误异常
        try:
            number_input = NumberInput(number=number)
        except ValidationError as e:
            print(e)
            continue

        number = int(number)
        break

    print(f"Your number is {number}")


input_a_number_with_pydantic()
