# Функция принимает на вход последовательность, которая поддерживает порядок
# элементов, возвращает функция объект итератор с обратным порядком элементов.
my_list = [4, 8, 2, 9, 1, 7, 2]
res = reversed(my_list)
print(type(res), res)
rev_list = list(reversed(my_list))
print(rev_list)

# Получается, что результат работы функции напрямую не использовать? Если нам
# нужен новый развёрнутый список, объект итератор стоит обернуть в функцию list. В
# таком случае мы получим новый развёрнутый список.
# 🔥 Важно! Подобный приём затратен по времени и по памяти.
# Обычно функция reversed используется в сочетании с циклом for in. Такой приём
# позволяет работать с элементами списка внутри цикла в обратном порядке.
for item in reversed(my_list):
    print(item)