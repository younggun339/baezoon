#include <stdio.h>

int main() {
    int inputCase;
    scanf("%d", &inputCase);
    while (inputCase != 0)
    {
        int a, b;
        scanf("%d %d",&a,&b);
        printf("%d\n",a+b);
        inputCase = inputCase -1;
        /* code */
    }
}