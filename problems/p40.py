import math

d = ''.join(str(i) for i in range(1_000_001))

s = math.prod(int(d[10**i]) for i in range(0, 7))

print(s)
