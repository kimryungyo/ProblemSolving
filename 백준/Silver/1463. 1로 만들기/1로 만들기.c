#include <stdio.h>

int main(void) {
    int N, next, count;
    int dp[1000001];
    for (int i = 0; i < 1000001; i++) { dp[i] = -1; }
    
    scanf("%d", &N);
    dp[N] = 0;
    
    for (int num = N; num > 1; num--) {
        
        if (dp[num] != -1) {
            count = dp[num];
            
            if (num % 3 == 0) {
                next = num / 3;
                if (  (dp[next] == -1) || (dp[next] > count)  ) {
                    dp[next] = count + 1;
                }
            }
            
            if (num % 2 == 0) {
                next = num / 2;
                if (  (dp[next] == -1) || (dp[next] > count)  ) {
                    dp[next] = count + 1;
                }
            }
            
            next = num - 1;
            if (  (dp[next] == -1) || (dp[next] > count)  ) {
                dp[next] = count + 1;
            }
            
        }
        
    }

    printf("%d\n", dp[1]);
    return 0;
}