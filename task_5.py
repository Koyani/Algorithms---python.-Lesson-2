#task_5
#Вывести на экран коды и символы таблицы ASCII, начиная с символа под номером 32 и заканчивая 127-м включительно.
#Вывод выполнить в табличной форме: по десять пар "код-символ" в каждой строке.
for number in range(32,128):
    print(f"{number}-{chr(number)}", end='')
    if number%10 == 0:
        print()
 