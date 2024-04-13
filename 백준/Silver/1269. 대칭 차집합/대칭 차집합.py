

A, B = map(int, input().split())

a = list(map(int, input().split()))
b = list(map(int, input().split()))

a= set(a)
b =set(b)

result = set.symmetric_difference(a,b)

print(len(result))