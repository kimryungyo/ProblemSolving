#include <iostream>
#include <vector>
#include <unordered_map>

using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);

    int N;
    cin >> N;

    vector<pair<int, int>> points;
    unordered_map<int, int> count_x, count_y;

    for (int i = 0; i < N; ++i) {
        int x, y;
        cin >> x >> y;
        points.emplace_back(x, y);

        count_x[x]++;
        count_y[y]++;
    }

    long long cases = 0;
    for (const auto& point : points) {
        int x = point.first, y = point.second;
        cases += (long long)(count_x[x] - 1) * (count_y[y] - 1);
    }

    cout << cases << endl;

    return 0;
}