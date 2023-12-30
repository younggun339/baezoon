import sys

inputCase = int(sys.stdin.readline().rstrip());
while inputCase != 0 :
    a, b = map(int, sys.stdin.readline().rstrip().split());
    a = int(a);
    b = int(b);
    print(a+b);
    inputCase = inputCase - 1;
