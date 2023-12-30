#include <stdio.h>

int main() {
    int N, X, ComparisonValue;
    scanf("%d %d", &N, &X);
    for(int i=0;i <N;i++ ) {
        scanf("%d ", &ComparisonValue);
        if(ComparisonValue<X){
            printf("%d ",ComparisonValue);
        }
    }
    return 0;
}

// int main() {
//     long long N, X;
//     scanf("%lld %lld\n", &N, &X);
//     char sequence[(N*2)-1];
//     scanf("%s",sequence);
//     for(int i=0;i < (N*2) -1 ;i+2 ) {
//         int ComparisonValue = sequence[i];
//         if(ComparisonValue < X){
//             printf("%d ",ComparisonValue); 
//         }
//         else {
//             continue;;
//         }
//     }