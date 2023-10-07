# 2. Напишите функцию, которая принимает на вход строку - абсолютный путь до файла.
# Функция возвращает кортеж из трёх элементов: путь, имя файла, расширение файла.
import os.path


def get_path_element(file_path: str) -> tuple:
    """
    Функция принимает на вход абсулютный путь к файлу и возвращает кортеж из трёх элементов:
    путь, имя файла, расширение файла.
    :param file_path: Абсолютный путь к файлу
    :return: кортеж из трёх элементов: путь, имя файла, расширение файла
    """

    return (os.path.join(*file_path.split('\\')[:-1]), file_path.split('\\')[-1].split('.')[0],
            file_path.split('\\')[-1].split('.')[1])


file_path = 'C:\\Program Files (x86)\\JetBrains\\IntelliJ IDEA Community Edition 2016.2.3\\bin\\idea64.exe'
print(get_path_element(file_path))
print(type(get_path_element(file_path)))
