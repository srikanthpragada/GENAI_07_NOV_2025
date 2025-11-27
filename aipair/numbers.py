def isprime(num):
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True


def isperfect(num):
    if num < 1:
        return False
    divisors_sum = 1 if num > 1 else 0
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            divisors_sum += i
            if i != num // i and num // i != num:
                divisors_sum += num // i
    return divisors_sum == num


def factorial(num):
    if num < 0:
        raise ValueError("Factorial is not defined for negative numbers")
    result = 1
    for i in range(2, num + 1):
        result *= i
    return result
