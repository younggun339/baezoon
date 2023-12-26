a = 1;
b = 1;
while (a+b) != 0 :
    a, b = map(int, input().split());
    a = int(a);
    b = int(b);
    if (a+b) == 0 :
        break;
    else :
        print(a+b);