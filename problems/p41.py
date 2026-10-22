import math

LIMIT = 9_999_999
primes = []

for num in range(2, round(math.sqrt(LIMIT))):
    skip = False
    for p in primes:
        if math.sqrt(num) < p:
            break
        if num % p == 0:
            skip = True
            break
    if skip:
        continue
    primes.append(num)

for num in range(LIMIT, 0, -1):
    snum = str(num)
    if ''.join(sorted(snum)) != '1234567'[:len(snum)]:
        continue
    skip = False
    for prime in primes:
        if num % prime == 0:
            skip = True
            break
    if skip:
        continue
    print(num)
    break

