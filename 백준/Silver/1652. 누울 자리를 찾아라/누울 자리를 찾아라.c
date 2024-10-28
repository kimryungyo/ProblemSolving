#include <stdio.h>

int find_sleep_spot_count(int N, char grid[N][N], int reverse) {
    int count = 0;

    for (int y = 0; y < N; y++) {
        int stack = 0;

        for (int x = 0; x < N; x++) {
            char block;
            
            if (reverse) {
                block = grid[y][x];
            } else {
                block = grid[x][y];
            }

            if (block == '.') {
                stack += 1;
                if (stack == 2) {
                    count += 1;
                }
            } else {
                stack = 0;
            }
        }

    }
    return count;
}

int main() {
    int n, vertical_count, horizontal_count;
    scanf("%d", &n);
    char grid[n][n];

    for (int i = 0; i < n; i++) {
        scanf("%s", grid[i]);
    }

    vertical_count = find_sleep_spot_count(n, grid, 1);
    horizontal_count = find_sleep_spot_count(n, grid, 0);

    printf("%d %d\n", vertical_count, horizontal_count);
    return 0;
}