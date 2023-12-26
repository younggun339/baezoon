#include <stdio.h>

int main() {
    int a;
    int b = 0;
    scanf("%d", &a);
    while (a != 0)
    {
        b = b + 1;
        printf("%d\n",b);
        a = a -1;
        /* code */
    }
    
}