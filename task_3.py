#task_3
#Сформировать из введенного числа обратное по порядку входящих в него цифр и вывести на экран. 
#Например, если введено число 3486, то надо вывести число 6843.
#number = int(input("Enter any integer number: ")

number = int(input("Please, enter a number more than 0: "))
palindrome = 0
while number > 0:
    palindrome = palindrome*10 + number%10 
    number = number // 10
print(palindrome)
