max_pair = ()
max_pair_v = 0


def is_prime(value):
    if value <= 1:
        return False
    for i in range(2, int(value**0.5) + 1):
        if value % i == 0:
            return False
    return True


for a in range(-999, 1000):
    for b in range(2, 1001):
        if not is_prime(b):
            continue
        n = 1
        while is_prime(n ** 2 + a * n + b):
            n += 1
        if n > max_pair_v:
            max_pair = (a, b)
            max_pair_v = n

print(max_pair[0] * max_pair[1])
