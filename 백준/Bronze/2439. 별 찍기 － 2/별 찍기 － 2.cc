#include <stdio.h>
int main(void) {
    int N;
    scanf("%d", &N);
    
    for (int i = 1; i < N + 1; i++) {
        for (int j = 0; j < N - i ; j++) {
            printf(" ");
        }
        
        for (int j = 0; j < i; j++) {
            printf("*");
        }
        printf("\n");
    }
}