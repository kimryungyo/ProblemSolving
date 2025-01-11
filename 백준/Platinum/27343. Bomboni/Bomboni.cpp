#include <bits/stdc++.h>
using namespace std;

typedef long long ll;

const ll MOD = 998244353;

int main(){
    ios::sync_with_stdio(false);
    cin.tie(0);
    
    int N, K;
    cin >> N >> K;
    
    vector<vector<int>> grid(N, vector<int>(N));
    for(int i = 0; i < N; i++) {
        for(int j = 0; j < N; j++) {
            cin >> grid[i][j];
        }
    }
    
    vector<vector<vector<ll>>> table(N, vector<vector<ll>>(N, vector<ll>(K, 0)));
    
    int initial_mod = grid[0][0] % K;
    if(initial_mod < 0) initial_mod += K;
    table[0][0][initial_mod] = 1;
    
    for(int i = 0; i < N; i++){
        for(int j = 0; j < N; j++){
            if(i == 0 && j == 0) continue;
            if(grid[i][j] == -1) continue;
            
            int value = grid[i][j];
            
            if(i > 0){
                for(int k = 0; k < K; k++){
                    if(table[i-1][j][k] > 0){
                        int new_val = (1LL * k * value) % K;
                        table[i][j][new_val] = (table[i][j][new_val] + table[i-1][j][k]) % MOD;
                    }
                }
            }
            
            if(j > 0){
                for(int k = 0; k < K; k++){
                    if(table[i][j-1][k] > 0){
                        int new_val = (1LL * k * value) % K;
                        table[i][j][new_val] = (table[i][j][new_val] + table[i][j-1][k]) % MOD;
                    }
                }
            }
        }
    }
    
    cout << table[N-1][N-1][0] << "\n";
}
