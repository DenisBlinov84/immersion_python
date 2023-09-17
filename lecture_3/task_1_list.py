# способы создания списка
list_1 = list()
list_2 = list((3.14, True, "Hello world!"))
list_3 = []
list_4 = [3.14, True, "Hello world!"]

# Кроме того список можно создать из другой последовательности. Достаточно передать её функции list.
new_list = list(list_4)

# доступ к элементам списка
my_list = [2, 4, 6, 8, 10, 12]
print(my_list[0])
# print(my_list[6]) # IndexError: list index out of range

my_list = [2, 4, 6, 8, 10, 12]
print(my_list[-1])  # Самый правый элемент списка, т.е. последний элемент, имеет индекс - 1, предпоследний - -2
# print(my_list[-10]) # IndexError: list index out of range
