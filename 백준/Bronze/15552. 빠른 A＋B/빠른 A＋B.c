
#include <stdio.h>

int main() {
    long long inputCase;
    scanf("%lld", &inputCase);
    while (inputCase != 0)
    {
        int a;
        long b;
        scanf("%d %ld",&a,&b);
        printf("%ld\n",a+b);
        inputCase = inputCase -1;
        /* code */
    }
}