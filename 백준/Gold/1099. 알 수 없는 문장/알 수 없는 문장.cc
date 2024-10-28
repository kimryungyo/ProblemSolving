// 아래 코드를 ChatGPT를 이용해 변환한 코드입니다.
// http://boj.kr/abcb4e9814564ca78cf0855482d8cca7

#include <iostream>
#include <unordered_map>
#include <vector>
#include <string>
#include <algorithm>
#include <climits>
#include <sstream>
using namespace std;

struct WordInfo {
    int length;
    unordered_map<char, int> count;
};

unordered_map<char, int> get_count(const string &str) {
    unordered_map<char, int> counter;
    for (char ch : str) {
        counter[ch]++;
    }
    return counter;
}

int get_read_cost(const string &str_a, const string &str_b) {
    int read_cost = 0;
    for (size_t i = 0; i < str_a.size(); ++i) {
        if (str_a[i] != str_b[i]) {
            read_cost += 1;
        }
    }
    return read_cost;
}

int main() {
    string input_string;
    getline(cin, input_string);
    int string_len = input_string.size();

    int n;
    cin >> n;
    cin.ignore();

    unordered_map<string, WordInfo> words;
    for (int i = 0; i < n; ++i) {
        string word;
        getline(cin, word);
        int length = word.size();
        unordered_map<char, int> count = get_count(word);
        words[word] = {length, count};
    }

    vector<int> min_cnt(string_len + 1, INT_MAX);
    min_cnt[0] = 0;

    for (int i = 0; i < string_len; ++i) {
        if (min_cnt[i] != INT_MAX) {
            for (const auto &pair : words) {
                const string &word = pair.first;
                const WordInfo &info = pair.second;
                int length = info.length;
                int pos = i + length;
                if (pos > string_len) continue;
                
                string sub_word = input_string.substr(i, length);
                unordered_map<char, int> sub_count = get_count(sub_word);

                if (sub_count == info.count) {
                    int read_cost = get_read_cost(word, sub_word);
                    int cost = min_cnt[i] + read_cost;

                    if (min_cnt[pos] == INT_MAX || cost < min_cnt[pos]) {
                        min_cnt[pos] = cost;
                    }
                }
            }
        }
    }

    cout << (min_cnt[string_len] == INT_MAX ? -1 : min_cnt[string_len]) << endl;
    return 0;
}