import random

list = [random.randint(0, 10) for i in range(10)]
list2 = [i ** 2 for i in list]
print('list = ', list)
print('list 2 = ', list2)

fruit_list = ['абрикос', 'апельсин', 'лимон', 'манго', 'яблоко']
fruit_list2 = ['физалис', 'манго', 'лимон', 'банан', 'абрикос']
fruit_list3 = (set(fruit_list) & set(fruit_list2))

print(fruit_list)
print(fruit_list2)
print(fruit_list3)

array = [random.randint(-10, 10) for i in range(10)]
array1 = [i for i in array if i % 3 == 0]
array2 = [i for i in array if i >= 0]
array3 = [i for i in array if i % 4 != 0]
print('Список = ', array)
print('Кратные 3 = ', array1)
print('Положительные = ', array2)
print('Не кратен 4 = ', array3)