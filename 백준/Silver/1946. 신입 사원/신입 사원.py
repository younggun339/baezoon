

# import sys
# from collections import deque

# t = int(sys.stdin.readline())
# recruit_count_list = []

# while t != 0:

#     n = int(sys.stdin.readline())

#     new_recruit_list = [ 0 for _ in range(n+1)]

#     for _ in range(n):
#         docu, inter = map(int, sys.stdin.readline().split())
#         new_recruit_list[docu] = inter

#     # new_recruit_list.sort(key = lambda x: (x[0]))

#     # print(new_recruit_list)

#     recruit_count = 0
#     recruit_list = []

#     idx = 1
#     big = new_recruit_list[1]
#     small = new_recruit_list[1]
#     for i in new_recruit_list[1:]:
#         # print(i)
#         # if i > big :
#         #     big = i
#         # print(idx)
#         # print(f'{idx}번째가 여태 나온 {big}보다 작은지 봐야지')
#         # print(small)
#         # print(f'{idx}가 {small}보다 작은지 봐야지 그리고 {i}가 {big}보다 큰지도')
#         # print(big)
#         if idx == (n//2)+(n%2) and i == (n//2)+(n%2):
#             idx += 1
#             continue
#         elif idx >= small and i>small:
#             idx += 1
#             continue
#         elif idx > big and i < big and i<small:
#             recruit_count += 1
#             recruit_list.append(i)
#         elif idx > big:
#             idx += 1
#             continue
#         elif i >big:
#             idx += 1
#             continue
#         # elif idx == (n//2)+(n%2) and i == (n//2)+(n%2):
#         #     idx += 1
#         #     continue
#         else :
#             recruit_count += 1
#             recruit_list.append(i)

#         if i > big :
#             big = i
#         elif i < small:
#             small = i

#         idx += 1
#         # if (max(new_recruit_list)+1) not in recruit_list:
#         #     recruit_list.append(idx)
#         #     idx += 1


#     # while 
#     # docu, inter = new_recruit_list.popleft()

#     recruit_count_list.append(recruit_count)
#     t -= 1

# for i in recruit_count_list:
#     print(i)
# # print(recruit_list)
    

import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    N = int(input())
    rank = [list(map(int, input().split())) for _ in range(N)]
    rank_asc = sorted(rank)
    top = 0
    result = 1
    
    for i in range(1, len(rank_asc)):
        if rank_asc[i][1] < rank_asc[top][1]:
            top = i
            result += 1
    
    print(result)

## https://velog.io/@ledcost/%EB%B0%B1%EC%A4%80-1946-%ED%8C%8C%EC%9D%B4%EC%8D%AC-%EC%8B%A0%EC%9E%85-%EC%82%AC%EC%9B%90-%EC%8B%A4%EB%B2%841-%EA%B7%B8%EB%A6%AC%EB%94%94