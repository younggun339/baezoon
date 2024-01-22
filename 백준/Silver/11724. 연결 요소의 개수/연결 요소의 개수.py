
from collections import defaultdict

# import sys
# sys.setrecursionlimit(10**6)

# adj_list = defaultdict()

# n, m = map(int, input().split())

# adj_list = [ []*(n+1) for _ in range(n+1)]

# for _ in range(m):
#     n1, n2 = map(int, input().split())

#     adj_list[n1].append(n2)
#     adj_list[n2].append(n1)

# # print(adj_list)

# visited = []

# non_visited = [1]

# def component(non_visited, adj_list, visited, count, n):

#     # start = non_visited.pop()

#     # # visited.append(start)
#     # print(visited)

#     # non_visited.append(start)

#     while non_visited:
#         node = non_visited.pop()

#         for a in adj_list[node]:
#             if a not in visited:
#                 non_visited.append(a)
#                 # visited.append(n)
#                 # for next in adj_list[n]:
#                 #     non_visited.append(next)
#         if node not in visited:
#             visited.append(node)
#     # print(visited)

#     for key in range(1,n+1):
#         # print(key)
#         if key not in visited:
#             non_visited.append(key)
#             break
#     # print(non_visited)
#     count +=1
#     # print(f'({count} 미리출력)')
#     # print(len(visited))
#     # print(n)
#     if len(visited) != n:
#         return component(non_visited, adj_list, visited, count, n)
#     # print(f'({count} 저에요 결과값)')
#     return count

# count = 0

# result = component(non_visited, adj_list, visited, count, n)

# print(result)

# # 시간 초과


################
# 아마도 위에건 방문을 했는지 안 했는지, 한번 dfs를 끝내고 다른 모든 노드에서
# 연결이 되어있는지 아닌지 찾는 과정때문에 메모리가 많이 드는 것 같음.
# 그래서 여기에선 아예 True, False로 반환해서 방문 목록을 굳이 다 조사하기보다
# 딱 visited의 index로 여부를 알 수 있기때문에 빨리 끝나는 것 같음.

import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

# dfs 함수
def dfs(graph, v, visited):
    visited[v] = True
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)

n, m = map(int, input().split()) # 정점의 개수, 간선의 개수
graph = [[] for _ in range(n+1)]
for i in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

count = 0 # 연결 노드의 수
visited = [False] * (n+1)
for i in range(1, n+1):
    if not visited[i]:
        dfs(graph, i, visited)
        count += 1 # dfs 한 번 끝날 때마다 count+1

print(count)

