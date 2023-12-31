#include <stdio.h>

int main() {
    int i = 0;
    int report[31];
    int number;
    int result_list[30]={0};
    int compare_list[30];
    for(i=0;i<28;i++)
    {
        scanf("%d",&number);
        report[i] = number;
    }

    // for(int d=0;d<28;d++){
    //     printf("%d\n", report[d]);
    //  }

    for(int a=0; a<30;a++){
        compare_list[a] = a+1;
        // printf("%d\n",compare_list[a]);
    }

    for(int k = 0; k<30; k++){
        for(int l= 0; l<28;l++){
            int compare_count, report_count;
            compare_count = (int)(compare_list[k]);
            report_count = (int)(report[l]);
            if(compare_count ==report_count){
                result_list[k] = 1;
            }
        }
    }

    for(int c=0; c<30;c++){
        if(result_list[c] != 1){
            printf("%d\n",c+1);
        }
    }

    // for(int j=0; j<30;j++){
    //     if(result_list[j]=0){
    //         printf("%d\n",j);
    //     }
    // }

    

}