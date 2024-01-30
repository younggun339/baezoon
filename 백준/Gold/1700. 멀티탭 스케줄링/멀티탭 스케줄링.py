 
# import sys
# from collections import deque


# n, k = map(int, input().split())


# electronics_list = list(map(int, sys.stdin.readline().split()))
# Multitap = [ 0 for _ in range(n)]

# electronics_list = deque(electronics_list)

# use_list = set(electronics_list)

# use_numuber_list = [ 0 for _ in range(k+1)]

# for i in use_list:
# #     for j in electronics_list:
# #         if j == i:
# #             use_numuber_list[i] += 1

# # print(use_list)
# # print(use_numuber_list)

# # # for i in Multitap:
# # #     for j in electronics_list:
# # #         if i == 0:
# # #             Multitap[idx] = j
# # #             electronics_list.popleft()
# # #         elif i != 0:
# # #             idx += 1
# # #             continue

# # for i in range(n):
# #     Multitap[i] = electronics_list[0]
# #     electronics_list.popleft()

# # print(Multitap)
# # print(electronics_list)

# # count = 0

# # while electronics_list:
# #     j = electronics_list.popleft()
# #     # print(f'{j}를 처리해주마')
# #     if j in Multitap:
# #         # print(f'이미 멀티탭 안에 있으니 생략하겠어')
# #         use_numuber_list[j] -= 1
# #         continue
# #     elif j not in Multitap:
# #         # print(f'엇 멀티탭에 없잖아')
# #         idx = 0
# #         for i in Multitap:
# #             # print(f'흠 현재 {i}가 멀티탭을 쓰고 있는데...')
# #             if i in electronics_list:
# #                 # print(f'앞으로도 쓸 거같으니까 넘어가겠어')
# #                 idx +=1
# #                 if idx == len(Multitap):
# #                     # print(f'이런! 앞으로 쓸 것들만 꼽혀있잖아?')

# #                     # idx_multi = Multitap.index(min(Multitap))
# #                     # Multitap[idx_multi] = j
# #                     # count += 1
# #                     # print(f'대충 작은 숫자가 이미 쓸만큼 썼겠지...?? 뽑자!')
# #             elif i not in electronics_list:
# #                 # print(f'앞으로 안 쓸 거같은데?')
# #                 Multitap[idx] = j
# #                 # print(f'지금 {j}를 꽂아야겠군')
# #                 use_numuber_list[j] -= 1
# #                 count += 1
# #                 break

# # print(Multitap)
# # print(electronics_list)

# # print(count)

 
import sys
from collections import deque


n, k = map(int, input().split())


electronics_list = list(map(int, sys.stdin.readline().split()))
Multitap = [ 0 for _ in range(n)]

electronics_list = deque(electronics_list)

for i in range(n):
    if electronics_list[0] not in Multitap:
        Multitap[i] = electronics_list[0]
        electronics_list.popleft()

idx_list = []

count = 0

while electronics_list:
    j = electronics_list.popleft()
    # print(f'{j}를 꽂아볼까?')
    if j in Multitap:
        # print(f'{j}는 이미 멀티탭에 있으니 넘어갈게')
        continue
    elif 0 in Multitap:
        Multitap[Multitap.index(0)] = j
    else :
        # print(f'{j}는 멀티탭에 없군')
        for i in Multitap:
            if i in electronics_list:
                # print(i)
                if i != j :
                    idx_list.append([electronics_list.index(i),i])
            else :
                # print(f'앞으로 안 쓰니 뽑아야겠다')
                
                Multitap[Multitap.index(i)] = j
                count += 1
                # print(f'현재 {Multitap}은 이렇게 꽂았네.')
                idx_list.clear()
                break
        if not idx_list:
            continue
        else:
            # print(idx_list)
            max_elec = max(idx_list, key = lambda x: x[0])
            # print(max_elec)
            # if max_elec[1] ==
            idx_two = Multitap.index(max_elec[1])
            # print(idx_two)
            # print(j)
            Multitap[idx_two] = j
            count += 1
            # print(f'좋아 {max_elec[1]}을 {j}로 바꿨다.')
            # print(f'현재 {Multitap} 은 이렇게 꽂혀있군.')
            idx_list.clear()
            continue
        # idx_two = Multitap.index(max_elec[1])
        # print(idx_two)
        # Multitap[idx_two] = j
        # count += 1
        # continue
print(count)