#task_1
#Написать программу, которая будет складывать, вычитать, умножать или делить два числа. 
#Числа и знак операции вводятся пользователем. 
#После выполнения вычисления программа не должна завершаться, а должна запрашивать новые данные для вычислений. 
#Завершение программы должно выполняться при вводе символа '0' в качестве знака операции. 
#Если пользователь вводит неверный знак (не '0', '+', '-', '*', '/'), 
#то программа должна сообщать ему об ошибке и снова запрашивать знак операции. 
#Также сообщать пользователю о невозможности деления на ноль, если он ввел 0 в качестве делителя.
    
while True:
        number1 = float(input("Enter first number: "))
        number2 = float(input("Enter second number: "))
        operation = input("Enter operation between numbers from \"-\", \"+\", \"/\", \"*\", to quit enter \"0\": ")
        if operation == "+":
            print(f"The sum between two numbers is {number1+number2}")
        elif operation == "-":
            print(f"The sum between two numbers is {number1-number2}")
        elif operation == "*":
            print(f"The result of multiplication between two numbers is {number1*number2}")
        elif operation == '/':
            if number2 != 0:
                print(f"The result of division is {number1/number2}")
            else:
                print("Divizion by zero is not permitted")
        elif operation == '0': 
            break
        else:          
            print("No such operation")
