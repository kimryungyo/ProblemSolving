#include <iostream>
#include <algorithm>
#include <cstdint>

constexpr int MAX_N = 2000000;
inline int bit_length(uint32_t n) {
    return n ? 32 - __builtin_clz(n) : 0;
}

int main() {
    std::ios_base::sync_with_stdio(false);
    std::cin.tie(nullptr);
    
    int N;
    std::cin >> N;
    
    static int NUMS[MAX_N];
    int num;
    for (int i = 0; i < N; ++i) {
        std::cin >> num;
        NUMS[i] = bit_length(num) - 1;
    }
    
    int mid = (N - 1) / 2;
    std::nth_element(NUMS, NUMS + mid, NUMS + N);
    
    int sum = 0;
    for (int i = 0; i <= mid; ++i) {
        sum += NUMS[i];
    }
    
    std::cout << sum + 1 << '\n';
    
    return 0;
}