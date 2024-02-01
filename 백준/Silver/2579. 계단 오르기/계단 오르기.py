
import sys

n = int(input())

stairs_list = [0]

for _ in range(n):
    stairs = int(input())
    stairs_list.append(stairs)

# print(stairs_list)

s = [[0,0] for _ in range(n+1)]

# print(s)

s[1] = [stairs_list[1],0]

# print(s)

def stairs_scores(n):

    # if n == 0:
    #     print(0)
    # elif n == 1:
    #     print(s[1])
    
    if n > 1:
        s[2] = [s[1][0]+stairs_list[2], stairs_list[2]]
    
        if n > 2:
            s[3] = [s[2][1]+stairs_list[3],s[1][0]+stairs_list[3]]

            if n > 3:
                for i in range(4,n+1):
                    s[i] = [s[i-1][1]+stairs_list[i], max(s[i-2][0]+stairs_list[i],s[i-2][1]+stairs_list[i])]
    
stairs_scores(n)

print(max(s[n][0], s[n][1]))
