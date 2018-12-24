#task_6
#В программе генерируется случайное целое число от 0 до 100. 
#Пользователь должен его отгадать не более чем за 10 попыток. 
#После каждой неудачной попытки должно сообщаться больше или меньше введенное пользователем число, чем то, что загадано. 
#Если за 10 попыток число не отгадано, то вывести загаданное число.
from random import *
n = randint(0, 100)
i = 1
print("You have 10 tries to guess the number")
while i <= 10:
    attempt = int(input(f"Try {i}: "))
    i += 1
    if attempt < n:
        print("Too little, increase the input number")
    elif attempt > n:
        print("Too much, decrease the number")
    else:
        print("You guessed the right number")
        break
else:
    print(f"You entered a wrong number 10 times. The right number is {n}.")