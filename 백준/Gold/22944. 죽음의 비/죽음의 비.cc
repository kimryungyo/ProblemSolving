#include <iostream>
#include <vector>
#include <set>
#include <queue>
#include <cmath>
#include <algorithm>
#include <tuple>

using namespace std;

struct State {
    pair<int, int> position;
    int count;
    int health;
    int umb_dura;
    set<pair<int, int>> used_umb;

    bool operator<(const State& other) const {
        return count > other.count; // for priority queue, we want smallest count first
    }
};

int get_dist(pair<int, int> point, pair<int, int> target) {
    int y = point.first, x = point.second;
    int e_y = target.first, e_x = target.second;
    return abs(y - e_y) + abs(x - e_x);
}

vector<pair<int, pair<int, int>>> get_dists_umbs(pair<int, int> point, const set<pair<int, int>>& umbrellas) {
    int y = point.first, x = point.second;
    vector<pair<int, pair<int, int>>> dists;

    for (const auto& umbrella : umbrellas) {
        int o_y = umbrella.first, o_x = umbrella.second;
        int dist = abs(y - o_y) + abs(x - o_x);
        dists.push_back({dist, umbrella});
    }

    sort(dists.begin(), dists.end());
    return dists;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, health, dura;
    cin >> n >> health >> dura;

    vector<vector<char>> maps(n, vector<char>(n));
    set<pair<int, int>> umbrellas;
    pair<int, int> start, end;

    for (int y = 0; y < n; ++y) {
        for (int x = 0; x < n; ++x) {
            cin >> maps[y][x];
            if (maps[y][x] == 'S') start = {y, x};
            else if (maps[y][x] == 'U') umbrellas.insert({y, x});
            else if (maps[y][x] == 'E') end = {y, x};
        }
    }

    int min_dist = -1;
    priority_queue<State> queue;
    queue.push({start, 0, health, 0, {}});

    while (!queue.empty()) {
        State state = queue.top();
        queue.pop();

        auto position = state.position;
        int count = state.count;
        int current_health = state.health;
        int umb_dura = state.umb_dura;
        auto used_umb = state.used_umb;

        int can_moves = current_health + umb_dura;

        int end_dist = get_dist(position, end);
        if (can_moves >= end_dist) {
            count += end_dist;
            if (min_dist == -1 || count < min_dist) {
                min_dist = count;
            }
        } else {
            auto umb_dists = get_dists_umbs(position, umbrellas);
            for (const auto& [umb_dist, umb] : umb_dists) {
                if (used_umb.count(umb)) continue;
                if (can_moves < umb_dist) continue;

                int new_health = current_health;
                int new_umb_dura = dura - 1;
                auto new_position = umb;
                auto new_used_umb = used_umb;
                new_used_umb.insert(umb);
                int new_count = count + umb_dist;

                new_health -= max(0, (umb_dist - 1) - umb_dura);

                State next = {new_position, new_count, new_health, new_umb_dura, new_used_umb};
                queue.push(next);
            }
        }
    }

    cout << min_dist << endl;
    return 0;
}
