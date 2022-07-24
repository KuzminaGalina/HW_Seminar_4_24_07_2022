# 3- Задайте натуральное число N. 
# Напишите программу, которая составит список простых множителей числа N.
# Пример: при N = 12 -> [2, 3]


def list_of_prime_factors(N):
    spisok = []
    div = 2
    while N > 1:
        if N % div == 0:
            spisok.append(div)
            N //= div
        else:
            div += 1
    return spisok

print(list_of_prime_factors(99))