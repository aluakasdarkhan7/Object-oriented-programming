import math

arr = [1.0, 2.0, 3.5, 4.0, 6.0, 7.2, 8.0, 9.9, 10.0, 11.1]

# Найдем максимум среди четных (делящихся на 2 без остатка) чисел
even_elements = [x for x in arr if x % 2 == 0]

if even_elements:
    max_even = max(even_elements)
    print("Максимум среди чётных элементов:", max_even)
else:
    print("Чётных элементов нет.")
