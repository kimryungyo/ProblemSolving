#include <stdio.h>
int main(void) {
    int H, M, T;
    scanf("%d %d", &H, &M);
    T = H * 60 + M;
    T -= 45;
    if ( T < 0 ) {
        T += 24 * 60;
    }
    printf("%d %d", T / 60, T % 60);
}