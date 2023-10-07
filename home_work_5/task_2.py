# Напишите однострочный генератор словаря, который принимает на вход три списка одинаковой длины:
# имена str, ставка int, премия str с указанием процентов вида “10.25%”.
# В результате получаем словарь с именем в качестве ключа и суммой премии в качестве значения.
# Сумма рассчитывается как ставка умноженная на процент премии

def generate_bonus(name: list, salary: list, percent: list) -> dict:
    """
    Функция возвращает словарь с именем в качестве ключа и суммой премии в качестве значения
    :param name: список имен (str)
    :param salary: список ставок (int)
    :param percent: список процентов премий (str)
    :return: словарь с именем в качестве ключа и суммой премии в качестве значения
    """
    # return {name[i]: (salary[i]*float(percent[i][:-1]) / 100).__round__(2) for i in range(len(name))
    #         if len(name) == len(salary) == len(percent)}

    return {n: (s * float(p[:-1]) / 100).__round__(2) for n, s, p in zip(name, salary, percent)
            if len(name) == len(salary) == len(percent)}


names = ['Alex', 'Den', 'Mike']
salaries = [789, 376, 987]
percents = ['10.25%', '15.50%', '8.75%']

print(generate_bonus(names, salaries, percents))
