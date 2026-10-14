# size = 3
# maps = {}
# x = 0
# y = 0
# paths = 0
#
# def calc_routes(x, y):
#     global paths
#     if x > size or y > size:
#         return 0
#     if (x, y) in maps:
#         paths += maps[(x, y)]
#         return 1
#     if x == size and y == size:
#         paths += 1
#         return 1
#     p1 = calc_routes(x + 1, y)
#     p2 = calc_routes(x, y + 1)
#     maps.update({(x, y): p1 + p2})
#     return maps[(x, y)]
#
# calc_routes(x, y)
#
# print(paths)

ords = {
    1: "one",
    2: "two",
    3: "three",
    4: "four",
    5: "five",
    6: "six",
    7: "seven",
    8: "eight",
    9: "nine",
}

decs = {
    10: "ten",
    20: "twenty",
    30: "thirty",
    40: "forty",
    50: "fifty",
    60: "sixty",
    70: "seventy",
    80: "eighty",
    90: "ninety",
}

excs = {
    11: "eleven",
    12: "twelve",
    13: "thirteen",
    14: "fourteen",
    15: "fifteen",
    16: "sixteen",
    17: "seventeen",
    18: "eighteen",
    19: "nineteen",
}

def to_ord(i):
    return ords.get(i, "")

def to_dec(i):
    return decs.get(i, "")

def to_hun(i):
    return ords.get(i / 100, "") + "hundred"

answer = ""
for i in range(1, 1000):
    if i // 10 == 0:
        answer += to_ord(i)
        continue
    if i // 100 == 0:
        ord = "" if i in excs else to_ord(i % 10)

        answer += excs.get(i, to_dec(i - i % 10)) + ord
        continue
    if i // 1000 == 0:
        dec = excs.get(i % 100, to_dec(i % 100 - i % 10))
        ord = "" if i % 100 in excs else to_ord(i % 10)
        answer += to_hun(i - i % 100)
        if dec or ord:
            answer = answer + "and" + dec + ord
        continue

answer += "onethousand"
answer.replace(" ", "")
print(len(answer))