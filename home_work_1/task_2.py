# Напишите код, который запрашивает число и сообщает является ли оно простым или составным.
# Используйте правило для проверки: “Число является простым, если делится нацело только на единицу и на себя”.
# Сделайте ограничение на ввод отрицательных чисел и чисел больше 100 тысяч.


while True:
    try:
        input_data = int(input('Введите число от 0 до 100000: '))
        if 0 < input_data < 100000:
            print('OK')
            break
        else:
            raise ValueError
    except ValueError:
        print('Вы ввели не число или число не входит в указанный диапазон. Попробуйте снова: ')

k = 0
for i in range(2, input_data // 2 + 1):
    if input_data % i == 0:
        k = k + 1
if k <= 0:
    print("Число простое")
else:
    print("Число не является простым")
