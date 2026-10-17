products = set()

for i in range(1, 99):
    for j in range(99, 9999):
        k = i * j
        if sorted(f"{i}{j}{k}") == sorted("123456789"):
            products.add(k)

print(sum(products))

