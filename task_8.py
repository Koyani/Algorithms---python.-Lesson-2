#task_8
#Посчитать, сколько раз встречается определенная цифра в введенной последовательности чисел.
#Количество вводимых чисел и цифра, которую необходимо посчитать, задаются вводом с клавиатуры.

digit = int(input("Enter a digit to check: "))
number = int(input("Enter the number of digits: "))
x = 0
for i in range(1, number + 1):
    d = int(input("Enter a digit: "))
    if d == digit:
        x+=1
    else:
        x==x    
print(f"Digit {digit} was entered {x} times.")