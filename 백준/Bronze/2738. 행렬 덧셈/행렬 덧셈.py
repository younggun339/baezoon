N, M = map(int, input().split());
i = 0;
j = 0;
a = 0;
b = 0;
c = 0;

row_one = [];
row_two = [];
row_result = [];
row_result = [0]*N;
while c<N :
    row_result[c] = [0]*M;
    c = c + 1;

while i<N :
    row_one.append(list(map(int, input().split())));
    i = i + 1;

while j<N :
    row_two.append(list(map(int, input().split())));
    j = j +1;


while a<N :
    while b<M :
        # print("a" + str(a));
        # print("b" + str(b));
        # print("row_one" +str(row_one[a][b]));
        # print("row_two" + str(row_two[a][b]));
        row_result[a][b] = row_one[a][b] + row_two[a][b];
        # print("row_result" + str(row_result[a][b]));
        b = b + 1;
    # print("a" + str(a));
    # print("b" + str(b));
    b = 0 ;
    a = a + 1;

# print(row_result);

for num in row_result :
    for result in num :
        print(str(result) + " ", end="");
    print("");