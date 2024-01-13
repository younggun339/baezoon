


# 주어진 수 N개 중에서 소수가 몇 개인지 찾아서 출력하는 프로그램을 작성하시오.

# 첫 줄에 수의 개수 N이 주어진다. N은 100이하이다. 다음으로 N개의 수가 주어지는데 수는 1,000 이하의 자연수이다.

n = int(input())
li =input().split()


# li = []
# for i in range(n):

#     li.append(map(int, input().split()))

count= n

# for j in li :
#     k = int(j)
#     print("k : " + str(k))
#     for a in range(k):
#         print("a+2 : " + str(a+2))
#         print("k+1 : " + str(k+1))
#         if (k+1) % (a+2) :
#             pass
#         # elif a == 1 :
#         #     pass
#         else :
#             print((k+1)%(a+2))
#             count -= 1
#             print("else : " + str(k))
#             break

# print(count)


for j in li :

    if int(j) == 1 :
        count -= 1
    elif int(j) == 2:
        pass
    elif int(j) == 3 :
        pass
    else :
        k = int(j)-1
        # print("범위값 : " + str(k))
        for i in range(2,k):
            # print("i부터 시작 : " + str(i))
            # print(f'{k+1}을 {i}로 나눌게요')
            if (k+1) % i == 0 :
                count -= 1
                # print(k+1)
                break


print(count)