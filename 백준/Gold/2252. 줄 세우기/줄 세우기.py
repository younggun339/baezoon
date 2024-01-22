

# from collections import defaultdict, deque

# n, m = map(int, input().split())

# # graph = defaultdict()

# graph = [ []*(n+1) for _ in range(n+1)]
# # print(graph)

# for i in range(m):
#     n1, n2 = map(int, input().split())
#     graph[n2].append(n1)

# # print(graph)

# hubo = deque()

# for node in range(1,n+1):
#     if len(graph[node]) == 0:
#         hubo.append(node)
# # print(hubo)

# result = []

# while hubo:

#     node = hubo.popleft()
#     result.append(node)

#     for i in range(1,n+1):
#         # print(i)
#         for value in graph[i]:
#             if value == node:
#                 graph[i].remove(value)
#                 # print(graph)
#                 if len(graph[i]) == 0:
#                     hubo.append(i)

# print(*result)

## 시간초과
#####################################
#진입차수를 형상화해서 그 숫자에 따라 조건 처리하고,
#진입차수 자체를 일일이 숫자로 지우는 형식으로 했다.
# 내 것이 시간초과인 이유는........

# 진입차수를 지우는 과정이 노드의 연결된 부모를 일일이 찾아서 대조해보기때문에.
# 하지만 이 식은 그냥 그 자식 노드들의 차수를 다 지워줬음.

# 주로 어떠한 속성을 확인할때 키와 값을 일일이 대조해서 찾기보다는
# 그걸 확인하는 리스트를 따로 만드나보네.



import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())

graph = [[] for _ in range(n+1)]
inDegree = [0 for _ in range(n+1)]
queue = deque()
answer = []

for i in range(m):
    a, b = map(int, sys.stdin.readline().rstrip().split())
    graph[a].append(b)
    inDegree[b] += 1

for i in range(1, n+1):
    if inDegree[i] == 0:
        queue.append(i)

while queue:
    tmp = queue.popleft()
    answer.append(tmp)
    for i in graph[tmp]:
        inDegree[i] -= 1
        if inDegree[i] == 0:
            queue.append(i)

print(*answer)