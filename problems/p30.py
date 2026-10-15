nums = []

for i in range(12, 10_000_000):
    sum_of_pows = 0
    for digit in str(i):
        sum_of_pows += int(digit)**5
    if sum_of_pows == i:
        nums.append(i)
    sum_of_pows = 0
print(sum(nums))
