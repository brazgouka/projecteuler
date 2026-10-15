from pathlib import Path

import math


def solve_quadratic(a, b, c):
    d = (b ** 2) - (4 * a * c)

    if d < 0:
        return ()
    elif d == 0:
        x = -b / (2 * a)
        return (x,)
    else:
        x1 = (-b + math.sqrt(d)) / (2 * a)
        x2 = (-b - math.sqrt(d)) / (2 * a)
        return (x1, x2)

with open(Path(__file__).with_name('42.txt'), 'r') as content_file:
    content = content_file.read()
    content = content.replace('"', '')
    content = ','.join(sorted(content.split(',')))
    name_sum = 0
    answer = 0
    for ch in content:
        if ch == ',':
            sq = solve_quadratic(1, 1, -name_sum * 2)
            if any(0 < x == int(x) for x in sq):
                answer += 1
            name_sum = 0
            continue
        name_sum += ord(ch) - 64
    print(answer)