

# 이진 트리를 입력받아 전위 순회(preorder traversal), 
# 중위 순회(inorder traversal), 
# 후위 순회(postorder traversal)한 결과를 출력하는 프로그램을 작성하시오.

# 첫째 줄에는 이진 트리의 노드의 개수 N(1 ≤ N ≤ 26)이 주어진다. 
# 둘째 줄부터 N개의 줄에 걸쳐 각 노드와 그의 왼쪽 자식 노드, 오른쪽 자식 노드가 주어진다. 
# 노드의 이름은 A부터 차례대로 알파벳 대문자로 매겨지며, 항상 A가 루트 노드가 된다. 
# 자식 노드가 없는 경우에는 .으로 표현한다.

# 첫째 줄에 전위 순회, 
# 둘째 줄에 중위 순회, 셋째 줄에 후위 순회한 결과를 출력한다.

# # 각 줄에 N개의 알파벳을 공백 없이 출력하면 된다
# n = int(input())

# tree = dict()

# for i in range(n):
#     a, b, c = map(str, input().split())
#     a, b, c = str(a), str(b), str(c)
#     tree[a] = [c, b] 
#     # print(tree)

# print(tree)

# # 전위 순회

# def dfs(graph, start_node):
#     ## deque 패키지 불러오기
#     from collections import deque
#     visited = []
#     need_visited = deque()
    
#     ##시작 노드 설정해주기
#     need_visited.append(start_node)
    
#     ## 방문이 필요한 리스트가 아직 존재한다면
#     while need_visited:
#         ## 시작 노드를 지정하고
#         node = need_visited.pop()
 
#         ##만약 방문한 리스트에 없다면
#         if node not in visited and node != '.':
 
#             ## 방문 리스트에 노드를 추가
#             visited.append(node)
#             ## 인접 노드들을 방문 예정 리스트에 추가
#             need_visited.extend(graph[node])
                
#     return print(visited)
    
# dfs(tree, 'A')

# # 중위 순회

# # def dfs2(graph, start_node):
# #     ## deque 패키지 불러오기
# #     from collections import deque
# #     visited2 = []
# #     need_visited2 = deque()
    
# #     ##시작 노드 설정해주기
# #     need_visited2.append(start_node)
    
# #     ## 방문이 필요한 리스트가 아직 존재한다면
# #     while need_visited2:
# #         ## 시작 노드를 지정하고
# #         node = need_visited2.pop()
# #         print(node)
 
# #         ##만약 방문한 리스트에 없다면
# #         if node not in visited2 and node != '.':
 
# #             ## 방문 리스트에 노드를 추가
# #             visited2.append(node)
# #             ## 현재의 노드를 value로 갖는, 자식은 아니어도 연결되어있는 노드 찾기.
# #             aws = []
# #             # print(graph.items())

# #             ## 연결되어있는 노드가 리스트 형태로 되어있어서, value로 한번 뽑은다음
# #             for key, value in graph.items():
# #                 # 리스트에서 요소를 하나씩 검사해서,
# #                 for j in value:
# #                     if j == node:
# #                         # 인접 노드 리스트에 반환.
# #                         aws.append(key)
# #                     # 그런데 루트는 부모 노드가 없기때문에
                        


# #             ## 인접 노드들을 방문 예정 리스트에 추가
# #             need_visited2.extend(aws)
                
# #     return print(visited2)


# # dfs2(tree, 'D')

# # for j in tree:
# #     left = tree[j][1]
# #     right = tree[j][0]
# #     print(f'{left}왼쪽 {right}오른쪽')

# # 중위 순회2

# def dfs2(graph, start_node, n):

#     ## deque 패키지 불러오기
#     from collections import deque
#     visited2 = []
#     # need_visited2 = deque()

#     #    ##시작 노드 설정해주기
#     # need_visited2.append(start_node)

#     leftlist = []
#     rightlist = []
#     rootlist = []

#     left = tree[start_node][1]
#     right = tree[start_node][0]

#     # for j in tree:
#     #     left = tree[j][1]
#     #     right = tree[j][0]
#     #     print(f'{left}왼쪽 {right}오른쪽')
#     leftlist.append(left)




#     def leftsearch(leftlist:list, visited2:list, graph):
#         while leftlist:
#             node = leftlist.pop()

#             if node not in visited2 and node != '.':

#                 for key, value in graph.items():
#                     if key == node:
#                         another = value
#                         if value[1] != '.':
#                             leftlist.append(value[1])
                    
#         visited2.append(node)

#         return visited2, leftlist

#     def rootsearch(rootlist:list, visited2:list, graph):

