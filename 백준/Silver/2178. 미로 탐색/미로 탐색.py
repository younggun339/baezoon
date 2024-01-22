
# from collections import defaultdict

# n, m = map(int, input().split())

# adj_list = [[[None]*m]*n]

# for i in range(n):
#     seq = str(input())
#     for j in seq:
#         adj_list[n][m] = int(j)


## 처음에 행렬 식으로 만들려다가... 뭔가 안 되길래.

# graph = defaultdict()

# for n in range(n):
#     for m in range(m):
#         if adj_list[n+1][m] == 1:
#             graph[n,m] = [n+1,m]
#         elif adj_list[n-1][m] == 1:
#             graph[n,m] = [n-1, m]
#         elif adj_list[n][m+1] == 1:
#             graph[n,m] = [n, m+1]
#         elif adj_list[n][m-1] == 1:
#             graph[n,m] = [n, m-1]


# def bfs(start_node,edges, visited, need_visited):

#     need_visited.push(start_node)

#     while need_visited:
#         node = need_visited.leftpop()
#         for next in graph[node]:
#             if next not in visited:
#                 need_visited.push(next)
        
#         visited.append(node)

## 노드 갯수만큼의 리스트를 만들어서, 이어진 간선을 모두 리스트로 만들어 해결하는 방식.
### 그렇지만 간선을 이렇게 많이 넣는 것 만으로 시간초과가 날 것 같다고...한다...

# graph = defaultdict()

# for i in range(1,n):
#     seq = str(input())
#     for j in seq:
#         graph[j+i*m] = int(seq[j])

# edge_list = defaultdict()

# for i in range(n*m):
#     if graph[i+1] == 1:
#         edge_list[i] = [i+1]
#     elif graph[i-1] == 1:
#         edge_list[i] = [i-1]
#     elif graph[i+m] == 1:
#         edge_list[i] = [i+m]
#     elif graph[i-m] == 1:
#         edge_list[i] = [i-m]


# INF = 999999999999

# distance = [INF]*(n*m)

# distance[0] = 0

# path = 1

# need_visited = [1]
# visited = []

# while need_visited:
#     start = need_visited.pop()
#     for node in edge_list[start]:
#         if distance[node] > path :
#             distance[node] = path
#             path +=1
#             visited.append(node)

#             for next in edge_list[node]:
#                 need_visited.append(next)


# print(distance[n*m])

##########################
# 앞 옆 그거 인덱스만 넣어서 확인한다네...
# 나 자신없다...


# import sys

# n, m = map(int, sys.stdin.readline().split())

# miro = [ [] for _ in range(n)]
# print(miro)
# for j in range(n):
#     seq = str(sys.stdin.readline().rstrip())
#     for i in seq:
#         # if i != '\n':
#         miro[j].append(int(i))
#     # # print(seq)
#     # for i in seq:
#     #     for k in range(m):
#     #         print(k)
#     #     # for i in seq:
#     #         print(i)
#     #         if i != '\n':
#     #             miro[j][k] = int(i)

# print(miro)

# # visited = [[False]*m]*n
# # path = 1
# # print(visited)

# # from collections import deque

# # que = deque()

# # def bfs(start_node, visited, path):

    

# #     if miro[start_node][start_node+1] == 1:
# #         if visited[start_node][start_node+1] is False:
# #             visited[start_node][start_node+1] = True
# #             path +=1
# #             miro[start_node][start_node+1] = path
# #             bfs(start_node+1, visited, path)
# #     elif miro[start_node+1][start_node] == 1:
# #         if visited[start_node+1][start_node] is False:
# #             visited[start_node+1][start_node] = True
# #             path +=1
# #             miro[start_node+1][start_node] = path
# #             bfs()
# #     elif miro[start_node-1][start_node] == 1:
# #         if visited[start_node-1][start_node] is False:
# #             visited[start_node-1][start_node] = True
# #             path +=1
# #             miro[start_node-1][start_node] = path
# #     elif miro[start_node][start_node-1] == 1:
# #         if visited[start_node][start_node-1] is False:
# #             visited[start_node][start_node-1] = True
# #             path +=1
# #             miro[start_node][start_node-1] = path

# ##################
## 그러니까...
# 아예 완전히 다른 값의 범위를 설정해줄 때는
# (변동이 규칙적이지만 0, 1,2 같은 순은 아닐 경우)
# 리스트 자체로 범위가 변하는 걸 순차적으로 구현한 후
# 그 n과 m내 사이에서 1이면
#queue로 관찰범위에 넣고, 그 자리를 여태 이동 경로에 +1했군.

# 내가 한 것에서는 뭘 못했냐면(범위지정)
# while로 bfs 돌리는 것도 좀.. 자신없었는듯..


import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())
graph = []

for _ in range(n):
    graph.append(list(map(int, input().rstrip())))

# 상하좌우
dx = [-1, 1, 0, 0] 
dy = [0, 0, -1, 1]

def bfs(x, y):
    
    queue = deque()
    queue.append((x,y))

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] == 1:
                queue.append((nx, ny))
                graph[nx][ny] = graph[x][y] + 1
    
    return graph[n-1][m-1]

print(bfs(0,0))