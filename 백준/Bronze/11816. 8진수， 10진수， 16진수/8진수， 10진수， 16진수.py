
arr = str(input())

if(arr[1] == 'x' and arr[0] == '0'):
    ## 16진수 인경우
    h = int(arr, 16)
    print(h)
elif(arr[0] == '0' and len(arr) != 1):
    ## 8진수 인 경우
    o = int(arr, 8)
    print(o)
else: 
    print(arr)