#         node = visited2.pop()
#         visited2.append(node)

#         for key, value in graph.items():
#             if value[1] == node:
#                 rootlist.append(key)
#                 visited2.append(key)
        
#         while rootlist:
#             parent = rootlist.pop()

#             for key, value in graph.items():
#                 if value[1] == parent:
#                     rootlist.append(key)
#                     visited2.append(key)

#         rootlist.append(parent)

#         return visited2, rootlist


#     def rightsearch(rightlist:list, leftlist:list, visited2:list, graph):
        
#         for key, value in graph.items():
#             if key == parent:
#                 if value[0] != '.':
#                     rightlist.append(value[0])

        
#         while rightlist:
#             rchild = rightlist.pop()
            
#             for key, value in graph.items():
#                 if key == rchild:
#                     if value[1] != '.':
#                         leftlist.append(value[1])
#                     elif value[0] != '.':
#                         visited2.append(rchild)
#                         rightlist.append(value[0])
                     
        
#         return visited2, rightlist, leftlist

#     while leftlist:
#         leftsearch(leftlist, visited2, graph)

#         rootsearch(rootlist, visited2, graph)
#         parent = rootlist.pop()

#         rightsearch(rightlist, leftlist, visited2, graph)

#     last = list(graph.keys())[n-1]
#     last = str(last)
#     visited2.append(last)

#     return print(visited2)

# dfs2(tree, 'A', n)

# last = list(tree.keys())[n-1]

# print(last)
        


# 후위 순회

# def dfs3(graph, start_node, n):

#     ## deque 패키지 불러오기
#     from collections import deque
#     visited3 = []
#     # need_visited2 = deque()

#     #    ##시작 노드 설정해주기
#     # need_visited2.append(start_node)

#     leftlist = []
#     rightlist = []
#     rootlist = []

#     left = tree[start_node][1]
#     right = tree[start_node][0]

#     # for j in tree:
#     #     left = tree[j][1]
#     #     right = tree[j][0]
#     #     print(f'{left}왼쪽 {right}오른쪽')
#     leftlist.append(left)



#     # 가장 끝 왼쪽 노드로 이동하는 함수.
#     # 만약 왼쪽 끝에 도달했다면, 그 왼쪽 끝 값을 방문 리스트에 넣는다.
#     def leftsearch(leftlist:list, visited3:list, graph):
#         # 왼쪽 수색 전까지 반복.
#         while leftlist:
#             # 수색해야하는 왼쪽 노드 꺼냄.
#             node = leftlist.pop()
#             # 이미 수색한 노드가 아니고, 빈 노드도 아니라면,
#             if node not in visited3 and node != '.':
#                 ## 그 노드의 왼쪽 노드를 꺼내서 수색 해야하는 노드로 더할 거야.(있다면.)
#                 for key, value in graph.items():
#                     if key == node:
#                         if value[1] != '.':
#                             leftlist.append(value[1])
                    
#         visited3.append(node)

#         return visited3, leftlist

#     # 루트를 찾아가면서 방문하는 함수.
#     def rootsearch(rootlist:list, visited3:list, graph):
#         #지금 방문한 시점에서 시작할게. 물론 제하지는 않을 거야.
#         node = visited3.pop()
#         visited3.append(node)

#         pparent = ''

#         # 만약 이 노드를 자식으로 갖는 부모가 있다면, 걔를 root로 간주할게. 
#         ######### 또 지나가면서 방문할 거야.
#         for key, value in graph.items():
#             if value[1] == node:
#                 rootlist.append(key)
#                 visited3.append(key)
        
#         # 만약 부모를 찾아가는 중인데,
#         while rootlist:
#             parent = rootlist.pop()
#             # 현재 가장 높은 부모에서, 얘를 부모로 갖는 얘가 있다면 계속 찾아줄거야.
#             # 그리고 걔들을 다 방문할 거야.
#             for key, value in graph.items():
#                 if value[1] == parent:
#                     # 근데! 만약 걔가 오른쪽 자식이 있다면 방문 안 할거야.
#                     if value[0] !='.':
#                         # rootlist.append(key)
#                         pparent = key
#                         print(pparent)
#                         pass
#                     elif value[0] == '.':
#                         #오른쪽 자식이 없다면, 방문할게.
#                         rootlist.append(key)
#                         visited3.append(key)
#                         print(key)
#                 elif value[0] == parent:
#                     rootlist.append(value[0])




#         # 다음으로 참조할, 시작할 노드를 임시로 여기에 넣어둘게.
#         # if pparent == '':
#         #     roootlist.append(key)
#         # else:
#         rootlist.append(pparent)
#         print(pparent)

