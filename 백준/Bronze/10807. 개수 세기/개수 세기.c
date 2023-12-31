#include <stdio.h>

int main() {
    int N, V, count;
    count = 0;
    int ComparisonValue[100];
    scanf("%d", &N);
    for(int i=0;i <N;i++ ) {
        scanf("%d ", &ComparisonValue[i]);
    }
    scanf("%d",&V);
    for (int i = 0; i < N; i++)
    {
        if(ComparisonValue[i] == V) {
            count = count +1;
        }
    }
    printf("%d",count);
    
    return 0;
}