a = 1

while True:
    if a % 3 == 0 and sorted(str(a)) == sorted(str(a * 2)) == sorted(str(a * 3)) == sorted(str(a * 4)) == sorted(str(a * 5)) == sorted(str(a * 6)):
        break
    a += 1
print(a)