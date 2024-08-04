
A, B, V = map(int, input().split())
all = V-A
soc = A-B
# print(all)
# print(soc)
# print(10000000009//1000000000)
plus = 1
one = all//soc
if one == 0:
    one = 1
elif all%soc >0:
    # print("elif")
    plus = 2
# print(one)
result = one+plus
if V<=A :
    result = 1

print(result)