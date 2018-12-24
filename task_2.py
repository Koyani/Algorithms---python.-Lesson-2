#task_2
#Посчитать четные и нечетные цифры введенного натурального числа. 
#Например, если введено число 34560, то у него 3 четные цифры (4, 6 и 0) и 2 нечетные (3 и 5).
number = int(input("Enter any integer number more than zero: "))
odd_digit_quantity = 0
even_digit_quantity = 0
for digit in str(number):
    if int(digit) % 2 == 0:
        even_digit_quantity = even_digit_quantity + int(digit)//int(digit)
    else:
        odd_digit_quantity = odd_digit_quantity + int(digit)//int(digit)
print(f"There are {even_digit_quantity} even digit(s) in your number")
print(f"There are {odd_digit_quantity} odd digit(s) in your number")