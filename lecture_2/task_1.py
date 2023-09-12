# a = 5
# print(type(a), id(a))
# a = 'Hello world'
# print(type(a), id(a))
# a = 42.0 * 3.141592 / 2.71828
# print(type(a), id(a))
# # ------------------------------------------
# data = 42
# print(isinstance(data, int))
#
# data = True
# print(isinstance(data, int))
#
# data = 3.14
# print(isinstance(data, (int, float, complex)))
# # ------------------------------------------
# num = 2 + 2 * 2
# digit = 36 / 6
# print(num, digit)
# print(num == digit)
# print(num is digit)
# # ------------------------------------------
# txt = 'Hello world'
# print(txt, id(txt))
# txt = txt.replace(' ', '_')
# print(txt, id(txt))
# # ------------------------------------------
# a = c = 2
# b = 3
# print(a, id(a), b, id(b), c, id(c))
# a = b + a
# print(a, id(a), b, id(b), c, id(c))
# # ------------------------------------------
# x = 42
# y = 'text'
# z = 3.1415
# print(hash(x), hash(y), hash(z))
# my_list = [x, y, z]
# # print(hash(my_list)) # получим ошибку, так как list изменяемый
# # ------------------------------------------
# # txt_1 = input()
# print(type(txt), id(txt), hash(txt))
# # ------------------------------------------
# a: int | float = 42
# # b: float = float(input('Введи число: '))
# a = a / b
# # ------------------------------------------
# # атрибуты:
# print("Hello world!".__doc__)
# print(str.__doc__)
# # ------------------------------------------
# # методы:
# print("Hello world!".upper())  # Переводит строку в верхний регистр
# print("Hello world!".count('l'))  # Колличество вхождений
# # ------------------------------------------
# print(dir("Hello world!"))  # Возвращает список атрибутов, которые можно применить
# # ------------------------------------------
# help(str)
#
