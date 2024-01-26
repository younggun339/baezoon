
import sys

n = int(sys.stdin.readline())

table = [0]*(n+1)

table[1] = 1

def dp(n, table):

    if n == 0 :
        return 0
    elif n == 1:
        return 1
    else:
        for i in range(2,n+1):
            # print(i)
            table[i] = table[i-1] + table[i-2]
        
        return table[i]


print(dp(n, table))