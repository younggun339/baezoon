#include <stdio.h>
#include <ctype.h>

int main() {
    char str[100];
    scanf("%s", str);
    int count = 0;
    while(str[count]){
        if(isupper(str[count])){
            str[count] = tolower(str[count]);
            }
        else if(islower(str[count])){
            str[count] = toupper(str[count]);
        }
        count++;
    }
    
    printf("%s", str);
        

}