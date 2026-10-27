import math

def is_prime(num):
    for i in range(2, math.isqrt(num) + 1):
        if num % i == 0:
            return False
    return True

num = 9
while True:
    if not is_prime(num):
        valid = False
        if not any(is_prime(num - 2 * sq * sq) for sq in range(1, math.isqrt(num // 2) + 1)):
            print(num)
            break
    num += 2
