
from collections import defaultdict

computer_edge = defaultdict()

n = int(input())
v = int(input())

for i in range(1,n+1):
    computer_edge[i] = []

for _ in range(v):
    n1, n2 = map(int, input().split())
    computer_edge[n1].append(n2)
    computer_edge[n2].append(n1)

# print(computer_edge)

start = 1

non_visited = [1]
visited = []

while non_visited:
    start = non_visited.pop()

    for node in computer_edge[start]:
        if node not in visited and node not in non_visited:
            non_visited.append(node)
            # visited.append(node)
            # for next in computer_edge[node]:
            #     non_visited.append(next)
    visited.append(start)

# print(visited)
print(len(visited)-1)