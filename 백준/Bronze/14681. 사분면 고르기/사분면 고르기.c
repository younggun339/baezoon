#include <stdio.h>

int main() {
    int a, b;
    scanf("%d",&a);
    scanf("%d",&b);
    if(a>0 && b>0){
        printf("%d",1);
    }
    else if (a<0 && b>0)
    {
        printf("%d",2);
        /* code */
    }
    else if (a<0 && b<0)
    {
        printf("%d",3);
        /* code */
    }
    
    else {
        printf("%d",4);
    }
    return 0;
}