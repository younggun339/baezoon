

n = int(input())
k = n
a = 0
b = 0

new = 0
cycle = 0

if k == 0 :
    cycle += 1

while new != k:
    
    if n < 10 :
        a = 0
        c = n
    else :
        a = n // 10
        c = n % 10

    new = (c*10) + ((a+c)%10)
    cycle += 1
    n = new


print(cycle)