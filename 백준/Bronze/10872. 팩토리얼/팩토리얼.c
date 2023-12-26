#include <stdio.h>

int main() {
    int a;
    int b = 0;
    int c = 1;
    scanf("%d", &a);
    while (a != 0)
    {
        b = b + 1;
        c = b*c;
        a = a -1;
        /* code */
    }
    printf("%d",c);
}