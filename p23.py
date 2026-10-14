import math

UPPER_LIMIT = 28123
answer = int(UPPER_LIMIT * (1 + UPPER_LIMIT) / 2)
nums = set()
abund = []
for i in range(1, UPPER_LIMIT):
    ab_sum = 1
    is_ab = False
    for j in range(2, round(math.sqrt(i)) + 1):
        if i % j == 0:
            ab_sum += j
            if j != i / j:
                ab_sum += i / j
        if ab_sum > i:
            is_ab = True
            break
    if is_ab:
        abund.append(i)
        for a in abund:
            if a + i <= UPPER_LIMIT:
                nums.add(a + i)
print(answer - sum(nums))
