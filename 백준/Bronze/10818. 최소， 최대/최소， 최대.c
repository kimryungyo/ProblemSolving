#include <stdio.h>
int main(void) {
    int n, num, min, max;
    min = 1000000;
    max = -1000000;
    scanf("%d\n", &n);
    for (int i = 0; i < n; i++) {
        scanf("%d", &num);

        if (num > max) {
            max = num;
        }

        if (num < min) {
            min = num;
        }
    }
    printf("%d %d", min, max);
}