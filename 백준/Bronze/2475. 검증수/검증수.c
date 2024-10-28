#include <stdio.h>
int main(void) {
    int sum, num, mod;
    sum = 0;
    for (int i = 0; i < 5; i++) {
        scanf("%d", &num);
        mod = num % 10;
        sum += mod * mod;
    }
    printf("%d", sum % 10);
    return 0;
}