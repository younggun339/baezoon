
import sys

n, k = map(int, sys.stdin.readline().split())

thing =[(0,0)]

for _ in range(n):
    w, v = map(int, sys.stdin.readline().split())
    thing.append((w,v))

# print(thing)

dp = [[0 for _ in range(k+1)] for _ in range(n+1)]

for j in range(1,k+1):
    for i in range(1, n+1):
        w = thing[i][0]
        v = thing[i][1]
        if j < w:
            dp[i][j] = dp[i-1][j]
        elif j >= w:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-w]+v)

# print(dp)

print(dp[n][k])