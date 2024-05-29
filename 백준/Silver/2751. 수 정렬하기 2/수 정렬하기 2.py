# N= int(input())

# listnum = []

# for i in range(N):
#     number = int(input())
#     listnum.append(number)

# def mergeSort(listnum):
#     N = len(listnum)
#     for i in range(N):
#         tmp = listnum[i]
#         j = i - 1
#         while (j >= 0 and tmp < listnum[j]):
#             listnum[j+1] = listnum[j]
#             j-=1
#         listnum[j+1] = tmp
#     return listnum

# def half(all):
#     num = len(all)
#     if num > 3:
#         left = all[0:num//2]
#         right = all[num//2:num]
#         left = half(left)
#         right = half(right)
#         all = mergeSort(left+right)
#         return all
#     all = mergeSort(all)
#     return all


# listnum = half(listnum)
# for i in listnum:
#     print(i)

import sys
n = int(input())

num = []

for _ in range(n):
    num.append(int(sys.stdin.readline()))

num.sort()

for i in num:
    print(i)