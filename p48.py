answer = 0

for i in range(1, 1001):
    answer += i**i
print(str(answer)[-10:])