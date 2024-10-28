#include <stdio.h>

int main(void) {
        int N, price, M, number, paid;
        int prices[10];
        scanf("%d", &N);

        for (int i = 0; i < N; i++) {
                scanf("%d", &price);
                prices[i] = price;
        }

        scanf("%d", &M);
        paid = 0;
        for (int i = 0; i < M; i++) {
                scanf("%d", &number);
                paid += prices[number-1];
        }

        printf("%d\n", paid);
        return 0;
}