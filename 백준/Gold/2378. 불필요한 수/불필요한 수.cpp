#include <bits/stdc++.h>
using namespace std;

static map<long long, int> prime_factorization(long long x) {
    map<long long, int> factors;
    long long num = x;
    long long d = 2;
    while (d * d <= num) {
        while (num % d == 0) {
            factors[d]++;
            num /= d;
        }
        d += (d == 2) ? 1 : 2;
    }
    if (num > 1) {
        factors[num]++;
    }
    return factors;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    long long N, M;
    cin >> N >> M;

    if (N == 1) {
        cout << 0 << "\n";
        return 0;
    }

    map<long long, int> factors = prime_factorization(M);

    long long n = N - 1;
    map<long long, vector<int>> factorial_exp;

    for (auto &kv : factors) {
        long long p = kv.first;
        int a = kv.second;

        vector<int> exponent_p_of_i(n + 1, 0);

        long long power = p;
        while (power <= n) {
            for (long long multiple = power; multiple <= n; multiple += power) {
                exponent_p_of_i[(size_t)multiple]++;
            }
            
            if (power > LLONG_MAX / p) break;
            power *= p;
        }

        vector<int> factorial_p_exp_p(n + 1, 0);
        for (int i = 1; i <= n; i++) {
            factorial_p_exp_p[i] = factorial_p_exp_p[i - 1] + exponent_p_of_i[i];
        }
        factorial_exp[p] = factorial_p_exp_p;
    }

    vector<int> unnecessary;
    for (int k = 0; k < N; k++) {
        bool divisible = true;
        for (auto &kv : factors) {
            long long p = kv.first;
            int a = kv.second;
            const auto &f = factorial_exp[p];
            int exp_ck = f[(size_t)n] - f[(size_t)k] - f[(size_t)(n - k)];
            if (exp_ck < a) {
                divisible = false;
                break;
            }
        }

        if (divisible) {
            unnecessary.push_back(k + 1);
        }
    }

    cout << (int)unnecessary.size() << "\n";
    if (!unnecessary.empty()) {
        for (int i = 0; i < (int)unnecessary.size(); i++) {
            cout << unnecessary[i] << (i + 1 == (int)unnecessary.size() ? '\n' : ' ');
        }
    }

    return 0;
}
