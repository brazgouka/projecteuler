answer = 1

for i in range(3, 1002, 2):
    spiral_sum = (i - 2) ** 2
    for j in range(1, 5):
        answer = answer + spiral_sum + (i - 1) * j

print(answer)