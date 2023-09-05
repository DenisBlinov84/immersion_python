# Посчитайте сумму чётных элементов от 1 до n, исключая кратные e.

n = 100
e = 3
i = 1
res = 0
while i <= n:
    if i % e == 0:
        i += 1
        continue
    elif i % 2 == 0:
        res = res + i
        print(i)
    i += 1
print(res)
