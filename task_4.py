#task_4
#Найти сумму n элементов следующего ряда чисел: 1 -0.5 0.25 -0.125 ...
#Количество элементов (n) вводится с клавиатуры.
number = int(input("Enter the number of elements in the sequence 1 -0.5 0.25 -0.125 ...: "))
sum = 0
element = 1
for i in range(number):
    sum += element
    element/= -2
print(sum)     
    