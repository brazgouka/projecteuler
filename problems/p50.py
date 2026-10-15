import math


def cons_prime_sum(num) -> int:
    primes = []
    nums = [True] * num
    max_prime = 0
    for n in range(2, num):
        if not nums[n]:
            continue
        primes.append(n)
        if not max_prime and n * 2 >= num:
            max_prime = n
        non_prime_idx = n * 2
        while non_prime_idx < num:
            nums[non_prime_idx] = False
            non_prime_idx += n
    cons_primes = []
    max_cons_sum = 0
    max_cons_len = 0
    for idx in range(round(math.sqrt(len(primes)))):
        for jdx in range(idx, len(primes)):
            if primes[jdx] > max_prime:
                break
            if primes[jdx] in cons_primes:
                continue
            cons_primes.append(primes[jdx])
            if sum(cons_primes) > num:
                cons_primes.pop(0)
                cons_primes.pop()
                cons_primes.pop()
                break
            if sum(cons_primes) in primes and len(cons_primes) >= max_cons_len:
                max_cons_len = len(cons_primes)
                max_cons_sum = sum(cons_primes)

    return max_cons_sum

print(cons_prime_sum(1_000_000))