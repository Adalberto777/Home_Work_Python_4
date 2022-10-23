# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.
# Написать функцию, которая принимает аргумент - целое число и возвращает список его простых множителей.
# Пример:
# simple_number(147420) => [2, 3, 5, 7, 13];
# simple_number(374220) => [2, 3, 5, 7, 11];
# from random import randint
import math

def prime_num_all(n):
    primes = [2]
    for num in range(3, n + 1, 2):
        if all(num % i != 0 for i in range(2, int(math.sqrt(num)) + 1)):
            primes.append(num)
    return primes

def get_prime_num_n(n, primes):
    fact = []
    for i in primes:
        if n % i == 0:
            n = n / i
            fact.append(i)
    return fact

n = int(input('Введите число: '))

primes = prime_num_all(n)

factors = get_prime_num_n(n, primes)
print(factors)