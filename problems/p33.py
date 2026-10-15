import math

answer_x = 1
answer_y = 1

for x in range(10, 100):
    for y in range(x + 1, 100):
        if int(str(y)[1]) != 0 and str(x)[1] == str(y)[0] and x/y == int(str(x)[0]) / int(str(y)[1]):
            print(x, y)
            answer_x *= x
            answer_y *= y

gcd = math.gcd(answer_x, answer_y)
simplified_denom = answer_y // gcd

print(simplified_denom)