

import sys
from collections import deque

# limit_number = 10**9
# sys.setrecursionlimit(limit_number)

m, n, h = map(int, sys.stdin.readline().split())

dx= [1,-1,0,0,n,-n]
dy = [0,0,1,-1,0,0]
# dz = [0,0,0,0,h-1,-h+1]

tomato = []

for _ in range(h):
    # for _ in range(m):
    for _ in range(n):
        row = list(map(int, sys.stdin.readline().split()))
        tomato.append(row)

que = deque()

for i in range(h*n):
    for j in range(m):
        if tomato[i][j] == 1:
            que.append((i,j))

# print(tomato)
# print(que)

day = 0
# nextque = deque()
result = []
day_list = []

def tomato_is(que, tomato):
    # print(f'현재 들어있는 {que} 현황은 이렇다.')
    # day += 1
    nextque = deque()
    while que :
        x, y= que.popleft()
        floor = x//n
        # print(f'{x+1},{y+1}에서 퍼져나간다')
        for i in range(6):
            nx = x + dx[i]
            ny = y + dy[i]
            # print(f'주변에 있는{nx+1}, {ny+1} 위치에 있는 토마토를 봐야지')
            # nz = x + dz[i]
            # print(ny)
            # print(nx)

            if(0 <= nx < n*h and 0 <= ny < m):
                if (tomato[nx][ny] == 0 and nx//n == floor):
                    que.append([nx,ny])
                    tomato[nx][ny] = tomato[x][y] + 1
                    
                elif(tomato[nx][ny] == 0):
                    if(i == 4 or i == 5):
                        que.append([nx,ny])
                        tomato[nx][ny] = tomato[x][y] + 1


            # if 0 <= nx <= n*h-1 and 0 <= ny <= m-1:
            #     # print(f'{n*h}랑 {m}초과 안했지?')
            #     if tomato[nx][ny] == 0 :
            #         # print(f'{nx+1},{ny+1}위치에 있는게 안 익었으니까..')
            #         # print(f'{day}날이 지났다고 표기해주고')
            #         tomato[nx][ny] = day
            #         nextque.append((nx,ny))
            #         # day_list.append(day)
            #         # print(f'{nx+1}에 {ny+1}위치에 익는 것도 봐야지..')

    # if nextque:
    #     tomato_is(nextque, tomato, day+1, day_list)
    # day_list.append(day)
    # # print(f'그래서 반환하는 {day_list}는...')
    # return day_list
    
non_tomato = 0
for i in range(h*n):
    for j in range(m):
        if tomato[i][j] == 0:
            non_tomato +=1

if non_tomato == 0:
    print(0)

if non_tomato !=0:
    tomato_is(que, tomato)

    flag = True

    for i in range(h*n):
        for j in range(m):
            if tomato[i][j] == 0:
                flag = False

    if flag is False:
        print(-1)
    else:
        print(max(map(max,tomato))-1)
        # print(final_day_list)