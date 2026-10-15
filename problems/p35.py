def is_prime(value):
    if value <= 1:
        return False
    for i in range(2, int(value**0.5) + 1):
        if value % i == 0:
            return False
    return True

circ_primes = []

for n in range(2, 1_000_000):
    if n in circ_primes:
        continue
    orig = str(n)[1:] + str(n)[0]
    if is_prime(n):
        while is_prime(int(orig)) and int(orig) != n:
            orig = str(orig)[1:] + str(orig)[0]
        if int(orig) == n:
            circ_primes.append(n)

print(len(circ_primes))

