"""
Дан список состоящий из данных разного типа.
Вернуть новый список, где при помощи функции map() каждый элемент типа int
первоначального списка приведён к типу str, элементы всех остальных типов передаются в новый список
без изменения их типа.
В качестве входной функции в map() использовать lambda-функцию.
"""

lst = [1, 3.66, 246, 'cccc', (1, 2, 3), 67, 3, 'dddd', [2, 5, 8]]
new_list = list(map(lambda x: str(x) if type(x) is int else x, lst))

print(new_list)
print(new_list[2], type(new_list[2]))
print(new_list[-1], type(new_list[-1]))
print(new_list[1], type(new_list[1]))
