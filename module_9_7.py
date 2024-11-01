# Модуль 9_7. Декораторы.
# =================================================
'''Функция, которая складывает 3 числа (sum_three)'''
'''Функция декоратор (is_prime), которая распечатывает "Простое",если результат 
        1ой функции будет простым числом и "Составное" в противном случае.'''
'''написать внутреннюю функцию wrapper в is_prime'''
def is_prime(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        a = 0
        for i in range(2, result+1):
            if result % i == 0:
                a += 1
        if a != 0:
            print('Простое число')
        else:
            print('Составное число')
        return result
    return wrapper
@is_prime
def sum_three(a, b, c):
    return a+b+c

result = sum_three(2, 3, 6)
print(result)
