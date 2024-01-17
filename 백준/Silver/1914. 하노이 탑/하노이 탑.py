# # 세 개의 장대가 있고 첫 번째 장대에는 반경이 서로 다른 n개의 원판이 쌓여 있다. 
# 각 원판은 반경이 큰 순서대로 쌓여있다. 이제 수도승들이 다음 규칙에 따라 첫 번째 장대에서 세 번째 장대로 옮기려 한다.

# # 한 번에 한 개의 원판만을 다른 탑으로 옮길 수 있다.
# # 쌓아 놓은 원판은 항상 위의 것이 아래의 것보다 작아야 한다.
# # 이 작업을 수행하는데 필요한 이동 순서를 출력하는 프로그램을 작성하라. 단, 이동 횟수는 최소가 되어야 한다.

# # 아래 그림은 원판이 5개인 경우의 예시이다.



# # 첫째 줄에 옮긴 횟수 K를 출력한다.

# # N이 20 이하인 입력에 대해서는 두 번째 줄부터 수행 과정을 출력한다. 
# 두 번째 줄부터 K개의 줄에 걸쳐 두 정수 A B를 빈칸을 사이에 두고 출력하는데, 
# 이는 A번째 탑의 가장 위에 있는 원판을 B번째 탑의 가장 위로 옮긴다는 뜻이다. 
# N이 20보다 큰 경우에는 과정은 출력할 필요가 없다.


import sys


# import typing

# import collections 

# a = []
# b = []



def hanoi(n:int, start:int, end:int):



    if n > 1:
        hanoi(n-1, start, 6-start-end)

        
        
    print(f'{start} {end}')
        # a.append(1)
        # b.append(start)
        # b.append(end)

    if n > 1:
        hanoi(n-1, 6-start-end, end)

    

n = int(sys.stdin.readline().strip())
print(2**n-1)
if n<= 20 : hanoi(n, 1, 3)


# print(2**n-1)

# for i in range(0,len(b),2):
#     c, d = b[i], b[i+1]
#     print(f'{c} {d}')





# n = int(input())

# import typing

# import collections 

# a = []
# b = []
# e = []


# def hanoi(n:int, start:int, end:int):
#     global e,a,b

    

#     if len(e) == 0:
#         if n > 1:
#             hanoi(n-1, start, 6-start-end)

            
#         a.append(1)
#         b.append(start)
#         b.append(end)
#         if start == (6-start-end) : 
#             e.append(1)

            

#         if n > 1:
#             n = n -1
#             start = 6-start-end
            



# hanoi(n, 1, 3)


# print(len(a))

# for i in range(0,len(b),2):
#     c, d = b[i], b[i+1]
#     print(f'{c} {d}')



# n = int(input())

# import typing

# import collections 



# def hanoi(n:int, start:int, end:int, a:list, b:list):


#     if n > 1:
#         hanoi(n-1, start, 6-start-end, a, b)

    
#     a.append(1)
#     b.append((start,end))



#     if n > 1:
#         hanoi(n-1, 6-start-end, end, a, b)


# a = []
# b = []

# hanoi(n, 1, 3, a, b)


# print(len(a))

# for move in b:
#     print(f'{move[0]} {move[1]}')

# for i in range(0,len(b),2):
#     c, d = b[i], b[i+1]
#     print(f'{c} {d}')
    

    
# def hanoi_moves(n: int, start: int, end: int, a: list, b: list):
#     if n == 1:
#         a.append(1)
#         b.append((start, end))
#     else:
#         hanoi_moves(n-1, start, 6-start-end, a, b)
#         a.append(1)
#         b.append((start, end))
#         hanoi_moves(n-1, 6-start-end, end, a, b)

# def hanoi(n: int, start: int, end: int):
#     a = []
#     b = []
#     hanoi_moves(n, start, end, a, b)
#     return a, b

# n = int(input())
# a, b = hanoi(n, 1, 3)

# print(len(a))
# for move in b:
#     print(f'{move[0]} {move[1]}')



