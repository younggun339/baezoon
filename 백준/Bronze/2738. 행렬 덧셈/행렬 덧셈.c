#include <stdio.h>

// int scanMatrix(int matrix[][], int M, int N){
//     int i = 0;
//     int j = 0;
//     while(i<N){
//         while (j<M)
//         {
//             scanf("%d ",&list(matrix[i][j]));
//             j = j + 1;
//         }
//     j = 0;
//     i = i + 1;
//     }
//     return matrix;
// }

int main() {
    int N, M;
    scanf("%d %d", &N, &M);
    int matrixOne[N][M], matrixTwo[N][M];
    int i = 0;
    int j = 0;
    int a = 0;
    int b = 0;
    int resultMatrix[N][M];

    
    for(int e =0; e<N; e++){
        for(int f=0; f<M; f++){
            resultMatrix[e][f] = 0;
            // printf("%d ", resultMatrix[e][f]);
        }
    }

    while(i<N){
        while (j<M)
     {
         scanf("%d",&matrixOne[i][j]);
         j = j + 1;
     }
     j = 0;
     i = i + 1;
    }

    while(a<N){
        while (b<M)
     {
         scanf("%d",&matrixTwo[a][b]);
         b = b + 1;
     }
     b = 0;
     a = a + 1;
    }

    // for(int i =0; i<N; i++){
    //     for(int j=0; j<M; j++){
    //         printf("%d ", matrixOne[i][j]);
    //     }
    //     printf("\n");
    // }

    // for(int i =0; i<N; i++){
    //     for(int j=0; j<M; j++){
    //         printf("%d ", matrixTwo[i][j]);
    //     }
    //     printf("\n");
    // }


    int c = 0;
    int d = 0;

    while(c<N){
        while (d<M)
        {
            resultMatrix[c][d] = matrixOne[c][d] + matrixTwo[c][d];
            d = d +1;
        }
        d = 0;
        c = c +1;
    }



    for(int e =0; e<N; e++){
        for(int f=0; f<M; f++){
            printf("%d ", (int)(resultMatrix[e][f]));
        }
        printf("\n");
    }


}