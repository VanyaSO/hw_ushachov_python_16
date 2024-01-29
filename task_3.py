# Написати рекурсивну функцію, яка виводить N зірок у ряд. Число N задає користу-вач. Проілюструйте роботу функції прикладом.
def print_symbol(number):
    if number == 1:
        return "*"
    else:
        return "*" + print_symbol(number-1)
    
    
def main():
    number = int(input("Enter number: "))

    print(print_symbol(number))

main()