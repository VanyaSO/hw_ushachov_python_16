# Написати рекурсивну функцію, яка обчислює суму всіх чисел у діапазоні від а до b.
# Користувач вводить а і b. Проілюструйте роботу функції
def range_sum(a, b):
    if a > b:
        return 0
    else:
        return a + range_sum(a + 1, b)
    
    
    
def main():
    start = int(input("Enter starting range: "))
    end = int(input("Enter ending range: "))
    
    if start > end:
        start, end = end, start
        
    print(range_sum(start, end))

main()