#include <stdio.h>

int main() {
    char keyword[1000];
    int i;
    scanf("%s", keyword);
    scanf("%d", &i);
    printf("%c",keyword[i-1]);
}