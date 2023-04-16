def filter_strings(input_array, max_length):
    """
    Функция фильтрует массив строк, оставляя только строки, длина которых меньше либо равна заданному максимальному значению.
    """
    result_array = []
    for string in input_array:
        if len(string) <= max_length:
            result_array.append(string)
    return result_array

# Вводим исходный массив строк с клавиатуры
input_array = input("Введите строки через пробел: ").split()

# Задаем максимальную длину строки
max_length = 3

# Формируем новый массив строк, длина которых меньше либо равна 3 символам
result_array = filter_strings(input_array, max_length)

# Выводим результат
print("Результат:")
for string in result_array:
    print(string)
