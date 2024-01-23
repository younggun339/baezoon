
import sys

n = int(sys.stdin.readline())

inout = (list(map(int, input().rstrip())))

graph = [[] for _ in range(n+1)]

visited = set()

for i in range(n-1):
    n1, n2 = map(int, sys.stdin.readline().split())
    graph[n1].append(n2)
    graph[n2].append(n1)

# print(graph)
# print(inout)

def dfs(start, graph, inout, path):
    # 받은걸 방문처리.
    visited.add(start)

    # 그리고, 실외인지 실내인지 받은 노드를 확인해서 만약 실내라면...
    if inout[start-1] == 1:
        # 그 노드랑 연결된 장소, 노드를 다 꺼냈을 때...
        for i in graph[start]:
            # 연결된 노드가 실외인지 실내인지 봐서, 실내고 방문하지않았다면...
            if inout[i-1] == 1 and i not in visited:
            # 경로 처리 할게요!
                path += 1
                visited.add(i)
            # 근데 실외라면...
            elif inout[i-1] == 0:
                # 그 실외 노드랑 연결된 걸 하나씩 꺼내서..
                for j in graph[i]:
                    # 그 실외 노드랑 연결된 노드가 실내라면..
                    if inout[j-1] == 1 and j not in visited:
                        # 경로 취급할게요!
                        path +=1
                        visited.add(j)
    
    visited.clear()

    return path

sum_path = 0
path = 0

for i in range(1, n+1):
    # print(sum_path)
    path_w = dfs(i, graph, inout, path)
    sum_path += path_w

print(sum_path)


# print(sum_path)