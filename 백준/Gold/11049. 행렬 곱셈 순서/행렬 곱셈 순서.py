

# import sys

# n = int(sys.stdin.readline())
# p = [(0,0)]

# # 행렬 행, 열 길이를 비용 계산을 위해 넣음.
# for _ in range(n):
#     p1, p2 = map(int, sys.stdin.readline().split())
#     p.append((p1,p2))

# # print(p)

# INF = 1e8
# #행렬 곱 부분 최적해 저장해둘 테이블.
# m = [ [ INF for _ in range(n+1)] for _ in range(n+1)]

# # print(m)

# # 자기 자신의 곱은 0이니까 0처리.
# for i in range(1,n+1):
#     m[i][i] = 0

# # print(m)

# for l in range(2,n+1):
#     # print(f'{l}길이의 체인을 보겠어')
#     for i in range(1, n-l+2):
#         # print(f'{i} 행렬부터 할건데')
#         j = i+l -1
#         # print(f'최종 종착지 행렬{j}를 설정할거야.')
#         # m[i][j] = INF
#         for k in range(i, j):
#             q = m[i][k] + m[k+1][j] + (p[i][0]*p[k][1]*p[j][1])
#             # print(f'{i} 행에 {k}열의 {m[i][k]}와 {k+1}행에 {j}열의 {m[k+1][j]}를')
#             # print(f'{i}번째 행렬이랑, {k}번째 행렬, {j}번째 행렬의 계산 비용과 합할거야.')
#             if q <= m[i][j]:
#                 m[i][j] = q
#         # print(m[0])
#         # print(m[1])
#         # print(m[2])
#         # print(m[3])
#         # print('--------')

# print(m[1][n])


# import sys

# n = int(sys.stdin.readline())

# # 행렬 행, 열 길이를 비용 계산을 위해 넣음.
# p = [tuple(map(int, sys.stdin.readline().split())) for i in range(n)]

# # print(p)

# INF = 1e8
# #행렬 곱 부분 최적해 저장해둘 테이블.
# m = [ [0]*n for i in range(n)]

# # print(m)

# # print(m)

# for l in range(n-1):
#     # print(f'{l}길이의 체인을 보겠어')
#     for i in range(n-1-l):
#         # print(f'{i} 행렬부터 할건데')
#         j = i+l +1
#         m[i][j] = INF
#         # print(f'최종 종착지 행렬{j}를 설정할거야.')
#         # m[i][j] = INF
#         for k in range(i, j):
#             m[i][j] = min(m[i][k] + m[k+1][j] + (p[i][0]*p[k][1]*p[j][1]), m[i][j])
#             # print(f'{i} 행에 {k}열의 {m[i][k]}와 {k+1}행에 {j}열의 {m[k+1][j]}를')
#             # print(f'{i}번째 행렬이랑, {k}번째 행렬, {j}번째 행렬의 계산 비용과 합할거야.')
#             # if q <= m[i][j]:
#             #     m[i][j] = q
#         # print(m[0])
#         # print(m[1])
#         # print(m[2])
#         # print(m[3])
#         # print('--------')

# print(m[0][-1])



n = int(input())
mat = [tuple(map(int, input().split())) for i in range(n)]

dp = [[0]*n for i in range(n)]
for cnt in range(n-1):
    for i in range(n-1-cnt):
        j = i+cnt+1
        dp[i][j] = 2**31
        for k in range(i, j):
            dp[i][j] = min(dp[i][j], dp[i][k] + dp[k+1][j] + mat[i][0]*mat[k][1]*mat[j][1])
print(dp[0][-1])