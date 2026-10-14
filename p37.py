def is_prime(value):
    if value <= 1:
        return False
    for i in range(2, int(value**0.5) + 1):
        if value % i == 0:
            return False
    return True

primes = [2, 3, 5, 7]

answer = []

def add_prime(n):
    for prime in range(1, 10, 2):
        nn = n * 10 + prime
        if is_prime(nn):
            pot = str(nn)
            while pot:
                if not is_prime(int(pot)):
                    break
                else:
                    pot = pot[1:]
            if not pot:
                answer.append(nn)
            add_prime(nn)

for n in primes:
    add_prime(n)

print(sum(answer))

