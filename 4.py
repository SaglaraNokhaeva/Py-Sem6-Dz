# Задайте список из вещественных чисел. Напишите программу, которая найдёт 
# разницу между максимальным и минимальным значением дробной части элементов.
# Пример:
# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19
razmer=int(input("Введите размерность списка: "))
from random import randint
numbers = []
for i in range(razmer):
    numbers.append(randint(0, 10000)/100)
print(numbers)
new_numbers=[round((i-int(i)),3)for i in numbers]
print(new_numbers)
max_el=new_numbers[0]
min_el=new_numbers[0]
for i in range(razmer):
    if new_numbers[i]>max_el:
        max_el=new_numbers[i]
    if new_numbers[i]<min_el:
        min_el=new_numbers[i]
print(max_el)
print(min_el)
print(max_el-min_el)