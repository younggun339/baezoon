

import sys

n, k = map(int, sys.stdin.readline().split())

coin_list = []

for _ in range(n):
    coin = int(sys.stdin.readline())
    coin_list.append(coin)

coin_list.reverse()

count = 0
inc_coin = k

for coin in coin_list:
    if inc_coin < coin:
        continue
    elif inc_coin >= coin:
        a = inc_coin//coin
        count += a

        inc_coin -= a*coin
        if inc_coin == 0:
            break

print(count)