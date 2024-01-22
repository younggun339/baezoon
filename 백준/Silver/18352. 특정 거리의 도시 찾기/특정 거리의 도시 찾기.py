
# 플로이드 워셜로 풀었으나 시간초과 예상.
# 또, x의 범위 설정이 ... 애매하다(리스트의 인덱스는 0부터 시작하는데, 키값은 1부터 시작함.)
# 사실 x범위정도야 0으로 시작시킨다음 아래 min에서는 1을 더해서 하면 되긴 하겠지만.

# from collections import defaultdict

# n, m, k, x = map(int, input().split())
# INF = 9999999999999

# graph = defaultdict()

# for i in range(1,n+1):
#     graph[i] = [INF]*n

# # print(graph[1][3])

# for _ in range(m):
#     n1, n2 = map(int, input().split())
#     graph[n1][n2-1] = 1

# for x in range(1,n+1):
#     for i in range(1,n+1):
#         print(i)
#         for j in range(n):
#             print(j)
#             graph[i][j] = min(graph[i][j], graph[i][x] + graph[x][j])

# i = 0
# count = 0

# for distance in graph[x]:
#     if distance == k:
#         print(i)
#         count += 1

#     elif i == n and count == 0:
#         print(-1)

###########################
from collections import defaultdict, deque
import sys

n, m, k, x = map(int, sys.stdin.readline().split())

graph = [[] for _ in range(n+1)]

for i in range(m):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)

visited = [False]*(n+1)
INF = 1e8
distance = [0]*(n+1)
result = []
# print(graph)
# print(visited)

def bfs(visited, distance, graph, k,x):

    que = deque([x])
    result = []
    visited[x] = True
    distance[x] = 0

    # que.append(x)
    # print(que)

    # for i in graph[x]:
    #     if visited[i] is False:
    #         visited[i] = True
    #         distance[i] = 1
    #         que.append(i)
    # print(que)
            
    # if k == 1:
    #     for i in graph[x]:
    #         print(i)
    #         pass

    while que:
        node = que.popleft()

        for i in graph[node]:
            # print(i)
            if visited[i] is False:
                # print(i)
                distance[i] = distance[node]+1
                # print(distance[i])
                visited[i] = True
                que.append(i)
            
                if distance[i]> k:
                    break
                elif distance[i] == k:
                    result.append(i)

    if len(result) == 0:
        print(-1)
    else:
        result.sort()
        for i in result:
            print(i, end='\n')
    


bfs(visited, distance, graph, k,x)