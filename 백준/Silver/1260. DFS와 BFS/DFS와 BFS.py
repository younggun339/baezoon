
# from collections import defaultdict 

# n, m, v = map(int, input().split())

# edges = defaultdict()

# for i in range(1,n+1):
#     edges[i] = []

# for i in range(m):
#     n1, n2 = map(int, input().split())
#     edges[n1].append(n2)
#     edges[n2].append(n1)

# connected = 0

# for i in range(1,n+1):
#     if len(edges[i]) != 0 :
#         connected += 1


# # print(edges)
# # DFS
    
# def dfs(start_node, edges, visited, n, connected):

#     visited.append(start_node)
#     # print(start_node)
#     minimum = None
#     flag = True
#     if len(edges[start_node]) != 0:
#         edges[start_node].sort()
#         for i in edges[start_node]:

#             if i not in visited:
#                 if minimum is None:
#                     minimum = i
#                 elif minimum > i:
#                     minimum = i

#             if edges[start_node][-1] == i and minimum is None:
#                 flag = False



#         # for i in range(1,n+1):
#         #     if len(edges[i]) != 0 :
#         #         connected += 1


#         if flag == True:
#             dfs(minimum, edges, visited, n, connected)

#         # if len(edges[start_node]) != 0:
#         #     dfs(minimum, edges, visited, n, connected)


#     elif len(edges[start_node]) == 0:
#         pass

#     return visited
    
# # BFS

# from collections import deque

# def bfs(start_node, edges, visited):
#     que = deque()

#     que.append(start_node)

#     while que:
#         node = que.popleft()

#         edges[node].sort()

#         for i in edges[node]:
#             if i not in visited and i not in que:
#                 que.append(i)
     
#         visited.append(node)

#     return visited

# visited = []


# dfs_list = dfs(v, edges, visited,n, connected)

# visited = []
# bfs_list = bfs(v, edges, visited)

# # print(dfs_list)
# # print(bfs_list)

# print(*dfs_list)
# print(*bfs_list)

# # graph = [ []*(n+1) for _ in range(n+1)]
# # print(graph)



###########################

#하.. 자꾸 틀렸다고 뜬다
# 로직은 똑같은거같은데..
# 오히려 인터넷에서 찾아본게 예외..가 있을거같은데
# 그냥 일단 내려놓음.

# 백준 1260 : DFS와 BFS

# 초기 세팅
N, link, V = map(int, input().split())
graph = [ []*(N+1) for _ in range(N+1)]

# 인접 리스트 만들기
for i in range(link):
    a,b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
    graph[a].sort()
    graph[b].sort()
    
# 방문 여부 체크
visited_1 = [False]*(N+1) # dfs용
visited_2 = [False]*(N+1) # bfs용

# 1. DFS 만들기
dfs_visited = []
def dfs(graph, v, visited):
    if visited[v] == False:
        visited[v] = True
        
    global dfs_visited
    dfs_visited.append(v)
    
    # 연결된 다른 노드를 재귀적으로 방문
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)
            

# 2. BFS 만들기
bfs_visited = []
from collections import deque

def bfs(graph, v, visited):
    queue = deque([v]) # start에 대한 큐
    
    if visited[v] == False:
        visited[v] = True
        
    global bfs_visited
    while queue:
        # 큐에서 하나씩 원소를 뽑아 출력
        i = queue.popleft()
        bfs_visited.append(i) # 방문한 노드 저장
        # 해당 원소(i)와 연결된 아직 방문하지 않은 원소들을 큐에 삽입
        for j in graph[i]:
            if not visited[j]:
                queue.append(j)
                visited[j] = True
            
            
dfs(graph, V, visited_1)
bfs(graph, V, visited_2)
print(*dfs_visited, sep = ' ')
print(*bfs_visited, sep = ' ')
