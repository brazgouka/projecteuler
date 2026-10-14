import math

final = 0

UPPER_LIMIT = 9

while math.factorial(9) * len(str(UPPER_LIMIT)) > int("9" * len(str(UPPER_LIMIT))):
    UPPER_LIMIT = UPPER_LIMIT * 10 + 9

for n in range(3, math.factorial(9) * len(str(UPPER_LIMIT))):
    answer = 0
    for m in str(n):
        answer += math.factorial(int(m))
        if answer > n:
            break
    if answer == n:
        final += answer

print(final)

