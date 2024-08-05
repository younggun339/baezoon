import sys
input = sys.stdin.readline

N = int(input())
array = [0] * 10001
for _ in range(N):
    k = int(input())
    array[k] += 1

for i in range(10001):
    if array[i] != 0:
        for _ in range(array[i]):
            print(i)