text = 'Hello world!'
print(text[6])
print(text[3:7])
# Индексы и срезы работают аналогично спискам.
# Если необходимо заменить элемент новым, индексы не подойдут. Для этих целей
# нужен метод replace
new_txt = text.replace('l', 'L', 2)
print(text, new_txt, sep='\n')
# Первый аргумент — подстрока, которую нужно заменить.
# Второй аргумент — подстрока, на которую нужно заменить.
# Третий аргумент — максимальное количество замен. Если его не указывать, будут
# заменены все совпадения.

# Как и у списка, строка поддерживает методы count для подсчёта вхождения и index
# для поиска элемента. Но у строки появился и новый метод find. Он работает
# аналогично index. Но если искомая подстрока отсутствует, вместо ошибки
# возвращает -1.
text = 'Hello world!'
print(text.count('l'))
print(text.index('l'))
print(text.find('l'))
print(text.find('z'))

# Реверс строк
# Для разворота строки используется обратный срез, как и в случае со списком.
text = 'Hello world!'
print(text[::-1])
