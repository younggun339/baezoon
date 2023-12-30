#include <stdio.h>
#include <string.h>

int main() {
    int number;
    scanf("%d", &number);
    for(int i = 0; i < number; i++){
        for(int j = 0; j < i+1; j++){
            printf("*");
        }
        printf("\n");
    }
    return 0;
    
}

// int main() {
//     int number;
//     char star[200];
//     char plusStar = "*";
//     scanf("%d", &number);
//     for(int i = 0; i < number; i++){
//         strcat(star,plusStar);
//         printf("%s\n",star);
//     }
//     return 0;
    
// }
// 하면 star의 타입문제 때문에 프린트에서 자료형을 찾지 못하는 경우.
// 그렇다면 정적공간을 할당한 문자열은 프린트할 수 없단말인가? 
