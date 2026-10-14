with open('22.txt', 'r') as content_file:
    content = content_file.read()
    content = content.replace('"', '')
    content = ','.join(sorted(content.split(',')))
    name_sum = 0
    count = 0
    answer = 0
    for ch in content:
        if ch == ',':
            count += 1
            answer += count * name_sum
            name_sum = 0
            continue
        name_sum += ord(ch) - 64
    answer = answer + (count + 1) * name_sum
    print(answer)