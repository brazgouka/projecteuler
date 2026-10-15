import math

answer = 0

for num in range(1, 1_000_000, 2):
    num_s = str(num)
    idx = 0
    while idx < len(num_s) / 2 and num_s[idx] == num_s[-idx - 1]:
        idx += 1
    if idx == math.ceil(len(num_s)/2) and str(bin(num))[2:] == str(bin(num))[::-1][:-2]:
        answer += num
print(answer)