

N = int(input())

image = []

for _ in range(N):
    arr = list(map(int, input().split()))
    image.append(arr)


# print(image);

# k = 0
# color = [0,0]

# for i in range(N):
#     for row in image[i]:
#         start = row[0]
#         for elem in row:
#             if (elem == start):
#                 if(k == N):
#                     if(start == 1):
#                         color[0]+=1
#                         break
#                     else:
#                         color[1]+=1
#                         break    
#                 k+=1
#                 continue
#             else :

#
                

# def page(image, N, color, k):

#     for i in range(N):
#         for row in image[i]:
#             start = row[0]
#             for elem in row:
#                 if (elem == start):
#                     if(k == N):
#                         if(start == 1):
#                             color[0]+=1
#                             break
#                         else:
#                             color[1]+=1
#                             break    
#                     k+=1
#                     continue
#                 else:
#                     page(image[])


# first = image[0]
# first_elem = first[0]

# flag = True
# k = 0

# for i in first:
#     if (first_elem == i):
#         if(k == N):
#             if(first_elem ==1):
#                 color[0] +=1
#                 break
#             else:
#                 color[1] +=1
#                 break
#         k +=1
#         continue
#     else:
#         flag = False
#         break

# if (flag is False):
#     second_one = first[:N//2]
#     second_two = first[N//2:]
#     second_three = image[N//2+1][:N//2]
#     second_four = image[N//2+1][N//2:]

# arr = image[0]

# def find_page(arr, N, image):
#     elem = arr[0]
#     print(f"좋아, {arr}을 잘라서 살펴볼까.")
#     print(f"{elem}을 기준으로..")
#     k = 0
#     flag = True
#     for i in arr:
#         print(f"{k}번째 숫자를 보니까..")
#         print(f"{i}네?")
#         if (elem == i):
#             if(k == N):
#                 print("벌써 끝번호야!")
#                 if(elem == 1):
#                     color[0] += 1
#                     print("여태 1만 나왔으니 1 올랐다고 체크!")
#                     break
#                 else:
#                     color[1] +=1
#                     print("여태 0만나왔으니 0만 나왔다고 체크!")
#                     break
#             print("일단 같은가... 다음걸 살펴보자.")
#             k+=1
#             continue
#         else:
#             print("다른게 나와버렸군... 그만!")
#             flag =False
#             print("자르러 가자!")
#             return devide(flag, image, N)
#     print("잘 끝났으니 마감하겠습니다.")
    
#     return 0

# def devide(flag, arr, N):
#     if (flag is False):
#         print("자르라고 하더군요")
#         second_one = arr[0][:N//2]
#         second_two = arr[0][N//2:]
#         second_three = arr[N//2+1][:N//2]
#         second_four = arr[N//2+1][N//2:]
#         print(f"첫번째 종이는 {second_one},")
#         print(f"두번째 종이는 {second_two},")
#         print(f"세번째 종이는 {second_three}")
#         print(f"네번째 종이는 {second_four}")
#         find_page(second_one, N//2)
#         find_page(second_two, N//2)
#         find_page(second_three, N//2)
#         find_page(second_four, N//2)

# find_page(arr, N, image)

# print(color)

# 나는 이미지를 자르느라 애먹었는데 여기선 이미지를 안자르네....
result = []

def solution(x, y, N) :
  color = image[x][y]
  for i in range(x, x+N) :
    for j in range(y, y+N) :
      if color != image[i][j] :
        solution(x, y, N//2)
        solution(x, y+N//2, N//2)
        solution(x+N//2, y, N//2)
        solution(x+N//2, y+N//2, N//2)
        return
  if color == 0 :
    result.append(0)
  else :
    result.append(1)


solution(0,0,N)
print(result.count(0))
print(result.count(1))