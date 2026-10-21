def pandigitize(num):
    mul = 1
    pan = ''
    while len(pan) < 9:
        ns = str(num * mul)
        if len(set(pan + ns)) != len(set(ns)) + len(set(pan)):
            return None
        pan += ns
        mul += 1
    return pan if '0' not in pan and len(set(pan)) == 9 else None

for num in range(9876, 1, -1):
    p =  pandigitize(num)
    if p:
        print(p, num)
        break