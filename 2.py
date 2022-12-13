# Задайте список из нескольких чисел. Напишите программу, которая найдёт 
# сумму элементов списка, стоящих на нечётной позиции.
# Пример:
# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

from random import randint
numbers = []
for i in range(10):
    numbers.append(randint(0, 10))
print(numbers)

summ_odd=0
for i in range(len(numbers)):
    if i%2==1:
        summ_odd+=numbers[i]
print(summ_odd)