# -*- coding: utf-8 -*-
import random

movies = [
    {"name": "The Dark Knight", "year": 2008, "rating": "9"},
    {"name": "Kaili Blues", "year": 2015, "rating": "7.3"},
    {"name": "Citizen Kane", "year": 1941, "rating": "8.3"},
    {"name": "Project Gutenberg", "year": 2018, "rating": "6.9"},
    {"name": "Burning", "year": 2018, "rating": "7.5"},
    {"name": "The Shawshank Redemption ", "year": 1994, "rating": "9.3"},
]


class Movie:
    """电影对象数据类"""

    def __init__(self, name, year, rating):
        self.name = name
        self.year = year
        self.rating = rating

    @property
    def rank(self):
        """按照评分对电影分级：

        - S: 8.5 分及以上
        - A：8 - 8.5 分
        - B：7 - 8 分
        - C：6 - 7 分
        - D：6 分以下
        """
        rating_num = float(self.rating)
        if rating_num >= 8.5:
            return "S"
        elif rating_num >= 8:
            return "A"
        elif rating_num >= 7:
            return "B"
        elif rating_num >= 6:
            return "C"
        else:
            return "D"


def get_sorted_movies(movies, sorting_type):
    """对电影列表进行排序并返回

    :param movies: Movie 对象列表
    :param sorting_type: 排序选项，可选值
        name（名称）、rating（评分）、year（年份）、random（随机乱序）
    """
    if sorting_type == "name":
        sorted_movies = sorted(movies, key=lambda movie: movie.name.lower())
    elif sorting_type == "rating":
        sorted_movies = sorted(movies, key=lambda movie: float(movie.rating), reverse=True)
    elif sorting_type == "year":
        sorted_movies = sorted(movies, key=lambda movie: movie.year, reverse=True)
    elif sorting_type == "random":
        sorted_movies = sorted(movies, key=lambda movie: random.random())
    else:
        raise RuntimeError(f"Unknown sorting type: {sorting_type}")
    return sorted_movies


all_sorting_types = ("name", "rating", "year", "random")


def main():
    # 接收用户输入的排序选项
    sorting_type = input("Please input sorting type: ")
    if sorting_type not in all_sorting_types:
        print(
            'Sorry, "{}" is not a valid sorting type, please choose from "{}", exit now'.format(
                sorting_type, "/".join(all_sorting_types)
            )
        )
        return

    # 初始化电影数据对象
    movie_items = []
    for movie_json in movies:
        movie = Movie(**movie_json)  # func(**d) 以关键字参数 key=value 的形式解包
        # print(movie.__dict__)
        movie_items.append(movie)

    # 排序并输出电影列表
    sorted_movies = get_sorted_movies(movie_items, sorting_type)
    for movie in sorted_movies:
        print(f"- [{movie.rank}] {movie.name}({movie.year}) | rating: {movie.rating}")


if __name__ == "__main__":
    main()


# ------ 动态解包 ------
def func(a, b, c):
    print(a, b, c)


if __name__ == "__main__":
    func(1, 2, 3)
    func(*[1, 2, 3])
    func(*"abc")

    a, b, c = {"a": 1, "b": 2, "c": 3}
    print(a)
    a, b, c = {"a": 1, "b": 2, "c": 3}.items()
    print(a)

    func(*{"a": 1, "b": 2, "c": 3})
    func(**{"a": 1, "b": 2, "c": 3})
    # 一个星号 * 和两个星号 ** 解包，结果完全不一样？
    # 答案是 ** 符号作用的对象是字典对象，它会自动解包成关键字参数 key=value 的格式
    # 如果字典对象中的 key 不是 a，b，c，会出现 TypeError: func() got an unexpected keyword argument
    # 总结:
    # 一个星号可作用于所有的可迭代对象，称为迭代器解包操作，作为 位置参数 传递给函数，
    #  两个星号只能作用于字典对象，称之为字典解包操作，作为 关键字参数 传递给函数。
    #  使用 * 和 ** 的解包的好处是能节省代码量，使得代码看起来更优雅
