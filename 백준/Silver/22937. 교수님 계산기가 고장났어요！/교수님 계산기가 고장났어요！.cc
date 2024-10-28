#include <iostream>
#include <string>
using namespace std;
typedef unsigned long long ull;

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);

    int test_cases; cin >> test_cases;
    while (test_cases--) {
        int sign = 0;
        string num1, num2; cin >> num1 >> num2;
        if (num1[0] == '-') {
            sign ^= 1;
            num1 = num1.substr(1, 11);
        }
        if (num2[0] == '-') {
            sign ^= 1;
            num2 = num2.substr(1, 11);
        }

        ull value1 = (ull)(num1[0] - '0') * 1000000000 + stoi(num1.substr(2, 9));
        ull value2 = (ull)(num2[0] - '0') * 1000000000 + stoi(num2.substr(2, 9));

        string result = to_string(value1 * value2);
        while (result.length() < 18) result = "0" + result;

        if (sign & 1) cout << '-';
        if (result.length() > 18) cout << result.substr(0, result.length() - 18) << '.' << result.substr(result.length() - 18, 18) << '\n';
        else cout << 0 << '.' << result << '\n';
    }
}

