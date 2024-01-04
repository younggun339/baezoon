#include <stdio.h>

int main() {

    char sequence[100];

    while (scanf("%[^\n]", sequence) != EOF) {
        printf("%s\n", sequence);
        getchar();
    }

    return 0;
}


// #include <stdio.h>
// #include <string.h>

// char* enter(char *dst){
//     char *p = dst;
//     while (*p != '\0') p++;
//     {
//         *p = '\n';
//         *(p+1) = '\0';
//     }
//     return dst;
// }

// int main() {
//     char input[101];
//     char sequence[100000];
//     char a;
//     // char enter = '\n';
//     while (scanf("%[^\n]", input) != EOF)
//     {
//         // scanf("%c", input);
//         // // strcat(sequence, enter);
//         // strcat(sequence, input);
//         if (sequence[0] == '\0')
//         {
//             scanf("%[^\n]s", input);
//             strcat(sequence, input);
//         }
//         else{
//             scanf(" %[^\n]s", input);
//             enter(sequence);
//             // strcat(sequence, enter);
//             strcat(sequence, input);
//         }
        
//     }
//     printf("%s", sequence);
//     return 0;
//     // scanf(" %[^\n]s", input);
//     // strcat(sequence, input);

//     // if(sequence[0] =='\0'){
//     //     scanf("%[^\n]s", input);
//     //     strcat(sequence, input);
//     // }
//     // else{
//     //     scanf(" %[^\n]s", input);
//     //     enter(sequence);
//     //     strcat(sequence, input);
//     // }
//     // scanf("%[^\n]s", input);
//     // strcat(sequence, input);
//     // scanf(" %[^\n]s", input);
//     // enter(sequence);
//     // strcat(sequence, input);
//     // printf("%s", sequence);
// }