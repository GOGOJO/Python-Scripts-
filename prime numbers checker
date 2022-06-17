def is_prime(n):
    if n > 1:
        for i in range(2, n):
            if n % i == 0:
                return False
    return True


def prime_finder(n):
    prime_numbers = []
    for i in range(2, n+1):
        if is_prime(i):
            prime_numbers.append(i)
    return prime_numbers


print(prime_finder(11))
