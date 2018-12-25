#task_7
#Напишите программу, доказывающую или проверяющую, 
#что для множества натуральных чисел выполняется равенство: 1+2+...+n = n(n+1)/2, где n - любое натуральное число.
number = int(input("Enter any natural number: "))
x = 0
y = number * (number + 1) // 2
for i in range(1, number + 1):
    x += i
if x==y:
    print("1+2+...+n = n(n+1)/2")
else:
    print("1+2+...+n != n(n+1)/2")
    
