#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    vector<int> nums = {-1,111,117,119,171,231,237,297,319,371,411,413,417,437,471,473,531,537,597,611,671,679,711,713,717,731,737,831,837,897,973,979,1131,1137,1311,1313,1317,1379,1797,1971,3113,3131,3173,3179,4197,4311,4313,4317,4797,6137,6179,7197,7971,31373};

    int T;
    cin >> T;

    while (T--) {
        int N;
        cin >> N;
        auto it = lower_bound(nums.begin(), nums.end(), N);

        if (it == nums.end() || *it > N) --it;

        cout << *it << "\n";
    }

    return 0;
}
