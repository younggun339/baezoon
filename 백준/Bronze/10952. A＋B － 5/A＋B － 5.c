#include <stdio.h>

int main() {
    int a= 1;
    int b = 1;
    while ( (a+b) != 0)
    {
        scanf("%d %d",&a,&b);
        if ((a+b) == 0)
        {
           break;
        }
        else{
            printf("%d\n",a+b);
        }
    }
    return 0;
}