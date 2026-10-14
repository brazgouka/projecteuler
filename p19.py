day_num = 1

months = [1, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30]

answer = 0
for i in range(1900, 2001):
    is_leap = i % 4 == 0 and i % 100 != 0
    months[2] = 29 if is_leap else 28
    months_agg = [x + sum(months[:i]) for i, x in enumerate(months)]
    days_in_year = 366 if is_leap else 365
    for day in range(1, days_in_year + 1):
        is_sunday = day_num % 7 == 0
        if day in months_agg and is_sunday:
            print(i, day, day_num)
            answer += 1
        day_num += 1

print(answer)
