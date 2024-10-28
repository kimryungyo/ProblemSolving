#include <stdio.h>
int main(void) {
    int A, B;
    int X, Y, Z;
    scanf("%d\n%d", &A, &B);
    X = B / 100;
    Y = B % 100 / 10;
    Z = B % 10;
    printf("%d\n", A * Z);
    printf("%d\n", A * Y);
    printf("%d\n", A * X);
    printf("%d\n", A * B);
}