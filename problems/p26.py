max_repeat = 0
answer = 0


for d in range(2, 1000):
    prev = []
    rest = 1
    while rest != 0:
        rest *= 10**len(str(d))
        if rest in prev:
            break
        prev.append(rest)
        rest = rest % d
    if rest != 0:
        lena = len(prev[:prev.index(rest)]) or len(prev)
        if lena > max_repeat:
            answer, max_repeat = d, lena

print(answer)