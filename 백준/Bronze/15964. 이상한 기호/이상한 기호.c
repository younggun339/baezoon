#include <stdio.h>

// int add(long a, long b) {
//     return (a+b)*(a-b);
// }

int main() {
    long a, b, c;
    scanf("%ld %ld", &a, &b);
    // c = add(a,b);
    printf("%ld", (a+b)*(a-b));
    
}