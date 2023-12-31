N = map(int, input());
array = map(int, input().split());
V = int(input());
count = 0;
for num in array :
    if num == V :
        count +=1;
    
print(count);

# 아마 map으로 감싸면 int가 아니라 map int 처럼 되어서 같다를 비교할때 타입이 달라서 다른 걸로 나오는 모양