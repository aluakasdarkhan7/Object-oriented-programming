import random

# Пример генерации массива A[5][10] со случайными действительными числами
A = [[random.uniform(-10, 10) for _ in range(10)] for _ in range(5)]

# Подсчет положительных и отрицательных чисел
positive_count = sum(1 for row in A for val in row if val > 0)
negative_count = sum(1 for row in A for val in row if val < 0)

print("Положительных чисел:", positive_count)
print("Отрицательных чисел:", negative_count)

if positive_count > negative_count:
    print("Положительных чисел больше.")
elif negative_count > positive_count:
    print("Отрицательных чисел больше.")
else:
    print("Положительных и отрицательных чисел поровну.")
