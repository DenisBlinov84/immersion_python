# Напишите функцию принимающую на вход только ключевые параметры и возвращающую словарь, где ключ — значение
# переданного аргумента, а значение — имя аргумента. Если ключ не хешируем, используйте его строковое представление.

import typing


def invert_kwargs_dict(**kwargs):
    return {(i[1] if isinstance(i[1], typing.Hashable) else " ".join(map(str, i[1]))): i[0] for i in kwargs.items()}


print(invert_kwargs_dict(first=40, second="thirty", third=["20", "and", 10]))

