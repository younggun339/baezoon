



import sys

n = int(input())
numer_seq = list(map(int, sys.stdin.readline().split()))

# print(numer_seq)

dp = [ 1 for _ in range(n+1)]

for i in range(1,n):
    for j in range(0,i):
        # print(f'만약 {i}번째가 뒤에 붙는걸 볼 건데, 앞의 {j}번째가 작은지 본다면..')
        if numer_seq[i] > numer_seq[j]:
            dp[i] = max(dp[i], dp[j]+1)

print(max(dp))

