#include <stdio.h>

int main() {
    int a;
    int c = 1;
    scanf("%d", &a);
    while (c != 10)
    {
        printf("%d * %d = %d\n",a,c,a*c);
        c = c +1;
    }
}