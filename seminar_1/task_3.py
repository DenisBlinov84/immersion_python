# Пользователь вводит число от 1 до 999. Используя операции с числами сообщите введено:
# цифра, двузначное число или трёхзначное.
# Для цифры верните её квадрат.
# Для двузначного числа произведение цифр.
# Для трёхзначного числа его зеркальное отображение

a = int(input('Введите число от 1 до 999: '))
while not 0 < a < 1000:
    a = int(input('Введите число от 1 до 999: '))
if a < 10:
    print(f'Введено число. Его квадрат: {(a * a)}')
elif a >= 10 and a < 100:
    print(f'Введено двузначное число. Произведение цифр равно: {(a % 10) * (a // 10)}')
elif a >= 100:
    print(f'Введено трёхзначное число. Его зеркальное отображение: {int(str(a)[::-1])}')
