# Дан список повторяющихся элементов. Вернуть список с дублирующимися элементами.
# В результирующем списке не должно быть дубликатов.

initial_list = [0, 0, 1, 2, 2, 3, 3, 3, 6, 7, 1, 1, 15, 15, 15, 17]
print(f'Исходный список: {initial_list}')
print(f'Повторяющиеся элементы: {[el for el in set(initial_list) if initial_list.count(el) > 1]}')