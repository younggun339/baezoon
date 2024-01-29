

# import sys
# from collections import deque

# n = int(sys.stdin.readline())

# I_list = []

# for _ in range(n):
#     start, end = map(int, sys.stdin.readline().split())
#     I_list.append([start,end])

# # print(I_list)

# I_list.sort(key = lambda x :(x[1], x[0]))

# # I_list_first = sorted(I_list_basic, key=lambda x: x[0])
# # I_list = sorted(I_list_first, key= lambda x: x[1])

# print(I_list)

# I_length = []

# for start, end in I_list:
#     time = end - start + 1
#     I_length.append(time)


# # print(I_length)

# # start_list = []
# # end_list = []

# final_list = []
# full_list = set()

# while I_length:

#     small = I_length.index(min(I_length))
#     I_length.remove(I_length[small])
#     # print(I_length)
#     # print(I_list)
    

#     start, end = I_list[small]
#     # print(start)
#     # print(end)

#     if all(val not in full_list for val in range(start+1,end+1)) and start not in full_list and end not in full_list:

#         for i in range(start+1,end):
#             full_list.add(i)
        
#         # print(full_list)

#         final_list.append((start,end))
#     I_list.remove([start,end])

#     # if start not in start_list and end not in end_list:
#     #     final_list.append((start,end))
#     #     start_list.append(start)
#     #     end_list.append(end)
#     # print(start_list)
#     # print(end_list)
#     # print(final_list)    
#     # print(I_length)

# print(len(final_list))


# 시간 초과...
# 인 이유가 있는 풀이였군
# 여기선 단순하게 정렬 두번해서 끝나는 시간을 계속 갱신해 넣어주는 형식으로 하고있다...

import sys

N = int(sys.stdin.readline())

time = [[0]*2 for _ in range(N)]
for i in range(N):
    s, e = map(int, sys.stdin.readline().split())
    time[i][0] = s
    time[i][1] = e

time.sort(key = lambda x: (x[1], x[0]))

cnt = 1
end_time = time[0][1]
for i in range(1, N):
    if time[i][0] >= end_time:
        cnt += 1
        end_time = time[i][1]

print(cnt)
# 출처: https://suri78.tistory.com/26 [공부노트:티스토리]