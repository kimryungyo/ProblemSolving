#include <iostream>
#include <vector>
#include <map>
#include <algorithm>
#include <string>

using namespace std;

int n;
map<int, int> points;
map<pair<int, int>, pair<int, int>> others;
vector<vector<pair<int, int>>> lines;
vector<pair<int, int>> sequences;

pair<int, int> convert_point(int point) {
    int x = point % (n + 1);
    int y = point / (n + 1);
    return {x, y};
}

void print_shape(const vector<pair<int, int>>& sequences) {
    vector<pair<pair<int, int>, pair<int, int>>> new_seq;
    for (const auto& line : sequences) {
        new_seq.push_back({convert_point(line.first), convert_point(line.second)});
    }

    for (int y = 0; y < n; ++y) {
        for (int x = 0; x < n; ++x) {
            pair<pair<int, int>, pair<int, int>> t1 = {{x, y}, {x + 1, y + 1}};
            pair<pair<int, int>, pair<int, int>> t2 = {{x + 1, y}, {x, y + 1}};
            if (find(new_seq.begin(), new_seq.end(), t1) != new_seq.end()) {
                cout << "\\";
            } else if (find(new_seq.begin(), new_seq.end(), t2) != new_seq.end()) {
                cout << "/";
            } else {
                cout << ".";
            }
        }
        cout << endl;
    }
}

bool root_valid() {
    vector<int> roots((n + 1) * (n + 1), -1);

    auto find_root = [&](int p) -> int {
        if (roots[p] == -1) return -1;
        while (roots[p] != p) {
            p = roots[p];
        }
        return p;
    };

    for (const auto& line : sequences) {
        int a = line.first, b = line.second;
        int a_root = find_root(a);
        int b_root = find_root(b);

        if (a_root == -1 && b_root == -1) {
            roots[a] = a;
            roots[b] = a;
        } else if (a_root == b_root) {
            return false;
        } else if (a_root == -1) {
            roots[a] = b_root;
        } else if (b_root == -1) {
            roots[b] = a_root;
        } else {
            roots[a_root] = b_root;
        }
        
        roots[a] = roots[b];
    }

    return true;
}

map<int, int> nodes, non_nodes;

bool validation() {
    if (!root_valid()) return false;
    
    auto line = sequences.back();
    for (int i : {line.first, line.second, others[line].first, others[line].second}) {
        if (points[i] != -1) {
            if (nodes[i] > points[i]) return false;
            if ((nodes[i] + non_nodes[i]) == 4) {
                if (nodes[i] != points[i]) return false;
            }
        }
    }

    return true;
}

void append_line(const pair<int, int>& line) {
    nodes[line.first]++;
    nodes[line.second]++;
    non_nodes[others[line].first]++;
    non_nodes[others[line].second]++;
    sequences.push_back(line);
}

void remove_line() {
    auto line = sequences.back();
    nodes[line.first]--;
    nodes[line.second]--;
    non_nodes[others[line].first]--;
    non_nodes[others[line].second]--;
    sequences.pop_back();
}

void dfs() {
    int idx = sequences.size();
    for (const auto& line : lines[idx]) {
        append_line(line);
        if (validation()) {
            if (sequences.size() == n * n) {
                print_shape(sequences);
                exit(0);
            }
            dfs();
        }
        remove_line();
    }
}

int main() {
    cin >> n;

    for (int i = 0; i <= n; ++i) {
        string s;
        cin >> s;
        for (int j = 0; j <= n; ++j) {
            points[i * (n + 1) + j] = (s[j] == '.') ? -1 : s[j] - '0';
        }
    }

    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < n; ++j) {
            pair<int, int> slash = {i * (n + 1) + (j + 1), (i + 1) * (n + 1) + j};
            pair<int, int> backslash = {i * (n + 1) + j, (i + 1) * (n + 1) + (j + 1)};
            lines.push_back({slash, backslash});
            others[slash] = backslash;
            others[backslash] = slash;
        }
    }

    sort(lines.begin(), lines.end(), [](const auto& a, const auto& b) {
        return points[a[0].first] + points[a[0].second] + points[a[1].first] + points[a[1].second] >
               points[b[0].first] + points[b[0].second] + points[b[1].first] + points[b[1].second];
    });

    for (int k = 0; k < (n + 1) * (n + 1); ++k) {
        int e = 0;
        if (k % (n + 1) == 0 || k % (n + 1) == n) e += 2;
        if (k <= n) e += 2;
        if (k >= (n + 1) * n) e += 2;
        if (e == 4) e = 3;

        nodes[k] = 0;
        non_nodes[k] = e;
    }

    dfs();

    return 0;
}