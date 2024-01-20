v, e = map(int, input().split())
v, e = int(v), int(e)


# 세번째 시도


graph = list()

for i in range(e):
    a, b, c = map(int, input().split())
    graph.append((c ,a, b))


from collections import defaultdict
from heapq import *


def prim(start_node, edges):
    mst = []
    connected_node = set(str(start_node))

    adj_list = defaultdict(list)

    for weight, n1, n2 in edges:
        adj_list[n1].append((weight, n1, n2))
        adj_list[n2].append((weight, n2, n1))

    candidate_edge_list = adj_list[start_node]
    heapify(candidate_edge_list)
    # print(candidate_edge_list)

    while candidate_edge_list:
        cost, n1, n2 = heappop(candidate_edge_list)

        if str(n2) not in connected_node:
            connected_node.add(str(n2))
            mst.append((cost, n1, n2))

            for edge in adj_list[n2]:
                if str(edge[2]) not in connected_node:
                    # print(edge)
                    heappush(candidate_edge_list, edge)

    return mst


mst = prim(1,graph)
sum_w = 0
# print(mst)

for weight, n1, n2 in mst:
    sum_w += weight

print(sum_w)