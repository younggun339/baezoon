
import sys

n = int(sys.stdin.readline())

table = [0]*(n+2)

# print(table)

table[1] = 1
table[2] = 2

def dp(n, table):

    if n == 1 :
        return 1
    elif n == 2:
        return 2
    else:
        for i in range(3,n+1):
            # print(i)
            table[i] = (table[i-1] + table[i-2])%15746
        
        return table[i]


print(dp(n, table))

# import sys
# sys.setrecursionlimit(10**6)


# import sys

# n = int(sys.stdin.readline())

# table = [0]*(n+1)

# table[1] = 1
# table[2] = 2

# def dp(n, table):

#     if n == 1 :
#         return 1
#     elif n == 2:
#         return 2
    
#     if table[n] !=0:
#         return table[n]
    
#     table[n] = dp(n-1) + dp(n-2)
#     return table[n]%15746

#     # else:
#     #     for i in range(3,n+1):
#     #         # print(i)
#     #         table[i] = table[i-1] + table[i-2]
        
#     #     return table[i]%15746


# print(dp(n, table))