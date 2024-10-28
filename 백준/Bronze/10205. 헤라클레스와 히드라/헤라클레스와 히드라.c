#include <stdio.h>

int main() {
    int K;
    scanf("%d", &K);
    
    for (int case_num = 1; case_num <= K; case_num++) {
        int heads;
        scanf("%d", &heads);
        
        char actions[1000];
        scanf("%s", actions);
        
        for (int i = 0; actions[i] != '\0'; i++) {
            if (actions[i] == 'c') {
                heads++;
            } else {
                heads--;
            }
        }
        
        printf("Data Set %d:\n", case_num);
        printf("%d\n", heads);
        printf("\n");
    }
    
    return 0;
}