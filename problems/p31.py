COINS = [1, 2, 5, 10, 20, 50, 100, 200]
AIM = 200

def compute(chain_total, coin):
    chain_total += coin
    if chain_total >= AIM:
        return int(chain_total == AIM)
    total = compute(chain_total, coin)
    idx = 1
    while COINS.index(coin) - idx >= 0:
        total += compute(chain_total, COINS[COINS.index(coin) - idx])
        idx += 1
    return total

print(sum(compute(0, coin) for coin in reversed(COINS)))
