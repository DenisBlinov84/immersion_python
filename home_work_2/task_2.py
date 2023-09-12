# Напишите программу, которая принимает две строки вида “a / b” - дробь с числителем и знаменателем.
# Программа должна возвращать сумму и произведение дробей.
# Для проверки своего кода используйте модуль fractions.

def process_fractions(frac1_str, frac2_str):
    # Преобразуем дроби из строк в числа
    num1, denom1 = map(int, frac1_str.split("/"))
    num2, denom2 = map(int, frac2_str.split("/"))

    # Вычисляем сумму дробей
    sum_frac_num = num1 * denom2 + num2 * denom1
    sum_frac_denom = denom1 * denom2
    sum_frac = (sum_frac_num, sum_frac_denom)

    # Вычисляем произведение дробей
    prod_frac_num = num1 * num2
    prod_frac_denom = denom1 * denom2
    prod_frac = (prod_frac_num, prod_frac_denom)

    return sum_frac, prod_frac


# Пример использования функции
frac1_str = "1/3"
frac2_str = "3/5"

sum_frac, prod_frac = process_fractions(frac1_str, frac2_str)

print(f"Сумма дробей {frac1_str} и {frac2_str} -> {sum_frac[0]}/{sum_frac[1]}")
print(f"Произведение дробей {frac1_str} и {frac2_str} -> {prod_frac[0]}/{prod_frac[1]}")
print()
# ----------------------------------------------------------------------------------------------
import fractions

f1 = fractions.Fraction(1, 3)
f2 = fractions.Fraction(3, 5)
print(f"Сумма дробей {f1} и {f2} -> {f1 + f2}")
print(f"Произведение дробей {f1} и {f2} -> {f1 * f2}")