#         return visited3, rootlist

    
#     def rightsearch(rightlist:list, leftlist:list, visited3:list, graph, parent:str):
        
#         rchild = 0

#         # 만약 지금 시작 노드에서, 오른쪽 노드가 비어있지 않다면 탐색 리스트에 넣어둘게.
#         for key, value in graph.items():
#             if key == parent:
#                 if value[0] != '.':
#                     rightlist.append(value[0])

#         # # 오른쪽을 계속 탐색할게.
#         # while rightlist:
#         # 일단 내가 볼 오른쪽이를 꺼낼게.
#         rchild = rightlist.pop()
        
#         # 그리고 오른쪽이가 왼쪽 자식이 있다면 왼쪽을 찾아야하는 리스트에 넣어놔서 다시 재수색 시킬거고.
#         ###### 오른쪽 자식이 있다면 지금은 방문처리하고 다음 오른쪽 자식으로 넘어갈게.
#         ####### 오른쪽 자식이 있다면, 수색 리스트에 넣어놔서 끝까지 수색할게.
#         for key, value in graph.items():
#             if key == rchild:
#                 if value[1] != '.':
#                     leftlist.append(value[1])
#                 # elif value[0] != '.':
#                 #     # visited3.append(rchild)
#                 #     rightlist.append(value[0])

#         #맨 끝에 도달했으니 방문할게.
#         # if rchild != 0:
#         #     visited3.append(rchild)

        
        
#         return visited3, rightlist, leftlist


#     def lastsearch(visited3,graph):
#         k = visited3.pop()
#         searchlist = []

#         searchlist.append(k)

#         while searchlist:
#             aws = searchlist.pop()
#             for key, value in graph.items():
#                 if value[0] == aws:
#                     visited3.append(key)
#                     searchlist.append(key)
#                 else :
#                     visited3.append(aws)
        
#         return visited3




#     while leftlist:
#         leftsearch(leftlist, visited3, graph)

#         print(visited3)
#         rootsearch(rootlist, visited3, graph)
#         parent = rootlist.pop()
#         # if parent == '':
#         #     parent = 
#         # else :
#         #     pass

#         print(visited3)
#         # print(parent)

#         # print(type(parent))
#         rightsearch(rightlist, leftlist, visited3, graph, parent)
#         print(visited3)

    
#     lastsearch(visited3, graph)

#     # last = list(graph.keys())[n-1]
#     # last = str(last)
#     # visited3.append(last)

#     return print(visited3)

# dfs3(tree, 'A', n)
# 후위 순회 하다 열받아서 그냥 솔루션씀...
# 깔끔하네....

# import sys
 
# N = int(sys.stdin.readline().strip())
# tree = {}
 
# for n in range(N):
#     root, left, right = sys.stdin.readline().strip().split()
#     tree[root] = [left, right]
        
# def preorder(root):
#     if root != '.':
#         print(root, end='')  # root
#         preorder(tree[root][0])  # left
#         preorder(tree[root][1])  # right
 
 
# def inorder(root):
#     if root != '.':
#         inorder(tree[root][0])  # left
#         print(root, end='')  # root
#         inorder(tree[root][1])  # right
 
 
# def postorder(root):
#     if root != '.':
#         postorder(tree[root][0])  # left
#         postorder(tree[root][1])  # right
#         print(root, end='')  # root
        


# preorder('A')
# print()
# inorder('A')
# print()
# postorder('A')
                
                    
        


# 예제 이상의 출력이 뭐가 잘못되는지 찾을 수 없어서 솔루션.
# 솔루션 자체는 금방 이해가 되어서 열받음..
import sys
input = sys.stdin.readline
#recursion error 방지
sys.setrecursionlimit(10**9)

arr = []
while True:
    try:
        x = int(input())
        arr.append(x)
    except:
        break


def solution(A):
    # 받은 배열 길이가 0이면 return
    if len(A) == 0:
        return

    tempL, tempR = [], []
    # 첫번째 값을 루트 노드로 설정
    mid = A[0]
    # 나머지 배열에 대해 for문을 돌면서 루트보다 커지는 부분을 기록해서 L과 R로 나눈다.
    for i in range(1, len(A)):
        if A[i] > mid:
            tempL = A[1:i]
            tempR = A[i:]
            break
    else:
    	#모두 mid보다 작은 경우
        tempL = A[1:]
    
    #왼쪽, 오른쪽 순으로 재귀 후 루트 노드 값 출력
    solution(tempL)
    solution(tempR)
    print(mid)

solution(arr)

