import math
inpu = list(map(int, input().split()))
# print(inpu)

H = inpu[0]
W = inpu[1]
N = inpu[2]
M = inpu[3]

col = H//(N+1)
#print(col)
hang = W//(M+1)
#print(hang)

if H%(N+1) > 0 and H>1 :
    col +=1

if W%(M+1) > 0 and W>1 :
    hang += 1

#print(col)
#print(hang)
result = col*hang

# result = math.trunc(result)
if result == 0:
    result = 1
print(result)


