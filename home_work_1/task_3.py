# Программа загадывает число от 0 до 1000. Необходимо угадать число за 10 попыток.
# Программа должна подсказывать “больше” или “меньше” после каждой попытки.
# Для генерации случайного числа используйте код:
# from random import randint num = randint(LOWER_LIMIT, UPPER_LIMIT)

from random import randint

num = randint(0, 1000)
search_num = -1
count = 10
while search_num != num:
    search_num = int(input("Угадайте число: "))
    print([["Загаданное число меньше", "Загаданное число больше"][search_num < num], "Угадали!"][search_num == num])
    count -= 1
    if count == 0:
        print("Попытки закончились")
        break
