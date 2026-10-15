import math

amicable = set()

def calc_proper_divisors(num):
    num_sum = 1
    for n in range(2, round(math.sqrt(num)) + 1):
        if num % n == 0:
            num_sum += n
            if num / n != n:
                num_sum += int(num / n)
    return num_sum

for num in range(2, 10000):
    if num in amicable:
        continue
    pd_sum = calc_proper_divisors(num)
    if calc_proper_divisors(pd_sum) == num and num != pd_sum:
        amicable.add(num)
        amicable.add(pd_sum)

print(amicable)
print(calc_proper_divisors(1184))
print(sum(amicable))