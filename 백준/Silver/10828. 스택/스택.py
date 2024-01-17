

# 정수를 저장하는 스택을 구현한 다음, 입력으로 주어지는 명령을 처리하는 프로그램을 작성하시오.

# 명령은 총 다섯 가지이다.

# push X: 정수 X를 스택에 넣는 연산이다.
# pop: 스택에서 가장 위에 있는 정수를 빼고, 그 수를 출력한다. 만약 스택에 들어있는 정수가 없는 경우에는 -1을 출력한다.
# size: 스택에 들어있는 정수의 개수를 출력한다.
# empty: 스택이 비어있으면 1, 아니면 0을 출력한다.
# top: 스택의 가장 위에 있는 정수를 출력한다. 만약 스택에 들어있는 정수가 없는 경우에는 -1을 출력한다.

# 첫째 줄에 주어지는 명령의 수 N (1 ≤ N ≤ 10,000)이 주어진다. 
# 둘째 줄부터 N개의 줄에는 명령이 하나씩 주어진다. 
# 주어지는 정수는 1보다 크거나 같고, 100,000보다 작거나 같다. 문제에 나와있지 않은 명령이 주어지는 경우는 없다.

# 출력해야하는 명령이 주어질 때마다, 한 줄에 하나씩 출력한다.

import sys

n = int(sys.stdin.readline())

## 대체 입력만 했는데, 함수 형태가 아닌데 그대로 출력이 된다고??
# 라는건 내 알고리즘 연상 능력...일 수도 있지만 남의 코드를 확인함.

# 입력을 테스트 개수만큼 받는걸 활성화하고, 들어오는 입력값에 따라 일치하면 처리하는 형식으로 구현했군.
# ......오.

stack = []

for i in range(n):

    command = sys.stdin.readline().split()

    if command[0] == 'push' :
        stack.append(command[1])
    elif command[0] == 'pop' :

        # 여기까지 쓰고보니, 사실 스택을 파이썬에서 구현한다면
        # 스택을 따로 클래스를 만들어 준 뒤 인스턴스 생성하고
        # 그 값을 호출해서 쓰는 거긴 할텐데, 따로 capacity를 지정해줘야하긴 하겠네..
        # 어차피 이론은 대충 알아서 반복 작업이니까 자동 커맨드로 해결하겠다.
        if len(stack) == 0:
            print(-1)
        else:
            print(stack.pop())
    elif command[0] == 'size' :
        print(len(stack))
    elif command[0] == 'empty' :
        if len(stack) == 0 :
            print(1)
        else : 
            print(0)
    
    elif command[0] == 'top' :
        if len(stack) == 0 :
            print(-1)
        else:
            a = stack.pop()
            print(a)
            stack.append(a)
        