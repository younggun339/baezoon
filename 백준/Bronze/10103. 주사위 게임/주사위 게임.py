import sys

input = sys.stdin.readline

n = int(input())

one = 100
two = 100
for _ in range(n):
    a, b = map(int, input().split())
    if a > b :
        two -=a
    elif a < b:
        one -=b
    else :
        continue

print(one)
print(two)