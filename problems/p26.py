max_repeat = 0
answer = 0

for d in range(2, 1000):
    nulls = len(str(d))
    delim = int("1" + "0" * nulls)
    rest = -1
    num = 0
    while rest not in (0, 1):
        rest = delim % d
        num += 1
        if str(rest) == str(delim)[0]:
            break
        delim = int(str(rest) + "0" * nulls)
    print(d, num)


