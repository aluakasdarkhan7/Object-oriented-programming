# 1. Обратный порядок списка
my_list = [10, 20, 30, 40, 50]
print("Обратный список:", my_list[::-1])

# 2. Сортировка по убыванию абсолютных значений
def list_sort(lst):
    return sorted(lst, key=abs, reverse=True)

numbers = [-10, 5, -3, 20, 0]
print("Сортировка по убыванию абсолютных значений:", list_sort(numbers))

# 3. Замена первого и последнего элемента
def change(lst):
    if len(lst) >= 2:
        lst[0], lst[-1] = lst[-1], lst[0]
    return lst

sample_list = [1, 2, 3, 4, 5]
print("Список после замены:", change(sample_list))