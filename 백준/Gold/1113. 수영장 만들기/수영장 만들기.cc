#include <bits/stdc++.h>

using namespace std;

int main(){

    ios::sync_with_stdio(false);

    cin.tie(0);

    

    int n, m;

    cin >> n >> m;

    

    vector<string> grid(n);

    for(int y = 0; y < n; ++y){

        cin >> grid[y];

    }

    

    vector<pair<int, int>> moves = { {0, 1}, {0, -1}, {1, 0}, {-1, 0} };

    

    long long count = 0;

    

    for(int h = 2; h <= 9; ++h){

        vector<vector<bool>> visited(n, vector<bool>(m, false));

        

        for(int y = 0; y < n; ++y){

            for(int x = 0; x < m; ++x){

                if((grid[y][x] - '0') < h && !visited[y][x]){

                    queue<pair<int, int>> q;

                    q.push({x, y});

                    visited[y][x] = true;

                    

                    bool is_border = false;

                    int group_count = 0;

                    

                    while(!q.empty()){

                        pair<int, int> current = q.front();

                        q.pop();

                        

                        int cx = current.first;

                        int cy = current.second;

                        group_count++;

                        

                        if(cx == 0 || cx == m-1 || cy == 0 || cy == n-1){

                            is_border = true;

                        }

                        

                        for(auto &move : moves){

                            int nx = cx + move.first;

                            int ny = cy + move.second;

                            

                            if(nx < 0 || nx >= m || ny < 0 || ny >= n){

                                is_border = true;

                                continue;

                            }

                            

                            if((grid[ny][nx] - '0') < h && !visited[ny][nx]){

                                visited[ny][nx] = true;

                                q.push({nx, ny});

                            }

                        }

                    }

                    

                    if(!is_border){

                        count += group_count;

                    }

                }

            }

        }

    }

    

    cout << count;

    

    return 0;

}