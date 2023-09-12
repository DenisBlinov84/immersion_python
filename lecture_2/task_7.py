import decimal

print(0.1 + 0.2)

pi = decimal.Decimal('3.141_592_653_589_793_238_462_643_383_279_502_884_197_169_399_375')  # выведет все числа
print(pi)

num = decimal.Decimal(1) / decimal.Decimal(3)  # можно выполнять точные вычисления
print(num)

decimal.getcontext().prec = 120  # с точностью 120 символов
science = 2 * pi * decimal.Decimal(23.452346) ** 2
print(science)
