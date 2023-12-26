#include <stdio.h>

int main() {
    int a;
    scanf("%d",&a);
    if(a%400==0){
        printf("%d",1);
    }
    else if (a%100 != 0 && a%4 ==0)
    {
        printf("%d",1);
        /* code */
    }
    else {
        printf("%d",0);
    }
    return 0;
}