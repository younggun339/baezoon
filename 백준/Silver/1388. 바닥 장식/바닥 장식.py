
import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())

graph = []

for _ in range(n):
    graph.append(list(map(str, input().rstrip())))

# print(graph)

dx = [1, -1]
dy = [1, -1]

visited = set()
que = deque()
count = 0


def namupan(que, visited, graph, count):

    count += 1
    garoque = deque()
    seroque = deque()
    x, y = que.popleft()

    if graph[x][y] == '-':
        seroque.append((x,y))
    elif graph[x][y] == '|':
        garoque.append((x,y))

    while garoque:
        # print(f'{garoque}를 봐야징')
        x, y = garoque.popleft()
        visited.add((x,y))

        for i in range(2):
            nx = x + dx[i]
            # print(f'{nx}, {y}')
            if 0<= nx <= n-1:
                # print(f'{nx}는 {m}보다 작넹')
                if graph[nx][y] == '|' and (nx,y) not in visited:
                    # print(f'{nx},{y}를 봐야징')
                    garoque.append((nx,y))
                    # print(f'{garoque}를 보면 되겟당')
                    visited.add((nx,y))

    while seroque:

        # print(f'{count} 올렷당')
        x, y = seroque.popleft()
        # print(f'{x},{y}를 보겟슴당')
        visited.add((x,y))
        # print(f'{visited} 방문 목록 확인하구')

        for i in range(2):
            ny = y + dy[i]
            
            if 0 <= ny <= m-1:
                # print(f'{ny}가 {m-1} 내이니깐')
                if graph[x][ny] == '-' and (x,ny) not in visited:
                    # print(f'{x},{ny}가 가로니깐 마저 봐야징')
                    seroque.append((x,ny))
                    # print(f'{seroque} 목록을 보면 되겟징?')
                    visited.add((x,ny))

    return count


for i in range(n):
    for j in range(m):
        if (i,j) not in visited:
            # print(i, j)
            que.append((i,j))
            count = namupan(que, visited, graph, count)

print(count)