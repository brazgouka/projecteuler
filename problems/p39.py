import math

answer = 0
answer_max = 0

for p in range(3, 1001):
    num_for_p = 0
    for b in range(1, math.ceil(p / 2)):
        a = p * (p -2 * b) / (2 * (p - b))
        if a == int(a):
            num_for_p += 1
            print(a, b, p - a - b)
    if num_for_p > answer_max:
        answer_max = num_for_p
        answer = p

print(answer)