#include <stdio.h>
int main(void) {
        int SCORE;
        scanf("%d", &SCORE);
        if ( SCORE >= 90 ) {
                printf("A");
        } else if ( SCORE >= 80 ) {
                printf("B");
        } else if (SCORE >= 70) {
                printf("C");
        } else if (SCORE >= 60) {
                printf("D");
        } else {
                printf("F");
        }
        printf("\n");
        return 0;
}

