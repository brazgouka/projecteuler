# TODO improve

pentagons = [1]
iter = 4
found = {}

while True:
    pentagons.append(pentagons[-1] + iter)
    iter += 3
    if pentagons[-1] in found:
        print(found.get(pentagons[-1])[0] - found.get(pentagons[-1])[1])
        break
    for p in pentagons:
        if pentagons[-1] - p in pentagons:
            found.update({pentagons[-1] + p: (pentagons[-1], p)})