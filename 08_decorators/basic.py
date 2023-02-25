import random
import time

# 装饰器无参数
# def timer(func):
#     def decorated(*args, **kwargs):
#         st = time.perf_counter()
#         ret = func(*args, **kwargs)
#         print("time cost: {} seconds".format(time.perf_counter() - st))
#         return ret
#
#     return decorated
#
# @timer
# def random_sleep():
#     time.sleep(random.random())


# 装饰器有参数
def timer(print_args=False):
    """装饰器：打印函数耗时

    :param print_args: 是否打印被方法名和参数，默认为 False
    """

    def decorator(func):
        def wrapper(*args, **kwargs):
            st = time.perf_counter()
            ret = func(*args, **kwargs)
            if print_args:
                print(f'"{func.__name__}", args: {args}, kwargs: {kwargs}')
            print("time cost: {} seconds".format(time.perf_counter() - st))
            return ret

        return wrapper

    return decorator


@timer(print_args=True)
def random_sleep():
    time.sleep(random.random())


if __name__ == '__main__':
    random_sleep()
