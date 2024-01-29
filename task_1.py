# Написати рекурсивну функцію знаходження ступеня числа.
def exponent_number(number, exponent):
    if exponent == 0:
        return 1
    else:
        return number * exponent_number(number, exponent - 1)


def main():
    print(exponent_number(5, 3))

main()


