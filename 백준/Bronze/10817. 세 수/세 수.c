#include <stdio.h>
int main(void) {
    int A, B, C;
    scanf("%d %d %d", &A, &B, &C);

    if ((B <= A && A <= C) || (C <= A && A <= B)) {
        printf("%d\n", A);
    } else if ((A <= B && B <= C) || (C <= B && B <= A)) {
        printf("%d\n", B);
    } else {
        printf("%d\n", C);
    }

    return 0;
}