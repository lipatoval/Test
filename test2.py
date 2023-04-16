def filter_strings(input_array, max_length):
    """
    Функция фильтрует массив строк, оставляя только строки, длина которых меньше либо равна заданному максимальному значению.
    """
    result_array = []
    for string in input_array:
        if len(string) <= max_length:
            result_array.append(string)
    return result_array

