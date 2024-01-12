
T = int(input())
i = 1
while i <= T :
    S = ""
    k = 0
    a, b = input().split()
    a = int(a)
    b = str(b)
    while k+1<= len(b):
        S = S + b[k]*a
        k = k +1
    i = i +1
    print(S)


