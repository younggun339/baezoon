

#### 첫번째 시도
# from collections import defaultdict

# # n = int(input())

# # visited =[1]

# # tree = defaultdict()

# # for i in range(n):
# #     n1, n2 = map(int, input().split())

# #     if n1 in visited:
# #         tree[n1] = [n2]
# #         visited.append(n2)
# #     elif n2 in visited:
# #         tree[n2] = [n1]
# #         visited.append(n1)

# # for i in range(n):
# #     for key, value in tree.items():
# #         if n == value:
# #             print(key)

## 두번째 시도

import sys
from collections import deque

n = int(sys.stdin.readline())

graph = [[] for _ in range(n+1)]
# print(graph)

for i in range(n-1):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

# print(graph)

INF = 1e8

parent = [INF] * (n+1)
check = [False] * (n+1)
check[1] = True

def parent_is(start):
    que = deque()

    que.append(start)

    while que:
        node = que.popleft()
        # print(node)
        # print(parent)
        # print(check)
        for i in graph[node]:
            if check[i] is False:
                parent[i] = node
                check[i] = True
                que.append(i)


parent_is(1)
# print(parent)

for i in parent:
    if i == INF :
        continue
    print(i)
